import time
import pandas as pd
import numpy as np
import datetime as dt

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
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
    cities = ['Chicago', 'New York City', 'Washington', 'All']
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All']
    
    while True:
        
        try:
            city = input("What city would you like to search: ")
            if city.title() in cities:
                break
            else:
                raise ValueError
        except ValueError:
            print("Please chose either New York City, Chicago, or Washington")

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("What month would you like to search: ")
            if month.title() in months:
                break
            else:
                raise ValueError
        except ValueError:
            print("Please choose a month between January and June")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("What day of the week would you like to search: ")
            if day.title() in days:
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid Response")

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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
    if month.lower() != 'all':
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
    
    df['Start Time'] = pd.to_datetime(df['Start Time']) #convert the Start Time column to datetime
    
    # display the most common month
    # this doesn't seem necessary as the user has chosn the month to be analyzed
    
    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_common_weekday = df['day_of_week'].mode()[0]
    print('The most common day of week is: ', most_common_weekday)

    # display the most common start hour
    df['hour_of_day'] = df['Start Time'].dt.hour
    most_common_hour = df['hour_of_day'].mode()[0]
    print('The most common hour of the day is: ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ', start_station)
    

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: ', end_station)

    # display most frequent combination of start station and end station trip
 #!!!!   frequent_combination = df['End Station'].mode()[0]
#    frequent_combination = df.groupby(['Start Station', 'End Station']).mode()[0]
#    print('The most frequent combination of start station and end station trip is: ', frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
     # display total travel time
    total_trip_duration  = (df['End Time']- df['Start Time']).sum()
    print('Total Travel Time: ', total_trip_duration)

    # display mean travel time
    average_trip_duration  = (df['End Time']- df['Start Time']).mean()
    print('Average Trip Duration: ', average_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types are as follows:\n', user_types)
    
    # Display counts of gender
    try:
        df['gender_data'] = df['Gender'].dropna(axis = 0)
        gender_count = df['gender_data'].value_counts()
        print('\nGender count is as follows:\n',  gender_count)
    except KeyError:
        print('\nNo gender data is available.')
    
    # Display earliest, most recent, and most common year of birth
    try:
        df['birth_data'] = df['Birth Year'].dropna(axis = 0)
        earliest_birth = int(df['Birth Year'].min())
        recent_birth = int(df['Birth Year'].max())
        most_common_birth = int(df['birth_data'].mode()[0])
        print('\nThe earliest year of birth is', earliest_birth)
        print('\nThe most recent year of birth is', recent_birth)
        print('\nThe most common year of birth is', most_common_birth)
    except KeyError:
        print('\nNo birth year data is available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    """Asks user if they're interested in seeing raw data, if so data is fead 5 lines at a time. """
    while True:
            
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        try:
            print_count = 0
            display_raw_data = input('\nWould you like to see raw data? ').lower()
            if display_raw_data in ['yes', 'no']:
                while display_raw_data == 'yes':
                    print(df[print_count:print_count + 5])
                    print_count += 5
                    display_raw_data = input('\nWould you like to see more raw data? ').lower()           
                if display_raw_data == 'no':
                    pass        
            else:
                raise ValueError            
        except ValueError:
            print('Invalid option, please try again.') 

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
