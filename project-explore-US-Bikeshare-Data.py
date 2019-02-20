#reference includes python and pandas documentation
import time
import math
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities=['chicago', 'new york city', 'washington']
months=['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
#    """
#    Asks user to specify a city, month, and day to analyze.

#    Returns:
#        (str) city - name of the city to analyze
#        (str) month - name of the month to filter by, or "all" to apply no month filter
#        (str) day - name of the day of week to filter by, or "all" to apply no day filter
#    """
    print('Hello! Let\'s explore some US bikeshare data!')
# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
# get user input for month (all, january, february, ... , june)
# get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            city=input('Would you like to see data for {}?\n'.format(cities)).lower()
        except Exception as e:
            print("Exception occurred: {}".format(e))
        else:
            if city in cities:
                break
            else:
                print('Incorrect input, please input again!')
    while True:
        try:
            i=input('Would you like to filter the data by month, day, both or not at all? Enter none for no time filter?\n').lower()
        except Exception as e:
            print("Exception occurred: {}".format(e))
        else:
            if i in ['month','day','both','none']:
                break
            else:
                print('Incorrect input, please input again!')
    if i=='month':
        while True:
            try:
                month=input('Which month? {}?\n'.format(months)).lower()
                day = 'all'
            except Exception as e:
                print("Exception occurred: {}".format(e))
            else:
                if month in months:
                    break
                else:
                    print('Incorrect input, please input again!')
    elif i=='day':
        while True:
            try:
                month = 'all'
                day=input('Which day of week? {}?\n'.format(days)).lower()
            except Exception as e:
                print("Exception occurred: {}".format(e))
            else:
                if day in days:
                    break
                else:
                    print('Incorrect input, please input again!')
    elif i=='both':
        while True:
            try:
                month=input('Which month? {}?\n'.format(months)).lower()
            except Exception as e:
                print("Exception occurred: {}".format(e))
            else:
                if month in months:
                    break
                else:
                    print('Incorrect input, please input again!')
        while True:
            try:
                month = 'all'
                day=input('Which day of week? {}?\n'.format(days)).lower()
            except Exception as e:
                print("Exception occurred: {}".format(e))
            else:
                if day in days:
                    break
                else:
                    print('Incorrect input, please input again!')
    elif i=='none':
        month = 'all'
        day = 'all'
    else:
        print('Incorrect input, please input again!')

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

    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        df=df[df['month'] == months.index(month) + 1]
    if day != 'all':
        df=df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    most_common_month = df['month'].value_counts().idxmax(skipna=False)
    print('The most common month is: {}'.format(months[most_common_month-1].title()))

    # display the most common day of week

    most_common_day = df['day_of_week'].value_counts().idxmax(skipna=False)
    print('\nThe most common day of week is: {}'.format(most_common_day))

    # display the most common start hour
    most_common_hour = pd.to_datetime(df['Start Time']).dt.hour.value_counts().idxmax(skipna=False)
    print('\nThe most common start hour is: {}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    start_station_f = df['Start Station'].value_counts()
    start_station_fmax_num = start_station_f.max()
    start_station_fmax = [key for key, value in dict(start_station_f).items() if value == start_station_fmax_num]
    print('The most commonly used start station is: {} with {} times'.format(start_station_fmax,start_station_fmax_num))
    #print('The most commonly used start station is: {} with {} times'.format(df['Start Station'].value_counts().idxmax(skipna=False),start_station_fmax_num))
    # display most commonly used end station
    end_station_f = df['End Station'].value_counts()
    end_station_fmax_num = end_station_f.max()
    end_station_fmax = [key for key, value in dict(end_station_f).items() if value == end_station_fmax_num]
    print('\nThe most commonly used end_station is: {} with {} times'.format(end_station_fmax,end_station_fmax_num))

    # display most frequent combination of start station and end station trip
    combine_group=df.groupby(['Start Station','End Station']).groups
    combine_f={}
    for key,value in combine_group.items():
        combine_f[key]=len(value)
    combine_fmax_num = pd.Series(combine_f).max()
    combine_fmax = [key for key, value in combine_f.items() if value == combine_fmax_num]
    print('\nThe most frequent combination of start station and end station trip is: {} with {} times'.format(combine_fmax,combine_fmax_num))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time (hours)
    trip_duration_total = df['Trip Duration'].sum()
    trip_duration_total_h=trip_duration_total//3600
    trip_duration_total_m=((trip_duration_total)%3600)//60
    trip_duration_total_s=((trip_duration_total)%3600)%60
    print('The total travel time is: {} hours {} minute {} seconds'.format(trip_duration_total_h,trip_duration_total_m,trip_duration_total_s))

    # display mean travel time
    trip_duration_mean = df['Trip Duration'].mean()
    trip_duration_mean_h=trip_duration_mean//3600
    trip_duration_mean_m=((trip_duration_mean)%3600)//60
    trip_duration_mean_s=((trip_duration_mean)%3600)%60
    print('\nThe mean travel time is: {} hours {} minute {} seconds'.format(trip_duration_mean_h,trip_duration_mean_m,trip_duration_mean_s))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_group=df.groupby(['User Type']).groups
    user_counts={}
    for key,value in user_group.items():
        user_counts[key]=len(value)
    print('Counts of user types:\n{}'.format(pd.Series(user_counts)))

    # Display counts of gender
    if city != 'washington':
        gender_group=df.groupby(['Gender']).groups
        gender_counts={}
        for key,value in gender_group.items():
            gender_counts[key]=len(value)
        print('\nCounts of gender types:\n{}'.format(pd.Series(gender_counts)))

    # Display earliest, most recent, and most common year of birth
        birth_year_earliest = df['Birth Year'].min()
        birth_year_recent = df['Birth Year'].max()
        birth_year_fmax=df['Birth Year'].value_counts().idxmax(skipna=False)
        if math.isnan(float(birth_year_earliest)):
            print('\nThe earliest year of birth: {}'.format(birth_year_earliest))
        else:
            print('\nThe earliest year of birth: {}'.format(int(birth_year_earliest)))
        if math.isnan(float(birth_year_recent)):
            print('\nThe most recent year of birth: {}'.format(birth_year_recent))
        else:
            print('\nThe most recent year of birth: {}'.format(int(birth_year_recent)))
        if math.isnan(float(birth_year_fmax)):
            print('\nThe most common year of birth: {}'.format(birth_year_fmax))
        else:
            print('\nThe most common year of birth: {}'.format(int(birth_year_fmax)))
    else:
        print('No gender and birth year infomation in the dataset')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df.empty:
            print('The DataFrame is empty!')
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df,city)
        raw = input('\nWould you like to see the raw data? Enter yes or no.\n').lower()
        if raw == 'yes':
            while True:
                try:
                    n=input('\nHow many rows do you want to view? Please enter an integer.\n')
                except Exception as e:
                    print("Exception occurred: {}".format(e))
                else:
                    while True:
                        try:
                            m=0
                            if float(n).is_integer:
                                print(df.head(int(n)))
                                m='Yeah!'
                            else:
                                print('Incorrect enter, please input again!')
                        except Exception as e:
                            print("Exception occurred: {}".format(e))
                            break
                        else:
                            while True:
                                try:
                                    a=input('\nWould you like to reinput the the row number? Enter yes or no\n')
                                except Exception as e:
                                    print("Exception occurred: {}".format(e))
                                    break
                                else:
                                    if a=='yes' or a=='no':
                                        break
                                    else:
                                        print('\nyes or no?\n')
                            if a=='yes' or a=='no':
                                break
                    if m=='Yeah!' and a=='no':
                        break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
