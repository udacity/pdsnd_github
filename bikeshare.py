import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input(
            '\nWhich city would you like to explore US Bikeshare data?: Chicago, New York City or Washington?\n ')).lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print(
                'Sorry, please enter the one of the following cities: Chicago, New York City or Washington ')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input(
            '\nWhich month would you like to explore data from? January, February, March, April, May, June or all?\n ')).lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('Sorry, please enter one of the following months: January, February, March, April, May, June or all. ')
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input(
            '\nWhich day would you like to explore data from? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all?\n '))
        if day.lower() not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print('Sorry please enter one of the following days: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all. ')
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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('Calculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('Commonly Used Start Station:', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('Commonly Used End Station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    end_start_station = df.groupby(['Start Station', 'End Station']).count()
    print('Frequently Taken Start and End Station Trip:',
          start_station, " - ", end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)
    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Average Travel Time:', avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Users:', user_types)
    # TO DO: Display counts of gender
    try:
        type_of_gender = df['Gender'].value_counts()
        print('Gender Types:', type_of_gender)
    except:
        print('There is no gender data for the month.')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df['Birth Year'].min()
        print('Earliest Birth:', earliest_birth)
    except:
        print('No data found')
    # Most recent
    try:
        most_recent_birth = df['Birth Year'].max()
        print('Most Recent Birth:', most_recent_birth)
    except:
        print('No data found')
    # Most common
    try:
        most_common_birth = df['Birth Year'].value_counts().idxmax()
        print('Most Common Birth:', most_common_birth)
    except:
        print('No data found')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
