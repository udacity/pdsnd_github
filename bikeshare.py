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
    city = input('Would you like to see data for Chicago, New York City or Washington?\n').lower()
    while city not in CITY_DATA:
        print('Sorry, your input was not clear! Please try again')
        city = input('Would you like to see data for Chicago, New York or Washington?\n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    accepted_months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']
    month = input('Would you like to filter the data by month or not? Please enter: Jan, Feb, Mar, Apr, May or Jun. Type "all" for no month filter.\n').lower()
    while month not in accepted_months:
        print('Sorry, it was not a valid input! Please try again.')
        month = input('Would you like to filter the data by month or not? Please enter: Jan, Feb, Mar, Apr, May or Jun. Type "all" for no month filter.\n').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    accepted_days = ['mon','tue','wed','thu','fri','sat','sun', 'all']
    day = input ('Would you like to filter the data by day or not? Please enter: Mon, Tue, Wed, Thu, Fri, Sat or Sun. Type "all" for no month filter.\n').lower()
    while day not in accepted_days:
        print('Sorry, it was not a valid input! Please try again.')
        day = input ('Would you like to filter the data by day or not? Please enter: Mon, Tue, Wed, Thu, Fri, Sat or Sun. Type "all" for no month filter.\n').lower()


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
    df['day_of_week'] = df['Start Time'].dt.day
    #df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['mon','tue','wed','thu','fri','sat','sun']
        day = days.index(day)+1
        # filter by day to create the new dataframe
        df = df[df['day_of_week'] == day]
        # df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    # popular_day_index = df['day_of_week'].mode()[0]
    # popular_day = days[popular_day_index-1]

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]


    print('Most Frequent Start Month:', popular_month)
    print('Most Frequent Start Day:', popular_day)
    print('Most Frequent Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]


    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]


    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + df['End Station']
    popular_trip = df['trip'].mode()[0]


    print('Most Frequent Start Station:', popular_start)
    print('Most Frequent End Station:', popular_end)
    print('Most Frequent Trip Station:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()


    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()


    print("\nTotal Travel Time in seconds is: ", total_time)
    print("\nMean Travel Time in seconds is: ", mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_users = df['User Type'].value_counts()


    # TO DO: Display counts of gender
    try:
        count_users = df['Gender'].value_counts()
        print('\nThe count of users is:\n',count_users)

    except:
        print('\nSorry, not available to show Gender for WS. Enter another input')

    # print('\nThe count of users is:\n',count_users)
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        popular_byear = df['Birth Year'].mode()[0]
        earliest_byear = df['Birth Year'].min()
        recent_byear = df['Birth Year'].max()

        print('\nMost Frequent Year of Birth is: ', popular_byear)
        print('\nEarliest Year of Birth is: ', earliest_byear)
        print('\nMost Recent Year of Birth is: ', recent_byear)

    except:
        print('\nSorry, not available to show year of birth. Enter another input')

    # print('\nMost Frequent Year of Birth is: ', popular_byear)
    # print('\nEarliest Year of Birth is: ', earliest_byear)
    # print('\nMost Recent Year of Birth is: ', recent_byear)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    index = 0
    accepted_input = ['yes', 'yeah']
    user_input = input('Would you like to display raw data? Please enter: "Yes" or "No" \n')
    while user_input in accepted_input and index+5 < df.shape[0]:
        user_input = input('Would you like to display 5 rows of raw data more?').lower()
        print(df.iloc[index:index+5])
        index += 5

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
