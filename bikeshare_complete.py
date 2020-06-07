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
        try: 
            city = input('What\'s the city you are interested in? Please type \'chicago\',\'new york city\' or \'washington\':\n').lower()
            city_list = ['chicago', 'new york city', 'washington']
            if city in city_list:
                print('So let\'s see something about {} bikesharing!'.format(city.title()))
                break
            else: 
                raise ValueError('badinput')
        except:
            print('That\'s not a valid input.')
        
    # get user input for month (all, january, february, ... , june)
    while True:
        try: 
            month = input('If you are interested in a specific month, please type it in letters, like \'month\'. \nPay attention: months are only available till june.\nIf you want to see all months, write \'all\'.\n').lower()
            month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
            if month in month_list:
                break
            else: 
                raise ValueError('badinput')
        except:
            print('That\'s not a valid input.')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try: 
            day = input('If you are interested in a specific day of the week, please type it in letters, like \'day\'.\nIf you want to see all days, write \'all\'.\n').lower()
            day_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']
            if day in day_list:
                break
            else: 
                raise ValueError('badinput')
        except:
            print('That\'s not a valid input.')

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
    city = city.lower()
    month = month.lower()
    day = day.lower()
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month_series = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12],index=months)
        month = month_series[month]
        
        # filter by month to create the new dataframe
        df = df[df['month']==month]
        

    # filter by day of week if applicable
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
        day_series = pd.Series([0,1,2,3,4,5,6],index=days)
        day = day_series[day]
        
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    popular_month = df['month'].mode()[0]
    print('The most common month is: {}'.format(popular_month))
    # display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('The most common day of week is:{} '.format(popular_day))
    
    # display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is: {}'.format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: {}'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most common end station is: {}'.format(popular_end_station))

    # display most frequent combination of start station and end station trip
    df['Station Combination']=df['Start Station'] + '_' + df['End Station']
    popular_combined_station = df['Station Combination'].mode()[0]
    print('The most common combination of start and end station is: {}'.format(popular_combined_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: {}'.format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time is: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
 
        
    user_types = df['User Type'].value_counts()
    print('The counts of user types is: \n{}'.format(user_types))

    if 'Gender' in df.columns:
        # Display counts of gender
        gender = df['Gender'].value_counts()
        print('The counts of gender is: \n{}'.format(gender))
    
    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].sort_values(ascending = True).values[0]
        print('The earliest year of birth is: {}'.format(earliest_birth))

        most_recent_birth = df['Birth Year'].sort_values(ascending = False).values[0]
        print('The most recent year of birth is: {}'.format(most_recent_birth))
        
        most_common_birth = df['Birth Year'].mode()[0]
        print('The most common year of birth is: {}'.format(most_common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    """
    Asks user if he wants to see 5 lines of raw data, display that data if the answer is 'yes'
    """
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    i = 0
    while True:
        try: 
            raw_data = input('Would you like to see some lines of raw data (yes/no)?\n')
            raw_data = raw_data.lower()
            if raw_data == 'yes' or raw_data == 'y':
                print(df[i:i+5])
                i = i + 5
            elif raw_data == 'no' or raw_data == 'n':
                break
            else: 
                raise ValueError('badinput')
        except:
            print('That\'s not a valid input.')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
