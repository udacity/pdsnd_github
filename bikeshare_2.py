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
    city = input("Would you like to explore Chicago, New York City or Washington? ").lower()

    while city not in ['chicago', 'new york city', 'washington']:
        print('City name is not matching')
        city = input("Would you like to explore Chicago, New York City or Washington? ").lower()

    # get user input for month (all, january, february, ... , june)
    month = input('Whcih month would you like to explore?').lower()
    while month not in ['january', 'february', 'march', 'abril', 'may', 'june']:
        print('Month is invalid')
        month = input('Whcih month would you like to explore?').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Type the day name:').lower()


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create new dataframe
        df = df[df['month'] == month]

    # filter by day of week
    if day != 'all':
        # filter by day of week
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'] = df['Start Time'].dt.month_name()
    most_common_month = df['month'].mode()[0]
    print("The most common month is:", most_common_month)

    # display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    most_common_day = df['day_of_week'].mode()[0]
    print("The most common day of the week:", most_common_day)

    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    common_starting_hour = df['start_hour'].mode()[0]
    print("The most common start hour:", common_starting_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is:", common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is:", common_end_station)

   # display most frequent combination of start station and end station trip
    df['Start End Stations'] = df['Start Station'] + ' and ' + df['End Station']
    popular_combination = df['Start End Stations'].mode()[0]
    print('Most frequent combination of start station and end station: ',popular_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total Travel Time:',total_travel_time)
    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean Travel Time:',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:", user_types)

    if city != 'washington':
    # Display counts of gender
        gender_count = df['Gender'].value_counts()
        print("Counts of Gender:", gender_count)

    # Display earliest, most recent, and most common year of birth
    earliest_year_birth = df['Birth Year'].min()
    print("Earliest Year of Biarth is:", earliest_year_birth)
    most_recent_year_birth =df['Birth Year'].max()
    print('Most Recent Year of Birth: ',most_recent_year_birth)
    most_common_year_birth = df['Birth Year'].mode()[0]
    print('Most Common Year of Birth: ',most_common_year_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
