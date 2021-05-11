import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['all', 'jan', 'feb', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

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
        city = input('Choose one the cities from Chicago, New York or Washington to explore \n> ').lower()
        if city.lower() in CITY_DATA:
            break
        else:
            print('Please Try again')
        
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Provide a month name from all, jan, feb, ... , june \n>')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Provide a day name from all, monday, tuesday, ... sunday \n>')

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
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month =  MONTH_DATA.index(month) + 1
        df = df[ df['month'] == month ]

    if day != 'all':
        df = df[ df['day_of_week'] == day.title()]
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f"The most common month from the given fitered data is: {common_month}")

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"The most common day of week is : {common_day}")

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print(f"The most common start hour is: {str(common_start_hour)}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is: {commonly_start_station}")

    # TO DO: display most commonly used end station
    commonly_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station is: {commonly_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    freq_comb = (df[['Start Station', 'End Station']]).mode().loc[0]
    print(f"The most frequent combination of start station is {freq_comb[0]} and end station is {freq_comb[1]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_travel_time = df['Trip Duration'].sum()
    print(f"The total travel time : {sum_travel_time}")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"The mean travel time is: {mean_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    cnt_user_type = df["User Type"].value_counts()
    for index in cnt_user_type.index:
        print(f"The counts of {index} is: {cnt_user_type[index]}")
    print("\n")


    # TO DO: Display counts of gender
    cnt_gender = df["Gender"].value_counts()
    for index in cnt_gender.index:
        print(f"The counts of {index} is: {cnt_gender[index]}")


    # TO DO: Display earliest, most recent, and most common year of birth
    print(f"Earliest year of birth is {df['Birth Year'].min()}")
    
    print(f"Most recent year of birth is {df['Birth Year'].max()}")
    
    print(f"Most common year of birth is {df['Birth Year'].mode()[0]}")

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
