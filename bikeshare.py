# import necessary packages

import os
import glob
import time
import pandas as pd
import numpy as np

# map city to file name
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv',
            '': '*.csv'}

# get path to data

path = input('Input the path to your data. Press enter if you are running this script from the same directory as your data.')
if path == '':
    path ='./'


while not os.path.exists(path):
    print('That is not a valid path.')
    path = input('Input the path to your data. Press enter if you are running this script from the same directory as your data.')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington, all)
    # warn for selection all due to data size

    city = input('Which city would you like to select? You may choose Chicago, New York, or Washington, or hit enter to select all.\n Warning! Selecting all will result in longer processing times: ').lower()
    print(city)

    # check input validity
    while city not in ([x for x in CITY_DATA.keys()]):
            print('That is not a valid selection. You may choose Chicago, New York, or Washington')
            city = input('Which city would you like to select? You may choose Chicago, New York, or Washington: ').lower()
            print(city)


    # get user input for month (all, january - june)

    month = input('Which month are you interested in? You may choose any month from Janary to June, or hit enter to select all ').lower()
    print(month)
    months = ['january', 'february', 'march', 'april', 'may', 'june', '']

    # check input validity
    while month not in months:
        print('That is not a valid selection. Please choose a month.')
        month = input('Which month are you interested in? You may choose any month from Janary to June, or hit enter to select all ').lower()
        print(month)

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = input('Which day of the week are you interested in? You may choose any day (Monday to Sunday), or hit enter to select all ').title()
    print(day)
    days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','']

    # check input validity
    while day not in days_of_week:
        print('That is not a valid selection. Please choose a day of the week.')
        day = input('Which day of the week are you interested in? You may choose any day (Monday to Sunday), or hit enter to select all ').lower()
        print(day)


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
    # Load the dataframe(s)

    city_file = CITY_DATA.get(city)
    fnames = glob.glob(os.path.join(path+city_file))
    df = pd.concat((pd.read_csv(f) for f in fnames), sort=True)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    #filter by month

    if month != '':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    #filter by day
    if day != '':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('\nMost Common Month:\n')
    if len(df['month'].unique()) == 1:
        print('You only ingested one month of data - {}'.format(month.title()))
    else:
        popular_month = df['month'].mode()[0]
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        popular_month = (months[popular_month-1]).title()
        print(popular_month)

    # display the most common day of week
    print('\nMost Common Day of the Week:\n')
    if len(df['day_of_week'].unique()) == 1:
        print('You only ingested one day of the week in your data - {}'.format(day))
    else:
        popular_day = df['day_of_week'].mode()[0]
        print(popular_day)

    # display the most common start hour
    print('\nMost Common Start Hour:\n')
    df['hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['hour'].mode()[0]
    print(popular_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is: {}\n'.format(popular_start_station))


    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most popular end station is: {}\n'.format(popular_end_station))


    # display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).reset_index()
    print('The most frequent combination of start station and end station is {} and {}'.format(combination['Start Station'][0],
                                                                                          combination['End Station'][0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tot_travel_time_hours = (df['Trip Duration'].sum()) // 3600
    tot_travel_time_minutes = ((df['Trip Duration'].sum()) % 3600) // 60
    tot_travel_time_seconds = ((df['Trip Duration'].sum()) % 3600) % 60
    print('The total amount of time traveled is {} hours, {} minutes, and {} seconds.'.format(tot_travel_time_hours,
                                                                                              tot_travel_time_minutes,
                                                                                              tot_travel_time_seconds))

    # display mean travel time
    mean_travel_time_hours = int((df['Trip Duration'].mean()) // 3600)
    mean_travel_time_minutes = int(((df['Trip Duration'].mean()) % 3600) // 60)
    mean_travel_time_seconds = round(((df['Trip Duration'].mean()) % 3600) % 60)
    print('\nThe average amount of time traveled per trip is {} hours, {} minutes, and {} seconds.'.format(mean_travel_time_hours,
                                                                                              mean_travel_time_minutes,
                                                                                              mean_travel_time_seconds))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    for i, v in user_types.items():
        print('There are {} of the User Type {}.'.format(v,i))

    print('\n')

    # Display counts of gender
    if 'Gender' in df.columns:

        gender = df['Gender'].value_counts()
        for i, v in gender.items():
            print('There are {} of the gender {}.'.format(v,i))
    else:
        print('You do not have gender information in your data.')

    print('\n')
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:

        earliest_birth_year = int(df['Birth Year'].min())
        latest_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print('The earliest birth year is {}\n'.format(earliest_birth_year),
              '\nThe most recent birth year is {}\n'.format(latest_birth_year),
              '\nThe most common birth year is {}\n'.format(most_common_birth_year))
    else:
        print('You do not have birth year information in your data.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays individual trip data, five records at a time."""
    view_raw = input('Would you like to view individual trip data? Enter \'Y\' for yes or any other key to skip: ').lower()
    print(view_raw)
    start_index = 0
    while view_raw == 'y':
        pd.options.display.max_columns = None
        print(df.iloc[start_index:start_index+4,:].to_string())
        view_raw = input('View more? Enter \'Y\' for yes or any other key to exit: ').lower()
        start_index += 4


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter \'Y\' or any other key to exit.\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
