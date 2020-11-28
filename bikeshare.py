import time
import datetime

import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv',  'Washington': 'washington.csv'}
cities = ['Chicago', 'New York City', 'Washington']
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_input_data(accepted_values):
    while True:
        # show possibilites
        str_accepted_values = ", or ".join(accepted_values)
        print("({0})".format(str_accepted_values))
        # get user choice
        response = str(input())
        # format to lower caps
        accepted_values_lower = [v.lower() for v in accepted_values]
        lower_response = response.lower()
        # repeat until choise is desired
        if lower_response in accepted_values_lower:
            return accepted_values_lower.index(lower_response)
        else:
            print('Wrong answer! please try again!')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    days.append('all')
    months.append('all')
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Please choose city:\n')
    city = get_input_data(cities)
    print('Please choose month\n')
    month = get_input_data(months)
    print('Please choose day of week\n')
    day = get_input_data(days)
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    file_name = CITY_DATA[cities[city]]
    print(file_name)
    df = pd.read_csv(file_name)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if months[month] != 'all':
        month_id = month + 1
        df = df[df['month'] == month_id]
    if days[day] != 'all':
        df = df[df['day_of_week'] == days[day]]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most common start month:', months[common_month])
    common_day = df['day_of_week'].mode()[0]
    print('Most common start day:', common_day)
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common start hour:', common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    common_start_station = df['Start Station'].mode()[0]
    print('Most common start station:', common_start_station)
    common_end_station = df['End Station'].mode()[0]
    print('Most common end station:', common_end_station)
    # display most commonly used start station
    combinations = df.groupby(['Start Station', 'End Station'])
    # display most commonly used end station
    most_common_combination = combinations.size().idxmax()
    print('Most common combination:', most_common_combination)
    # display most frequent combination of start station and end station trip
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    duration = (df['End Time'] - df['Start Time'])
    # TO DO: display total travel time
    sum_duration = duration.sum()
    print("Total travel time: {}".format(sum_duration))
    # TO DO: display mean travel time
    mean_duration = duration.mean()
    print("Mean travel time: {}".format(mean_duration))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    unique_count_of_usertype = len(df['User Type'].unique())
    print("Unique count of user type: {}".format(unique_count_of_usertype))
    unique_count_of_gender = len(df['Gender'].unique())
    print("Unique count of gender: {}".format(unique_count_of_gender))
    earliest_birth = df['Birth Year'].min()
    recent_birth = df['Birth Year'].max()
    common_birth = df['Birth Year'].mode()[0]
    print("Earliest: {}, most recent: {}, and most common year of birth: {}".format(
        earliest_birth, recent_birth, common_birth))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def print_raw_data(df, index, show_rows):
    print(df.iloc[:][index:index+show_rows])


def main():
    index = 0
    show_next_n_rows = 5
    message_user_wants_raw_data = '\nWould you like to see {0} lines of raw data? Enter yes or no.\n'.format(
        show_next_n_rows)
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        try:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            while(input(message_user_wants_raw_data).lower() == 'yes'):
                print_raw_data(df, index, show_next_n_rows)
                index += show_next_n_rows
        except Exception as e:
            print(
                "No data has been found, please change parameters, exception details:\n{0}".format(e))
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
