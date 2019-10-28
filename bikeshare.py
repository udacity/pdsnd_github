import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
        invalid_inputs = "Sorry, Invalid input. Please try again" 
    
    print('Hello! Let\'s explore some US bikeshare data!\n')
   
    # TO DO: get user raw_input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city = input("\nWhich city would you like to filter by: New York, Chicago or Washington?\n").lower()
        if city in ['chicago', 'new york', 'washington']:
            break
        else:
            print(invalid_inputs)
    
    # TO DO: get user raw_input for month (all, january, february, ... , june)
    while True :
        month = input("\nWhich month would you like to filter by: January, February, March, April, May, June or type 'all' if you do not have any preference?\n").lower()
        if month in ["january", "february", "march", "april", "may", "june", "all"]:
            break
        else:
            print(invalid_inputs)

    # TO DO: get user raw_input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input("\nWhich day would you like to filter by: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference.\n").lower()
        if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
            break
        else:
            print(invalid_inputs)


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
    file_name = CITY_DATA[city]
    print ('\nAccessing data from: {}\n'.format(file_name))
    df = pd.read_csv(file_name)
    
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # filter by month if applicable
    if month != 'all':
        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month

        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Start Time'].dt.month == month]

    # filter by day if applicable
    if day != 'all':
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        
        # filter by day of week to create the new dataframe
        df = df[df['Start Time'].dt.weekday_name == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nMost Frequent Times of Travel...\n')
    start_time = time.time()

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(arg = df['Start Time'], format = '%Y-%m-%d %H:%M:%S')

    # Create new columns for month, weekday, hour
    month = df['Start Time'].dt.month
    week_day = df['Start Time'].dt.weekday_name
    hour = df['Start Time'].dt.hour
    
    # TO DO: display the most common month
    popular_month = month.mode()[0]
    print('\nMost common month is: {}\n'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = week_day.mode()[0]
    print('\nMost common day of week is: {}\n'.format(popular_day))

    # TO DO: display the most common start hour
    popular_hour = hour.mode()[0]
    print('Most frequent start hour is: {}\n'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nMost Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nMost commonly used start station is: ',df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print('\nMost commonly used end station is: ',df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    combine_stations = df['Start Station'] + "*" + df['End Station']
    common_station = combine_stations.value_counts().idxmax()
    print('\nMost frequent used combinations are:{} to {}\n'.format(common_station.split('*')[0], common_station.split('*')[1]))

    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # Convert seconds to readable time format
    def calculate_time(time):
        time1 = time
        days = time1 // (86400)
        time1 %= (86400)
        hours = time1 // 3600
        time1 %= 3600
        minutes = time1 // 60
        time1 %= 60
        seconds = time1
        print('{} days {} hours {} minutes {} seconds'.format(days, hours, minutes, seconds))

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('\nTotal travel time is: ')
    calculate_time(total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('\nMean travel time is: ')
    calculate_time(mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    subscribers_count = df['User Type'].str.count('Subscriber').sum()
    customers_count = df['User Type'].str.count('Customer').sum()
    print('\nNumber of subscribers is: {}\n'.format(int(subscribers_count)))
    print('\nNumber of customers is: {}\n'.format(int(customers_count)))

    # Display counts of gender
    if('Gender' in df):
        male_count = df['Gender'].str.count('Male').sum()
        female_count = df['Gender'].str.count('Female').sum()
        print('\nNumber of male users is: {}\n'.format(int(male_count)))
        print('\nNumber of female users is: {}\n'.format(int(female_count)))

    # Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        earliest_year = df['Birth Year'].min()
        print('\n Oldest Birth Year is: {}\n '.format(int(earliest_year)))
        recent_year = df['Birth Year'].max()
        print('\n Youngest Birth Year is: {}\n'.format(int(recent_year)))
        common_year = df['Birth Year'].value_counts().idxmax()
        print('\n Most popular Birth Year is: {}\n'.format(int(common_year)))

    print("\nThis took %s seconds." % (time.time() - start_time))    
    print('-'*40)
  
def raw_data(df):
    user_input = input('\nDo you want to see raw data? Enter yes or no.\n')
    line_number = 0

    while True :
        if user_input.lower() != 'no':
            print(df.iloc[line_number : line_number + 5])
            line_number += 5
            user_input = input('\nDo you want to see more raw data? Enter yes or no.\n')
        else:
            break     

def main():
    while 1 == 1 :
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