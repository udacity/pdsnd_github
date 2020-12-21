import time
import pandas as pd
import numpy as np

#Create dictonaries for accepted cities, months, and days
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = {'all': 0, 'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}

DAY_DATA = {'all': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}

#Gather user inputs for the data to analyze
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Args:
        None
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #Get user input for city (chicago, new york city, washington).
    city = ''
    while city not in CITY_DATA.keys():
        city = input("Please select your city. Accepted inputs are Chicago, New York City, or Washington. ").lower()
        if city not in CITY_DATA.keys():
            print("\nNot a valid input. Please select Chicago, New York City, or Washington.\n")

    #Get user input for month (all, january, february, ... , june)
    month = ''
    while month not in MONTH_DATA.keys():
        month = input("Please select the month you would like to analyze from January-June. You may also select all for all data. ").lower()
        if month not in MONTH_DATA.keys():
            print("\nNot a valid input. Please select a valid month or all for all data.\n")
    #Get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in DAY_DATA.keys():
        day = input("Please select the day of the week you would like to analyze from Sunday-Monday. You may also select all for all data. ").lower()
        if day not in DAY_DATA.keys():
            print("\nNot a valid input. Please select a valid day of the week or all for all data.\n")

    #Return user input data
    print('-'*40)
    return city, month, day

#Load data from city files
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
    df['day_of_week'] = df['Start Time'].dt.day_name()

    #Filter month if needed
    if month != 'all':
        MONTH_LIST = ['january', 'february', 'march', 'april', 'may', 'june']
        month = MONTH_LIST.index(month) + 1
        df = df[df['month'] == month]

    #Filter day if needed
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    #Return relevant data as a dataframe
    return df

#Calculate time statistics for the chosen data
def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - dataframe with filtered bikeshare data
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month from this dataset is: " + str(common_month))

    #Display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of the week from this dataset is: " + str(common_day))

    #Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The most common start hour from this dataset is: " + str(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Calculate station statistics for the chosen data
def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df - dataframe with filtered bikeshare data
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("The most commonly used start station from this dataset is: " + str(common_start))

    #Display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("The most commonly used end station from this dataset is: " + str(common_end))

    #Display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " to " + df['End Station']
    station_combo = df['combination'].mode()[0]
    print("The most commonly used combination of sations from this dataset is: " + str(station_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Calculate trip duration statistics for the chosen data
def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - dataframe with filtered bikeshare data
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time from this dataset is: " + str(total_travel_time))

    #Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time from this dataset is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Calculate user statistics for the chosen data
def user_stats(df):
    """
    Displays statistics on bikeshare users.
    Args:
        (DataFrame) df - dataframe with filtered bikeshare data
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    user_counts = df['User Type'].value_counts()
    print("The counts of user types from this dataset are:\n" + str(user_counts))

    #Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print("The counts of gender from this dataset are:\n" + str(gender_counts))
    except:
        print("There is no gender data for this city.")

    #Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print("The earliest birth year from this dataset is: " + str(earliest_year))
        recent_year = df['Birth Year'].max()
        print("The most recent birth year from this dataset is: " + str(recent_year))
        common_year = df['Birth Year'].mode()[0]
        print("The most common birth year from this dataset is: " + str(common_year))
    except:
        print("There is no birth year data for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Loop to display raw data 5 rows at a time at user request
def display_data(df):
    """
    Displays raw data at users request, 5 lines at a time
    Args:
        (DataFrame) df - dataframe with filtered bikeshare data
    """
    raw_data = 0
    while True:
        data_request = input("Would you like to view the raw data? Please choose yes or no.").lower()
        if data_request == 'yes':
            raw_data = raw_data + 5
            print(df.iloc[raw_data : raw_data + 5])
            more_raw_data = input("Would you like to view 5 more lines of raw data? Please choose yes or no. ").lower()
            if more_raw_data == 'no':
                break
        elif data_request != 'yes':
            return


#Main function that calls all previous functions
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('Would you like to restart? Enter yes or no. ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
