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
    city=''
    while city.lower() not in ['chicago', 'new york city', 'washington']:
        city=str(input ('Please select Chicago, New York City or Washington data set: \n'))
        if city.lower() not in ['chicago', 'new york city', 'washington']:
            print ('\nNot a supported value. Please change your input.\n')



    # TO DO: get user input for month (all, january, february, march, april, may , june)
    month=''
    while month.lower() not in ['january','february','march','april','may','june','all']:
        month=str(input ('Which month? January, February, March, April, May, June or All? Please select: \n'))
        if month.lower() not in ['january','february','march','april','may','june','all']:
            print ('\nNot a supported value. Please change your input.\n')



    # TO DO: get user input for day of week (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)
    day=''
    while day.lower() not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        day=str(input ('Which day of the week e.g. Monday or all? \n'))
        if day.lower() not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            print ('Not a supported value. Please select a day of week e.g. Monday')


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
    filename=''
    if city.lower() =='chicago':
        filename='chicago.csv'

    if city.lower() =='washington':
        filename='washington.csv'

    if city.lower() =='new york city':
        filename='new_york_city.csv'

    df = pd.read_csv(filename)
    print (filename)



    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month.lower() != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    """ here ends input filters """

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    df['months'] = df['Start Time'].dt.month

    # most popular hour
    popular_month = df['months'].mode()[0]

    print('Most Popular Month:', popular_month)


    # TO DO: display the most common day of week

    df['week'] = df['Start Time'].dt.dayofweek

    # most popular hour
    popular_weekday = df['week'].mode()[0]

    print('Most Popular Weekday:', popular_weekday)



    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    popular_startstation = df['Start Station'].value_counts().idxmax()
    print('Most Popular Start Station:\n', popular_startstation)



    # TO DO: display most commonly used end station

    popular_endstation = df['End Station'].value_counts().idxmax()
    print('Most Used End Station:\n', popular_endstation)

    # TO DO: display most frequent combination of start station and end station trip

    popular_combi = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print ('\nMost frequent combination of start station and end station: \n\n', popular_combi)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_sec= df['Trip Duration'].sum()
    total_travel_min= total_travel_sec // 60
    total_travel_hours= total_travel_min // 60
    print ('Total Travel Time (hours): ',total_travel_hours)

    # TO DO: display mean travel time

    total_travel_sec_avg= df['Trip Duration'].mean()
    total_travel_min_avg= total_travel_sec_avg // 60

    print ('Mean Travel Time (minutes): ',total_travel_min_avg)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type= df['User Type'].value_counts()
    print ('\nUser types: \n',user_type)

    if city =='Chicago' or city =='New York City':

        # TO DO: Display counts of gender

        user_gender= df['Gender'].value_counts()
        print ('\nGender of User: \n',user_gender)

        # TO DO: Display earliest, most recent, and most common year of birth

        earliest_bd= df['Birth Year'].min()
        print ('\nEarliest Birthday: \n',int(earliest_bd))

        recent_bd= df['Birth Year'].max()
        print ('Recent Birthday: \n',int(recent_bd))

        most_bd= df['Birth Year'].value_counts().idxmax()
        print ('Most Common Birth Year: \n',int(most_bd))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_rawdata(df):

    # dsplays 5 rows of raw data

    counter = 5
    while True:
        showrawdata = input('\n\nDisplay 5 rows of raw data? Please type Yes or No:\n')
        if (showrawdata.lower() == 'yes'):
            print(df.iloc[counter],'\n')
            counter= counter + 5
            continue
        elif (showrawdata.lower() == 'no'):
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_rawdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
