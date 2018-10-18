#import packages
import time
import pandas as pd
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)


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
    city = ''
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('Would you like to see data for Chicago, New York City, or'
                    ' Washington?\n')
        if city.lower() == 'chicago' or  city.lower() == 'new york city' or city.lower() == 'washington':
            break
        else:
            print('Sorry, I do not understand your input. Please input either '
                      'Chicago, New York, or Washington.')

    # get user input for month (all, january, february, ... , june)
    month = ''
    while month.lower() not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input('Which months would you like to explore the data for January,\n'
                        'February, March, April, May, June or All?\n')
        if month.lower() == 'january' or  month ==  'february' or  month ==  'march' or month ==  'april' or  month ==  'may' or  month ==  'june' or  month == 'all':
            break
        else:
            print('Sorry, I do not understand your input. Please input either '
                        'January, February, March, April, May, June or All')

    # get user input for day of week (all, mondasy, tuesday, ... sunday)
    day = ''
    while day.lower() not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        day = input('Which days would you like to explore the data by Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All?\n')
        if day.lower() == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all':
            break
        else:
            print('Sorry, I do not understand your input. Please input either '
                        'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All\n')

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

    if city == 'washington' or city == 'new york city':
        df['Gender'] = 'NAN'

    if city == 'washington' :
        df['Birth Year'] = 0

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1

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

    # display the most common month
    print('Most Popular Month:',df['month'].mode()[0])

    # display the most common day of week
    print('Most Popular Day of week:', df['day_of_week'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most Popular Start Hour is {}.'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(df['Start Station'].mode()[0])

    # display most commonly used end station
    print(df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    most_pop_trip = df['Trip'].mode().to_string(index = False)
    print('The most popular trip is {}.'.format(most_pop_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['datediff'] =(df['End Time'] - df['Start Time'])
    totaltime = df['datediff'].sum()
    print('Total Travel Time:\n', totaltime)
    # display mean travel time
    datediff = df['datediff'].mean()
    print('Mean Travel Time:\n', datediff)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of User Types: ',user_types)
    # Display counts of gender

    men = df.query('Gender == "Male"').Gender.count()
    women = df.query('Gender == "Female"').Gender.count()
    print('There are {} male users and {} female users.'.format(men, women))

    # Display earliest, most recent, and most common year of birth
    birth_year_min =df['Birth Year'].min()
    print('Earliest Birth Year:\n', int(birth_year_min))
    birth_year_max = df['Birth Year'].max()
    print('Most Recent Birth Year:\n', int(birth_year_max))
    birth_year_mode = df['Birth Year'].mode()
    print('Most Popular Birth Year:\n', int(birth_year_mode))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df
def display_data(df):
    """Displays raw bikeshare data upon request"""

    print('\nCalculating data pull...\n')
    start_time = time.time()

    data = input('\nWould you like to see the data? Enter yes or no.\n')
    if data.lower() == 'yes':
        print(df)
    else:
        Print('You entered No')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
