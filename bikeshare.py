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
    
    city = ''
    
    city = str(input("Which city data would you like to explore? Please choose between Chicago, Washington or New York City. \n"))
    city = city.lower()
    
    while True:
        if city not in CITY_DATA.keys():
            #.keys allows to look at keys in dictionary above 
           city = input("Unfortunately, we don't have data for that city! Please try again!\n")
           continue 
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = ''
    
    month = str(input("Great! What month would you like to explore?\nYou can choose to either see data for all months, January, February, March, April, May or June.\n"))
    month = month.lower()
    
    while True:
        if month not in months:
            month = input("Unfortunately, we don't have data for that month! Please try again.\n")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    
    day = str(input("Great! What day would you like information for?\nIf you'd like information on all days, type 'all' \n"))
    day = day.lower()
    
    while True: 
        if day not in days:
            day = input("That is not a correct day. Please try again. \n")
        else:
            break

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
    
    df['month'] = df['Start Time'].dt.strftime('%b')
    df['day'] = df['Start Time'].dt.weekday_name.str.lower()
    df['hour'] = df['Start Time'].dt.hour.astype(str)
    
    month_dict = {'january':'Jan', 
                  'february':'Feb', 
                  'march':'Mar', 
                  'april':'Apr', 
                  'may':'May', 
                  'june': 'Jun'}
    
    if month != 'all':
        new_month = month_dict[month]
        df = df[df['month']==new_month]
        
    if day in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
        df = df[df['day']==day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print('\nThe most common month is: ' + popular_month)
    
    # TO DO: display the most common day of week
    popular_day = df['day'].value_counts().idxmax()
    print('\nThe most common day of week is: ' + popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('\nThe most common start hour is: ' + popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('\nThe most common used Start Station is: ' + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('\nThe most common used End Station is: ' + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_combination = df.groupby(['Start Station']) ['End Station'].value_counts().idxmax()
    common_combination = ' and '.join(common_combination)
    print('\nThe most frequent combination of Start Station and End Stations are: ' + common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    # TO DO: display total travel time
    total_travel_time = (df['Trip Duration'].sum() / 60)

    print('\nThe total travel time on this day was: ' + str(total_travel_time) + ' minutes')

    # TO DO: display mean travel time
    mean_travel_time = (df['Trip Duration'].mean() / 60)
    print('\nThe mean travel time on this day was: ' + str(mean_travel_time) + ' minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nDifferent user types: \n' + str(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts()
        print('\nUser Genders: \n' + str(count_gender))
    else:
        print('\nSorry there is no Gender data for this city.')
    

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Gender' in df.columns:
        earliest_birth = df['Birth Year'].min()
        print('\nThe earliest birth year is: ' + str(earliest_birth))
   
        most_recent_birthyear = df['Birth Year'].max()
        print('\nThe most recent birth year is: ' + str(most_recent_birthyear))
    
        most_common_birthyear = df['Birth Year'].value_counts().idxmax()
        print('\nThe most common birth year is: ' + str(most_common_birthyear))
    else:
        print('\nSorry, there is no data on Birth Years for this city.')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def show_raw_data(df, start, stop):
    return df.loc[start:stop]

def display_raw_data(df):
    
    raw_data = input('\nWould you like to see some raw data? \n')
    
    start_index = 0
    stop_index = 5
    
    while raw_data.lower() == 'yes':
        print(show_raw_data(df, start_index, stop_index))
        more_raw_data = input('\nWould you like to see more raw data? \n')
        if more_raw_data == 'yes':
            #iterate through df
            start_index += 5
            stop_index += 5
            print(show_raw_data(df, start_index, stop_index))
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display_raw_data(df)

        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()