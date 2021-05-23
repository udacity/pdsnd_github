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
    while True:
        city = input("Input a city name from the options: 'Chicago', 'New York City', 'Washington':\n")
        if city.lower() not in ('chicago', 'new york city', 'washington'):
            print("Invalid choose. Please choose from the options provided")
        else:
            break


    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Input any month from 'January' to 'June' or Input 'All':\n")
        if month.lower() not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Invalid choice. Please choose from the options provided")
        else:
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Input any day of the week or Input 'All':\n")
        if day.lower() not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("Invalid choice. Please choose from the options provided")
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
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    #df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("Most common month: \n", popular_month)


    #display the most common day of week
   # df['day_of_week'] = df['Start Time'].dt.day_name
    popular_day_of_week = df['day_of_week'].mode()[0]
    print("Most common day of the week: \n", popular_day_of_week)


    #display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['hour'].mode()[0]
    print("Most common start hour: ", popular_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station: ", popular_start_station) 


    #display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("\nMost commonly used end station: ", popular_end_station)


    #display most frequent combination of start station and end station trip
    frequent_start_end_station = ('Start Station: ' + df['Start Station'] + ' & ' + 'End Station: ' + df['End Station']).mode()[0]
    print("\nMost frequent combination of start station and end station trip: \n", frequent_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: \n", total_travel_time)


    #display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print("Average travel time: ", avg_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("\nUser Type Information\n")
    #Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types \n", user_types)
    

    print("\nGender Information\n")
    #Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print("Counts of gender \n", gender_count)
    else:
        print("No gender information for this city\n")


    print("\nBirth Year Information\n")    
    #Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        print("Earliest birth year: ", earliest_birth_year)
        
        recent_birth_year = df['Birth Year'].max()
        print("Most recent birth year: ", recent_birth_year)
          
        popular_birth_year = df['Birth Year'].mode()[0]
        print("Most common birth year: ", popular_birth_year)
    else:
        print("No birth year information for this city")



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
