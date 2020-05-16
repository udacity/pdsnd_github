import time
import datetime
import calendar
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = get_city()
            filter_data = input('Would to like to filter by month, day, both or all ? ')
            filter_data = filter_data.lower()
            if filter_data == 'month':
                month = get_month()
                day = 'all'
            elif filter_data == 'day':
                day = get_day()
                month = 'all'
            elif filter_data == 'both':
                month = input('Which month would you like to explore from January - June or All ? ')
                month = month.lower()
                day = input('Would you like to explore data for any particular day from Monday-Sunday or All the days ? Type day name or all ')
                day = day.lower()
            else:
                month = 'all'
                day = 'all'
            break
        except ValueError:
            print('Please enter the right name')


    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('-'*40)
    return city, month, day

def get_city():
    city = input('Which city would you like to explore new york, chicago or washington? ')
    city = city.lower()
    if city == 'new york':
        city = 'new york city'
    return city
def get_month():
    month = input('Which month would you like to explore from January - June or All ? ')
    month = month.lower()
    return month
def get_day():
    day = input('Would you like to explore data for any particular day from Monday-Sunday or All the days ? Type day name or all ')
    day = day.lower()
    return day

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
    # extract month from start time
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    #df['month'] = df['month'].apply(lambda x: calendar.month_abbr[x])


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        df['month'] = df['Start Time'].dt.strftime('%b')
    # extract day from start time
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = ['january', 'february', 'march', 'april', 'may', 'june']

    # TO DO: display the most common month
    # popular month
    common_month = df['month'].mode()[0]


    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common month people like to ride is {0}: '.format(common_month))
    print('It is likely that they ride on a {0}: '.format(common_day))
    print('People ride mostly at {0} hour'.format(common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    popular_start_station_count = df['Start Station'].count()

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    popular_end_station_count = df['End Station'].count()

    # TO DO: display most frequent combination of start station and end station trip
    combo_station = df.groupby(['Start Station', 'End Station'])
    popular_combo_station = combo_station.size().idxmax()
    print('Popular start station for this city is: {0} and the count is {1} '.format(popular_start_station, popular_start_station_count))
    print('Popular end station for this city is: {0} and the count is {1} '.format(popular_end_station, popular_end_station_count))
    print('Popular combined station for this city is:{0}  '.format(popular_combo_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    seconds = df['Trip Duration'].sum()
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    print('Total travel time is {0} days {1} hours {2} and {3} seconds.'.format(days, hours, minutes, seconds))


    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    avg_minutes, avg_travel_time = divmod(avg_travel_time, 60)
    avg_hours, avg_minutes = divmod(avg_minutes, 60)
    avg_days, avg_hours = divmod(avg_hours, 24)
    print('Mean travel time is {0} days {1} hours {2} and {3} seconds.'.format(days, avg_hours, avg_minutes, avg_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    user_types_list = user_types.index.tolist()
    subscribers = user_types.loc['Subscriber']
    customers = user_types.loc['Customer']

    if 'Dependent' in user_types_list:
        dependents = user_types.loc['Dependent']
        print('There are {0} subscribers, {1} customers and {2} dependents'.format(subscribers, customers, dependents))
    else:
        print('There are {0} subscribers, {1} customers '.format(subscribers, customers))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        male = gender.loc['Male']
        female = gender.loc['Female']
        print('There are {0} males and {1} females who ride bicycle'.format(male, female))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print('earliest birth: ',earliest_birth)
        print('recent birth: ', recent_birth)
        print('common birth year', common_birth_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def ask_more_data(df):
    x = 5


    while x < len(df.index):
        see_more_data = input('Would you like to see more data? Type yes or no ')
        if see_more_data.lower() == 'yes':
            y = x+5
            print(df[x:y])
        elif see_more_data.lower() == 'no':
            break
        x = x+5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        ask_more_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
