import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv',
	      'los angeles': 'los_angeles.csv',
              'san francisco': 'san_francisco.csv',
              'san diego': 'san_diego.csv' }
months = ['all', 'january', 'feruary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'octorber', 'november', 'december']
days = ['all', 'sunday', 'monday', 'tuesday', 'wendesday', 'thursday', 'friday', 'saturday']

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
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            city = str(input('Please enter the name of city: ').lower())
            if city in CITY_DATA.keys():
                pass
            else:
                city = str(input('Please enter the name of city again!').lower())
            
            month = str(input('Please enter the name of month: ').lower)
            if month in months:
                pass
            else:
                month = str(input('Please enter the name of month again!').lower())
               
            day = str(input('Please enter the name of day of week: ').lower())
            if day in days:
               break
            else:
                day = str(input('Please enter the name of day of week again!').lower())
        except (ValueError, KeyError):
            print('That is not valid entry. Please try it again.')
        except KeyboardInterrupt:
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
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'nobember', 'december']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
       
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    if day == 'all':
        df = df

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'nobember', 'december']
    keys_month = df['month'].value_counts().index
    vals_month = df['month'].value_counts()
    month_dist = dict(zip(keys_month, vals_month))
    most_common_month = [months[i].title() for i in range(1, 13) if max(month_dist) == i]
    most_common_month.append(month_dist[max(month_dist)])
    
    print('The most common month: ({}, {})\n'.format(most_common_month[0], most_common_month[1]))

    # TO DO: display the most common day of week
    keys_day = df['day_of_week'].value_counts().index
    vals_day = df['day_of_week'].value_counts()
    day_dist = dict(zip(keys_day, vals_day))
    most_common_day = [max(day_dist), day_dist[max(day_dist)]]
    print('The most common day of week: ({}, {})\n'.format(most_common_day[0], most_common_day[1]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    keys_hour = df['hour'].value_counts().index
    vals_hour = df['hour'].value_counts()
    hour_dist = dict(zip(keys_hour, vals_hour))
    most_common_hour = [max(hour_dist), hour_dist[max(hour_dist)]]
    print('The most common start hour: ({}, {})\n'.format(most_common_hour[0], most_common_day[1]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    ss_keys = list(df['Start Station'].value_counts().index)
    ss_vals = list(df['Start Station'].value_counts())
    ss_dist = dict(zip(ss_keys, ss_vals))
    most_popular_start_station = max(ss_dist)
    max_val_ss = ss_dist[most_popular_start_station]
    print('The most commonly used start station: ({}, {})\n'.format(most_popular_start_station, max_val_ss))
   
    # TO DO: display most commonly used end station
    es_keys = list(df['End Station'].value_counts().index)
    es_vals = list(df['End Station'].value_counts())
    es_dist = dict(zip(es_keys, es_vals))
    most_popular_end_station = max(es_dist)
    max_val_es = es_dist[most_popular_end_station]
    print('The most commonly used end station: ({}, {})\n'.format(most_popular_end_station, max_val_es))
    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start  station and end station trip: Start Station: ({}, {}), End Station: ({}, {})'.format(most_popular_start_station, max_val_ss, most_popular_end_station, max_val_es))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_tt = df['Trip Duration'].sum()
    print('Total Travel Time: {}'.format(total_tt))
    # TO DO: display mean travel time
    avg_tt = df['Trip Duration'].mean()
    print('The mean of Travel Time: {}'.format(avg_tt))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
    	gender = df['Gender'].value_counts()
    	print(gender)
    else:
	pass
    # TO DO: Display earliest, most recent, and most common year of birth
    keys_year = df['Birth Year'].value_counts().index
    vals_year = df['Birth Year'].value_counts()
    year_dist = dict(zip(keys_year, vals_year))
    earliest = min(keys_year)
    recent = max(keys_year)
    common = max(year_dist)
    print('The earliest year of birth:     {}\n'.format(earliest))
    print('The most recent year of birth:  {}\n'.format(recent))
    print('The most common year of birth:  {}\n'.format(common))

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
