import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def correct_input(str_inp, runtype):
    """to check the correctness of the input
    """
    while True:
        line_input = input(str_inp)
        try:
            if line_input in ['chicago','new york city','washington'] and runtype == 1:
                break
            elif line_input  in ['january', 'february', 'march', 'april', 'may', 'june','all'] and runtype == 2:
                break
            elif line_input in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all'] and runtype == 3:
                break
            else:
                if runtype == 1:
                    print("please enter: chicago, new york city or washington")
                if runtype == 2:
                    print("please enter: january-june or all")
                if runtype == 3:
                    print("please enter: sunday-saturday or all")
        except ValueError:
            print("wrong input!")
    return line_input


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
    city = correct_input("Enter a city: ", 1)
    

    # TO DO: get user input for month (all, january, february, ... , june)
    month = correct_input("Enter a month between January and June: ", 2)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = correct_input("Enter a day betwwen monday and saturday: ", 3)

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

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]

    print('Most Popular Month:', popular_month)

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]

    print('Most Day Of Week:', most_common_day)

    # display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('Most Start Station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most End Station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    frequent_combination=df.groupby(['Start Station','End Station'])
    popular_frequent_combo_station = frequent_combination.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', popular_frequent_combo_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total Travel Time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:',most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:',most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:',earliest_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_info(df):
    """
    displays five rows of bikeshare data
    """
    response_locket = ['yes', 'no']
    read_data = ''
    counter = 0
    while read_data not in response_locket:
        print('\nDo you wish to view the raw bikeshare data?')
        print('\nright responses: \nyes or no')
        read_data = input().lower()
        if read_data == 'yes':
           print(df.head())
        elif read_data not in response_locket:
            print('wrong input!')
            print('nreloading...\n')
    while read_data == 'yes':
        print('wish to view more data?')
        counter +=5
        read_data = input().lower()
        if read_data == 'yes':
              print(df[counter:counter+5])
        elif read_data != 'yes':
              break
              
print('_'*40)
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        data_info(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()