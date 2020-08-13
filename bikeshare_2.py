import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input(str('\nWhich city would you like to see data on?''New York City, Chicago, or Washington?\n ').lower())
        if city in ('washington', 'chicago', 'new york city'):
            break
        elif city == 'new york':
            city += ' city'
            break
        else:
            print('\n\nYour answer does not match any of the above options, please try again!\n')

    months = ['january', 'february',
            'march', 'april',
            'may', 'june', 'all']

    while True:
        month = input(str('\nWould you like to search by one of the following months?\nJanuary, February, March, April, May, June, or all of them?\n' ).lower())
        if month in months:
            break
        else:
            print ('Your answer does not match any of the above options, please try again!\n')

    days = ['all', 'monday', 'tuesday',
    'wednesday, thursday, friday',
    'saturday', 'sunday']

    while True:
        day = input(str('\nWould you like to search by one of the following days?\nSunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or all of them?\n' ).lower())
        if day in days:
            break
        else:
            print ('Your answer does not match any of the above options, please try again!\n')

    print('-'*40)
    return city, month, day

# def load_data(city, month, day):
#     """
#     Loads data for the specified city and filters by month and day if applicable.
#
#     Args:
#         (str) city - name of the city to analyze
#         (str) month - name of the month to filter by, or "all" to apply no month filter
#         (str) day - name of the day of week to filter by, or "all" to apply no day filter
#     Returns:
#         df - Pandas DataFrame containing city data filtered by month and day
#     """
#
#
#
#     return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    popular_start = df['Start Station'].mode()[0]
    print('Most Popular Start:', popular_start)

    popular_end = df['End Station'].mode()[0]
    print('Most Popular End:', popular_end)

    print('Most frequent combination start and end station:',(df['Start Station'] + ' --- ' + df['End Station']).mode()[0])


    # display most commonly used start station
    # display most commonly used end station
    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    print('Total travel time: ',df['Trip Duration'].sum())

    print('Average travel time', df['Trip Duration'].mean())

    # display total travel time
    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""
#     print(df)
    print('\nCalculating User Stats...\n')
    start_time = time.time()
 # Display counts of user types
    popular_user = df['User Type'].mode()[0]
    print('User Counts:', df.groupby(['User Type'])['End Station'].count())

    if city == 'washington':
        print("gender counts are not available in washington")
        print("earliest year, most recent year and most common year of birth are not available in washington")

    else:
        print('Gender Counts:', df.groupby(['Gender'])['Birth Year'].count())

        genders = [{'Male','Female'}]
        gender_types = pd.DataFrame(genders, index=['Gentypes'])
        print('Gentypes')

        earliest_year =df['Birth Year'].min()
        print('Most Earliest Year:', earliest_year)

        last_year =df['Birth Year'].max()
        print('Most Recent Year:', last_year)

        popular_year = df['Birth Year'].mode()[0]
        print('Most Popular Year:', popular_year)

    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    df['weekday'] = df['Start Time'].dt.dayofweek
    popular_day = df['weekday'].mode()[0]
    print('Most Popular Day:', popular_day)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start = 0
    raw_data = input("Would you like to see raw data 5 lines at a time? yes or no: ").lower()
    while True:
        if raw_data != 'no':
            print(df.iloc[start:start + 5])
            start += 5
            raw_data = input("Would you like to continue? yes or no: ").lower()
        else:
            break

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
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()

#     print(df)
    return df

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #df = load_data('chicago', 'march', 'monday')
        time_stats(df)
        display_data(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
