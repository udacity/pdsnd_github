import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    also see below
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for the following:
    city = ''
    while city.lower()  not in ['chicago', 'new york city', 'washington']:
        city = input("which city would you like to explore?")
        if city.lower() not in ['chicago', 'new york city', 'washington']:
            print ('Sorry, please enter either' 'chicago', 'new york city', 'washington')
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    month = ''
    while month.lower() not in months:
        month = input("which month would you like to explore?")
        if month.lower() not in months:
            print('Sorry', 'please enter month between jan. and june')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("enter day to filter? " ).lower()

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
    print(df.columns)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'none':
    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','all']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
# filter by day of week if applicable
    if day != 'none':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].value_counts().idxmax()
    print('The most popular start station is {}.'.format(popular_start))

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].value_counts().idxmax()
    print('The most popular end station is {}.'.format(popular_end))

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most common used start station and end station : {}, {}".format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is :", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time is :", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        print('gender_counts are: ', df['Gender'].value_counts())
    else:
        print('No gender data available')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('earliest_year_of_birth is: ', df['Birth Year'].min())
        print('most_recent_year_of_birth is: ', df['Birth Year'].max())
        print('most_common_year_of_birth is: ', df['Birth Year'].value_counts().idxmax())
    else:
        print('No birth year data available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    # Ask user to show raw data
    display_raw_data = input('would you interested to display data?: ').lower()
    if display_raw_data in ('yes','y'):
        print('Data Limit: ', df.shape[0])
        for i in range(5, df.shape[0], 5):
            print(df.iloc[i - 5:i])
            more_data = input('Want to see more data: ').lower()
            if more_data in ('no', 'n'):
                break

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
