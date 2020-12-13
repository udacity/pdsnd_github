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
    while True:
        try:
            city = input('Would you like to see data for chicago, new york city or  washington? ').lower()
            if city in ["chicago", "new york city", "washington"]:
                break
            else:
                print("Please enter a correct city name")
        except:
                print('Oops! Something went wrong')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Would you like to see data for month (all, january, february, ... , june)? ').lower()
            if month in ["january", "february", "march", "april", "may", "june"]:
                break
            else:
                print("Please enter a correct month name")
        except:
            print('Oops! Something went wrong')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Would you like to see data for day of week (all, monday, tuesday, ... sunday)? ').lower()
            if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
                break
            else:
                print("Please enter a correct day name")
        except:
            print('Oops! Something went wrong')

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
    popular_month = df['month'].mode()[0]
    print('the most common month: ', popular_month )

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('the most commonday of week: ', popular_day )

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('the most common start hour: ', popular_month )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('the most common start station: ', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('the most common end station: ', popular_end_station )
    # TO DO: display most frequent combination of start station and end station trip
    df['Start & End Station'] = df['Start Station'] + df['End Station']
    popular_start_end_station = df['Start & End Station'].mode()[0]
    print('the most common start & end station: ', popular_start_end_station )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print('total travel time: ', total_duration)

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print('mean travel time: ', mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user = df['User Type'].value_counts()
    print('total counts of user types: ', counts_user)


    if city != 'washington':
        # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print('total counts of gender: ', gender_counts)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print(f'earliest year: {earliest_year} \n recent year: {recent_year} \n most frequent year: {common_year}')

    else:
        print('sorry, there\'s no gender or birth year data to display')


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


        show_row = input('\nWould you like to see five lines of raw data? Enter yes or no.\n').lower()
        x = 0
        if show_row == 'yes':
            print(df[x:x + 5])

            while True:
                x = x + 5
                show_row1 = input('\nWould you like to see five more? Enter yes or no.\n').lower()
                if show_row1 == 'yes':
                    print(df[x:x + 5])
                else:
                     break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
