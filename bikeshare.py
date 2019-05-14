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
    city_list = ['chicago', 'new york city', 'washington']
    city = input('Would you like to see data for chicago, new york city, or washington? ').lower()
    print(city)

    while city not in city_list:
        print('That\'s not a valid city name')
        try:
            city = input('Would you like to see data for chicago, new york city, or washington? ').lower()
            print(city)
        except:
            break

    month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('Would you like to filter by which month- all, january, february, march, april, may, or june? ').lower()
    print(month)
    while month not in month_list:
        print('That\'s not a valid month name')
        try:
            month = input('Would you like to filter by which month- all, january, february, march, april, may, or june? ').lower()
            print(month)
        except:
            break

    day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('Would you like to filter by which day- all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday? ').lower()

    while day not in day_list:
        print('That\'s not a valid day name')
        try:
            day = input('Would you like to filter by which day- all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday? ').lower()
            print(day)
        except:
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

    # in this section calculate the most common month, day, hour and then count the number of them 
def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 'all':
        most_common_month = df['month'].mode()[0]
        df_most_common_month = df[df['month']==most_common_month]
        print('the most common month:', most_common_month)
        print('Count:', len(df_most_common_month))
    else:
        print("There is no the most common month since you have selected one specific month!")

    # display the most common day of week
    if day == 'all':
        most_common_day = df['day_of_week'].mode()[0]
        df_most_common_day = df[df['day_of_week']==most_common_day]
        print('the most common day:', most_common_day.title())
        print('Count:', len(df_most_common_day))
    else:
        print("There is no the most common day since you have selected one specific day!")

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    df_common_hour = df[df['hour']==common_hour]
    print('the most common start hour:', common_hour)
    print('Count:', len(df_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    df_common_start_station = df[df['Start Station']==common_start_station]
    print('the most common start station:', common_start_station)
    print('Count:', len(df_common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    df_common_end_station = df[df['End Station']==common_end_station]

    print('the most common end station:', common_start_station)
    print('Count:', len(df_common_end_station))

    # display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'].map(str) + '&' + df['End Station']
    popular_start_end = df['Start End'].value_counts().idxmax()
    df_popular_start_end = df[df['Start End']==popular_start_end]
    print('the most frequent combination of start end station:', popular_start_end)
    print('Count:', len(df_popular_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()

    print('total travel time:', total_duration)


    # display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print('the mean of travel time:', mean_duration)


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
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("Gender column is not present in dataframe")


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        print ("earliest", earliest)
        recent = df['Birth Year'].max()
        print("recent", recent)
        common_year = df['Birth Year'].mode()[0]
        print ("common_year", common_year)
    else:
        print("Birth Year column is not present in dataframe")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    restart = input('\nDo you like to display 5 records of raw data ? Enter yes or no.\n')
    if restart.lower() == 'yes':
        print(df.head())
    while restart.lower() == 'yes':
        restart = input('\nDo you like to display more records of raw data ? Enter yes or no.\n')
        if restart.lower() == 'yes':

            try:
                staring_row_index = int(input('\nWhat is the staring row indiex you like to display.\n'))
                #print(staring_row_index)
            except ValueError:
                print('That\'s not an integer value')
                staring_row_index = int(input('\nWhat is the staring row indiex you like to display.\n'))
                #print(staring_row_index)
            try:
                ending_row_index = int(input('\nWhat is the ending row indiex you like to display.\n'))
                #print(ending_row_index)
            except ValueError:
                print('That\'s not an integer value')
                ending_row_index = int(input('\nWhat is the ending row indiex you like to display.\n'))
                #print(ending_row_index)
            print(df.iloc[staring_row_index:ending_row_index,:])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
