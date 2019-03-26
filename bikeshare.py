import time
import pandas as pd
import numpy as np

#I am adding this for the github project in bikeshare.py
#I am testing my work.

City_Data = { 'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

Cities = ['chicago', 'new york city', 'washington']

Months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

Days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

#Welcome
print 'Thanks to Udacity, this is the first time I am using Python to understand data.'
print 'Let\'s start!'
name = raw_input('But, first, what is your name? ')
print (name)

#Select city, month and day
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
# get user input for month (all, january, february, ... , june)
# get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        city = raw_input('Please select one of the cities you are interested among Chicago, New York City and Washington?' ).lower()
        if city in Cities:
            break
        else:
            print ('For now, these are the only cities available. Please only select one of them').lower()
            city = raw_input()

    while True:
        month = raw_input('Please select a month you are interested? Or select All if you are interested in reviewing the whole year?').lower()
        if month in Months:
            break
        else:
            print ('Please select a month, from January to December, you are interested?').lower()
            month = raw_input()

    while True:
        day = raw_input('Please select a day you are interested? Or select All if you are interested in reviewing the whole week?').lower()
        if day in Days:
            break
        else:
            print ('Please select a day, from Monday to Sunday, you are interested?').lower()
            day = raw_input()

    print ('-'*40)
    return city, month, day

#Time based stats
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

    df = pd.read_csv(City_Data[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    df['End Time'] = pd.to_datetime(df['End Time'])

    df['month'] = df['End Time'].dt.month
    df['day_of_week'] = df['End Time'].dt.weekday_name
    df['hour'] = df['End Time'].dt.hour

    if month != 'All':
        month = Months.index(month) + 1
        df = df[ df['month'] == month ]

    if day != 'All':
        df = df[ df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print ('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    # display the most common day of week
    # display the most common start hour

    most_common_month = df['month'].value_counts().idxmax()
    print ('The most common month is :', most_common_month)

    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print ('The most common day of week is :', most_common_day_of_week)

    most_common_start_hour = df['hour'].value_counts().idxmax()
    print ('The most common start hour is :', most_common_start_hour)

    print ("\nThis took %s seconds." % (time.time() - start_time))
    print ('-'*40)

#Station base stats
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    # display most commonly used end station
    # display most frequent combination of start station and end station trip

    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print ('The most common start station :', most_common_start_station)

    most_common_end_station = df['End Station'].value_counts().idxmax()
    print ('The most common end station :', most_common_end_station)

    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print ('The most common start and end station : {}, {}'.format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print ("\nThis took %s seconds." % (time.time() - start_time))
    print ('-'*40)

#Trip stats
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print ('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    # display mean travel time

    total_travel_time = df['Trip Duration'].sum()
    print ("Total travel time is :", total_travel_time)

    mean_travel_time = df['Trip Duration'].mean()
    print ("Mean travel time is :", mean_travel_time)

    print ("\nThis took %s seconds." % (time.time() - start_time))
    print ('-'*40)

#User stats
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print ('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # Display counts of gender
    # Display earliest, most recent, and most common year of birth

    print ('Counts of user types:\n')
    user_counts = df['User Type'].value_counts()
    for index, user_count in enumerate(user_counts):
        print ('  {}: {}'.format(user_counts.index[index], user_count))

    print ()

    if 'Gender' in df.columns:
        user_stats_gender(df)

    if 'Birth Year' in df.columns:
        user_stats_birth(df)

    print ("\nThis took %s seconds." % (time.time() - start_time))
    print ('-'*40)

def user_stats_gender(df):
    print ('Counts of gender is:\n')
    gender_counts = df['Gender'].value_counts()
    for index, gender_count in enumerate(gender_counts):
        print('  {}: {}'.format(gender_counts.index[index], gender_count))

    print()

def user_stats_birth(df):

    birth_year = df['Birth Year']

    earliest_year = birth_year.min()
    print ('The oldest person is born in:', earliest_year)

    most_recent = birth_year.max()
    print ('The youngsest person is born in:', most_recent)

    most_common_year = birth_year.value_counts().idxmax()
    print ('The most common birth year is:', most_common_year)

#Raw data review
def display_data(df):
    row_length = df.shape[0]
    for i in range(0, row_length, 5):
        display = raw_input('If you like to continue reviewing the data more in detail, please say Yes or No' ).lower()
        if display != 'yes':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        user_stats_gender(df)
        user_stats_birth(df)
        display_data(df)

        restart = input('\nWould you like to do it again or not? Please enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	   main()
