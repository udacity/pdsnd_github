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
        city = input('Would you like to see data for Chicago, New York City or Washington?\n').lower()
        if city not in ('chicago', 'new york city', 'washington'):

            print('Incorrect city. Please try again!\n')
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('For which of the first six month of 2017 would you like to filter the data all, january, february, march, april, may or june?\n').lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):

            print('Incorrect filter selection. Please try again!\n')
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('For which week day would you like to filter the data all, monday, tuesday, wednesday, thursday, friday, saturday or sunday?\n').lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):

            print('Incorrect filter selection. Please try again!\n')
            continue
        else:
            break


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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


  # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

# extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour


    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month=='all':
        popular_month = df['month'].mode()[0]

        print('Most common month (1=jan, 2=feb, 3=mar etc.):', popular_month)


    # TO DO: display the most common day of week
    if day=='all':
        popular_day = df['day_of_week'].mode()[0]

        print('Most common day of week:', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('Most common start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('Most common start station', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most common end station', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_station'] = df['Start Station'] + ' -TO- ' + df['End Station']
    popular_trip = df['start_end_station'].mode()[0]

    print('Most common trip', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = np.array(df['Trip Duration']).sum(axis=0)

    print('Total travel time in seconds', total_travel_time)

    # TO DO: display mean travel time

    mean_travel_time = np.array(df['Trip Duration']).mean(axis=0)

    print('Mean travel time in seconds', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_subscriber = pd.Series(df['User Type']).str.count('Subscriber').sum()

    count_customer = pd.Series(df['User Type']).str.count('Customer').sum()

    print('Count user type Subscriber', count_subscriber)

    print('Count user type Customer', count_customer)

    # TO DO: Display counts of gender

    if city == 'washington':
        print('No Gender data available for Washington')

    else:

        count_male = (pd.Series(df['Gender']).str.count('Male').sum()).astype(int)

        count_female = (pd.Series(df['Gender']).str.count('Female').sum()).astype(int)

        print('Count Female user', count_female)

        print('Count Male user', count_male)

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print('No Birth data available for Washington')

    else:
        earliest_birth = (pd.Series(df['Birth Year']).min()).astype(int)

        recent_birth = (pd.Series(df['Birth Year']).max()).astype(int)

        common_birth = (df['Birth Year'].mode()[0]).astype(int)

        print('Earliest Year of Birth', earliest_birth)
        print('Recent Year of Birth', recent_birth)
        print('Common Year of Birth', common_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays rows of raw data city table at one time. Per each order 5 more rows"""
    i=0
    while True:
        raw_data_request = input('If you would like to see raw data for the city selected, answer with yes or no.\n').lower()
        i+=5
        if raw_data_request == 'yes':
            display_raw_data = df.head(i)
            print(display_raw_data)
            print('\nFor further data answer with yes to break answer with no!\n')
            continue
        else:
            break
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
