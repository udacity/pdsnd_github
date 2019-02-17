import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities= ['chicago','new york' , 'washington']

months = ['january', 'february', 'march', 'april', 'may', 'june']

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

time_list = ['month', 'day','none']


def valid_data(message):
    """
    An utility function to obtain user specific input value
    Args:
        (str) message - an information message for a particular request
    Returns:
        (str) user_entry  - requested data from user
    """
    valid_list = ['yes','no']
    while True:
        user_entry = input(message).lower()
        if user_entry in valid_list:
            break
        else:
            print("invalid entry")

    return user_entry


def display_data(df):
    """
    Displays 5 lines of raw data upon request from user.
    Displays the data if the answer is 'yes', and continue these prompts and displays until the user says 'no'.

    Args:
        data frame
    Returns:
        none
    '''"""

    row_length = df.shape[0]
    start = 0
    for i in range(start,row_length,5):
        entry = valid_data("Would you like to view individual trip data? Type 'yes' or 'no' \n").lower()
        row_data = df.iloc[i: i + 5]
        if entry.lower() != 'yes':
            break

        print(row_data)

    print('-'*40)


#validate time filter
def get_time_filter(message, time_list):
    """
    An utility function to obtain user specific input value
    Args:
        (str) message - an information message for a particular request
    Returns:
        (str) user_data - requested data from user
    """

    while True:
        user_time_filter = input(message).lower()
        if user_time_filter in time_list:
            break
        else:
            print("invalid entry")

    return user_time_filter


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    """
    Would you like to filter the data by month, day, or not at all?
    (If they chose month) Which month - January, February, March, April, May, or June?
    (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?"""
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington?\n').lower()
        #city = city.lower()
        if city in cities:
            break
        else:
            print("Sorry that was an invalid entry.Lets try again\n")


    # Ask the user for filter choice
    time_filter = get_time_filter("Would you like to filter the data by month, day, or not at all? Type 'none' for no time filter. \n",time_list )

    while True:
        # TO DO: get user input for month (january, february, ... , june)
        if time_filter == "month":
            month = input("Which month - January, February, March, April, May, or June? \n").lower()
            if month in months:
                day = "none"
                break
            else:
                print("Sorry that was an invalid entry.Lets try again\n")

        # TO DO: get user input for day of week (monday, tuesday, ... sunday)
        if time_filter == "day":
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \n").lower()
            if day in days:
                month = "none"
                break
            else:
                print("Sorry that was an invalid entry.Lets try again\n")
        # TO DO: if no filteration is selected
        if time_filter == "none":
            month = "none"
            day = "none"
            break

    print('-'*40)
    return city,month,day


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
    #file name extraction from the dataframes
    filename = CITY_DATA[city]

    # load data file into a dataframe
    df = pd.read_csv(filename)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'none':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'none':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months_list = ['january', 'february', 'march', 'april', 'may', 'june']
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].value_counts().idxmax()
    print('What is the most popular month for travelling ?')
    print(months_list[popular_month-1].title())
    print()

    # TO DO: display the most common day of week
    df['dow'] = df['Start Time'].dt.weekday_name
    popular_dow = df['dow'].mode()[0]
    print('What is the most popular day of week for travelling ?')
    print(popular_dow)
    print()

    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('What is the Most Common Hour for travelling ?')
    print(popular_hour)
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))

    print()
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('What is the most commonly used start station ?')
    most_common_start_station = df['Start Station'].mode()[0]
    print('Start Station:',most_common_start_station)
    print('Counts:', df['Start Station'].value_counts()[most_common_start_station])
    print()

    # TO DO: display most commonly used end station
    print('What is the most commonly used end station ?')
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print('End Station:',most_common_end_station)
    print('Counts:', df['End Station'].value_counts()[most_common_end_station])
    print()

    # TO DO: display most frequent combination of start station and end station trip
    print('What is the most frequent combination of start station and end station trip ?')
    df['Start End'] = df['Start Station'].map(str) + '  to ' + df['End Station']
    popular_start_end = df['Start End'].value_counts().idxmax()
    print('Start TO End Station:',popular_start_end )
    print('Counts:', df['Start End'].value_counts()[popular_start_end])
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('What is the total travel time?')
    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time)
    print()

    # TO DO: display mean travel time
    print('What is the average travel time?')
    avg_travel_time = df['Trip Duration'].mean()
    print(avg_travel_time)
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('What is the user type breakdown ?')
    user_types = df.groupby(['User Type']).size()
    print(user_types)
    print()

    # TO DO: Display counts of gender (avialable for Ny and chicago)
    print('What is the gender breakdown ?')
    try:
        count_gender = df.groupby(['Gender']).size()
        print(count_gender)
    except KeyError:
        print("No gender data to share  ")
    print()

    # TO DO: Display earliest, most recent, and most common year of birth
    print('What is the oldest , youngest and most common year of birth respectively ?')
    try:
        oldest_year = df['Birth Year'].min()
        youngest_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('Oldest year of birth  :' ,oldest_year)
        print('Youngest year of birth:' ,youngest_year)
        print('Common year of birth  :' ,common_year)
    except KeyError:
        print("No birth year to share  ")
    print()

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
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
