import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS_ALL = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
WEEKDAY_ALL = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6, 'all': 7}

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
    for city in CITY_DATA.keys():
        city = input('Enter a city name (chicago, new york city, or washington): \n').lower()
        if city in CITY_DATA.keys():
            try:
                break
            except:
                print('Please enter a valid city.  Your choices are chicago, new york city, or washington')
            finally:
                print("Your choice of city is: {}".format(city))

    # get user input for month (all, january, february, ... , june)
    for month in MONTHS_ALL.keys():
        month = input('Choose a month (all, january, february, march, april, may, june): \n').lower()
        if month in  MONTHS_ALL.keys():
            try:
                break
            except:
                print('Please enter a valid month.  Your choices are all, january, february, march, april, may, or june')
            finally:
                print("The month you selected is: {}".format(month))
    # get user input for day of week (all, monday, tuesday, ... sunday)
    for day in WEEKDAY_ALL.keys():
        day = input('Choose a day of the week (all, monday, tuesday, wednesday, thursday, friday, saturday,  sunday): \n').lower()
        if day in WEEKDAY_ALL.keys():
            try:
                break
            except :
                print('Please enter a valid month.  Your choices are all, monday, tuesday, wednesday, thursday, friday, saturday, sunday')
            finally:
                print("The day of the week you want to see is : {}".format(day))

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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour

    if city == 'washington':
        df['Gender'] = "No gender data for washington"
        df['Birth Year'] = "No birth year information for washington"

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['','january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = months[df['month'].mode()[0]]
    print('The most common month is: {}'.format(most_common_month).title())


    # display the most common day of week
    most_common_dow = df['day_of_week'].mode()[0]
    print('The most common day of the week is: {}'.format(most_common_dow).title())

    # display the most common start hour
    most_common_shour = df['hour'].mode()[0]
    print('The most common starting hour is: {}'.format(most_common_shour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mc_st_station = df['Start Station'].mode()[0]
    print('The most common start station is: {}'.format(mc_st_station))


    # display most commonly used end station
    mc_end_station = df['End Station'].mode()[0]
    print('The most common end station is: {}'.format(mc_end_station))


    # display most frequent combination of start station and end station trip
    mc_start_end = df[['Start Station', 'End Station']].mode().loc[0]
    print('The most frequent combination of start and end station is: {} and {}'.format(mc_start_end[0], mc_start_end[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Dep Time'] = pd.to_datetime(df['Start Time'])
    df['Arr Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['Arr Time'] - df['Dep Time']
    tot_trav_time = df['Travel Time'].sum()
    print('The total travel time is {} seconds'.format(tot_trav_time))

    # display mean travel time
    mean_travel_time = df['Travel Time'].mean()
    print('The average travel time is {} seconds'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    gender = df['Gender'].value_counts()
    print(gender)


    # Display earliest, most recent, and most common year of birth
    earliest_yob = df['Birth Year'].min()
    print('The earliest year of birth is: {}'.format(earliest_yob))
    mr_yob = df['Birth Year'].max()
    print('The most recent year of birth is: {}'.format(mr_yob))
    mc_yob = df['Birth Year'].mode()
    print('The most common year of birth is: {}'.format(mc_yob))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    print("Displaying the first 5 lines of raw data")
    m = 0
    n = 5
    rdata = df.iloc[m:n]
    print(rdata)
    masdata = input('\nWould you like to see the next 5 lines of raw data?  Enter yes or no\n').lower()
    while True:
        if masdata == 'yes':
            m+=5
            n+=5
            rdata = df.iloc[m:n]
            print(rdata)
            print('\nDisplaying lines {} through {} of raw data\n'.format(m+1,n))
            masdata = input('\nWould you like to see another 5 lines of raw data?  Enter "yes" for more or any key(s) for no\n').lower()
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(city, month, day)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
