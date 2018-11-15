import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    var_0 = True
    var_1 = True
    var_2 = True

    while var_0 is True:
        city = input("Which city would you like to analyze? ").lower()
        if city in ['chicago','washington','new_york_city']:
            print('Thanks, got the city.')
            var_0 = False
        else:
            print("Sorry, I can't accept that input. Please try again!")


    while var_1 is True:
        month = input("Which months data are you interested in? ").lower()
        if month in ['january','february','march','april','may','june','july','august','september','october','november','december', 'all']:
            print('Thanks, got the month.')
            var_1 = False
        else:
            print("Sorry, I can't accept that input. Please try again!")

    while var_2 is True:
        day = input("Which day of the week are you interested in? ").lower()
        if day in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday', 'any']:
            print('Thanks, got the day.')
            var_2 = False
        else:
            print("Sorry, I can't accept that input for day. Please try again!")

    return [city, month, day]

def load_data(city, month, day):
    """this function takes the user inputs and customizes the dataframe based on it"""


    while True:
       try:
           df = pd.read_csv(CITY_DATA[city])
           df['Start Time'] = pd.to_datetime(df['Start Time'])
           df['month'] = df['Start Time'].dt.month
           df['day'] = df['Start Time'].dt.weekday_name

           if month != 'all':
               months = ['january','february','march','april','may','june','july','august','september','october','november','december']
               month = months.index(month) + 1
               df['month'] = month

           if day != 'any':
               days = ["monday","tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
               if day not in days:
                   raise Exception
               df['day'] = day
               print(df)
               print(month,day)



           return df

       except:
           print('Please try again')
           print('Look at me I am refactoring')
           city, month, day = get_filters()
           break


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].value_counts().nlargest(1)
    common_day = df['day'].value_counts().nlargest(1)
    df['travel_hour'] = df['Start Time'].dt.hour
    common_hours = df['travel_hour'].value_counts().nlargest(1)

    #print the common periods
    print('The most common month is {}'.format(common_month))
    print('The most common day is {}'.format(common_day))
    print('The most common hour is {}'.format(common_hours))
    print('also refactoring here')

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_station_start = df['Start Station'].value_counts().nlargest(1)
    common_station_end = df['End Station'].value_counts().nlargest(1)
    df['Stations Combined'] = 'starts at ' + df['Start Station'] + ' and goes down to ' + df['End Station']
    common_trip = df['Stations Combined'].value_counts().nlargest(1)

    print('The most common start station is {}'.format(common_station_start))
    print('The most common end station is {}'.format(common_station_end))
    print('The most common trip {}'.format(common_trip))
    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('The total travel time is {}'.format(total_travel_time))
    print('The mean trip duration is {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    try:
        user_counts = df['User Type'].value_counts()
        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        # Display earliest, most recent, and most common year of birth
        print(gender_counts)
        print(user_counts)
        df['Birth Year'] = pd.to_datetime(df['Birth Year'])
        print("The earliest birth date is {}, the most recent is {}, the most common is {}".format(df['Birth Year'].min(), df['Birth Year'].max(), df['Birth Year'].mode()))

    except KeyError:
        print("There were no birth dates in this data set.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():

    counter = 0
    var_3 = True

    city, month, day = get_filters()
    df = load_data(city, month, day)
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
    print(df.head())

    while var_3 is True:
        user_input = input("Would you like to see 5 more rows? (Y/N) ").lower()
        if user_input in ["y"]:
            counter += 1
            data_frame_rows = 5 + counter*5
            print(df.head(data_frame_rows))
        else:
            print("Thank you, I hope this was helpful!")
            var_3 = False
main()
