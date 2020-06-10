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
    print('Hello! Let\'s explore some US bikeshare data together!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("Choose a city between chicago, new york city or washington: ").lower()
    while city not in CITY_DATA: 
         print('Sorry, the city you entered is not correct. Try again.')
         city = input("Choose a city between chicago, new york city or washington: ").lower()


    # get user input for month (all, january, february, ... , june)

    month = input("Choose a month from january to june or all: ").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print('Sorry, the month you entered is not correct. Try again.')
        month = input("Choose a month from january to june or all: ").lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = input("Choose a day from monday to sunday or all: ").lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        print('Sorry, the day of week you entered is not correct. Try again.')
        day = input("Choose a day from monday to sunday or all: ").lower()

    print('-'*40)
    return city, month, day



MONTH_DATA = {'january': 1,
              'february': 2,
              'march': 3,
              'april': 4,
              'may': 5,
              'june': 6 }

DAY_DATA = {'monday': 0,
            'tuesday': 1,
            'wednesday': 2,
            'thursday': 3,
            'friday': 4,
            'saturday': 5,
            'sunday': 6 }


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    # we access the value of the dictionary through the key
    print("The city you entered is: ", city)
    print ("The month you enteres is: ", month)
    print ("The day you entered is: ", day)
    print('Hello! Let\'s explore some US bikeshare data together!')
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day -ye name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['weekday'] = df['Start Time'].dt.dayofweek
    df['month'] = df['Start Time'].dt.month
    
    if month != 'all':
        # filter the city file by month from Jan to Jun to create the new dataframe
        df = df[df['month'] == MONTH_DATA[month]]
        
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['weekday'] == DAY_DATA[day]]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    print('Most common month: ')
    print(df['month'].mode()[0])

    # display the most common day of week

    print('Most common day of week: ')
    print(df['weekday'].mode()[0])

    # display the most common start hour

    df["hour"] = df['Start Time'].dt.hour

    print('Most common start hour: ')
    print(df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
  

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most common start station: ')
    print(df['Start Station'].mode()[0])

    # display most commonly used end station
    print('Most common end station: ')
    print(df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print('Most common trip journey: ')
    df ['start_end'] = df['Start Station'] + '' + df['End Station']
    print(df['start_end'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    print ('Total travel time: ')
    print(df['Trip Duration'].sum())

    # display mean travel time

    print ('Average travel time: ')
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

 


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types

    print ('Counts of user types: ')
    print(df['User Type'].value_counts()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def gender_stats(df):
    """Displays statistics on gender of bikeshare users."""

    print('\nCalculating Gender Stats...\n')
    start_time = time.time()

    # display counts of gender types

    if 'Gender' in df.columns:
        print('Count male: ')
        print(df['Gender'].value_counts()['Male'])
        
        print('Count female: ')
        print(df['Gender'].value_counts()['Female'])

        print('Count gender: ')
        print(df['Gender'].value_counts()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def birth_year_stats(df):
    """Displays statistics on the birth years of bikeshare users."""

    print('\nCalculating Birth Year Stats...\n')
    start_time = time.time()
   

    # display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        print('Earliest year of birth: ')
        print(int(df['Birth Year'].min()))

        print('Most recent year of birth: ')
        print(int(df['Birth Year'].max()))

        print('Most common year of birth: ')
        print(int(df['Birth Year'].mode()[0]))

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
        gender_stats (df)
        birth_year_stats (df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while restart.lower() not in ("yes", "no"):
            restart = input('\nSorry, the answer you entered is not correct. If you would like to start again, choose between yes or no.\n')
        if restart.lower() != 'yes':
            break
        else:
            print 
  

if __name__ == "__main__":
	main()


	



