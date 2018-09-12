import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    """
    place cities, months and days in a list (lowercase)
    so they can be referenced in the loop below
    """
    cities = ['chicago', 'new york city', 'washington']
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    days = ['all','sunday','monday', 'tuesday','wednesday','thursday','friday', 'saturday']
    """
    Use a while loop to manage user input and convert it to a string
    """
    while True:
        try:
            """
            Steps: receive user input, convert input as a string,
            once input is received - strip, lowercase the input
            """
            city = input(str('\nEnter Chicago, New York City or Washington: \n'))
            city = city.strip().lower()
            """
            Managing user input until input needs are satisfied
            Using the break, continue and pass statements for user input
            """
            if city in cities:
                break
        except (NameError, ValueError, IndexError, KeyError):
                """
                Place the input response on a new line
                Except keyboard interrupts
                """
                print('\nHi! Hey, please enter Chicago, New York City or Washington. \n')

        except KeyboardInterrupt:
            print('\nProgram interrupted by user\n')


    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    """
    Use a while loop to manage the user input stream and
    convert the user input into a string
    """
    while True:
        """
        Lowercase each element of the list after first converting the user input to a string
        Consume user input, strip, lowercase, then check to see if the element is in the list
        """
        try:
            month = input(str('\nPlease enter a month between January and June or all:  \n'))
            month = month.strip().lower()
            if month in months:
                break
        except ValueError:
            print ('\nHey, there! Your requested month is not between January and June. Please try again!\n')
        except KeyboardInterrupt:
            print('\nProgram interrupted by user\n')

    days = ['all','sunday','monday', 'tuesday','wednesday','thursday','friday', 'saturday']

    while True:
        try:
            day = input(str('\nPlease enter a day between Sunday and Saturday or all. \n'))
            day = day.strip().lower()
            if day in days:
                break
        except ValueError:
            print ('\nHi! The day you entered is not in the list. You can get this right. Try again!\n')
        except KeyboardInterrupt:
            print('\nProgram interrupted by user\n')

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

    """
    Steps
    Convert the Start Time column to datetime
    Extract month and day of week from Start Time to create new columns
    Filter by month if applicable
    Use the index of the months list to get the corresponding int
    """

    # convert the Start Time column to datetime

    """
    convert the Start Time column to datetime
    """
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    """
    extract month and day of week from Start Time to create new columns
    """
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable

    """
    filter by month if applicable
    """
    if month != 'all':
    # use the index of the months list to get the corresponding int
    """
    use the index of the months list to get the corresponding int
    filter by month to create the new dataframe
    filter by day of week if applicable
    filter by day of week to create the new dataframe
    """
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]
        if day != 'all':
            df = df[df['day_of_week'] == day.title()]

    print('\nRun some analysis of user statistics...\n')
    start_time = time.time()

    return df

def time_stats(df):
    try:

        """Displays statistics on the most frequent times of travel."""

        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # TO DO: display the most common month
        print('\nMost common month...\n')
        print(df['Start Time'].dt.month.mode()[0])

        # TO DO: display the most common day of week
        print('\nMost common day of week...\n')
        print(df['day_of_week'].mode()[0])

        # TO DO: display the most common start hour
        print('\nMost common start hour...\n')
        df['hour'] = df['Start Time'].dt.hour
        print(df['hour'].mode()[0])
    except IndexError:
        print('\nThe time statistic is out of range\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    try:
        """Displays statistics on the most popular stations and trip."""

        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # TO DO: display most commonly used start station
        print('\nThe Most Popular Start Station...\n')
        # Get the first element if there are multiple modes!
        print(df['Start Station'].mode()[0])

        # TO DO: display most commonly used end station
        print('\nCalculating The Most Popular End Station...\n')
        print(df['End Station'].mode()[0])

        # TO DO: display most frequent combination of start station and end station trip
        print('\nMost frequent combination of start station and end station trip..\n')
        ## Source: Intro to data analysis lectures on pandas for the groupby function!
        start_station_end_station = df.groupby(['Start Station','End Station']).idxmax().index[-1]
        print(start_station_end_station)
        print('*'*80)
        print("\nThis took %s seconds." % (time.time() - start_time))
    except IndexError:
        print('\nOut of range\n')
    print('-'*40)

def trip_duration_stats(df):
    try:
        """Displays statistics on the total and average trip duration."""

        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # TO DO: display total travel time
        print('\nDisplaying total travel time statistics in minutes...\n')
        print((df['Trip Duration'].sum())*.016667)

        # TO DO: display mean travel time
        print('\nCalculating Trip Duration Average in minutes..\n')
        print((df['Trip Duration'].mean())*.016667)

        #Display the trip duration that occurs the most
        print('\nCalculating Trip Duration Mode in minutes...\n')
        print((df['Trip Duration'].mode()[0])*.016667)
        print("\nThis took %s seconds." % (time.time() - start_time))
    except (IndexError, KeyError):
        print('\nOut of range\n')
    print('-'*40)

def user_stats(df):
    try:
        """Displays statistics on bikeshare users."""

        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        print('\nDisplay counts of user types...\n')
        print(df['User Type'].value_counts()[0:])
        # TO DO: Display counts of gender
        print('\nDisplay counts of gender...\n')
        print(df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nEarliest, most recent, and most common year of birth...\n')
        print(df['Birth Year'].min())
        print(df['Birth Year'].max())
        # Get the first element if there are multiple modes!
        print(df['Birth Year'].mode()[0])
    except (KeyError, IndexError):
        print('\nUser Statistic is unavailable for this city\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    Indexrow = 0
    ''' Displays 5 lines of data based on user input.
        If user wants more data,
        five more lines of data are displayed
    '''
    display_info = input(str('\nDo you want to see raw data? Please type Yes or No!\n'))
    display_info = display_info.strip().lower()

    while True:
        if display_info == 'yes':
            new_df = df[Indexrow:Indexrow+5]
            print('\nThe raw data is presented below!\n')
            print(new_df)
            print('-'*80)
            Indexrow += 5
        display_info = input(str('\nDo you want to see more data? Please type Yes or No!\n'))
        if display_info != 'yes':
            break
    print('-'*80)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
