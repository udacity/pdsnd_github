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
    city = input("Which city would you like to explore? ")
    while city.lower() not in ['chicago','new york city','washington']:
        print("I'm sorry. Please enter a city. ")
        city = input("Which city would you like to explore? ")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month would you like to filter the data by? If you would like all months, enter 'all'. ")
    while month.lower() not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print("I'm sorry. Please enter a month or 'all'. ")
        month = input("Which month would you like to filter the data by? If you would like all months, enter 'all'. ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day of the week would you like to filter the data by? If you would like all days, enter 'all'. ")
    while day.lower() not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        print("I'm sorry. Please enter a day or 'all'. ")
        day = input("Which day would you like to filter the data by? If you would like all days of the week, enter 'all'. ")

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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    calendar = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May',
            6: 'Jun'}
    df['month'] = df['Start Time'].dt.month
    df['month'] = df['month'].apply(lambda x: calendar[x])
    popular_month = df['month'].mode().values[0]
    print('Most Frequent Month:', popular_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode().values[0]
    print('Most Frequent Day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode().values[0]
    print('Most Frequent Start Hour:', popular_hour, '00')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode().values[0]
    print('Most Commonly Used Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode().values[0]
    print('Most Commonly Used End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    tup = df.groupby(['Start Station', 'End Station']).size().idxmax()
    popular_combined_station = ', '.join(tup)
    print('Most Common Combination of Start and End Station:', popular_combined_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_sum = df['Trip Duration'].sum()
    trip_sum_int = trip_sum.astype(np.int)
    days = trip_sum_int // 86400
    hours = (trip_sum_int % 86400) // 3600
    minutes = (trip_sum_int - days*86400 - hours*3600) // 60
    seconds = trip_sum_int - days*86400 - hours*3600 - minutes*60
    print('Total Duration of All Trips:', days, 'days', hours, 'hours', minutes, 'minutes', seconds, 'seconds')

    # TO DO: display mean travel time
    trip_mean = df['Trip Duration'].mean()
    trip_mean_int = trip_mean.astype(np.int)
    days = trip_mean_int // 86400
    hours = (trip_mean_int % 86400) // 3600
    minutes = (trip_mean_int - days*86400 - hours*3600) // 60
    seconds = trip_mean_int - days*86400 - hours*3600 - minutes*60
    print('Mean Duration of All Trips:', days, 'days', hours, 'hours', minutes, 'minutes', seconds, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().values
    print('Counts of user types:\n', 'Subscriber:', user_types[0],'\n', 'Customer:', user_types[1],'\n')
    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts().values
        print('Counts of Gender:\n', 'Male:', gender_counts[0],'\n', 'Female:', gender_counts[1])
    except KeyError:
        print("No data available for gender\n")
        pass
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_yob = df['Birth Year'].min()
        earliest_yob_int = earliest_yob.astype(np.int)
        print('Earliest Year of Birth:', earliest_yob_int)

        recent_yob = df['Birth Year'].max()
        recent_yob_int = recent_yob.astype(np.int)
        print('Most Recent Year of Birth:', recent_yob_int)

        popular_yob = df['Birth Year'].mode().values[0]
        popular_yob_int = popular_yob.astype(np.int)
        print('Most Common Year of Birth:', popular_yob_int)
    except KeyError:
        print("No data available for Year of Birth")
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Asks user whether they would like to view 5 rows of raw data, and continually displays data in rows of 5 until their answer is 'no'. If yes, it prints the raw data available in rows of 5.
    """
    start = 0
    count = 5
    try:
        df = df[['Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year']]
        view_data = input("Would you like to see the first 5 rows of raw data? Please type yes or no: ")
        while True:
            if view_data == 'yes':
                print(df.iloc[start:count])
                count += 5
                start += 5
                view_data = input("Would you like to see the next 5 rows of raw data? Please type yes or no: ")
            elif view_data == 'no':
                break
            else:
                view_data=input("Please enter yes or no: ")
                continue
    except KeyError:
        df = df[['Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type']]
        view_data = input("Would you like to see the first 5 rows of raw data? Please type yes or no: ")
        while True:
            if view_data == 'yes':
                print(df.iloc[start:count])
                count += 5
                start += 5
                view_data = input("Would you like to see the next 5 rows of raw data? Please type yes or no: ")
            elif view_data == 'no':
                break
            else:
                view_data = input("Please enter yes or no: ")
                continue

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

    
