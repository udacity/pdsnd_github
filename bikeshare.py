"""
The bunch of codes analyzes US bikeshare data for 3 cities(Washington , New York City and Chicago) and
interactively displays a summary statistics for eachself.

Ntare Guy Elkana 
"""
#import libraries 
import pandas as pd
import numpy as np
import time

CITY_DATA = { 
              'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' 
            }

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
    
    city = input('Would you like to see data for Chicago, New York, or Washington, Please Enter your city: ').lower()
    while city not in ['chicago','new york city','washington']:
        city = input('City inputed not valid, Please enter sa valid city: ').lower()
    
    # get user input for month (all, january, february, ... , june)    
    month = input('Please the month name: ').lower()
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter a day of the week: ')


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
    #import files
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))
    
    #Convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    #extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month,:]
        
    if day != 'all':
         # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day,:]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

     # display the most common month
    print("The most common month is: {}".format(
        str(df['month'].mode().values[0]))
    )

    # display the most common day of week
    print("The most common day of the week: {}".format(
        str(df['day_of_week'].mode().values[0]))
    )

    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most common start hour: {}".format(
        str(df['start_hour'].mode().values[0]))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('\n The most common Start station: {}'.format(
        df['Start Station'].mode().values[0]
    ))
    
    # display most commonly used end station
    print('\n The most common End station: {}'.format(
        df['End Station'].mode().values[0]
    ))
    # display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+" "+df['End Station']
    print('\n The most frequent Station is: {}'.format(df['routes'].mode().values[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['duration'] = df['End Time'] - df['Start Time']
    print('\n The Total Trip duration is: {}'.format(df['duration'].sum()))
    # display mean travel time
    print('\n The mean travel time is: {}'.format(df['duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 
    


    
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\n The number of User types is: {}'.format(df['User Type'].value_counts()))
    
    if city != 'washington':
        
        # Display counts of gender
        print('Gender Counts is: {}'.format(df['Gender'].value_counts()))
        
        #early birthday
        print('\n The earliest Birth Year is: {}'.format(str(int(df['Birth Year'].min()))))
              
        #Latest birthday
        print('\n The latest Birth Year is: {}'.format(str(int(df['Birth Year'].max()))))
        
        #Common birthday
        print('\n The common Birthday Year is: {}'.format(str(int(df['Birth Year'].mode().values[0]))))      
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """
    Display contents of the CSV file to the display as requested by
    the user.
    """

    start_loc = 0
    end_loc = 5

    display_active = input("Do you want to see the raw data?: ").lower()

    if display_active == 'yes':
        while end_loc <= df.shape[0] - 1:

            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5

            end_display = input("Do you wish to continue?: ").lower()
            if end_display == 'no':
                break

    
def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)
              
        restart = input('\nWould you like to continue explore US Bikeshare Data with us ? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break      
        

     
       
if __name__ == "__main__":
	main()