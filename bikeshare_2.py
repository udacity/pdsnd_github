import time
import math
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
    city = input("Input city name here: ").lower()

    while city not in ['chicago', 'new york city', 'washington']:
        city = input(
        "City is invalid. Please input another city: ").lower()

    # get user input for month (all, january, february, ... , june)
    month = input("Input month here: ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Input day of the week here: ").lower()

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month of bike usage is: {}".format(
        str(df['month'].mode().values[0]))
    )

    # display the most common day of week
    print("The most common day of the week is: {}".format(
        str(df['day_of_week'].mode().values[0]))
    )

    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most common start hour is: {}".format(
        str(df['start_hour'].mode().values[0]))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most popular start station is: {}".format(
        df['End Station'].mode().values[0])
    )

    # display most commonly used end station
    print("The most popular end station is: {}".format(
        df['routes'].mode().values[0])
    )

    # display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station'] + " " + df['End Station']
    print("The most popular combination of start and end stations are: {}".format(
        df['routes'].mode().values[0])
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time is: {}".format(
        str(df['duration'].sum()))
    )

    # display mean travel time
    print("The average travel time is: {}".format(
        str(df['duration'].mean()))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Showing the actual count of various user types:")
    print(df['User Type'].value_counts())

    if city != 'washington':
    # Display counts of gender
        print("Total count per gender:")
        print(df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    print("The earliest birth year is: {}".format(
        str(int(df['Birth Year'].min())))
    )

    print("The latest birth year is: {}".format(
        str(int(df['Birth Year'].max())))
    )

    print("The most common birth year is: {}".format(
        str(int(df['Birth Year'].mode().values[0])))
        )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    choice = input('Would you like to read some of the raw data? Yes/No ').lower()
    print()
    if choice=='yes' or choice=='y' or choice=='yus':
        choice=True
    elif choice=='no' or choice=='n' or choice=='nope':
        choice=False
    else:
        print('You did not enter a valid choice. Let\'s try that again. ')
        display_data(df)
        return

    if choice:
        while 1:
            for i in range(5):
                print(df.iloc[i])
                print()
            choice = input('Another five? Yes/No ').lower()
            if choice=='yes' or choice=='y' or choice=='yus':
                continue
            elif choice=='no' or choice=='n' or choice=='nope':
                break
            else:
                print('You did not enter a valid choice.')
                return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
