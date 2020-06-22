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
    cities = ['chicago', 'new york city', 'washington']

    validCity = False
    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington?').lower()
        if city in cities:
            break

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september','october', 'november', 'december']

    while True:
        month = input('Which month - January, February, March, April, May, or June?').lower()
        if month in months:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'sunday']
    while True:
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday:').lower()
        if day in days:
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day_of_week'] = pd.DatetimeIndex(df['Start Time']).weekday_name

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
    df['day_of_week'] = pd.DatetimeIndex(df['Start Time']).week
    df['month'] = pd.DatetimeIndex(df['Start Time']).month

    popular_hour = df['hour'].mode()[0]
    common_day_of_week = df['day_of_week'].mode()[0]
    popular_month = df['month'].mode()[0]

    # display the most common month

    print('Popular Hour', popular_hour)
    print('Common day of week', common_day_of_week)
    print('Popular Month', popular_month)

    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # print(df['Start Station'])
    # print(df['End Station'])

    Start_Station = df['Start Station'].mode()[0]
    end_station = df['End Station'].mode()[0]

    df['start_end_trip_station'] =  df['Start Station'] + df['End Station']
    start_end_trip_station = df['start_end_trip_station'].mode()[0]

    # display most commonly used start station
    print('Common start station', Start_Station)

    # display most commonly used end station
    print('Common end station', end_station)

    # display most frequent combination of start station and end station trip
    print('most frequent combination of start station and end station trip', start_end_trip_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_duration_sum = df['Trip Duration'].sum()
    print("Total trip duration in seconds:", trip_duration_sum)

    # display mean travel time
    trip_duration_mean = df['Trip Duration'].mean()
    print("Mean of total trip duration in seconds:", trip_duration_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    if city.lower() != 'washington':
        # Display counts of gender
        gender = df['Gender'].value_counts()
        print(gender)
        # Display earliest, most recent, and most common year of birth

        common_birth_year = df['Birth Year'].mode()[0]
        earliest_birth_year = df['Birth Year'].max(axis=0)
        recent_birth_year = df['Birth Year'].min(axis=0)

        print('Most common Birth Year', common_birth_year)
        print('Earliest Birth Year', earliest_birth_year)
        print('Recent Birth Year', recent_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    data = 0
    while True:
        rowans = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        if rowans.lower() == 'yes':
            print(df[data : data+5])
            data += 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
main()
