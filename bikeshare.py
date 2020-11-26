import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'newyork': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Ask user to specify a city, month, and day to analyze.

    Return:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('- '*20)

    while 1:
    
        print('Would you like to see data for "Chicago", "New York", or "Washington"?')
        city = input('Type city here: ').lower().replace(" ", "")
        if(city in CITY_DATA):
            print('- '*20)
            print('Filter shows results for city {} only'.format(city))
            break;
        else:
            print('Please type a valid city!')
        
    print('- '*20)
    print('Would you like to filter the data by "month", "day", or not at "all"?');
    filter = input('Type filter here: ').lower()
    if filter == "month":
        while 1:
            try:
                print('- '*20)
                print('Which month - 1 January, 2 February, 3 March, 4 April, 5 May, or 6 June?')
                month = int(input('Enter month as integer: '))
                day = "all"
                # month validation ... change to 12 if having a full year of data
                if month > 0 & month <= 6:
                    print('- '*20)
                    print('Filter set to month {}'.format(pd.to_datetime(month, format='%m').strftime('%B')))
                    break;
                else:
                    print('Please type a valid month (1-6)!')
            except:
                break;
    elif filter == "day":
        while 1:
            try:
                print('- '*20)
                print('Which day - 1 Monday, 2 Tuesday, 3 Wednesday, 4 Thursday, 5 Friday, 6 Saturday, or 7 Sunday?')
                day = int(input('Enter day as integer: '))
                month = "all"
                # day validation
                if day > 0 & day <= 7:
                    print('- '*20)
                    print('Filter set to day {}'.format(pd.to_datetime(day, format='%d').strftime('%A')))
                    break;
                else:
                    print('Please type a valid day (1-7)!')
            except:
                break;
    else:
        print('-'*40)
        print('No filter selected. Showing all results unfiltered.')
        month="all"
        day="all"
    
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

    # Unnamed, Start Time, End Time, Trip Duration, Start Station, End Station, User Type, Gender, Birth Year

    df = pd.read_csv(CITY_DATA[city])
    # Convert data to proper formats
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    if month != "all":
        df = df[df['Start Time'].dt.month == month]

    if day != "all":
        df = df[df['Start Time'].dt.weekday == day-1]

    try:
        print('Would you like to see more information?')
        if input('Type "yes" or "no": ').lower() == "yes":
            n=0
            print(df.iloc[n*5:(n+1)*5])
            while input('Continue? (Type "yes" or "no"): ') != "no":
                n=n+1
                print(df.iloc[n*5:(n+1)*5])
    except:
        print('An error occured!')
            
    print('-'*40)

    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print('- '*20)

    # display the most common month
    print('The most common month was {} {}'.format(df['Start Time'].dt.month.mode()[0], df['Start Time'].dt.strftime('%B').mode()[0]))
    print('- '*20)

    # display the most common day of week
    print('The most common start day was {} {}'.format(df['Start Time'].dt.weekday.mode()[0]+1, df['Start Time'].dt.strftime('%A').mode()[0]))
    print('- '*20)

    # display the most common start hour
    print('The most common start hour was {}'.format(df['Start Time'].dt.hour.mode()[0]))
    print('- '*20)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print('- '*20)

    # display most commonly used start station
    print("The most commonly used start station was {}".format(df['Start Station'].mode()[0]))
    print('- '*20)

    # display most commonly used end station
    print("The most commonly used end station was {}".format(df['End Station'].mode()[0]))
    print('- '*20)

    # display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip was {}".format(df.groupby(['Start Station','End Station']).size().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print('- '*20)

    # display total travel time
    travel_time=df['End Time']-df['Start Time']
    print('The total travel time was {}'.format(travel_time.sum()))
    print('- '*20)

    # display mean travel time
    print('The mean travel time was {}'.format(travel_time.mean()))
    print('- '*20)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print('- '*20)
    try:
        # Display counts of user types
        print("The counts of user types was \n{}".format(df['User Type'].value_counts()))
        print('- '*20)

        # Display counts of gender
        print("The counts of gender was \n{}".format(df.groupby('Gender').size()))
        print('- '*20)
        
        # Display earliest, most recent, and most common year of birth
        print("The earliest birth year was {}".format(int(df['Birth Year'].min())))
        print('- '*20)
        print("The most recent birth year was {}".format(int(df['Birth Year'].max())))
        print('- '*20)
        print("The most common birth year was {}".format(int(df['Birth Year'].mode()[0])))
        print('- '*20)
    except KeyError:
        print("No data available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    """Launches software."""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # display stats
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # restart?
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
