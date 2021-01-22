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
    month_values = ['january','february','march','april','may','june']
    day_values = ['sunday','monday','tuesday','wednasday','thursday','friday','saturday']

    while True:
        city = input("Please provide the city: ").lower()
        if city in CITY_DATA:
            break
            
        print(city + " " + " not in the valid city names. please try again.")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please provide the month: ").lower()
        if month in month_values or month =='all':
            break
        print(month + " " + " not in the valid the month in this intervals. please try again.")
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please provide the day: ").lower()
        if day in day_values or day =='all':
            break
        print(day + " " + " not in the valid the month in this intervals. please try again.") 


    print('-'*40)
    return city, month, day

#lıading the information of data
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
    df = pd.read_csv(CITY_DATA[city]) 
    #print(df.info)
    df ['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df ['Month'] = df['Start Time'].dt.month
    
    df ['Day Week'] = df['Start Time'].dt.day_name()
    
    month_values = ['january','february','march','april','may','june']
    
    if month != "all" and day != "all":
        month = month_values.index(month)+1
        df = df[df ['Month']==month]
        df = df[df ['Day Week'] == day.title()]
    elif month == "all" and day != "all":
        df = df[df ['Day Week'] == day.title()]
    elif month != "all" and day == "all":
        df = df[df ['Month']==month]
    
    print(df.head())
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month=df['Month'].mode()[0]
    print('Most common month which rent bike was {}.'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_dayofweek=df['Day Week'].mode()[0]
    print('Most common day which rent bike was {}.'.format(most_common_dayofweek))

    # TO DO: display the most common start hour
    most_common_start_hour=df['Start Time'].dt.hour.mode()[0]
    print('Most common hour which rent bike was {}.'.format(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print('Most common start station was {}.'.format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print('Most common end station was {}.'.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Station'] = df['Start Station'] + '-->' + df['End Station']
    start_finish =df['Start End Station'].mode()[0]
    print('Most common end station was {}.'.format(start_finish))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Tota Travel Time is {} hours'.format(round(total_travel_time/3600,2)))    

    # TO DO: display mean travel time
    average_travel_time=df['Trip Duration'].mean()
    print('Average Travel Time is {} hours'.format(round(average_travel_time/60,2))) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types=df['User Type'].value_counts()
    print('The count of user types is {}.'.format(count_user_types))

    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print("Gender column is not found in this city information")
    else:
        gender_info=df['Gender'].value_counts()
        print('The count of gender is {}.'.format(gender_info))
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print("Birth Year column is not found in this city information")
    else:
        earliest_birth=int(df['Birth Year'].min())
        print('The earliest year of birth is {}.'.format(earliest_birth))
        
        recent_birth=int(df['Birth Year'].max())
        print('The oldest year of birth is {}.'.format(recent_birth))
        
        most_common_year_birth=int(df['Birth Year'].mode()[0])
        print('The most common year of birth is {}.'.format(most_common_year_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df):
    rawdata_input=input("\Do you want to show raw data? Enter answer y or n:")
    line_count=0
    
    while 1==1:
        if rawdata_input =='y':
            print(df.iloc[line_count:line_count+15])
            line_count+=15
            rawdata_input=input("\Do you want to show raw data? Enter answer y or n:")
        else:
            break
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
