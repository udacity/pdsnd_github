import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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
    while True:
        city = input("Write a city name: Chicago, New York City or Washington!").lower()
        if city not in CITY_DATA:
            print("wrong answer")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month? type 'all' for all months").lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("wrong answer")
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("which day? type 'all' to see all days ").lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("wrong answer")
            continue
        else:
            break

    print(month)
    print(day)
    print('-' * 40)
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
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    try:
        print('Most Common Month:', df['month'].mode()[0])
    except:
        print('you choose a single month')


    # TO DO: display the most common day of week
    try:
        print('Most Common day:', df['day_of_week'].mode()[0])
    except:
        print('you choose a single day')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    mix_station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', mix_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('total travel time:', total_travel_time / 60, " minutes")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('average travel time:', mean_travel_time / 60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()
    print('\nGender Types:\n', gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = int(df['Birth Year'].min())
        print('\nEarliest Year:', earliest_year)
    except KeyError:
        print("\nEarliest Year:\nNo data available for this month.")

    try:
        most_recent_year = int(df['Birth Year'].max())
        print('\nMost Recent Year:', most_recent_year)
    except KeyError:
        print("\nMost Recent Year:\nNo data available for this month.")

    try:
        most_common_year = int(df['Birth Year'].value_counts().idxmax())
        print('\nMost Common Year:', most_common_year)
    except KeyError:
        print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    x = 0
    while True:
        ask = input('Do you want to see raw data? Enter yes or no')
        if (ask == 'yes'):
            print (df.iloc[x:x+5])
            x+=5
        elif (ask == 'no'):
            break
        else:
            print('only answer yes or no')
    return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
