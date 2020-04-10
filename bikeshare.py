import datetime
import time
import math
import pandas as pd
import calendar
import numpy as np



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = { 'january': 1,
                'february': 2,
                'march': 3,
                'april': 4,
                'may': 5,
                'june': 6,
                'jan': 1,
                'feb': 2,
                'mar': 3,
                'apr': 4,
                'may': 5,
                'jun': 6}


WEEK_DATA = { 'monday': 0,
                'tuesday': 1,
                'wednesday': 2,
                'thursday': 3,
                'friday': 4,
                'saturday': 5,
                'sunday': 6,
                'mon': 0,
                'tues': 1,
                'wed': 2,
                'thur': 3,
                'fri': 4,
                'sat': 5,
                'sun': 6}


def get_filters():
    """
    Request for analysis that the user specify a city, month, and day.
    Returns:
        (str) city - name of the city that will be analyzed
        (str) month - name of the month to filter by, or "all" to apply no  filter
        (str) day - name of the day of week to filter by, or "all" to apply no filter
    """
    print('Hello! Through this interactive sccript you will be able to explore the Udacity  bikeshare data in the US!')
    print()
    # TO DO: get user input for city (chicago, new york city, washington).
    while 1:
        print('Which city should we look for?')
        city = input('Chicago/CH, New York City/NYC, or Washington/WA? ').lower()
        print()
        if city=='ch':
            city='chicago'
        if city=='ny' or city=='nyc':
            city='new york city'
        if city=='wa' or city=='washington dc':
            city='washington'
        if city not in CITY_DATA:
            print('Kindly enter a valid city')
            continue
        city = CITY_DATA[city]
        break
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... , sunday)
    while 1:
        choice = input('Choose to filter the data by month and/or week? Yes/No ').lower()
        print()
        if choice=='yes' or choice=='y' or choice=='yes':
            choice=True
        elif choice=='no' or choice=='n' or choice=='nope':
            choice=False
        else:
            print('That was not a valid choice. Please try again. ')
            continue
        break

    while 1:
        if choice:
            filter=input('You can filter by month / day / both ').lower()
            print()
            if filter=='month':
                print('Which month\'s data to look at?')
                month = input('January/jan, February/feb, March/mar, April/apr, May, June/jun- ').lower()
                print()
                if month not in MONTH_DATA:
                    print('Invalid input. Please attempt again ?')
                    continue
                month = MONTH_DATA[month]
                day='all'
            elif filter=='day':
                print('Which day\'s data to look at? ')
                day = input('Monday/mon, Tuesday/tues, Wednesday/wed, Thursday/thur, Friday/fri, Saturday/sat, Sunday/sun- ').lower()
                print()
                if day not in WEEK_DATA:
                    print('Invalid input. Please attempt again?')
                    continue
                day = WEEK_DATA[day]
                month='all'
            elif filter=='both':
                print('Which month\'s data to look at?')
                month = input('January/jan, February/feb, March/mar, April/apr, May, June/jun- ').lower()
                print()
                if month not in MONTH_DATA:
                    print('Invalid input. Please attempt again ?')
                    continue
                month = MONTH_DATA[month]
                print('And day of the week?')
                day = input('Monday/mon, Tuesday/tues, Wednesday/wed, Thursday/thur, Friday/fri, Saturday/sat, Sunday/sun- ').lower()
                print()
                if day not in WEEK_DATA:
                    print('Invalid input. Please attempt again ?')
                    continue
                day = WEEK_DATA[day]
            else:
                print('Invalid input. Please attempt again??')
                continue
            break
        else:
            day='all'
            month='all'
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads the data for the specified city and filters by month and day if applicable.
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
    """Displays statistics as per the most frequent times of travel."""

    print('\nCalculating times when travel occurs most frequently ...\n')
    start_time = time.time()

    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    #temporary_df = pd.read_csv(city)
    # TO DO: display the most common month
    most_freq_month = df['month'].mode()[0]
    for num in MONTH_DATA:
        if MONTH_DATA[num]==most_freq_month:
            most_freq_month = num.title()
    print('The most common month during which travel takes place is {}'.format(most_freq_month))

    # TO DO: display the most common day of week
    most_freq_day = df['day_of_week'].mode()[0]
    for num in WEEK_DATA:
        if WEEK_DATA[num]==most_freq_day:
            most_freq_day = num.title()
    print('The most common day of week for travel is {}'.format(most_freq_day))

    # TO DO: display the most common start hour
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour
    most_freq_hour = df['hour'].mode()[0]
    print('The most common hour for travel is {}'.format(most_freq_hour))
    df.drop('hour',axis=1,inplace=True)
    df.drop('day_of_week',axis=1,inplace=True)
    df.drop('month',axis=1,inplace=True)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics related to the most popular stations and trip."""

    print('\nCalculating The most popular stations and trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print()
    print('The most commonly used start station as per your request  was {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print()
    print('The most commonly used end station as per your request was {}'.format(df['End Station'].mode()[0]))

    # TO DO: display the most frequent combination of start station and end station trip
    print()
    most_freq_station_comb = df['Start Station'] + ' to ' + df['End Station']
    print('The most frequent combination of start and end station trip was {}'.format(most_freq_station_comb.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Display statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    travel_durations = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])

    # TO DO: display total travel time
    print()
    td_sum = df['Trip Duration'].sum()
    sum_seconds = td_sum%60
    sum_minutes = td_sum//60%60
    sum_hours = td_sum//3600%60
    sum_days = td_sum//24//3600
    print('Passengers travelled a total of {} days, {} hours, {} minutes and {} seconds'.format(sum_days, sum_hours, sum_minutes, sum_seconds))

    # TO DO: display mean travel time
    print()
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
    print()
    types_of_users = df.groupby('User Type',as_index=False).count()
    print('Number of types of users are {}'.format(len(types_of_users)))
    for i in range(len(types_of_users)):
        print('{}s - {}'.format(types_of_users['User Type'][i], types_of_users['Start Time'][i]))

    # TO DO: Display counts of gender
    print()
    if 'Gender' not in df:
        print('Shoot, no gender data available for this city :(')
    else:
        gender_of_users = df.groupby('Gender',as_index=False).count()
        print('Number of genders of users mentioned in the data are {}'.format(len(gender_of_users)))
        for i in range(len(gender_of_users)):
            print('{}s - {}'.format(gender_of_users['Gender'][i], gender_of_users['Start Time'][i]))
        print('Gender data for {} users is not available.'.format(len(df)-gender_of_users['Start Time'][0]-gender_of_users['Start Time'][1]))

    # TO DO: Display earliest, most recent, and most common year of birth
    print()
    if 'Birth Year' not in df:
        print('Data related to birth year of users is not available for this city.')
    else:
        birth = df.groupby('Birth Year', as_index=False).count()
        print('Earliest year of birth was {}.'.format(int(birth['Birth Year'].min())))
        print('Most recent year of birth was {}.'.format(int(birth['Birth Year'].max())))
        print('Most common year of birth year was {}.'.format(int(birth.iloc[birth['Start Time'].idxmax()]['Birth Year'])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    choice = input('Would you like to read some of the raw data? Yes/No ').lower()
    print()
    if choice=='yes' or choice=='y' or choice=='yes':
        choice=True
    elif choice=='no' or choice=='n' or choice=='nope':
        choice=False
    else:
        print('That was not a valid choice. Please attempt again. ')
        display_data(df)
        return

    if choice:
        while 1:
            for i in range(5):
                print(df.iloc[i])
                print()
            choice = input('Another five? Yes/No ').lower()
            if choice=='yes' or choice=='y' or choice=='yes':
                continue
            elif choice=='no' or choice=='n' or choice=='nope':
                break
            else:
                print('That was not a valid choice.')
                return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nIf you would  like to restart? Enter yes or no.\n').lower()
        print()
        if restart != 'yes' and restart != 'y' and restart != 'yes':
            break

if __name__ == "__main__":
	main()
