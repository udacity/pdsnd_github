import time
import pandas as pd
import numpy as np
from scipy import stats

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_LIST = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAYS_LIST = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    print('Hello! Let\'s explore some bikeshare data in three major US cities!')
    # get user input for city (chicago, new york city, washington). 
    try:
        city = input('Which city you would like to see? Please choose chicago, new york city or washington?\n')
        while city not in CITY_DATA:
            print('Seems like there is a typo or error, please consider your spelling! Make sure its lower case.')
            city = input('Which city you would like to analyze? chicago, new york city or washington?\n')
    
        # get user input for month (all, january, february, ... , june)
        month = input('Which month from january to june you would like to analyze? Or all of them?\n')
        while month not in MONTH_LIST:
            print('Seems like there is a typo or error, please consider your spelling! Make sure its lower case.')
            month = input('Which month from january to june you would like to analyze? Or all of them?\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('Which day of the week you would like to analyze? Or all of them?\n')
        while day not in DAYS_LIST:
            print('Seems like there could be a typo or error, please consider your spelling! Make sure its lower case.')
            day = input('Which day of the week you would like to analyze? Or all of them?\n')
    
        return city, month, day
    except Exception as exc:
        print('An error with your inputs occured: {}'.format(exc))
    print('-'*40)
        
def load_data(city, month, day):
    try:
        df = pd.read_csv(CITY_DATA[city])
     
        #convert the Start and End Time columns to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        #extract data from Start Time for new columns
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
        print('Could not load the file, as an Error occurred: {}'.format(e))

def time_stats(df, city):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    try:
        popular_month_num = df['Start Time'].dt.month.mode()[0]
        popular_month = MONTH_LIST[popular_month_num-1].title()
        print('The most popular month in', city, 'is:', popular_month)
    except Exception as e:
        print('Could not calculate the most common month, as an Error occurred: {}'.format(e))

    # display the most common day of week
    try:
        popular_day_of_week = df['day_of_week'].mode()[0]
        print('The most popular weekday in', city, 'is:',popular_day_of_week)
    except Exception as e:
        print('Could not calculate the most common day of week, as an Error occurred: {}'.format(e))


    # display the most common start hour
    try:
        popular_start_hour = df['hour'].mode()[0]
        print('The most popular starting hour in', city, 'is:',popular_start_hour)
    except Exception as e:
        print('Could not calculate the most common start hour, as an Error occurred: {}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df, city):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    try:
        popular_start_station = df['Start Station'].mode()[0]
        popular_start_station_amount = df['Start Station'].value_counts()[0]
        print('The most popular start station in', city, 'is:',popular_start_station, 'and was used', popular_start_station_amount, 'times.')
    except Exception as e:
        print('Could not calculate the most used start station, as an Error occurred: {}'.format(e))
    #display most commonly used end station
    try:
        popular_end_station = df['End Station'].mode()[0]
        popular_end_station_amount = df['End Station'].value_counts()[0]
        print('The most popular end station in', city, 'is:',popular_end_station, 'and was used', popular_end_station_amount, 'times.')
    except Exception as e:
        print('Could not calculate the most used end station, as an Error occurred: {}'.format(e))
    
    # display most frequent combination of start station and end station trip
    try:
        popular_trip = df.loc[:, 'Start Station':'End Station'].mode()[0:]
        popular_trip_amt = df.groupby(["Start Station", "End Station"]).size().max()
        print('the most popular trip is:\n', popular_trip, '\n and was driven', popular_trip_amt,'times')
    except Exception as e:
        print('Could not calculate the most frequent combination of start station and end station, as an Error occurred: {}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df, city):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # display total travel time
    try:
        df['Time Delta'] = df['End Time'] - df['Start Time']
        total_time_delta = df['Time Delta'].sum()
        print('the total travel time was:', total_time_delta)
    except Exeption as e:
        print('Could not calculate the total travel time of users, as an Error occurred: {}'.format(e))
    # display mean travel time
    try:
        total_mean = df['Time Delta'].mean()
        print('the average travel time was:', total_mean)
    except Exception as e:
        print('Could not calculate the average travel time of users, as an Error occurred: {}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        print('The amount and type of users in', city, 'are as follows:\n', df['User Type'].value_counts().to_frame())
    except Execption as e:
        print('Could not calculate the type of users, as an Error occurred: {}'.format(e))
    # Display counts of gender
    if city != 'washington':
        count_of_gender = df['Gender'].nunique()
        print('the count of gender is: ', count_of_gender)
        print(df['Gender'].value_counts().to_frame())
    else:
        print('The gender data for washington was not available')
     # Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()
        print('The age structure of our customers in', city, 'is:\n' 'Oldest customer was born in:', int(earliest_year),'\n' 'Youngest customer was born in:', int(most_recent_year),'\n' 'Most of our customers were born in:', int(most_common_year))
    else:
        print('The age data for washington was not available')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    start_loc = 0
    end_loc = 5

    display_active = input("Do you want to see the first five lines of raw data?: ").lower()

    if display_active == 'yes':
        while end_loc <= df.shape[0] - 1:

            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5

            end_display = input("Do you wish to see more?: ").lower()
            if end_display == 'no':
                break
                
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, city)
        station_stats(df, city)
        trip_duration_stats(df, city)
        user_stats(df,city)


        raw_data(df)
	while True: 
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
            if restart == 'yes' or restart == 'no':
                break
            else:
                print('Please enter yes or no.')


if __name__ == "__main__":
	main()

