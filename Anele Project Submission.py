Explore US Bikeshare Data

Use Python to understand U.S. bikeshare data. Calculate statistics and build an interactive environment where a user chooses the datata and filter for a dataset to analyze


:::::::GUIDELINES:::::::::

import time
import pandas as pd
import numpy as np

These are new changes

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


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()



:::::::SUBMISSION:::::::::

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
    print('Hello my name is Anele Vala!')
   
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

# TO DO: get user input for month (all, january, february, ... , june)

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    print('The list of cities to choose from:')
    print('Chicago: 1')
    print('New York: 2')
    print('Washington: 3')


    
def get_filter_city():
    
    city = input('Please select a number between 1, 2 and 3 to choose the city: ')
    city = city.lower()
    while True:    
            if city == '1' or city == 'chicago':
                print("\nChicago\n")
                return 'chicago'
            if city == '2' or city == 'new york':
                print("\nNew York City\n")
                return 'new york city'
            elif city == '3' or city == 'washington':
                print("\nWashington\n")
                return 'washington'
            else:
                print('\nPlease enter 1, 2 or 3\n')
                city = input('Please choose the city: ')
                city = city.lower()
    return city
def get_filter_city():
    
    city = input('Please select a number between 1, 2 and 3 to choose the city: ')
    city = city.lower()
    while True:    
            if city == '1' or city == 'chicago':
                print("\nChicago\n")
                return 'chicago'
            if city == '2' or city == 'new york':
                print("\nNew York City\n")
                return 'new york city'
            elif city == '3' or city == 'washington':
                print("\nWashington\n")
                return 'washington'
            else:
                print('\nPlease enter 1, 2 or 3\n')
                city = input('Please choose the city: ')
                city = city.lower()
    return city

# TO DO: get user input for month (all, january, february, ... , june)



def get_filter_month():
    
    print('Please choose a month from these ones listed:')
    print('January: 1')
    print('February: 2')
    print('March: 3')
    print('April: 4')
    print('May: 5')
    print('June: 6')
    
    month = input('Please select a number between 1, 2, 3, 4, 5 and 6 to choose a month: ')
    month = month.lower()
    while True:    
            if month == '1' or month == 'January':
                print("\nJanuary\n")
                return 'January'
            if month == '2' or month == 'February':
                print("\nFebruary\n")
                return 'February'
            if month == '3' or month == 'March':
                print("\nMarch\n")
                return 'March'
            if month == '4' or month == 'April':
                print("\nApril\n")
                return 'April'
            if month == '5' or month == 'May':
                print("\nMay\n")
                return 'May'
            elif month == '6' or month == 'June':
                print("\nJune\n")
                return 'June'
            else:
                print('\nPlease enter 1, 2, 3, 4, 5 or 6\n')
                month = input('Please choose the month from the list: ')
                month = month.lower()
    return month

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)



def get_filter_day():
    
    print('Please choose a day of the week from the list provided:')
    print('Monday: 1')
    print('Tuesday: 2')
    print('Wednesday: 3')
    print('Thursday: 4')
    print('Friday: 5')
    print('Saturday: 6')
    print('Sunday: 7')

    day = input('Please select a number between 1, 2, 3, 4, 5, 6 and 7 to choose a day of the week: ')
    day = day.lower()
    while True:    
        if day == '1' or day == 'Monday':
                print("\nMonday\n")
                return 'Monday'
        if day == '2' or day == 'Tuesday':
                print("\nTuesday\n")
                return 'Tuesday'
        if day == '3' or day == 'Wednesday':
                print("\nWednesday\n")
                return 'Wednesday'
        if day == '4' or day == 'Thursday':
                print("\nThursday\n")
                return 'Thursday'
        if day == '5' or day == 'Friday':
                print("\nFriday\n")
                return 'Friday'
        if day == '6' or day == 'Saturday':
                print("\nSaturday\n")
                return 'Saturday'
        elif day == '7' or day == 'Sunday':
                print("\nSunday\n")
                return 'Sunday'
        else:
                print('\nPlease enter 1, 2, 3, 4, 5, 6 or 7\n')
                day = input('Please choose the day from the list provided: ')
                day = day.lower()
    return day



def load_data(city):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    start_time = time.time()

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'], errors='coerce')

    # month, day of week and hour 
    df['month'] = df['Start Time'].dt.month                 # range (1-12)
    df['day_of_week'] = df['Start Time'].dt.dayofweek       # range (0-6)
    df['hour'] = df['Start Time'].dt.hour                   # range (0-23)

    return df



def time_stats(df):
    """Display statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)


    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)


    # TO DO: display most commonly used end station

    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)


    # TO DO: display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df


def trip_duration_stats(df):
    """Display statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")


    # TO DO: display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    return df

def user_stats(df, city):
    """Display statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df

def display_raw_data(df):
    start_loc = 0
    end_loc = 6
    display_active = input("Do you want to see the raw data?: ").lower()

    if display_active == 'yes':
        while end_loc <= df.shape[0] - 1:

            print(df.iloc[start_loc:end_loc,:])
            start_loc += 6
            end_loc += 6

            end_display = input("Do you wish to continue?: ").lower()
            if end_display == 'no':
                break


def main():
    while True:
        city = get_filters()
        city = get_filter_city()
        moth = get_filter_month()
        day = get_filter_day()
        df = load_data(city)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == '__main__':
    main()
