import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
days = ['all', 'sunday', 'monday', 'tuesday', 'wendsday', 'thursday', 'friday', 'saturday']
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    day = days[0]
    month = months[0]

    # get user input for city (chicago, new york city, washington).
    while True:
        print('Choose a city! Chicago, New York city or Washington. Which you prefer to analyze?\n')
        city = input()   
        if city.lower() not in cities:
            print('Sorry, invalid entry. Please try again!\n')
        else:
            while True:
                filter = input('Do you prefer to filter by Month, Day or show all? Type "all" to skip filtering date\n')
                if filter.lower() not in ['month', 'day', 'all']:
                    print('Sorry, invalid entry. Please try again!\n')
                else:
                    if filter.lower() == 'month':
                        print('You have choosen {}!\n'.format(filter))
                        # While loop used to avoid errors
                        while True:
                            # get user input for month (all, january, february, ... , june)
                            month = int(input('Which month are you looking for? Type 0 for all, 1 for January, 2 for February, 3 for March and so on\n'))
                            if month not in range(0, 7):
                                print('Sorry, invalid entry. Please try again!\n')
                            else:
                                month = months[int(month)]
                                print('You have choosen {}\n'.format(month))
                                break
                        break
                    elif filter.lower() == 'day':
                        print('You have choosen {}!\n'.format(filter))
                        # While loop used to avoid errors
                        while True:
                            # get user input for day of week (all, monday, tuesday, ... sunday)
                            day = int(input('Which day are you looking for? Type 0 for all, 1 for Sunday, 2 for Monday...\n'))
                            if day not in range(0, 8):
                                print('Sorry, invalid entry. Please try again!\n')
                            else:
                                day = Days[int(day)]
                                print("You have choosen {}\n".format(day))
                                break
                        break
                    elif filter.lower() == 'all':
                        print('You have choosen {}!\n'.format(filter))
                        break
            break
    print('It seems you want to see the data of {}, filter by {} and {}\n'.format(city, month, day))

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


    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month.lower() != 'all':
        # use the index of the months list to get the corresponding int
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = Months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month_index = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    common_month = months[common_month_index-1]
    print('The Most Common Month is:',common_month)


    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The Most Common Day Of Week is:',common_day_of_week)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('The Most Popular Hour is:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip:...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:',common_start_station)


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:',common_end_station)

    # display most frequent combination of start station and end station trip
    df['Trip']=df.apply(lambda x:'%s TO %s' % (x['Start Station'],x['End Station']),axis=1)
    print('The most frequent combination of start station & end station trip:--->',df['Trip'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration:...\n')
    start_time = time.time()

    # display total travel time
    print('Total Travel Time is:',df['Trip Duration'].sum())


    # display mean travel time
    print('Mean Travel Time is:',df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#calculates user_stats for 'chicago' & 'new york' cities
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of User types is:\n',df['User Type'].value_counts())

    # Display counts of gender with exception for Washington
    while 'Gender' not in df:
        print('No gender data for washington\n')
        break
    else:
        gender = df['Gender'].value_counts()
        print(gender, '\n')

    # Display earliest, most recent, and most common year of birth with exception for Washington
    while 'Birth Year' not in df:
        print('No birth year data for washington')
        break
    else:
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('Earliest year of birth:', earliest_year)
        print('Most recent year of birth:', recent_year)
        print('Most common year of birth:', common_year)
        
        
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