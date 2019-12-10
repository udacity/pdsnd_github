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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input('Would you like to see data for Chicago, New York, or Washington? ')).lower()
    while(city != 'chicago' and city != 'new york' and city != 'washington'):
        city = str(input('Please choose one of the cities to see data Chicago, New York, or Washington. ')).lower()
    
    if(city == 'new york'):
        city = 'new york city'
    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input('Would you like to filter the data by (January, February, March, April, May, June) or not? ')).lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while(month != 'not' and month not in months):
        month = str(input('Please choose one of the months (January, February, March, April, May, June) or not. ')).lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input('Would you like to filter the data by (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturdaye) or not? ')).lower()
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    while(day != 'not' and day not in days):
        day = str(input('Please choose one of the days (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturdaye) or not. ')).lower()

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
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'not':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'not':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Month:', popular_month)

    # TO DO: display the most common day of week
    popular_dow = df['day_of_week'].mode()[0]
    print('Most Frequent Day of Week:', popular_dow)

    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Frequent Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Frequent End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_both_station = (df['Start Station'] + ', ' + df['End Station']).mode()[0]
    print('Most Frequent Both Station:', popular_both_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip = df['Trip Duration'].sum()
    print('Total Trip Duration:', total_trip)

    # TO DO: display mean travel time
    mean_trip = df['Trip Duration'].mean()
    print('Average Trip Duration:', mean_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCount of User Types:\n', df['User Type'].value_counts())

    if('Gender' in df.columns):
        # TO DO: Display counts of gender 
        print('\nCount of Gender:\n', df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print('\nEarliest Year of birth:', earliest_year)
        print('\nMost Recent Year of birth:', most_recent_year)
        print('\nMost Common Year of birth:', most_common_year)
    else:
        print('\nWashington file does not have Gender and Year of birth data.')

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
