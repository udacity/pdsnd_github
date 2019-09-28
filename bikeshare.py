import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
# list all all month of available record
months_list = ['all','january','february','march','april','may','june']
# list of all days of records
days_list = ['monday','tuesday','wednessday','thursday','friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = month = day =''
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input('Would you like to see data for Chicago, New York city, or Washington? \n')).lower()
    while city not in ['chicago','new york city','washington']:
        city = str(input('Invalid city name, type the correct city name : ')).lower()
        
    #Specify on how to filter the data
    data_filter = str(input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter. \n')).lower()
    while data_filter not in ['none','month','day','both']:
        data_filter = str(input('Invalid input, type the correct filter by : ')).lower()
     
  
    if data_filter == 'none':
        print('#'*70)
        month='all'
        day='all'
        return city, month, day
    elif data_filter == 'month':
    #get user input for month (all, january, february, ... , june)
        month = str(input('Which month? January, February, March, April, May, or June? \n')).lower()
        while month not in months_list:
            month = str(input('Invalid month, type the correct month: ')).lower() 
        day = 'all'
        print('#'*70)
        return city, month, day
    elif data_filter == 'day':
    #get user input for day of week (monday, tuesday, ... sunday)
        day = str(input('Which day? Monday, Tuesday, Wednesday, Tuesday, Friday, Saturday, or Sunday? \n')).lower()
        while day not in days_list:
            day = str(input('Invalid day, type the correct day: ')).lower()
        month = 'all'
        print('#'*70)
        return city, month, day
    else:
    #get user input for month (all, january, february, ... , june)
        month = str(input('Which month? January, February, March, April, May, or June? \n')).lower()
        while month not in months_list:
            month = str(input('Invalid month, type the correct month: ')).lower()
            
        #get user input for day of week (monday, tuesday, ... sunday)
        day = str(input('Which day? Monday, Tuesday, Wednesday, Tuesday, Friday, Saturday, or Sunday? \n')).lower()
        while day not in days_list:
            day = str(input('Invalid day, type the correct day: ')).lower()
            
        print('#'*70)
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
    #generate dataframe for a particular city given by a user
    df = pd.read_csv(CITY_DATA[city])
    
    # extract month and day of week from Start Time to create new columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # generate new dataframe base on a given month
    if month !='all':
            month = months.index(month)
            df = df[df['month'] == month]
    # generate new dataframe base on a given day
    if day !='all':
            df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n=>Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month = df['month'].mode()[0]
    print('the most common month is: {}'.format(months_list[month].title()))
    print('-'*40)
    # display the most common day of week
    print('the most common day of week is: {}'.format(df['day_of_week'].mode()[0]))
    print('-'*40)
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('the most common start hour is: {}'.format(df['hour'].mode()[0]))

    running_time = time.time() - start_time
    print("\nThis took %s seconds." % (running_time))
    print('#'*70)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n=>Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_c_start_station = df['Start Station'].mode()[0]
    print('The most common start station is : {}'.format(most_c_start_station))
    print('-'*40)
    # display most commonly used end station
    most_e_start_station = df['End Station'].mode()[0]
    print('The most common end station is : {}'.format(most_e_start_station))
    print('-'*40)
    # display most frequent combination of start station and end station trip
    freq_start_and_end_station = (df['Start Station'] +' "&" '+df['End Station']).mode()[0]
    print('The most frequent start "&" end station trip is : {}'.format(freq_start_and_end_station))

    running_time = time.time() - start_time
    print("\nThis took %s seconds." % (running_time))
    print('#'*70)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n=>Calculating Trip Duration...\n')
    start_time = time.time()
    
    # display total travel time
    time_of_travel = df['Trip Duration'].sum()
    print('Total trip duration is: {}'.format(time_of_travel))
    print('-'*40)
    # display mean travel time
    mean_of_travel = df['Trip Duration'].mean()
    print('Mean of travel time is: {}'.format(mean_of_travel))

    running_time = time.time() - start_time
    print("\nThis took %s seconds." % (running_time))
    print('#'*70)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n=>Calculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    count_of_user_type = df['User Type'].value_counts()
    print('counts of user types:')
    print(count_of_user_type)
    print('-'*40)
    
    try:
        # Display counts of gender
        count_of_gender = df['Gender'].value_counts()
        print('counts of user\'s gender:')
        print(count_of_gender)
        print('-'*40)
        # Display earliest, most recent, and most common year of birth
        earliest_DOB = df['Birth Year'].min()
        recent_DOB = df['Birth Year'].max()
        common_DOB = df['Birth Year'].mode()[0]
        print('The most earliest year of birth is : {}'.format(earliest_DOB))
        print('.'*40)
        print('The most recent year of birth is : {}'.format(recent_DOB))
        print('.'*40)
        print('The most common year of birth is {}: '.format(common_DOB))
    except KeyError:
        print('Gender & DOB column is not available for the current city selected')

    running_time = time.time() - start_time
    print("\nThis took %s seconds." % (running_time))
    print('#'*70)
def display_data(df):
    """
    ask user if he wants to Loads 5 rows of data and make all the statistics analysis.
    the function keep on asking the user if the user reply with yes it will keep on adding 5, 5 rows
    until the user reply with no
    """

    count_row = 5
    while True:
        df = df.iloc[:count_row]
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        count_row += 5
        row_data = str(input('do you want to see raw data? \n')).lower()
        if row_data != 'yes':
            break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
