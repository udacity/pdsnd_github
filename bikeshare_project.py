import time
import pandas as pd
import numpy as np
import datetime
import calendar

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


    city = input("What city would you like to analyze? Name city - Chicago, New York City or Washington: \n").lower()
    while city not in('chicago', 'new york city', 'washington'):
        print("That's not a valid entry please try again\n")
        city = input("What city would you like to analyze? Name city - Chicago, New York City or Washington:   \n").lower()


    # get user input for month (all, january, february, ... , june)
    month = input("What month would you like to analyze? Name one month, or type 'All'. Only January to June are available:   \n").lower()
    while month not in('january', 'febuary', 'march', 'april', 'may', 'june','all'):
        print('That\'s not a valid entry - remember only first 6 month are available\n')
        month = input("What month would you like to analyze? Name one month, or type 'All'. Only January to June are available:   \n").lower()

    #get day input
    day = input("What day of week would you like to analyze? Name one day, or type 'All' \n").lower()
    while day not in('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        print('That\'s not a valid entry: please try again.\n')
        day = input("What day of the week would you like to analyze? Name on day or type 'all':  \n")


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
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'], infer_datetime_format=True)

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    ##clean up column headings
    #df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    print("\nThe most common month for bike hire is: ")

    df['month'] = df['month'].apply(lambda x: calendar.month_name[x])
    mode_month_hire = df.month.mode()
    print(mode_month_hire.iloc[0])

    # display the most common day of week
    print("\nThe most common day of the week for bike hire is: ")
    print(df.day_of_week.mode().iloc[0])

    # display the most common start hour
    print("\nThe most common time to hire a bike is: ")
    mode_start_time = df.start_time.mode().iloc[0]
    print(mode_start_time.strftime('%X'))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()

    # display most commonly used start station
    print('\nThe most commonly used start station is: ')
    print(df.start_station.mode().iloc[0])

    # display most commonly used end station
    print('\nThe most commonly used end station is: ')
    print(df.end_station.mode().iloc[0])

    # display most frequent combination of start station and end station trip
    print('\nThe most frequent combo of start and end station is: ')

    #create new column with start and end stations
    df['start_and_end_station'] = df['start_station'] + ' - travel to - ' + df['end_station']
    print(df.start_and_end_station.mode().iloc[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    ##clean up column headings
    #df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('\nThe total hours travel time is: ')
    print(round((df.trip_duration.sum()/60)/60))

    # display mean travel time
    print('\nThe average travel time in minutes is: ')
    print(round((df.trip_duration.mean()/60), 2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def tidy_data(df):
    """A function to tidy the data for review analysis."""

    ##clean up column headings
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

def user_stats(df):
    """Displays statistics on bikeshare users."""

    ##clean up column headings - this has been moved to tidy_data(df) function
    #df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

    #set birth_year column as Int64 - Moved to tidy_data(df) function (removed since doesn't work for Washington)
    df['birth_year'] = df['birth_year'].astype(pd.Int64Dtype())

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types - output convert to string to remove dtype fomatting.
    print("\nCount of user type as follows: ")
    print(df['user_type'].value_counts().to_string())

    ## TO DO - this paused program... I'm guessing with the Y axis code
    ##df.plot(x ='user_type', y=('user_type').count('user_type'), kind = 'bar')

    # Display counts of gender
    print("\nCount of gender as follows: ")
    print(df.groupby('gender').size().to_string())

    # Display earliest, most recent, and most common year of birth
    print('\nEarliest year of birth:')
    min_yob = df.birth_year.min()
    print(min_yob)

    print('\nMax year of birth: ')
    max_yob = df.birth_year.max()
    print(max_yob)

    print('\nMost common year of birth: ')
    mod_yob = df.birth_year.mode().iloc[0]
    print(mod_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    #print first 5 rows of df
    show_5rows = input('Would you like to see the first five rows? Yes?  ').lower()

    #variables to decide which 5 rows to print.
    x = 0
    y = 5

    #while loop to specify whether to print first five and subsequent 5

    while show_5rows == 'yes':
        print(df.iloc[x:y])
        x += 5
        y += 5
        show_5rows = input('Would you like to see the next five rows? Yes or No?  ').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)


        if city == 'washington':
            tidy_data(df)
            time_stats(df)
            station_stats(df)
            print("\nNo user stats are available for Washington")
            trip_duration_stats(df)
            display_raw_data(df)

        else:
            tidy_data(df)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_raw_data(df)



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
