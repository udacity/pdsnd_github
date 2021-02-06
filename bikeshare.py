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
    while True:
        city = input('Would you like to see data for chicago, new york city or washington?: ').lower()
        if city in (CITY_DATA):
            print('\nSelected city: {}\n'.format(city))
            break
        else:
            print('\nNot a valid selection. Please try again: ')
            continue
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = input('What month would you like to filter by? Enter: january, february, march, april, may, june, or all: ').lower()
        if month in months:
            print('\nSelected month: {}\n'.format(month))
            break
        else:
            print('\nNot a valid selection. Please try again: ')
            continue
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
        day = input('What day of the week would you like to filter by? Enter: monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all: ').lower()
        if day in days:
            print('\nSelected day: {}\n'.format(day))
            break
        else:
            print('\nNot a valid selection. Please try again: ')
            continue
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
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day.lower() != 'all':
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
           
    return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('The most common month is ', popular_month)
    
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day of week is ', popular_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour to start to travel is ', common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('Most commonly use Start Station:', common_start_station)

    # TO DO: display most commonly used start station
    print("The most common start station is: {} ".format(df['Start Station'].mode().values[0]))
    
    # TO DO: display most commonly used end station
    print("The most common end station is: {} ".format(df['End Station'].mode().values[0]))
    
    # TO DO: display most frequent combination of start station and end station trip
    df['station_combi'] = df['Start Station'] + " " + df['End Station']
    print("The most common start and end station combo is: {} ".format( df['station_combi'].mode().values[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

   # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print("Total travel time is ",total_duration)

    # TO DO: display mean travel time
    average_trip_duration = df["Trip Duration"].mean()
    print('Average travel time is ',average_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

   # TO DO: Display counts of user types
    print("Here are the counts of various user types:")
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    # TO DO: Display counts of gender
    if 'Gender' in df:
        Gender_count = df['Gender'].value_counts()
        print(Gender_count)
    else:
        print("No Gender information in this city.")

   
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('No Birth Year information in this city')
    else:         
        earliest_birth_year = df['Birth Year'].min()
        print("Earliest birth year is ",earliest_birth_year)
        most_recent_birth_year = df['Birth Year'].max()
        print('Recent birth year is ',most_recent_birth_year)
        common_birth_year = df['Birth Year'].mode()[0]
        print('The most common birth year is',common_birth_year)
  
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
  
   while True:
        view_input_five = input('\nWould you like to see next 5 rows of data? Please enter yes or no:').lower()
        if view_input_five in ('yes', 'y'):
            n = 0     
            print(df.iloc[n:n+5])
            n += 5
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
        display_data(df) 
  

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
