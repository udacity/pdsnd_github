import time
import pandas as pd
import numpy as np
from tabulate import tabulate as tb

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


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    def getcity():
        """
        Prompts the user to enter a city from specified list that is defined as a dictionary
        Searches dictionary for a match
        Returns city name
        """
        print('Would you like to see data for Chicago, New York, or Washington?\n 1. Chicago\n 2. New York City\n 3. Washington')

        city_dict = {'1' : 'Chicago',
                     '2' : 'New York City',
                     '3' : 'Washington' }
        city_opt = ()

        while city_opt not in city_dict:
            print('Please input 1, 2, or 3')
            city_opt = input()
        city = city_dict[city_opt]

        return city

    city = getcity()


    # TO DO: get user input for month (all, january, february, ... , june)
    def getmonth():
        """
        Prompts user to input month from a list that is defined as a dictionary.
        Searches month dictionary for match.
        Returns month.
        """
        print('Please choose a month \n 0. All\n 1. January\n 2. February\n 3. March\n 4. April\n 5. May\n 6. June\n')
        month_dict = {'0' : 'All',
                     '1' : 'January',
                     '2' : 'February',
                     '3' : 'March',
                     '4' : 'April',
                     '5' : 'May',
                     '6' : 'June',
                     }
        month_opt = ()
        while month_opt not in month_dict:
            month_opt = input('Please input 1 - 6 or 0 for All months')
        month = month_dict[month_opt]
        return month

    month = getmonth()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    def getday():
        """
        Prompts user to input day from a list that is defined as a dictionary
        Searches dictionary for a match
        Returns day
        """
        print('Please select a day of the week\n 0. All\n 1. Monday\n 2. Tuesday\n 3. Wednesday\n 4. Thursday\n 5. Friday\n 6. Saturday\n 7. Sunday')
        day_dict = {'0' : 'All',
                    '1' : 'Monday',
                    '2' : 'Tuesday',
                    '3' : 'Wednesday',
                    '4' : 'Thrusday',
                    '5' : 'Friday',
                    '6' : 'Saturday',
                    '7' : 'Sunday'
                  }
        day_opt = ()
        while day_opt not in day_dict:
            day_opt = input('Please input 1 - 7 for day of week or 0 for all days')
        day = day_dict[day_opt]
        return day

    day = getday()

    print('You selected "{}" as the city.'.format(city))
    print('You selected "{}" as the month.'.format(month))
    print('You selected "{}" as the day.'.format(day))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load city data from csv file
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nThe most common month is ...')
    print(df['month'].mode()[0])
    print('-'*40)

    # TO DO: display the most common day of week
    print('\nThe most common day of week is ...')
    print(df['day_of_week'].mode()[0])
    print('-'*40)

    # TO DO: display the most common start hour
    print('\nThe most common start hour is ...')
    print(df['Start Time'].dt.hour.mode()[0])
    print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nThe most commonly used Start station is ...')
    print(df['Start Station'].mode()[0])
    print('-'*40)

    # TO DO: display most commonly used end station
    print('\nThe most commonly used End station is ...')
    print(df['End Station'].mode()[0])
    print('-'*40)

    # TO DO: display most frequent combination of start station and end station trip
    print('\nThe most frequent combination of Start and End stations is ...')
    print(df.groupby(['Start Station', 'End Station']).size().nlargest(1))
    print('-'*40)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nThe total travel time is ...')
    print(df['Trip Duration'].sum())
    print('-'*40)


    # TO DO: display mean travel time
    print('\nThe mean travel time is ...')
    print(df['Trip Duration'].mean())
    print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The count of user types is ...')
    print(df.groupby(['User Type']).size())
    print('-'*40)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('\nThe count by gender is ...')
        print(df.groupby(['Gender']).size())
        print('-'*40)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nThe earliest year of birth is ...')
        print(int(df['Birth Year'].nsmallest(1)))
        print('\nThe most recent year of birth is ...')
        print(int(df['Birth Year'].nlargest(1)))
        print('\nThe most common year of birth is ...')
        print(int(df['Birth Year'].mode()))
        print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Ask user if they would like to see 5 lines of raw data.
    Iterate 5 lines of data until if user input is 'yes'
    Break if user input is 'no'
    """

    rawdata = input('\nWould you like to see 5 rows of raw data? Please enter Yes or No.\n').lower()
    if rawdata in ('yes', 'y'):
        count = 0
        while True:
            print(tb(df.iloc[count:count + 5],showindex = False, headers = 'keys',tablefmt = 'rst'))
            count += 5
            rawdata = input('\nWould you like to see 5 more rows of data? Please enter Yes or No.\n').lower()
            if rawdata not in ('yes', 'y'):
                break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
