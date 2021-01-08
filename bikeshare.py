import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all','january', 'february', 'march', 'april', 'may', 'june']
day_of_week = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

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
    city = input('input for city (chicago, new york city, washington)')
    while city not in CITY_DATA:
        print('error: input for city among chicago, new york city and washington')
        city = input('input for city (chicago, new york city, washington)')
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('input for month (all, january, february, ... , june)')
    while month not in months:
        print('error: input for month (all, january, february, ... , june)')
        month = input(' input for month (all, january, february, ... , june)')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('input for day of week (all, monday, tuesday, ... sunday)')
    while day not in day_of_week:
        print('error: input for day of week (all, monday, tuesday, ... sunday)')
        month = input('input for day of week (all, monday, tuesday, ... sunday)')
        

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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month_number = df['Start Time'].dt.month.mode()[0]
    most_common_month = months[common_month_number].title()
    print('the most common month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()
    print('the most common day of week:', most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('the most common start hour:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    most_commonly_used_start_station_number = df['Start Station'].value_counts()[0]
    print('most commonly used start station:', most_commonly_used_start_station,  most_commonly_used_start_station_number)

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    most_commonly_used_end_station_number = df['End Station'].value_counts()[0]
    print('most commonly used end station:', most_commonly_used_end_station,  most_commonly_used_start_end_number)


    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination_start_station_end_station = df.loc[:. 'Start Station':'End Station'].mode()[0:]
    most_frequent_combination_start_station_end_station_number = df.groupby(['Start Station':'End Station']).size().max()
    print('most frequent combination of start station and end station trip:', most_frequent_combination_start_station_end_station, most_frequent_combination_start_station_end_station_number) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Time Duration'] = df['End Time'] - df['Start Time']
    print('total travel time:', df['Time Duration'].sum())

    # TO DO: display mean travel time
    print('mean travel time:', df['Time Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types:', df['User Type'].value_count())

    # TO DO: Display counts of gender
    print('counts of gender:', df['Gender'].value_count())

    # TO DO: Display earliest, most recent, and most common year of birth
    print('earliest, most recent, and most common year of birth:', df['Birth Year'].min(), df['Birth Year'].max(), df['Birth Year'].mode())

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
