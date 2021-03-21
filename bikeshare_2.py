import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = {'january':1,
          'february':2,
          'march':3,
          'april':4,
          'may':5,
          'june':6}

days = {'1':'Sunday',
        '2':'Monday',
        '3':'Tuesday',
        '4':'Wednesday',
        '5':'Thursday',
        '6':'Friday',
        '7':'Saturday'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # initialze variables
    city = ''
    month = ''
    day = ''
    print('Hello! Let\'s explore some US bikeshare data!\n')
    
    # city filter
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n')
        if  city.lower() not in CITY_DATA.keys():
            print('ERROR: Please input a valid city name.')
        elif city.lower() in CITY_DATA.keys():
            city = city.lower()
            break
        print('\n')
        
    # temp to filter whether month or days question will pop
    temp = input('Would you like to filter the data by month, day, both, or not at all? Type "all" for no time filter.\n')
    print('\n')
    if temp == 'month' or temp == 'both':
        month = input('Which month? January, February, March, April, May, or June?\n')
        print('\n')
        month = month.lower()
        if month not in months.keys():
            print('Please input a valid month.')
    else:
        month = 'all'
    
    if temp == 'day' or temp == 'both':
        day = input('Which day? Please type your response as an integer (e.g., 1=Sunday, 2=Monday)\n')
        print('\n')
    else:
        print('You selected days are not specified.')
        day = 'all'
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
    
    # filter by month
    if month != 'all':
        df = df[df['month'] == months[month]]
    # filter by day
    if day != 'all':
        df = df[df['day_of_week'] == days[day].title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month =df['month'].mode()[0]
    print('Most common Month:', common_month)
    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', common_day)
    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start Station: {}'.format(common_start_station))
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most commonly used end Station: {}'.format(common_end_station))

    # display most frequent combination of start station and end station trip
    # create a new column 'Start End': use str.cat to concatenate the stations
    df['Start End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    start_end_combination = df['Start End'].mode()[0]
    print('Most frequent combination of trips from: {}.'.format(start_end_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time_hours = total_travel_time/360
    print('Total travel time: {} hours'.format(total_travel_time_hours))
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time_hours = mean_travel_time/360
    print('Mean travel time: {} hours'.format(mean_travel_time_hours))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:')
    print(user_types)
    
    # exclude Washington for missing data
    if CITY_DATA[city]!= 'washington.csv':
        # Display counts of gender
        gender = df['Gender'].value_counts()
        print('\nCounts of gender:')
        print(gender)
        # Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        print('Earliest year of birth: {}'.format(earliest_birth))
        most_recent_birth = df['Birth Year'].max()
        print('Most recent year of birth: {}'.format(most_recent_birth))
        common_birth = df['Birth Year'].mode()[0]
        print('Most common year of birth: {}'.format(common_birth))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        if view_data == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
        else:
            break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print('Starting to display your selected data!')
        print('-'*40)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
