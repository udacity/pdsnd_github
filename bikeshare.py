import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
months = ['january','february', 'march', 'april', 'may', 'june']
days = ['monday','tuesday','wednesday','thursday','friday','satuday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
    
        city = input('choose a city to analyze between: chicago, new york city and washington').lower().strip()
        if city in cities:
            break
        else:
            print('the city is not right. tray again')

    while True:

        month = input("which month do you want to analyze? type: 'all' in case you want to analyze all of them, take into account up to june").lower().strip()
        if month in months:
            break
        elif month == 'all':
            break
        else:
            print('month is not valid, try again')
        
    while True:
    
        day = input("which day do you want to analyze? type: 'all' in case you want to analyze all of them").lower().strip()
        if day in days:
            break
        elif day == 'all':
            break
        else:
            print('day is not valid, try again')


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
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    days = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    df['day_of_week'] = df['day_of_week'].apply(lambda x: days[x])
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':

        months = ['january','february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df=df[df['month'] == month]

    if day != 'all':

        df= df[df['day_of_week']== day]
    
    return df


def time_stats(df):
    
"""Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df['month'].mode()
    print('the most common month is: ',popular_month)

    popular_day = df['day_of_week'].mode()
    print('the most common day is: ',popular_day)


    popular_start_hour = df['hour'].mode()
    print('Most Popular Start Hour:', popular_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    
"""Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    popular_start_station = df['Start Station'].mode()
    print('Most Popular start station: ', popular_start_station)

    
    popular_end_station = df['End Station'].mode()
    print('Most Popular end station: ', popular_end_station)

    best_combination = df[['Start Station', 'End Station']].mode()
    print('The most combination used start station and end station : {}, {}'\
            .format(best_combination, best_combination))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_time = df['Trip Duration'].sum()
    total_trip_duration = df['Trip Duration'].sum()
    m, s = divmod(total_trip_duration, 60)
    h, m = divmod(m, 60)
    print('the trip duration took {} hours and {} minutes'.format(h,m))
    
    mean_per_trip = df['Trip Duration'].mean()
    print('the mean of time per trip is: ',mean_per_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    count_user_types = df['User Type'].value_counts()
    print('user types:\n',count_user_types)
    if 'Gender' and 'Birth Year' in df.columns:
        
        count_gender = df['Gender'].value_counts()            
        print('Gender:\n',count_gender)
        earliest = df['Birth Year'].min()
        print('the earliest birth day is: ',earliest)
        recent = df['Birth Year'].max()
        print('the most recent birth day is: ',recent)
        common = df['Birth Year'].mode()
        print('the most common birth day is: ',common)     
         
    else:
        print('oups neither Gender nor Birth year are in Washington table')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)    
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        start_loc = 0 
        view_data = "yes"
        while view_data == "yes":
            df = pd.read_csv(CITY_DATA[city])
            view_data = input("do you want to see 5 more raw data? yes or no: ")
            if view_data == "yes":
                start_loc+=6
                print(df.head(n=start_loc))
            else:
                restart = input('\nWould you like to restart? Enter yes or no.\n')
                if restart.lower() != 'yes':
                    break
if __name__ == "__main__":
	main()
