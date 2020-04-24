import time
import math
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}
MONTH_DATA = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6}
DAY_DATA = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}


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
    while 1:
        print('For which country you want to have data about?')
        city = input('Chicago (C), New York City (NYC) or Washington (W)? \n')
        print()
        if city=='C' or city=='Chicago':
            city='chicago'
        if city=='NYC'or city=='New York City':
            city='new york city'
        if city=='W' or city=='Washtington':
            city='washington'
        if city not in CITY_DATA:
            print('Please enter C, NYC or W')
            continue
        city = CITY_DATA[city]
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while 1:
       print('For which month you want to have data about?')
       month = input('All, January, February, March, April, May, June \n')
       print()
       if month in MONTH_DATA:
          month = MONTH_DATA[month]
       elif month not in MONTH_DATA and month != 'All':
          print('Your input was false. Please try again.')
       elif month == 'All':
          month = 'all'
       break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while 1:
        print('For which day you want to have data about?')
        day = input('All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday \n')
        print()
        if day in DAY_DATA:
           day = DAY_DATA[day]
        elif day not in DAY_DATA and day != 'All':
           print('Your input was false. Please try again.')
        elif day == 'All':
           day = 'all'
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
    df = pd.read_csv(city)
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    if day != 'all':
        df = df[df['day_of_week'] == day]
    if month != 'all':
        df = df[df['month'] == month]
    df.drop('day_of_week',axis=1,inplace=True)
    df.drop('month',axis=1,inplace=True)
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['month'] = pd.to_datetime(df['Start Time']).dt.month

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    for num in MONTH_DATA:
        if MONTH_DATA[num]==most_common_month:
            most_common_month = num.title()
    print('The most common month of travel is {}'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    for num in DAY_DATA:
        if DAY_DATA[num]==most_common_day:
            most_common_day = num.title()
    print('The most common day of week of travel is {}'.format(most_common_day))

    # TO DO: display the most common start hour
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour of travel is {}'.format(most_common_hour))
    df.drop('hour',axis=1,inplace=True)
    df.drop('day_of_week',axis=1,inplace=True)
    df.drop('month',axis=1,inplace=True)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station was {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most commonly used end station was {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    most_common_station_comb = df['Start Station'] + ' to ' + df['End Station']
    print('The most frequent combination of start station and end station trip was {}'.format(most_common_station_comb.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    travel_durations = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])

    # TO DO: display total travel time
    td_sum = df['Trip Duration'].sum()
    sum_seconds = td_sum%60
    sum_minutes = td_sum//60%60
    sum_hours = td_sum//3600%60
    sum_days = td_sum//24//3600
    print('The total travel time was {} days, {} hours, {} minutes and {} seconds'.format(sum_days, sum_hours, sum_minutes, sum_seconds))


    # TO DO: display mean travel time
    td_mean = math.ceil(df['Trip Duration'].mean())
    mean_seconds = td_mean%60
    mean_minutes = td_mean//60%60
    mean_hours = td_mean//3600%60
    mean_days = td_mean//24//3600
    print('Passengers travelled an average of {} hours, {} minutes and {} seconds'.format(mean_hours, mean_minutes, mean_seconds))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    types_of_users = df.groupby('User Type',as_index=False).count()
    print('There are {} different user types.'.format(len(types_of_users)))
    for i in range(len(types_of_users)):
        print('{}s - {}'.format(types_of_users['User Type'][i], types_of_users['Start Time'][i]))


    # TO DO: Display counts of gender
    print()
    if 'Gender' not in df:
        print('There is no gender data available.')
    else:
        gender_of_users = df.groupby('Gender',as_index=False).count()
        print('There are {} different genders.'.format(len(gender_of_users)))
        for i in range(len(gender_of_users)):
            print('{}s - {}'.format(gender_of_users['Gender'][i], gender_of_users['Start Time'][i]))
        print('There is no gender data for {} users available.'.format(len(df)-gender_of_users['Start Time'][0]-gender_of_users['Start Time'][1]))

    # TO DO: Display earliest, most recent, and most common year of birth
    print()
    if 'Birth Year' not in df:
        print('There is no birht data available.')
    else:
        birth = df.groupby('Birth Year', as_index=False).count()
        print('The earliest year of birth was {}.'.format(int(birth['Birth Year'].min())))
        print('The most recent year of birth was {}.'.format(int(birth['Birth Year'].max())))
        print('The most common year of birth year was {}.'.format(int(birth.iloc[birth['Start Time'].idxmax()]['Birth Year'])))

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
