import time
import pandas as pd
import numpy as np
#input('Would you like to filter the data by month, day, both, or not at all? Type "None" for no time filter.\n')
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
        city = input('Would you like to see data for Chicago, New York, Washington?\n').lower()
        if city in ['chicago', 'new york', 'washington']:
            break
        else:
            print('Invalid Entry! Please try again\n')

# TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input('Which month? January, Febraury, March, April, May, or June?\n').lower()
        if month in ["january", "february", "march", "april", "may", "june", "all"]:
            break
        else:
            print('Invalid Entry! Please try again\n')

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('Which day?\n').lower()
        if day in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
            break
        else:
            print('Invalid Entry! Please try again\n')

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

    # filter by month if applicable
    if month != 'all':
        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # extract month and day of week from Start Time to create new columns
        df['day_of_week'] = df['Start Time'].dt.weekday_name

        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create new columns for month, weekday, hour
    month = df['Start Time'].dt.month
    weekday_name = df['Start Time'].dt.weekday_name
    hour = df['Start Time'].dt.hour

    # TO DO: display the most common month
    popular_month = month.mode()[0]
    print('Most common month is {}'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = weekday_name.mode()[0]
    print('Most common day is {}'.format(popular_day))


    # TO DO: display the most common start hour
    popular_hour = hour.mode()[0]
    print('Most common start hour is {}'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()
    print('\nMost common start station is {}\n'.format(most_common_start_station))


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()
    print('\nMost common end station is {}\n'.format(most_common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    combination_trip = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    most_frequent_trip = combination_trip.value_counts().idxmax()
    print('\nMost popular trip is from {}\n'.format(most_frequent_trip))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    day = total_travel_time // (24 * 3600)
    time1 = total_travel_time % (24 * 3600)
    hour = total_travel_time // 3600
    total_travel_time %= 3600
    minutes = total_travel_time // 60
    total_travel_time %= 60
    seconds = total_travel_time
    print('Total travel time is {} days {} hours {} minutes {} seconds\n'.format(day, hour, minutes, seconds))


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    day2 = mean_travel_time // (24 * 3600)
    mean_travel_time %= (24 * 3600)
    hour2 = mean_travel_time // 3600
    mean_travel_time %= 3600
    minutes2 = mean_travel_time // 60
    mean_travel_time %= 60
    seconds2 = mean_travel_time
    print('Mean travel time is {} hours {} minutes {} seconds\n'.format(hour2, minutes2, seconds2))


    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        user_genders = df['Gender'].value_counts()
        print(user_genders)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("\nEarliest year of birth: {} ".format(earliest_birth_year))
        print("\nMost recent year of birth: {}".format(most_recent_birth_year))
        print("\nMost common year of birth: {}".format(common_birth_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
