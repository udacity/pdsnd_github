import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    cities = ['chicago','new york','washington']
    months = ['january','february',
              'march','april','may',
              'june','all']
    days_of_week = ['monday','tuesday',
                    'wednesday','thursday',
                    'friday','saturday',
                    'sunday','all']
    
    while True:  #While loop to get city
        try:
            city = input('Which city would you like to see?')
            city = city.lower()

        except ValueError:
            print('heck nah')
            continue

        if city not in cities:
            print('Invalid city...try again \n')
            continue
        else:
            break
    
    
    while True:  #while loop to get month
        try:
            month = input("\nYou can pick a month between January and June, inclusive. For all months, enter 'all'. \n")
            month = month.lower()

        except ValueError:
            print('try again')
            continue

        if month not in months:
            print('Invalid month...try again \n')
            continue
        else:
            break
    
    
    while True:  #while loop to get day
        try:
            day = input('\nYou can pick a specific day of the week. If you need to look at the whole week, just enter "all"\n')
            day = day.lower()

        except ValueError:
            print('heck nah')
            continue

        if day not in days_of_week:
            print('Invalid day...try again \n')
            continue
        else:
            break
            
    print('-'*40)                    
    return (city, month, day)

    
    
    
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
    df = pd.read_csv(CITY_DATA[city]) #load data
    
#     modify data format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month_col'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.weekday_name
    df['day of week'] = df['day of week'].str.lower()
# filter dataframe by month    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        m = months.index(month) + 1
        df = df[df['month_col'] == m]
 # filter dataframe by day   
    if day != 'all':
        df = df[df['day of week'] == day]
  #raw data      
    for i in range (0, len(df), 5):
        response = input ('Would you like to see raw data?')
        if response == 'yes':
            print(df.iloc[i:i+5])
        elif response == 'no':
            break
                    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    
   # find popular month
   # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # find the most popular hour
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', popular_month) 
    
    
   # find popular day of week
   # extract day from the Start Time column to create an day column
    df['day'] = df['Start Time'].dt.day
    # find the most popular day
    popular_day = df['day'].mode()[0]
    print('Most Popular Start Day:', popular_day) 
   
    
    # find popular start hour
   # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour) 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


    
def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()        
    
   # find popular start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)
    
    # find popular start station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station) 
    
    frequent_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most common combination of stations is: ", frequent_combination)  
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    #find trip duration     
    sum_time =  df['Trip Duration'].sum()
    print("Total time is: ", sum_time) 
    #find average trip duration
    average_time = df['Trip Duration'].mean()
    print("Average time is: ", average_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    #find user types
    user_types = df['User Type'].count()
    print("User types are: ", user_types)
    #find gender count
    if 'Gender' in df.columns:    
        gender_count = df['Gender'].count()
        print("Gender count is: ", gender_count)
    else:
        print('No gender info to calculate')
    #shows earliest birth year, most recent birth year and the most popular birth year
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        most_popular_year = df['Birth Year'].mode()[0]
        print("Earliest birth year, recent birth year and most popular year are {}, {} and {}.".format(earliest_birth_year, recent_birth_year, most_popular_year))
    else:
        print('No birth year to calculate')
    
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