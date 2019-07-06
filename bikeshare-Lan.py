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
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #city = input("Please enter a city (chicago, new york city, washington): ")
    while True:
        city = input("Please enter a city (chicago, new york city, washington): ")
        if city.lower() == 'chicago' or city.lower() == 'new york city' or city.lower() == 'washington':
            break
        
    # TO DO: get user input for month (all, january, february, ... , june)
    
    #print (month)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        month = input("\nPlease enter a month (all, january, february, ... , june): ")
        if (month.lower() == 'january' or month.lower() == 'february' or month.lower() == 'march' or month.lower() == 'april' or month.lower() == 'may' or month.lower() == 'june' or month.lower() == 'july' or month.lower() == 'august' or month.lower() == 'sept' or month.lower() == 'october' or month.lower() == 'november' or month.lower() == 'december'):
            break        
    while True:
        day = input("\nPlease enter a day of week (all, monday, tuesday, ... sunday): ")
        if(day.lower() == 'monday' or day.lower() == 'tuesday' or day.lower() == 'wednesday' or day.lower() == 'thursday' or day.lower() == 'friday' or day.lower() == 'saturday' or day.lower() == 'sunday'):
            break
    print('-'*40)      
    return city.lower(),month.lower(),day.lower()	
	
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
    #df = pd.read_csv(CITY_DATA[city])	
    print(city, month, day)
    if city=='chicago':
        df = pd.read_csv('chicago.csv')
        
    if city=='new york city':
        df = pd.read_csv('new_york_city.csv')        
    if city=='washington':
        df = pd.read_csv('washington.csv')    
	
	# convert the Start Time column to datetime    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day    

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
	    # use the index of the months list to get the corresponding int
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
        day = days.index(day) + 1
		
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month    
    popular_month = df['month'].mode()[0]

    print('\nMost Popular Start Month: ', popular_month)

    # TO DO: display the most common day of week    
    popular_day = df['day'].mode()[0]

    print('\nMost Popular Day: ', popular_day)

    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
	# extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('\nMost Popular Start Hour: ', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
	
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station       
    popular_start_station = df['Start Station'].mode()[0]
    print('\nMost Popular start_station: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nMost Popular end_station: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_station = df['Start Station'].mode()[0]
    print('\nMost Popular start_station:', popular_start_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].value_counts()
    print("\nThe total time is: ", total_travel_time)
    # TO DO: display mean travel time
    average_duration = df['Trip Duration'].mean
    print("\nThe evarage time (in seconds) is : ", average_duration)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    #user_types = df['User Type'].value_counts()
    print('\nUser counts: ')
    #print(user_types)	
    # TO DO: Display counts of gender
    #if df.columns=='Gender':
    if 'Gender' in df:
        genders = df['Gender'].value_counts()
        print(genders)
    else:
        print('\nNo gender data available for this city.\n')
        #df['Gender'].values == "n/a"
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].max
        most_recent_year = df['Birth Year'].min
        most_common_year = df['Birth Year'].std
        print('\nEarliest year: ')
        print(earliest_year)
        print('\nMost recent year: ')
        print(most_recent_year)
        print('\Most common year: ')
        print(most_common_year)
    else:
        print ("\nNo Birth year data available for this city. \n")
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    
    i = 0
    j= i+5
    
    while True:
        print('\n Raw data 5 rows:\n')
        print(df.iloc[i:i+5])
        i+=5
        display = input('nWould you like to see more raw data? Enter yes or no.\n')
        if display.lower() != 'yes':
            break     
        print("\n No gender data available \n")  			
def main():
    while True:
        city, month, day = get_filters()
        print(city, month, day)
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\n Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()