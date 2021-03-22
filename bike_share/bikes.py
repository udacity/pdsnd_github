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
    city = input('\nFor which city would you like data?\n' +
                    'Chicago \n' +
                    'New York City \n' +
                    'Washington \n' +
                    '\n').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('\nSorry, data is only available for Chicago, New York City, and Washington\n').lower()

    # get user input for month (all, january, february, ... , june)
    month = input('\nWould you like data for a specific month or all?:\n').lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input('\nSorry, data is only available between January and June or all:\n').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nWould you like data for a specific day or all?:\n').lower()
    while day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        day = input('\nSorry, data is only available between Sunday through Saturday or all:\n').lower()

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

    # converts start/end time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extracting month, day of week and hour from start time
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour

    # filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

    # filter by month to create the new DataFrame
        df = df[df['month'] == month]

    # filter by day of week
    if day != 'all':
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday',
                'friday', 'saturday']
        day = days.index(day.lower()) + 1

    # filter by day to create the new DataFrame
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 'all':
        print('\nThe most common month is: {}'.format((df['month'].mode())[0]))
    else:
        print('The most common filtered month is: {}'.format(month).title())
    # display the most common day of week
    if day == 'all':
        print('\nThe most common day is: {}'.format((df['day_of_week'].mode())[0]))
    else:
        print('\nThe most common filtered day is: {}'.format(day).title())

    # display the most common start hour
    print('\nThe most common start hour is: {}'.format((df['hour'].mode())[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('\nThe most common start station is: {}'.format(df['Start Station'].mode()[0]))
    # display most commonly used end station
    print('\nThe most common end station is: {}'.format(df['End Station'].mode()[0]))
    # display most frequent combination of start station and end station trip
    df['Start_End Station'] = df['Start Station']+' - '+df['End Station']
    print('\nThe most frequent start and end stations are: {}'.format(df['Start_End Station'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    totat_trip_duration = df['Trip Duration'].sum()
    print('\nThe total travel time is: {}'.format(totat_trip_duration))

    # display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    print('\nThe average travel time is: {}'.format(mean_trip_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User types: \n{}'.format(df['User Type'].value_counts()))
    try:
        print('\nGender count: \n{}'.format(df['Gender'].value_counts()))
    except KeyError:
        print('\nNo gender data found')

    # Display earliest, most recent, and most common year of birth
    try:
        print('\nEarliest year of birth: {}'.format(int(min(df['Birth Year']))))
        print('\nMost recent year of birth: {}'.format(int(max(df['Birth Year']))))
        print('\nMost common year of birth: {}'.format(int(df['Birth Year'].mode()[0])))
    except KeyError:
        print('\nNo birth year data found')
    except ValueError:
        print('\nNo birth year data found')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    """ Shows raw data if requested by user """
    # row indexing
    show_rows = 5
    rows_start = 0
    rows_end = show_rows - 1

    print('\nWould you like to view 5 rows of individual trip data?\n')
    # gives user displayed rows
    while True:
        view_data = input('\nPlease enter yes or no\n')
        if view_data.lower() == 'yes':
            print('\nDisplaying rows {} to {}:'.format(rows_start + 1, rows_end + 1))

            print('\n', df.iloc[rows_start : rows_end + 1])
            rows_start += show_rows
            rows_end += show_rows

            print('\nWould you like to see the next {} rows?\n'.format(show_rows))
            continue
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
