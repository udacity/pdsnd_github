import time
import pandas as pd
import calendar as cal
import datetime as dt
import numpy as np

"""Why calendar library??  I wanted to try using some libraries that were not included after reading a lot of
different articles and documentation.  I am sure this is the "hard" way to do a lot of these solutions"""

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}


def run_programs(program):
    """now works"""
    inp = ''  # I have to set it each call? This seems weird but forcing it to blank each time seems to work?
    while inp != 'y':
        inp = input('Would you like me to run {} ? (Y/N):'.format(program)).lower()
        if inp == 'n':
            break
    return inp


def get_filters(city_list):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # I thought about using dictionaries here - but I wasn't able to get them to work properly.
    month_select = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
    day_select = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid
    # inputs
    while True:
        try:
            city = str(input('What City are you looking for? (Chicago, New York, Washington): ')).lower()
        except NameError:
            print('Invalid Entry \n')
            continue
        except TypeError:
            print('Invalid Entry \n')
            continue
        else:
            if city in city_list.keys():
                break
            else:
                print('Data Not Available \n')
                continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input('What month are you looking for? (January, February... All): ')).title()
        except NameError:
            print('Invalid Entry \n')
            continue
        except TypeError:
            print('Invalid Entry \n')
            continue
        else:
            if month in month_select:
                break
            else:
                print('That is not a month \n')
                continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input('What day are you looking for? (Monday, Tuesday... All): ')).title()
        except NameError:
            print('Invalid Entry \n')
            continue
        except TypeError:
            print('Invalid Entry \n')
            continue
        else:
            if day in day_select:
                break
            else:
                print('That is not a day \n')
                continue

    print('-' * 40)
    return city, month, day


def num_month(month):
    # converts string month to integer value for return to lambda
    if month == "January":
        return 1
    elif month == "February":
        return 2
    elif month == "March":
        return 3
    elif month == "April":
        return 4
    elif month == "May":
        return 5
    elif month == "June":
        return 6
    else:
        print('Month Not Available - Defaulting to January')
        return 1


def num_day(day):
    # this was used in lambda but runs much faster without it
    if day == "Monday":
        return 0
    elif day == "Tuesday":
        return 1
    elif day == "Wednesday":
        return 2
    elif day == "Thursday":
        return 3
    elif day == "Friday":
        return 4
    elif day == "Saturday":
        return 5
    elif day == "Sunday":
        return 6
    else:
        print('Something Went Wrong - Using default values')
        return 0


def load_data(city, month, day, CITY_DATA):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    unsorted = pd.read_csv(CITY_DATA.get(city))
    unsorted['Start Time'] = pd.to_datetime(unsorted['Start Time'])

    if month != 'All':
        unsorted = unsorted[(unsorted['Start Time'].dt.month == num_month(month))]
        if day != 'All':
            unsorted = unsorted[(unsorted['Start Time'].dt.weekday == num_day(day))]
    else:
        if day != 'All':
            unsorted = unsorted[(unsorted['Start Time'].dt.weekday == num_day(day))]
    df = unsorted
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    df['month'] = df['Start Time'].dt.month
    top_mo = df
    top_mo['Mo_Name'] = top_mo['month'].apply(lambda x: cal.month_abbr[x]) # wanted to try using lambda here
    print('\nMost common month is: \n{}'.format(top_mo['Mo_Name'].mode()[0]))
    # TO DO: display the most common day of week
    df['Weekday'] = df['Start Time'].dt.day_name()
    top_dy = df
    print('\nThe most common Weekday is: \n{}'.format(top_dy['Weekday'].mode()[0]))
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    df['hour'] = df['hour'].astype(str) + ':00'
    top_hr = df
    print('\nThe most common starting hour is: \n{}'.format(top_hr['hour'].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts()
    start_station = start_station.sort_values(ascending=False)
    print('\nMost Common Start Station is: \n {}'.format(start_station.head(1)))
    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts()
    end_station = end_station.sort_values(ascending=False)
    print('\nMost Common End Station is: \n {}'.format(end_station.head(1)))
    # TO DO: display most frequent combination of start station and end station trip
    comb_station = df
    comb_station['comb_station'] = comb_station['Start Station'] + ' -> ' + comb_station['End Station']
    print('\nThe most common station route is: \n {}'.format(comb_station['comb_station'].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']
    # TO DO: display total travel time
    print('\nTotal Travel Time in this segment of data: \n {}'.format(df['Travel Time'].sum()))
    # TO DO: display mean travel time
    print('\nMean Travel Time in this segment of data: \n {}'.format(df['Travel Time'].mean()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nUser Types: \n{}'.format(df['User Type'].value_counts()))
    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\nGenders: \n{}'.format(df['Gender'].value_counts()))
    else:
        '\nThis data does not have Gender information available...Sorry.\n'
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('\nThe Earliest Birth year for this segment: \n{}'.format(int(df['Birth Year'].min())))
        print('The most recent birth year for this segment: \n{}'.format(int(df['Birth Year'].max())))
        print('The most common birth  year for this segment: \n{}'.format(df['Birth Year'].mode()[0]))
    else:
        '\nNo Birth Data Available...Sorry.\n'
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def show_five(df):
    """shows 5 rows at a time and ends on no."""
    st = 0
    fn = 5
    while True:
        print(df[st:fn])
        st += 5
        fn += 5
        ans = input('Show 5 more? (y/n): ').lower()
        if ans != 'y':
            print('Bye!')
            break
        else:
            continue


def main():
    while True:
        city, month, day = get_filters(CITY_DATA)
        df = load_data(city, month, day, CITY_DATA)
        # The below still repeats some code but it doesn't repeat a lot - I'm curious if there's a better way?
        if run_programs('time stats') == 'y':
            time_stats(df)
        if run_programs('station stats') == 'y':
            station_stats(df)
        if run_programs('trip stats') == 'y':
            trip_duration_stats(df)
        if run_programs('user stats') == 'y':
            user_stats(df)
        if run_programs('five rows') == 'y':
            show_five(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
