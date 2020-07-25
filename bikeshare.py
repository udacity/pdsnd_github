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
    
    while True:
        try:
            city = input('Please enter city name (chicago, new york city, washington:')
            if city in CITY_DATA:
                break
            else:
                print('the city name is not correct, please try again')
        except:
            print('the city name is not correct, please try again')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Please enter month (january, february, ..., june): ')
            if month.lower() in ['january', 'february', 'march', 'april', 'may', 'june']:
                break
            else:
                print('the month name is not correct, please try again')
        except:
            print('the month name is not correct, please try again')
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Please enter day (all, monday, tuesday, ..., sunday): ')
            if day.lower() in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                break
            else:
                print('the day name is not correct, please try again')
        except:
            print('the day name is not correct, please try again')


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
    try:
        df = pd.read_csv(CITY_DATA[city])
    except:
        print('No data file available, please check')
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].apply(lambda x : x.hour)
    df['month'] = df['Start Time'].apply(lambda x : x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x : x.weekday_name)
        
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = [i for i, _ in enumerate(months) if months[i] == month][0] + 1
        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode().values[0]
    print('the most common month is: {}'.format(common_month))


    # TO DO: display the most common day of week
    common_dayofweek = df['day_of_week'].mode().values[0]
    print('the most common day of week is: {}'.format(common_dayofweek))

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode().values[0]
    print('the most common start hour is: {}'.format(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode().values[0]
    print('the most common start station is: {}'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode().values[0]
    print('the most common end station is: {}'.format(common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End_Station'] = [row['Start Station'] + ' TO ' + row['End Station'] for _, row in df.iterrows()]
    common_start_end_station = [i for i in df['Start_End_Station'].mode()] #to use list in case of there are many common routes
    print('the most common start-end station is: {}'.format(common_start_end_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('total time is: {}'.format(total_time))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('average time is: {}'.format(mean_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('user type: \n{}'.format(user_type))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_type = df['Gender'].value_counts()
        print('gender type: \n{}'.format(gender_type))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        min_birth = int(df['Birth Year'].min())
        max_birth = int(df['Birth Year'].max())
        common_birth = int(df['Birth Year'].mode().values[0])
        print('Earliest year of birth: {}\nRecent year of birth: {}\nCommon year of birth: {}\n'.format(min_birth, max_birth, common_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():

    print("---- Bike Data Analysis ----")
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        raw_data = input('\nWould you like to see raw data? Enter yes or no.\n')
        index = 0
        while raw_data.lower() == 'yes':
            if raw_data.lower() == 'yes':
                print(df.iloc[index:index+5])
            raw_data = input('\nWould you like to see the next 5 rows of raw data? Enter yes or no.\n')
            if raw_data.lower() == 'yes':
                index += 5
            else:
                break
                

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Your answer is NO, we will stop the program')
            break


if __name__ == "__main__":
	main()
