#US bikeshare Project
import time
import pandas as pd
import numpy as np
import datetime


CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

CITY = ['chicago', 'new york city', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_city():

    """
    Asks user to specify a city
    :return:
     (str) city - name of the city to analyze
    """

    print('Hello! Let\'s explore some US bikeshare data!\n')
    print('Let\'s get started! Shall we?\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city.lower() not in CITY:
        city = input('\nWhich city would you like to view Chicago, New York City or Washington \n'
                     'Please Enter the name of the city \n')

        if city.lower() == 'chicago':
            print('\nFun Fact about Chicago : Chicago has the largest collection of'
                  ' Impressionist paintings outside of Paris.\n ')
            print('-' * 40)
            return city.lower()
        elif city.lower() == "new york city":
            print('\nFun Fact about New York City : Times Square is named after the New York Times.'
                  ' \nIt was originally called Longacre Square until the Times moved there in 1904.')
            print('-' * 40)
            return city.lower()
        elif city.lower() == 'washington':
            print('\nFun Fact about Washington : Bass guitar was originally invented in Washington.')
            print('-' * 40)
            return city.lower()
        else:
            print("\nSorry I couldn't understand your input \nPlease enter either Chicago, "
                  "New York City or Washington")




def get_time_period():
    """
    Ask user for time period
    :return:
    (str) Time filter
    """
    time_period = ''
    while time_period.lower() not in ['month', 'day', 'none']:
        time_period = input('\nWould you life to filter the data by month, day or not at all? '
                            '\nType "none" for no time filter \n')
        if time_period.lower() not in ['month', 'day', 'none']:
            print('\nSorry, I didn\'t your input, Please try again \n '
                  'Enter either "month" or "day" or "none" \n')
    return time_period.lower()


def get_month():
    """
       Ask user for month
       :return:
       (str) month
       """
    month = ''

    while month.lower() not in MONTHS:
        month = input('\nPlease Enter a month from January to June \n')
        if month.lower() not in MONTHS:
            print('\nSorry I didn\'t understand your input \nPlease Try again')

    return month.lower()


def get_day():
    """
       Ask user for day
       :return:
       (str) Day
       """

    day = ''

    while day.lower() not in DAYS:
        day = input('\nPlease enter a day\n')
        if day.lower() not in DAYS:
            print('\nSorry I didn\'t understand your input \nPlease try again')

    return day.lower()


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
        month = MONTHS.index(month) + 1

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
    index = int(df['Start Time'].dt.month.mode())
    most_pop_month = MONTHS[index - 1]

    print(f'\nThe most popular month is {most_pop_month}')

    # display the most common day of week
    index = int(df['Start Time'].dt.dayofweek.mode())
    most_pop_day = DAYS[index]
    print(f'The most popular day of week is {most_pop_day}')

    # display the most common start hour
    most_com_time = df['Start Time'].dt.hour.mode() [0]
    print(f'The most Popular time is {most_com_time} Hrs')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    pop_start = df['Start Station'].mode()[0]
    print(f'The Most popular Start Station is {pop_start}')

    # display most commonly used end station
    pop_end = df['End Station'].mode()[0]
    print(f'The Most popular End Station is {pop_end}')

    # display most frequent combination of start station and end station trip
    popular_trip = df.groupby(['Start Station', 'End Station']).size().nlargest(1).reset_index(name ='count')
    print(f'The most frequent combination of start and end station trip is \n{popular_trip}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()

    t_time = str(datetime.timedelta(seconds = int(total_time)))
    print(f'Total Time Travel = {t_time}')

    # display mean travel time
    avg_time = df['Trip Duration'].mean()
    a_time = datetime.timedelta(seconds=int(avg_time))
    print(f'Average Time Travel = {a_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f'The Types of users are \n{user_types}')

    # Display counts of gender
    gender = df['Gender'].value_counts()
    print(f'\nGender Counts are \n{gender}')

    # Display earliest, most recent, and most common year of birth
    earliest = df['Birth Year'].min()
    recent = df['Birth Year'].max()
    common = df['Birth Year'].mode()[0]
    print(f'\nMost Oldest people are born in {int(earliest)}')
    print(f'Most Youngest people are born in {int(recent)}')
    print(f'Most Popular birth year is {int(common)}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """
    Displays 5 individual trip data based on users request
    :param df:
    :return: Nothing
    """
    start = 0
    end = 5

    question = 'Would you like to view individual trip data? \nType "yes" or "no" \n'

    while True:
        display = input(question)
        if display.lower() in ['yes', 'no']:
            if display.lower() == 'yes':
                print(df[start:end])
                start += 5
                end += 5
                question = 'Would you like to view the next 5 individual trip data? \nType "yes" or "no" \n'
            else:
                break
        else:
            print('Sorry I didn\'t understand your input \nPlease Type "yes" or "no" \n')


def main():
    while True:
        city = get_city()

        day = 'all'
        month = 'all'

        time_period = get_time_period()
        if time_period == 'month' or time_period == 'day':
            if time_period == 'month':
                month = get_month()
            elif time_period == 'day':
                day = get_day()

        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)

        if city != 'washington':
            user_stats(df)

        display_data(df)

        restart = input('\nWould you like to restart? Type "yes" or "no".\n')
        while restart.lower() not in ['yes', 'no']:
            print("Invalid input. Please type 'yes' or 'no'.")
            restart = input('\nWould you like to restart? Type "yes" or "no".\n')
        if restart.lower() != 'yes':
            print('Thank You')
            break


if __name__ == "__main__":
    main()
