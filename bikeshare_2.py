import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
list_city = ['chicago', 'new york city', 'washington']
list_month = ["january", "february", "march", "april", "may", "june", "all"]
list_day_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]

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
    city = input("\nWhich city would you like to perform an analysis- Chicago, New York City, or Washington?: \n").lower()
    while city not in list_city:
        print("\nSorry the city that you entered is not in our data. Please enter a different city: ")
        city = input("\nWhich city would you like to perform an analysis- Chicago, New York City, or Washington?:  \n").lower()
    print('\n{} is the city that you entered'.format(city))

    # get user input for month (all, january, february, ... , june)
    month = input("\nWhich month you would like to see- All, January, February, March, April, May, or June?\n").lower()
    while month not in list_month:
        print("\nSorry the month that you entered is unavaialble. Please re-enter a different month: ")
        month = input("\nWhich month you would like to see- All, January, February, March, April, May, or June?\n").lower()
    print('\n{} is the month that you entered'.format(month))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nWhich dat you would like to see- All, Monday, Tuesday, Wedsnesday, Thursday, Friday, Saturday, or Sunday?\n").lower()
    while day not in list_day_of_week:
        print("Sorry the day that you entered is unavaialble. Please re-enter a different day: ")
        day = input("\nWhich day you would like to see- All, Monday, Tuesday, Wedsnesday, Thursday, Friday, Saturday, or Sunday?\n").lower()
    print('\n{} is the day that you entered'.format(day))
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
    # Load data file into a dataframe
    df  = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new coulmns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the correspinding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("Most Popular Month is ", popular_month)
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most Popular Day is ", popular_day)
    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("Most Popular Hour is ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most Popular Start Station is ", popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most Popular End Station is ", popular_end_station)

    # display most frequent combination of start station and end station trip
    df['Combined Station'] = df['Start Station'] + ' + ' + df['End Station']
    popular_combine_station = df['Combined Station'].mode()[0]
    print("Most Popular Combined Station is ", popular_combine_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Duration in Minutes'] = df['Trip Duration'] / 60
    total_travel_time = df['Duration in Minutes'].sum()
    print(" Total travel time in minutes is: ", total_travel_time, ' minutes')

    # display mean travel time
    mean_travel_time = df['Duration in Minutes'].mean()
    print(" The mean travel time in mintues is: ", mean_travel_time, ' minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('\nThe amount and gender of users are:\n',gender)
    except Exception:
        # Washington file does not contain Gender infromation
        print('\nGender is not avaialble for this city')

    # Display earliest, most recent, and most common year of birth

    try:
        earliest_year = df['Birth Year'].min()
        print('\nThe ealiest year is ', int(earliest_year))
        most_recent_year = df['Birth Year'].max()
        print('The most recent year is ', int(most_recent_year))
        most_common_year = df['Birth Year'].mode()[0]
        print('The most common year is ', int(most_common_year))
    except Exception:
        # Washington file does not contain Birth Year infromation
        print('\nYear is not avaialble for this city')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays 5 lines of raw data"""

    show_raw_data = input('\nWould you like to see a preview of the raw data? Enter yes or no.\n').lower()

    while show_raw_data == 'yes':
        print('This is the preview of the raw data\n:', df.head())
        show_raw_data = input('\nWould you like to keep seeing this preview of the raw data? Enter yes or no.\n').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
