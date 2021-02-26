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

    while True:
        city = input("Enter the city name please: ").lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print("Invalid input, please try again.")

        else:
            print(city)
            break


    month = input("Pleae Enter the month: ").lower()

    
    day = input("Please Enter the day: ").lower()

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

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]


        df['day_of_week'] = df['Start Time'].dt.weekday_name

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

    df['day'] = df['Start Time'].dt.weekday_name
    common_day = df['day'].mode()[0]
    print('Most Common Day:', common_day)

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print(f"Most Common Start Station has Used is {df['Start Station'].mode()[0]}")

    print(f"Most Common End Station has Used is {df['End Station'].mode()[0]}")

    print(f"Common Start Station is {df['Start Station'].mode()[0]} and for End Station is {df['End Station'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print(f"Total of Travel Time is {df['Trip Duration'].sum()}")

    print(f"Average of Travel Time is {df['Trip Duration'].mean()}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print(f"counts of User Types are: \n{df['User Type'].value_counts()}")


    if 'Gender' in df:
        print(f"counts of Gender are: \n {df['Gender'].value_counts()}")
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')


    print(f"summary statistics: ")

    print(df.describe())


    if 'Birth Year' in df:
        print(f"Most common year of birth is:  {df['Birth Year'].mode()[0]}")
        print(f"Most recent year of birth is:  is {df['Birth Year'].max()}")
    else:
        print('Birth Year stats cannot be calculated because Gender does not appear in the dataframe')

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
