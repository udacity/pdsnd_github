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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Checks that a valid city is entered. If not, asks user to enter again.
    check_city = 0
    while check_city == 0:
        city = input("Choose from one of the following cities: chicago, new york city, washington: ").lower()
        print("City is: ", city)
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            check_city = 1
        else:
            print("This is not a valid city, please try again.\n\n")

    # get user input for month (all, january, february, ... , june)
    # Checks that a valid month is entered. If not, asks user to enter again.
    check_month = 0
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    while check_month == 0:
        month = input("Which month would you like to filter results by (enter 'all' for no filter): ").lower()
        if month in months or month == 'all':
            check_month = 1
        else:
            print("This is not a valid month, please try again.\n\n")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    # Checks that a valid day is entered. If not, asks user to enter again.
    check_day = 0
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    while check_day == 0:
        day = input("Which day of the week would you like to filter results by (enter 'all' for no filter): ").lower()
        if day in days or day == 'all':
            check_day = 1
        else:
            print("This is not a valid day, please try again.\n\n")

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

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most Frequent Month: ', df['month'].mode()[0])

    # display the most common day of week
    print('Most Frequent Day of Week: ', df['day_of_week'].mode()[0])

    # display the most common start hour
    print('Most Frequent Start Hour: ', df['Start Time'].dt.hour.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most Frequent Start Station: ', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('Most Frequent End Station: ', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    popular_combo = df['Start Station'] + ' to ' + df['End Station']
    print('Most Frequent Trip Combination: ', popular_combo.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time: ', df['Trip Duration'].sum())

    # display mean travel time
    print('Average travel time: ', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Count of User Types:\n', df['User Type'].value_counts().to_frame().to_string(header=False))

    # Display counts of gender
    if 'Gender' in df.columns:
        print('\nCount of Genders:\n', df['Gender'].value_counts().to_frame().to_string(header=False))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nEarliest Birth Year (oldest): ', int(df['Birth Year'].min()))
        print('Most Recent Birth Year (youngest): ', int(df['Birth Year'].max()))
        print('Most Common Birth Year: ', int(df['Birth Year'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Asks the user if they would like to display raw data. Displays statistics on bikeshare users.

    Args:
        (str) raw - user input (yes or no only)

    Returns:
        df (5 lines) - Pandas DataFrame containing city data filtered by month and day
    """
    data_check = 0
    while data_check == 0:
        user_input = input("Would you like to see 5 lines of raw data (yes or no): ").lower()
        if user_input == 'yes':
            print(df.head())
        elif user_input == 'no':
            data_check = 1
        else:
            print("This is not a valid option, please try again.\n\n")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
