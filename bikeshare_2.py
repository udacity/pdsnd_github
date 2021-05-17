import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input(
        'Enter valid city name(chicago, new york city, washington)')
    while city.lower() not in ('chicago', 'new york city', 'washington'):
        city = input(
            'Enter valid city name(chicago, new york city, washington)')

    # get user input for month (all, january, february, ... , june)
    month = input('Enter valid month (all, january, february, ... , june)')

    while month.lower() not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
        month = input('Enter valid month (all, january, february, ... , june)')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter the day of the week')
    while day.lower() not in ('all', 'monday', 'tuesday', 'sunday'):
        day = input('Enter the day of the week')

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
        df - Pandas  DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_weak'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february',
                  'march', 'april', 'may', 'june']
        months = months.index(month)+1

        df = df[df['month'] == months]

    if day != 'all':
        df = df[df['day_of_weak'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(df['Start Time'].dt.month.mode()[0])
    # display the most common day of week
    print(df['Start Time'].dt.weekday_name.mode()[0])

    # display the most common start hour
    print(df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('display most commonly used start station:',
          df['Start Station'].mode()[0])

    # display most commonly used end station
    print('display most commonly used end station',
          df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print(' display most frequent combination of start station and end station trip',
          (df['Start Station'] + "||" + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    duration = df['Trip Duration'].sum()
    print('display total travel time:', duration)
    # display mean travel time
    mean = duration.mean()
    print('mean travel time', mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_type = df.groupby(['User Type']).count()
    print('counts of user types:', count_type)
    # Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df.groupby(['Gender']).count()
        print('counts of gender', count_gender)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        most_recent = df['Birth Year'].min()
        most_common_year = df['Birth Year'].mode()[0]
        print('most common year of birth', most_common_year)
        print('most recent year of birth', most_recent)

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

        line = 1
        while True:
            raw = input(
                '\nWould you like to see some data? Enter yes or no.\n')
            if raw.lower() == 'yes':
                print(df[line:line+5])
                line = line+5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
