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
    print('\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input("\nSelect a city:\n Chicago\n New York City\n Washington\n\n").lower()
        if city not in cities:
            print('Oops! Please try inputting the city again.')
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    while True:
        month = input("\nSelect a month (all, January, February, March, April, May, June): \n").lower()
        if month not in months:
            print('Oops! Please try again with one of the options provided.')
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    while True:
        day = input("\nSelect a day (all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): \n").lower()
        if day not in days:
            print('Oops! Please try again with one of the options provided.')
            continue
        else:
            break

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
    df['day'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)

    # display the most common day of week
    common_day = df['day'].mode()[0]
    print('Most common day:', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('Most common start hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station:', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('Most commonly used end station:', common_end_station)

    # display most frequent combination of start station and end station trip
    frequent_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most frequent combination of start station and end station:', frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', round(total_travel_time, 2), 'seconds', '(~', int(round(total_travel_time/86400)), 'days)')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time:', round(mean_travel_time, 2), 'seconds', '(~', int(round(mean_travel_time/60)), 'minutes)')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    if city == 'new york city' or city == 'chicago':
        # Display counts of gender
        genders = df['Gender'].value_counts()
        print('\nGender Count:\n', genders)

        # Display earliest, most recent, and most common year of birth
        earliest_year = int(df['Birth Year'].min())
        print('\nEarliest year of birth:\n', earliest_year)

        recent_year = int(df['Birth Year'].max())
        print('\nMost recent year of birth:\n', recent_year)

        common_year = int(df['Birth Year'].mode()[0])
        print('\nMost common year of birth:\n', common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    yes_option = ('yes', 'y')
    no_option = ('no', 'n')
    # Prompt the user with a message and get their input.
    option_input = input('\nDo you want to see raw data?\n Yes\n No\n\n')
    # Convert their input to lowercase.
    option_input = option_input.lower()
    starting = 0

    while(option_input in yes_option):
        if option_input in yes_option:
            # call method
            print(df.iloc[starting : starting + 5])
            print('-'*40)
            starting += 5
            option_input = input('Do you want to see more raw data?\n Yes\n No\n\n')
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
