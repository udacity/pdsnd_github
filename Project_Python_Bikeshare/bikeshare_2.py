import time
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    city = input("Hey! Let's explore us some data of Chicago, Washington or New York City. Please input the name of the city: ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Maybe you made a typo? Please input a valid name to choose your city:\n').lower()

    # get user input for month (all, january, february, ... , june)


    month = input("Which month you are looking for? Please input name of the month. If you want to select all input 'all': ").lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Sorry man! Looks like you made a typo or we do not have data for this month. Please, try again").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)


    day = input("If you are looking for a specific day please enter the name of the day. If not just enter 'all' to select all days: ").lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            day = input("Sorry! This was not a valid input. Please retry.").lower()


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
    #Load data city
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))
    print("\nLoading Data ...")

    #convert Start Time column to Datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time. Create Columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #filter by month if applicalble
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june' ]
        month = months.index(month) + 1

        #filter by month. Create new DF
        df = df.loc[df['month'] == month]

        #filter by day of week if applicable
    if day != 'all':
        #filter by day of week to create new DF
        df = df.loc[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # Set up day, month. Hour from df['Start Time']
    most_common_month = df['month'].mode()[0]
    most_common_day = df['day_of_week'].mode()[0]
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    most_common_start_hour = df['hour'].mode()[0]

    # display the most common month
    print('The most common month is {}'.format(most_common_month))

    # display the most common day of week
    print('The most common day is {}'.format(most_common_day))

    # display the most common start hour
    print('The most common start hour is {}'.format(most_common_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Use value_counts again to calculate most used start and end station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    most_commonly_used_end_station = df['End Station'].mode()[0]

    # display most commonly used start station
    print('The most commonly used start station is {}'.format(most_commonly_used_start_station))

    # display most commonly used end station
    print('The most commonly used end station is {}'.format(most_commonly_used_end_station))

    # display most frequent combination of start station and end station trip
    combined_stations = df['Start Station'] + ' - ' + df['End Station']
    print('The most common frequently used combination of start station & end station is {}'.format(combined_stations.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    # using floor division to get floating point values back to display  D, h, m & s
    travel_time_total = sum(df['Trip Duration'])
    travel_time_total_days = travel_time_total//86400
    travel_time_total_hours = travel_time_total//3600%60
    travel_time_total_minutes = travel_time_total//60%60
    travel_time_total_secons = travel_time_total%60

    print('The total travel time of passengers was {} day, {} hours, {} minutes & {} seconds'.format(travel_time_total_days, travel_time_total_hours, travel_time_total_minutes, travel_time_total_secons))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time_minutes = mean_travel_time // 60
    print('The mean travel time of passengers was {} minutes'.format(mean_travel_time_minutes))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types are: ', user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print('Gender Count:')
        print(gender_count)



    # Display earliest, most recent, and most common year of birth

    #earliest year
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print("The earliest year of birth is: ", earliest_year)
    #most recent year
    if 'Birth Year' in df.columns:
        most_recent_year = df['Birth Year'].max()
        print("The most recent year of birth is: ", most_recent_year)
    #most common year of birth
    if 'Birth Year' in df.columns:
        most_common_year = df['Birth Year'].mode()[0]
        print("The most common year of birth is: ", most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    """
    Raw data is displayed upon request by the user in this manner:
    Script should prompt the user if they want to see 5 lines of raw data, display that data if the answer is 'yes',
    and continue these prompts and displays until the user says 'no'.
    """
    #ask for user input handle raw input with lower()
    display = input('You want to explore some lines of real data? Enter Yes / No').lower()
    iloc_number = 0


    # while loop to check user input and ask for more data. Return question again if not yes or no
    while True:
        if display == 'yes':
            #use as noted integer-location based indexing for selection by position
            if df.iloc[iloc_number:iloc_number + 5].empty:
                print('It seems like we have come to the end of the data. Lets start over again\n')
                main()
            print(df.iloc[iloc_number:iloc_number + 5])
            iloc_number += 5
            display = input('Do you want to explore 5 lines more of real data? Enter Yes / No').lower()
        elif display == 'no':
            break
        else:
            display = input('Maybe you made a typo? Print yes to show 5 rows of data. Enter No to to do not').lower()

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
