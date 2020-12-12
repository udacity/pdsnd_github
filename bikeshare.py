import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all','january', 'february', 'march', 'april', 'may', 'june']
WEEK_DATA=['all', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday']

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
    city=' '
    while city.lower() not in CITY_DATA:
        city= input("Enter the name of the City either (chicago, new york city, washington): \n" )
        if city.lower() in CITY_DATA:
            city = city.lower()
            break 
            #I put break becuse is keep asking me wther if i put ture city or not
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month=' '
    while month.lower() not in MONTH_DATA:
         month = input("\nEnter the name of the month : (Enter either 'all' for no filtering or january, february, ... , june)\n")
         if month.lower() in MONTH_DATA:
              month = month.lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=' '
    while day.lower() not in WEEK_DATA:
         day = input("\nEnter the name of the Day of Week : (Enter either 'all' for no filtering or  monday, tuesday, ... sunday)\n")
         if day.lower() in WEEK_DATA:
              day = day.lower()

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
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    popular_month = df['month'].mode()[0]
    print('\nMost Common month:\n', popular_month)


    # TO DO: display the most common day of week  
    popular_day = df['day_of_week'].mode()[0]
    print('\nMost Common Day Of Week:\n', popular_day)


    # TO DO: display the most common start hour

    popular_hour = df['hour'].mode()[0]
    print('\nMost Common Start Hour:\n', str(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nMost Common Start Stations: \n', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nMost Common End Stations: \n', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    f_group = df.groupby(['Start Station' , 'End Station'])
    most_combination_sation = f_group.size().sort_values(ascending=False).head(1)
    print('\nmost frequent combination of start station and end station trip: \n', most_combination_sation)
    # most_combination_sation =( df['Start Station'] + df['End Station'] ).mode()[0]
    #print('\nmost frequent combination of start station and end station trip: \n', most_combination_sation)
 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nThe total travel time\n', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nThe mean travel time\n', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nThe counts of user type :\n', user_types)


    # TO DO: Display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print('\nThe counts of Gender :\n',str(gender))
          # TO DO: Display earliest, most recent, and most common year of birth
        birth_year = df['Birth Year'].mode()[0]
        print('\nThe most common year of birth :\n', birth_year)
        earliest_birth_year = df['Birth Year'].min()
        print('\nThe earliest birth :\n', earliest_birth_year)
        recent_birth_year = df['Birth Year'].max()
        print('\nThe recent  birth :\n', recent_birth_year)
        
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

def display_raw_data(df):
    i = 0
    raw = input("\nDo you like to view the five row of raw data? Enter yes or no.\n") # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        print(df[i:i+5])
        raw = input('\nDo you like to view the next five row of raw data? Enter yes or no.\n') # TO DO: convert the user input to lower case using lower() function
        i += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
