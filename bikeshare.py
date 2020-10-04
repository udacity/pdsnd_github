import time
import pandas as pd
import numpy as np
from collections import defaultdict
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = {
          'jan' : 1,
          'feb' : 2,
          'mar' : 3,
          'apr' : 4,
          'may' : 5,
          'jun' : 6,
          'jul' : 7,
          'aug' : 8,
          'sep' : 9,
          'oct' : 10,
          'nov' : 11,
          'dec' : 12,
    }

DAYS = {
        'mon' : 0,
        'tue' : 1,
        'wed' : 2,
        'thu' : 3,
        'fri' : 4,
        'sat' : 5,
        'sun' : 6,
   }
  

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
    while True:
        city = input("City:").lower()
        if city in CITY_DATA:
            break
        print("Invalid city. Enter one of %s" % ", ".join(CITY_DATA.keys()))
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Month:").lower()
        if month in MONTHS or month == 'all':
            break
        print("Invalid month. Enter one of %s" % ", ".join(MONTHS.keys()))
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Day:").lower()
        if day in DAYS or day == 'all':
            break
        print("Invalid day. Enter one of %s" % ", ".join(DAYS.keys()))

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
    csv_file_name = CITY_DATA[city]
    df = pd.read_csv(csv_file_name, skiprows=0, parse_dates=['Start Time', 'End Time'])
    # Filter for month
    if month != 'all':
        df_month = (df['Start Time']).dt.month == MONTHS[month]
        df = df[df_month]
    
    # Filter for day.
    if day != 'all':
        df_day = (df['Start Time']).dt.dayofweek == DAYS[day]
        df = df[df_day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    month = df['Start Time'].dt.month.value_counts().index[0]
    day = df['Start Time'].dt.dayofweek.value_counts().index[0]
    hour = df['Start Time'].dt.hour.value_counts().index[0]

    print("Most common month: %s" % calendar.month_abbr[month]) 
    print("Most common day: %s" % calendar.day_abbr[day])
    print("Most common hour: %d" % hour)
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    start_stations = df['Start Station'].value_counts()
    end_stations = df['End Station'].value_counts()
    start_end = df.groupby(['Start Station', 'End Station']).size().idxmax()
    
    print("Most common start: %s" % start_stations.index[0])
    print("Most common end: %s" % end_stations.index[0])
    print("Most common route: %s -> %s" % start_end)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time: %d s" % total_travel_time)

    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time: %d s" % mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type_count = df['User Type'].value_counts()
    print(user_type_count, "\n")
    
    if city == 'washington':
        print("No Gender for washington")
        print("No Birth Year for washington")
    else:
        gender_count = df['Gender'].value_counts(dropna=False)
        print(gender_count, "\n")
    
        yob_count = df['Birth Year'].value_counts().sort_index()
        yob_common = yob_count.idxmax()
        yob_earliest = yob_count.index[0]
        yob_latest = yob_count.index[-1]
        print("Most common YOB: %d" % yob_common)
        print("Earliest YOB: %d" % yob_earliest)
        print("Most recent YOB: %d" % yob_latest)

 print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def ask_raw_data():
    while True:
        ans = input('\nWould you like to see raw data? Enter yes or no.\n').lower()
        if ans == 'yes':
            return True
        elif ans == 'no':
            return False
        
            
city = 'chicago'

def main():
    while True:
        global city
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        for i in range(0, len(df), 5):
            raw_data = ask_raw_data()
            if raw_data:
                print(df.iloc[i:i+5])

            else:
                break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

