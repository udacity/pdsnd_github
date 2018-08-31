#import all necessary packages and functions
import time
import pandas as pd
import numpy as np

## Filenames
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

    # get user input for city
    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input('\nWhich city would you like to analyze? Enter: {}\n'.format(', '.join(cities).title()))
        if city in cities:
            break
        print('Please enter a valid response.')

    # get user input for month
    while True:
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = input('\nWhich month would you like to analyze? Enter: {}\n'.format(', '.join(months).title()))
        if month in months:
            break
        print('Please enter a valid month.')

    # get user input for day of week
    while True:
        days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = input('\nWhich day of week would you like to analyze? Enter: {}\n'.format(', '.join(days).title()))
        if day in days:
            break
        print('Please enter a valid response.')

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


def popular_time_stats(df):
    """Displays statistics on the most popular times of travel."""

    print('\nCalculating The Most Popular Times of Travel...\n')
    start_time = time.time()

    # most popular month
    month = df.month.mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_popular_month = months[month - 1].capitalize()
    print('Month:', most_popular_month)

    # most popular day of week
    popular_day = df['day_of_week'].value_counts().reset_index()['index'][0]
    print('Day:', popular_day)

    # most popular start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df.hour.mode()[0]
    print('Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def popular_station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # most popular start and end stations
    start_station = df['Start Station'].value_counts().reset_index()['index'][0]
    end_station = df['End Station'].value_counts().reset_index()['index'][0]
    print('Start Station: ', start_station)
    print('End Station: ', end_station)

    # most popular trip
    result = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\nTrip:\n')
    print(result)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # total and average trip durations
    df['Travel Time'] = pd.to_datetime(df['End Time']) - df['Start Time']
    print('Total:', np.sum(df['Travel Time']))
    print('Average:', np.mean(df['Travel Time']))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # User Types
    print('Breakdown of User Types:')
    users = df['User Type'].value_counts()
    print(users)

    # Gender
    try:
        print('\nBreakdown of Gender:')
        gender = df['Gender'].value_counts()
        print(gender)
    except:
        print('No gender data to share.')

    # Years of Birth
    try:
        print('\nYears of Birth:')
        oldest = np.min(df['Birth Year'])
        youngest = np.max(df['Birth Year'])
        pop_year = df['Birth Year'].mode()[0]
        print('Oldest:', oldest)
        print('Youngest:', youngest)
        print('Most Popular:', pop_year)
    except:
        print('No birth year data to share.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        popular_time_stats(df)
        popular_station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
