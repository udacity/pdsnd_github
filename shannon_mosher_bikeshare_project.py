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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('Please select Chicago, New York City or Washington ').lower()

    while not (city == 'chicago' or city == 'new york city' or city == 'washington'):
        city = input('Please select Chicago, New York City or Washington ').lower()

    # get user input for month (all, january, february, ... , june)
    month = input('Please select month - January, Febraury, March, April, May, June or all: ').lower()

    while not (month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all' ):
        month = input('Please select month - January, Febraury, March, April, May, June or all: ').lower()
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please select day - Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all: ').lower()

    while not (day == 'sunday' or day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'all' ):
        day = input('Please select day - Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all: ').lower()

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # find the most popular month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # display the most popular day of week    
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular day:', popular_day)

    # find the most popular hour
    # extract hour from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station: ',start_station)
    
    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most Popular End Station: ',end_station)

    # display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'].map(str) + '&' + df['End Station']
    station_combo = df['Start End'].value_counts().idxmax()
    print('Most Popular Station Combo: ',station_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
            
    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Duration Used: ',total_time)

    # display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Average Duration Used: ',avg_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
  
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender'in df.columns:
        gender_count = df['Gender'].value_counts()
        
        print(gender_count)
    
    else:
        print("No gender in this city's data")
  
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year'in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
          
        print('Earliest Birth Year: ',earliest_birth_year)
        print('Most Recent Birth Year: ',recent_birth_year)
        print('Most Common Birth Year: ',common_birth_year)
    
    else:
        print("No birth year in this city's data")
  

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