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
    city = input("Which city do you want the information for?").lower()
    while city != ('Chicago', 'new york city', 'washington'):
        break
    else:
        print('Invalid Input\n')


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month do you want the information for?").lower()
    while month != ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
        break
    else:
        print('Invalid Input\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day of week do you want the information for?").lower()
    while month != ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
        break
    else:
        print('Invalid Input\n')

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
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

    # TO DO: display the most common month
    print('The most common month is: {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('The most common day of week is: {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('The most common hour is: {}'. format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common used start station: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common end station: {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start and end station is: {}'.format(df.groupby(['Start Station','End Station']).size().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is: {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The mean travel time is: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The number of user types: {}'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('The number of gender types: {}'.format(df['Gender'].value_counts()))
    else:
        print('There is no Gender data for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('The earliest date of birth: {}'.format(int(df['Birth Year'].min())))
        print('The recent date of birth: {}'.format(int(df['Birth Year'].max())))
        print('The most common date of birth: {}'.format(int(df['Birth Year'].mode()[0])))
    else:
        print('There is no Birth Year data for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    display = input('Do you want to see raw data? Yes or No? \n').lower()
    i = 0
    print (df.iloc[i:i+5])
    while True:
        more = input('Do you want to see 5 more rows of data? Yes or No? \n').lower()
        if more == 'yes':
            i +=5
            print (df.iloc[i:i+5])
        elif more == 'no':
            break


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
