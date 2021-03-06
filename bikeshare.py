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
    #Running this loop to ensure the correct user input gets selected else repeat
    while city not in CITY_DATA.keys():
        print("\nPlease choose your city:")
        print("\n1. Chicago 2. New York City 3. Washington")
        print("\nAccepted input:\nFull name of city; not case sensitive (e.g. chicago or CHICAGO).\nFull name in title case (e.g. Chicago).")
        #Taking user input and converting into lower to standardize them
        #You will find this happening at every stage of input throughout this
        city = input().lower()
        if city not in CITY_DATA.keys():
            print("\nPlease check your input, it doesn\'t appear to be conforming to any of the accepted input formats.")
            print("\nRestarting...")

    print(f"\nYou have chosen {city.title()} as your city.")
    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nPlease enter the month which between January to June:")
        print("\nAccepted input:\nFull month name; not case sensitive (e.g. january or JANUARY).\nFull month name in title case (e.g. January).")
        print("\n(You may also opt to view data for all months, please type 'all' to apply no month filter or january, february, ..., december for that.)")
        month = input().lower()

        if month not in MONTH_DATA.keys():
            print("\nSorry we were not able to get the  of month filter data, Please input either 'all' to apply no month filter or january, february, ... , december)\n")
            print("\nRestarting...")

    print(f"\nYou have chosen {month.title()} as your month.")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day.lower() not in DAY_DATA:
        day = input("\nWhat is day to filter data? (E.g. Input either 'all' to apply no day filter or monday, tuesday, ... , sunday)\n")
        if day.lower() in DAY_DATA:
            #We were able to get the name of the month to analyze data.
            day = day.lower()
        else:
            #We were not able to get the name of the month to analyze data so we continue the loop.
            print("Sorry we were not able to get the  of day filter data, Please input either 'all' to apply no day filter or monday, tuesday, ... , sunday)\n")
    print(f"\nYou have chosen {day.title()} as your day.")
    print(f"\nYou have chosen to view data for city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")
    print('-'*80)       
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

   
    # load the data into dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert start time column to datetimel
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month                 
    df['day'] = df['Start Time'].dt.weekday_name   
    df['hour'] = df['Start Time'].dt.hour
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
        df = df[df['day'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f"Most Popular Month (1 = January,...,6 = June): {common_month}")
    
    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print(f"Most Popular Day (Sunday, Monday,...,Saturday): {common_day}")
    
    # TO DO: display the most common hour
    common_hour = df['hour'].mode()[0]
    print(f"Most Popular hour: {common_hour}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = df['Start Station'].mode()[0]
    print(f"Most Popular start station: {commonly_start_station}")

    # TO DO: display most commonly used end station
    commonly_end_station = df['End Station'].mode()[0]
    print(f"Most Popular end station: {commonly_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print(f"Most Popular frequent_combination: {frequent_combination}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
   
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time}")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    print(f"Counts of user types: {counts_user_types}")

    # TO DO: Display counts of gender
    counts_gender = df['Gender'].value_counts()
    print(f"Counts of gender: {counts_gender}")

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth_year = df['Birth Year'].min()
    print(f"Earliest year of birth: {earliest_birth_year}")
    
    most_recent_birth_year = df['Birth Year'].max()
    print(f"Most recent year of birth: {most_recent_birth_year}")
    
    most_common_birth_year = df['Birth Year'].mode()[0]
    print(f"Most common year of birth: {most_common_birth_year}")
    
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
