import time
import pandas as pd
import numpy as np
import calendar as cal

class Format:
    end = '\033[0m'
    underline = '\033[4m'

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
    print() 
    print('='*48 + '\n' + ' Hello! Let\'s explore some US bikeshare data!')
    print('='*48 + '\n')
    print()  
    
    # Get user input for city (chicago, new york city, washington).
    city = input('Please provide an input for ONE of the following cities (Chicago, New York City, Washington): ').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        print()
        print('='*36)
        print('**Invalid Input, Please Try Again**')
        print('='*36 + '\n')
        city = input ('Select ONE of the following cities (Chicago, New York City, Washington): ').lower()
        
    # Get user input for month (all, january, february, ... , june)
    month = input('\nPlease provide an input from "January" to "June" OR enter "all" for all months: ').lower()
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        print()
        print('='*36)
        print('**Invalid Input, Please Try Again**')
        print('='*36 + '\n')
        month = input('Select EITHER a month from "January" to "June" OR "all" for all months: ').lower()
        
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nPlease provide an input from "Monday" to "Sunday" OR enter "all" for all days: ').lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        print()
        print('='*36)
        print('**Invalid Input, Please Try Again**')
        print('='*36 + '\n')
        day = input('Select EITHER a day from "Monday" to "Sunday" OR enter "all" for all days: ').lower()
        
    print('-'*85)
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
    # Load csv data files into pandas DataFrame 
    df = pd.read_csv(CITY_DATA[city])
    
    
    # Convert the Start Time column to a datetime data type 
    df['Start Time'] = pd.to_datetime(df['Start Time'])    
    
    # Extract the hour, weekday name and month from Start Time to create 3 new columns
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
        
    # If applicable, filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe data type
        df = df[df['month'] == month]    
    
    # If applicable, filter by day
    if day != 'all':
        # filter by day of week to create the new dataframe data type
        df = df[df['day_of_week'] == day.title()]    
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print()
    print('='*48)
    print('Calculating The Most Frequent Times of Travel...')
    print('='*48)
    print()
    start_time = time.time()

    # Display the most common month
    popular_month = df['month'].value_counts().idxmax()
    popular_month_name = cal.month_name[popular_month]

    # Display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()

    # Display the most common start hour
    popular_start_hour = df['hour'].value_counts().idxmax()
    
    print(Format.underline + 'Most common month for trips' + Format.end + ': ', popular_month_name)
    print()
    print(Format.underline + 'Most common day for trips' + Format.end + ': ', popular_day)
    print()
    print(Format.underline + 'Most common start hour for trips' + Format.end + ': ', popular_start_hour)
    print()
    print('-'*40)
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print()
    print('='*49)
    print('Calculating The Most Popular Stations and Trips...')
    print('='*49)
    print()
    start_time = time.time()

    # Display most commonly used start station
    popular_start_st = df['Start Station'].value_counts().idxmax()

    # Display most commonly used end station
    popular_end_st = df['Start Station'].value_counts().idxmax()

    # Display most frequent combination of start station and end station trip
    df['Start to End Station'] = df['Start Station'] + ' and ' + df['End Station']
    popular_start_end_st = df['Start to End Station'].value_counts().idxmax()
                                                                    
    print(Format.underline + 'Most commonly used start station' + Format.end + ': ', popular_start_st)
    print()
    print(Format.underline + 'Most commonly used end station' + Format.end + ': ', popular_end_st)
    print()
    print(Format.underline + 'Most frequent combination of start station and end station trip' + Format.end + ': ', popular_start_end_st)
    print()
    print('-'*40)
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print()
    print('='*28)
    print('Calculating Trip Duration...')
    print('='*28)
    print()
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(Format.underline + 'Total travel time' + Format.end + ': ', total_travel_time, 'seconds.')
    print()

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(Format.underline + 'Mean of travel time' + Format.end + ': ', mean_travel_time, 'seconds.')
    
    print()
    print('-'*40)
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print()
    print('='*25)
    print('Calculating User Stats...')
    print('='*25)
    print()
    start_time = time.time()

    # Display counts of user types
    count_user_types = df['User Type'].value_counts().to_frame()
    print(Format.underline + 'Counts of user types:' + Format.end) 
    print()
    print(count_user_types)
    print()
    
    # Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts().to_frame()
        print(Format.underline + 'Counts of gender:' + Format.end)
        print()
        print(count_gender)
        print()
    else:
        print()
        print('='*44)
        print('Sorry, there is no data available for Gender')
        print('='*44)
        print()
        
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = int(df['Birth Year'].min())
        most_recent_birth = int(df['Birth Year'].max())
        most_common_birth = int(df['Birth Year'].mode())
        print('='*63)
        print('Displaying earliest, most recent, and most common year of birth')
        print('='*63)
        print()
        print(Format.underline + 'Earliest year of birth' + Format.end +': ' , earliest_birth)
        print()
        print(Format.underline + 'Most recent year of birth' + Format.end +': ' , most_recent_birth)
        print()
        print(Format.underline + 'Most common year of birth' + Format.end +': ' , most_common_birth)
    else:
        print()
        print('='*48)
        print('Sorry, there is no data available for Birth Year')
        print('='*48)
        print()
    print()
    print('-'*40)
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    x = 1
    pd.set_option('display.max_rows', 300001)
    pd.set_option('display.max_columns', 14)
    pd.set_option("expand_frame_repr", False)
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no (Data will be outputed to an excel file called "output.xlsx": \n')
        if raw.lower() == 'yes':
            try:
                rows = int(input('\nplease enter the number of rows you would like to see (between "1" and "300001"): \n'))
                if rows <= 300001:
                    x = 1
                    x += rows
                     print('='*24)
                    print('**PRINTING OUTPUT FILE**')
                    print('='*24 + '\n')
                    print()
                    df[:x].to_excel('output.xlsx')
                    
                else:
                    print('='*70)
                    print('**Invalid Input, Please input a number between "1" and "300001" Try Again**')
                    print('='*70 + '\n')
                    rows = int(input('please enter the number of rows you would like to see: '))
            except Exception as e:
                print("Exception occurred: {}".format(e))
                pass
        elif raw.lower() == 'no':
            break
        else:
           print('='*44)
            print('**Invalid Input, Please enter "yes or "no"**')
            print('='*44 + '\n')
            continue
            
    
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
