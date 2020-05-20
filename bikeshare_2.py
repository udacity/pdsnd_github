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
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("\nEnter which city you would like to filter by:\n Chicago, Washington or New York.\n").lower()
        if city not in ('chicago','washington','new york'):
            print("\nPlease enter from the following options: \n Chicago, Washington or New York.\n")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nEnter which Month you would like to filter by:\n January, Febuary, March, April, May, June or type 'all' to see all months.\n").lower()
        if month not in ('January', 'Febuary', 'March', 'April', 'May', 'June','all'):
            print("\nPlease enter from the following options: \n January, Febuary, March, April, May, June or type 'all' to see all months.\n")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nEnter which day you would like to filter by:\n Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' to see all days.\n").lower()
        if day not in ('sunday', 'monday', 'tuesday','wednesday', 'thursday', 'friday', 'saturday','all'):
            print("\nPlease enter from the following options: \n Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' to see all days.\n")
            continue
        else:
            break

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
    #load city data
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
   	 	#filtering by month if not all
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

    if day != 'all':
        # filtering the day of week if not all
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    if common_month == 1:
        common_month = 'January'
    if common_month == 2:
        common_month = 'Febuary'
    if common_month == 3:
        common_month = 'March'
    if common_month == 4:
        common_month = 'April'
    if common_month == 5:
        common_month = 'May'
    if common_month == 6:
        common_month = 'June'
    if common_month == 7:
        common_month = 'July'
    if common_month == 8:
        common_month = 'August'
    if common_month == 9:
        common_month = 'September'
    if common_month == 10:
        common_month = 'October'
    if common_month == 11:
        common_month = 'November'
    if common_month == 12:
        common_month = 'December'
    print('The most common month is: ', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day is: ', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('Most common start hour:', common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
