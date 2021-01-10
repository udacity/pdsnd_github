import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

MONTH_DATA = ['january',
              'february',
              'march',
              'april',
              'may',
              'june',
              'all']

DAY_DATA = ['monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
            'all']


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
    try:
        city = input(
            '\nWhich city do you want to analyze? Choose one: Chicago, Washington or New York City\n').strip().lower()

        while city not in CITY_DATA:
            print("\nSomething wrong? Don't worry, try again!")
            city = input('\nWhich city do you want to analyze? Choose one: Chicago, Washington or New York City\n')

        # get user input for month (all, january, february, ... , june)
        month = input(
            '\nWhich month do you want to analyze? Choose one: all, january, february, ... , june\n').strip().lower()
        while month not in MONTH_DATA:
            print("\nSomething wrong! Don't worry, try again!")
            month = input('\nWhich month do you want to analyze? Choose one : all, january, february, ... , june\n')

        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input(
            '\nWhich day do you want to analyze? Choose one: all, monday, tuesday, ... sunday\n').strip().lower()
        while day not in DAY_DATA:
            print("\nSomething wrong! Don't worry, try again!")
            day = input('\nWhich day do you want to analyze? Choose one: all, monday, tuesday, ... sunday\n')

        return city, month, day
    except Exception as ex:
        print('Inputs are incorrect.Get_Filters function is getting error: {}'.format(ex))
    print('-' * 40)


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

        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        df['hour'] = df['Start Time'].dt.hour

        # Check month is valid
        if month != 'all':
            month = MONTH_DATA.index(month)
            df = df.loc[df['month'] == month]
        # Check day is valid
        if day != 'all':
            df = df.loc[df['day_of_week'] == day.title()]
        return df
    except Exception as ex:
        print('The file is corrupt. Load_Data function is getting error: {}'.format(ex))


def time_stats(df, city):
    """Displays statistics on the most frequent times of travel."""

    print('\nPopular times of travel...\n')
    start_time = time.time()

    # display the most common month
    try:
        popular_month_num = df['Start Time'].dt.month.mode()[0]
        popular_month = MONTH_DATA[popular_month_num - 1].title()
        print('The most common month :', popular_month)
    except Exception as ex:
        print('The most common month couldn\t calculate.Time_stats function is getting error: {}'.format(ex))

    # display the most common day of week
    try:
        popular_day_of_week = df['day_of_week'].mode()[0]
        print('The most common day of week :', popular_day_of_week)
    except Exception as ex:
        print('The most common day of week couldn\t calculate.Time_stats function is getting error: {}'.format(ex))

    # display the most common start hour
    try:
        popular_start_hour = df['hour'].mode()[0]
        print('The most common hour of day:', popular_start_hour)
    except Exception as ex:
        print('The most common hour of day couldn\t calculate.Time_stats function is getting error: {}'.format(ex))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df, city):
    """Displays statistics on the most popular stations and trip."""

    print('\nPopular stations and trip...\n')
    start_time = time.time()

    # display most commonly used start station
    try:
        popular_start_station = df['Start Station'].mode()[0]
        popular_start_station_amount = df['Start Station'].value_counts()[0]
        print('The most common start station is:', popular_start_station, 'and was used', popular_start_station_amount,
              'times.')
    except Exception as ex:
        print('The most common start station couldn\t calculate.Station_Stats function is getting error: {}'.format(ex))
    # display most commonly used end station
    try:
        popular_end_station = df['End Station'].mode()[0]
        popular_end_station_amount = df['End Station'].value_counts()[0]
        print('The most common end station is:', popular_end_station, 'and was used', popular_end_station_amount,
              'times.')
    except Exception as ex:
        print('The most common end station couldn\'t calculate.Station_Stats function is getting error: {}'.format(ex))

    # display most frequent combination of start station and end station trip
    try:
        popular_trip = df.loc[:, 'Start Station':'End Station'].mode()[0:]
        popular_trip_amt = df.groupby(["Start Station", "End Station"]).size().max()
        print('The most common trip from start to end is:\n', popular_trip, '\n and was driven', popular_trip_amt,
              'times')
    except Exception as ex:
        print(
            'The most common trip from start to end couldn\'t calculate.Station_Stats function is getting error: {}'.format(
                ex))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df, city):
    """Displays statistics on the total and average trip duration."""

    print('\nTrip duration...\n')
    start_time = time.time()

    # display total travel time
    try:
        df['Time Delta'] = df['End Time'] - df['Start Time']
        total_time_delta = df['Time Delta'].sum()
        print('The total travel time :', total_time_delta)
    except Exeption as ex:
        print('Total travel time couldn\'t calculate. Trip_Duration_Stats function is getting error.{}'.format(ex))

    # display mean travel time
    try:
        total_mean = df['Time Delta'].mean()
        print('The average travel time:', total_mean)
    except Exception as ex:
        print(
            'The average travel time couldn\'t calculate. Trip_Duration_stats function is getting error.{}'.format(ex))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nUser info...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        print('Total users by user types:\n', df['User Type'].value_counts())
    except Execption as ex:
        print('\nTotal users by user types couldn\'t calculate.User_Stats function is getting error: {}'.format(ex))
    # Display counts of gender
    try:
        print('\nTotal users by gender:\n', df['Gender'].value_counts())
    except Exception as ex:
        print('\nTotal users by gender couldn\'t calculate.User_Stats function is getting error:: {}'.format(ex))
    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birthy = df['Birth Year'].min()
        most_recent_birthy = df['Birth Year'].max()
        most_common_birthy = df['Birth Year'].mode()
        print('\nThe age structure of customers:\n' 'The oldest customer by year of birth:', int(earliest_birthy),
              '\n' 'The youngest customer by year of birth:', int(most_recent_birthy),
              '\n' 'The most common year of birth:', int(most_common_birthy))
    except Exception as ex:
        print(
            '\nThe age structure of our customers couldn\'t calculate.User_Stats function is getting error: {}'.format(
                ex))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    """Display descriptive statistics"""

    start_time = time.time()
    start_loc = 0
    end_loc = 5
    df_length = len(df.index)

    try:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').strip().lower()

        while True:

            if end_loc > df_length:
                print("\nThere is no data to display.\n")
                break
            else:
                print("\nDisplay only 5 rows of data.\n")
                print(df.iloc[start_loc:end_loc])
                print("\nThis took %s seconds." % (time.time() - start_time))
                print('-' * 40)
                start_loc += 5
                end_loc += 5
                view_display = input("\nDo you wish to continue?Enter yes or no\n").strip().lower()

                if view_display != 'yes':
                    break

    except Exception as ex:
        print('Display_data function is getting error: {}'.format(ex))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, city)
        station_stats(df, city)
        trip_duration_stats(df, city)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.strip().lower() != 'yes':
            break


if __name__ == "__main__":
    main()
