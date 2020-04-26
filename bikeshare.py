
import time
import pandas as pd
import numpy as np
from scipy import stats


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



MONTH_LIST = ['january',
              'february',
              'march',
             'april',
             'may',
             'june',
             'all']

DAYS_LIST = ['monday',
              'tuesday',
              'wednesday',
             'thursday',
             'friday',
             'saturday',
            'sunday',
            'all']

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
    try:
        city = input('Which city you would like to analyze? chicago, new york city or washington?')
        while city not in CITY_DATA:
            print('Seems like there is a typo or something else, please consider your spelling!')
            city = input('Which city you would like to analyze? chicago, new york city or washington?')
    
        print('your choice was: ', city)
    

        # get user input for month (all, january, february, ... , june)
        month = input('Which month you would like to analyse from january to june? Or simply all of them?')
        while month not in MONTH_LIST:
            print('Seems like there is a typo or something else, please consider your spelling!')
            month = input('Which month you would like to analyse from january to june? Or simply all of them?')

        print('your choice was: ', month)
   



    # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('Which day you would like to analyse? Or simply all of them?')
        while day not in DAYS_LIST:
            print('Seems like there is a typo or something else, please consider your spelling!')
            day = input('Which day you would like to analyse? Or simply all of them?')

        print('your choice was: ', day)
    
        return city, month, day
    except Exception as e:
        print('An error with your inputs occured: {}'.format(e))
    print('-'*40)
    

        

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
    try:
        df = pd.read_csv(CITY_DATA[city])
     
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name 
        df['hour'] = df['Start Time'].dt.hour

        # filter by month if applicable
        if month != 'all':
        # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = MONTH_LIST.index(month) + 1 
    
            # filter by month to create the new dataframe
            df = df[df['month'] == month]

    # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()] 
        return df
    except Exception as e:
        print('Couldn\'t load the file, as an Error occurred: {}'.format(e))

def time_stats(df, city):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    try:
        popular_month_num = df['Start Time'].dt.month.mode()[0]
        popular_month = MONTH_LIST[popular_month_num-1].title()
        print('The most popular month in', city, 'is:', popular_month)
    except Exception as e:
        print('Couldn\'t calculate the most common month, as an Error occurred: {}'.format(e))

    # display the most common day of week
    try:
        popular_day_of_week = df['day_of_week'].mode()[0]
        print('The most popular weekday in', city, 'is:',popular_day_of_week)
    except Exception as e:
        print('Couldn\'t calculate the most common day of week, as an Error occurred: {}'.format(e))


    # display the most common start hour
    try:
        popular_start_hour = df['hour'].mode()[0]
        print('The most popular starting hour in', city, 'is:',popular_start_hour)
    except Exception as e:
        print('Couldn\'t calculate the most common start hour, as an Error occurred: {}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df, city):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    try:
        popular_start_station = df['Start Station'].mode()[0]
        popular_start_station_amount = df['Start Station'].value_counts()[0]
        print('The most popular start station in', city, 'is:',popular_start_station, 'and was used', popular_start_station_amount, 'times.')
    except Exception as e:
        print('Couldn\'t calculate the most used start station, as an Error occurred: {}'.format(e))
    #display most commonly used end station
    try:
        popular_end_station = df['End Station'].mode()[0]
        popular_end_station_amount = df['End Station'].value_counts()[0]
        print('The most popular end station in', city, 'is:',popular_end_station, 'and was used', popular_end_station_amount, 'times.')
    except Exception as e:
        print('Couldn\'t calculate the most used end station, as an Error occurred: {}'.format(e))
    
    # display most frequent combination of start station and end station trip
    try:
        popular_trip = df.loc[:, 'Start Station':'End Station'].mode()[0:]
        popular_trip_amt = df.groupby(["Start Station", "End Station"]).size().max()
        print('the most popular trip is:\n', popular_trip, '\n and was driven', popular_trip_amt,'times')
    except Exception as e:
        print('Couldn\'t calculate the most frequent combination of start station and end station, as an Error occurred: {}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df, city):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # display total travel time
    try:
        df['Time Delta'] = df['End Time'] - df['Start Time']
        total_time_delta = df['Time Delta'].sum()
        print('the total travel time was:', total_time_delta)
    except Exeption as e:
        print('Couldn\'t calculate the total travel time of users, as an Error occurred: {}'.format(e))
    # display mean travel time
    try:
        total_mean = df['Time Delta'].mean()
        print('the mean travel time was about:', total_mean)
    except Exception as e:
        print('Couldn\'t calculate the mean travel time of users, as an Error occurred: {}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        print('The amount and type of users in', city, 'are as followed:\n', df['User Type'].value_counts())
    except Execption as e:
        print('Couldn\'t calculate the type of users, as an Error occurred: {}'.format(e))
    # Display counts of gender
    try:
        print('The amount and gender of users in', city, 'are as followed:\n',df['Gender'].value_counts())
    except Exception as e:
        print('Couldn\'t calculate the amount and gender of users, as an Error occurred: {}'.format(e))
     # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()
        print('The age structure of our customers in', city, 'is:\n' 'oldest customer was born in:', int(earliest_year),'\n' 'youngest customer: was born in:', int(most_recent_year),'\n' 'most of our customer are born in:', int(most_common_year))
    except Exception as e:
        print('Couldn\'t calculate the age structure of our customers, as an Error occurred: {}'.format(e))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, city)
        station_stats(df, city)
        trip_duration_stats(df, city)
        user_stats(df,city)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
