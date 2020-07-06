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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(
            "\nWhich City are you interested in? New York City, Washington or Chicago?\n")
        city = city.lower()
        if city not in ('new york city', 'washington', 'chicago'):
            print("Please try again.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            "\nWhich month are you interested in? January, February, March, April, May, June, type 'all' if you do not enter a month?\n")
        month = month.lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Please try again.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWhich day are you interested in? Please enter the day: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you prefer not to enter a day.\n")
        day = day.lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("Please try again.")
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
    df['day_of_week'] = df['Start Time'].dt.day_name()

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

    # TO DO: display the most common month
    c_month = df['month'].value_counts().idxmax()
    print('This is the most common month:', c_month)

    # TO DO: display the most common day of week
    c_day = df['day_of_week'].value_counts().idxmax()
    print('This is the most common day:', c_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    c_hour = df['hour'].value_counts().idxmax()
    print('This is the most common hour:', c_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    S_Station = df['Start Station'].value_counts().idxmax()
    print('This is the most commonly used start station:', S_Station)

    # TO DO: display most commonly used end station
    E_Station = df['End Station'].value_counts().idxmax()
    print('\nThis is the most commonly used end station:', E_Station)

    # TO DO: display most frequent combination of start station and end station trip
    C_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nThis is the most commonly used combination of start station and end station trip:',
          S_Station, " & ", E_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    T_Time = sum(df['Trip Duration'])
    print('This is the total travel time:', T_Time/86400, " Days")

    # TO DO: display mean travel time
    M_Time = df['Trip Duration'].mean()
    print('This is the mean travel time:', M_Time/60, " Minutes")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    u_types = df['User Type'].value_counts()
    # print(u_types)
    print('User Types:\n', u_types)

    # TO DO: Display counts of gender
    try:
        g_types = df['Gender'].value_counts()
        print('\nThese are the gender types:\n', g_types)
    except KeyError:
        print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        E_Year = df['Birth Year'].min()
        print('\nThis is the earliest year:', E_Year)
    except KeyError:
        print("\nEarliest Year:\nNo data available for this month.")

    try:
        MR_Year = df['Birth Year'].max()
        print('\nThis is the most recent year:', MR_Year)
    except KeyError:
        print("\nMost Recent Year:\nNo data available for this month.")

    try:
        MC_Year = df['Birth Year'].value_counts().idxmax()
        print('\nThis is the most common year:', MC_Year)
    except KeyError:
        print("\This is the most common year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def list_data(df):
    user_list = input(
        "\nWould you like to see 5 rows of the raw data? Enter yes or no.\n").lower()
    i = 0
    while (user_list == "yes"):
        for j in range(5):
            try:
                print(df.iloc[i])
                print("\n")
                i += 1
            except KeyError:
                print("No more requested data exists in this file.\n")
        user_list = input(
            "\nWould you like to print another five rows? Enter yes or no.\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        list_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
