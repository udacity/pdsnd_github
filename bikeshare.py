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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter city (chicago, new york city, washington): ').lower()
    while city  not in CITY_DATA: 
          print('value error')
          city = input('Enter city (chicago, new york city, washington): ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month=['January','February','March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month= input('Enter month Number:').lower()
    while month not in month: 
         print('value error')
         month= input('Enter month Number:').lower()

        
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=['Sunday', 'Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    day= input('Enter day Number:  ').lower()
    while day  not in day: 
          print('value error')
          day= input('Enter day Number:  ').lower()

 
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
    return df

    """
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.dayofweek
    
    if month != 'all':
        df = df[df['month'] == int(month)]
        
    if day != 'all':
       df = df[df['day'] == int(day)]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month= df['month'].mode()[0]
    print('Most Common month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day=df['day'].mode()[0]
    print('Most Common day Of Week:', most_common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour=df['hour'].mode()[0]
    print('Most Mommon Start Hour:', most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start= df['Start Station'].mode()[0]
    print('Most Common Start Station:',most_common_start )


    # TO DO: display most commonly used end station
    most_common_end= df['End Station'].mode()[0]
    print('Most Common End Station:', most_common_end)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df['Start Station'].mode()[0]+df['End Station'].mode()[0]
    print('Most Frequent Combination Of Start Station and End Station Trip:', most_frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


        # TO DO: display total travel time
    total_trip_duration=df['Trip Duration'].sum()
    print('Total values of travel time:\n', total_trip_duration)

        # TO DO: display mean travel time
    average_trip_duration= df['Trip Duration'].mean()
    print('Average values of travel time:\n', average_trip_duration )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    if 'Gender' in df:
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print(df['Gender']) 
         # TO DO: Display earliest, most recent, and most common year of birth
        birth_year= df['Birth Year'].mode()[0]
        print('Most Common Of Birth Year:', birth_year)
        print('Earlist Of Birth Year:', birth_year)
        print('Most Recent Of Birth Year:', birth_year)
    else:
        print("Gender and Birth Year not exist")
    
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
        x=0
        while True:
            data= input("Do you want to display data? Enter yes or no ")
            if data !='yes':
                break
            else:
                print(df.iloc[x:x+5])
                x=x+5
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
           break


if __name__ == "__main__":
	main()
