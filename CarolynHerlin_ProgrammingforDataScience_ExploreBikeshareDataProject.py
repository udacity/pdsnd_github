import time
import datetime
import statistics
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

repeat = False

# prompt user to make selections that will determine which filters are applied
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
    cities = ['chicago', 'new york city', 'washington']
    city_test=False

    # Tests to make sure the user's section is valid
    while city_test==False:
        city = input("Enter the city you want to see data for. Valid options are Chicago, New York City, and Washington. ")
        if city.lower() in cities:
            city_test=True
            break
        else:
            print()
            print("That was not a valid choice. Please try again. ")
            city_test=False

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    month_test=False


    while month_test==False:
        month = input("Data is available for January through June. Enter the name of the month you want data for. Enter all to get data for all months. ")
        if month.lower() in months:
            month_test=True
            break
        else:
            print()
            print("That was not a valid choice. Please try again. ")
            month_test=False


    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    day_test=False

    while day_test==False:
        day = input("Enter the day of the week you want data for. Enter all to get data for all days. ")
        if day.lower() in days:
            day_test=True
            break
        else:
            print()
            print("That was not a valid choice. Please try again. ")
            month_test=False

    return city, month, day

def select_data():
     # get user input for type of data they want to see
    data = 0

    while data < 1 or data > 6:
        data = int(input("\nSelect the type of data you want to see. Enter 1 for data about travel times. Enter 2 for data about station usage. Enter 3 for data about trip duration. Enter 4 for data about riders. Enter 5 to see raw data. Enter 6 to select all.\n"))
        if data >= 1 and data <= 6:
            break
        else:
            print()
            print("That was not a valid choice. Please try again. ")

    print('-'*40)
    return data

def load_data(city, month, day, data):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    csv_file_name = CITY_DATA[city.lower()]
    df = pd.read_csv(csv_file_name)

    # need to handle nulls
    df.dropna(axis = 0, inplace = True)
    #print(df.isnull().sum())

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month.lower() != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1 
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month_int = df['month'].mode()[0]-1
    common_month = months[common_month_int].title()
    if month.lower()!='all':
        print('The most popular month for travel in the data set you selected is {} because all the data you selected is for {}.'.format(common_month, common_month))
    else:
        print('The most popular month for travel is {}.'.format(common_month))
    print()

    # display the most common day of week
    common_day_list = df['day_of_week'].value_counts()[:1].index.tolist()
    common_day = common_day_list[0]
    if day.lower()!=all:
        print('The most popular day for travel in the data set you selected is {} because all the data you selected is for {}.'.format(common_day.title(), common_day.title()))
    else:
        print('The most popular day for travel is {}.'.format(common_day.title()))
    print()

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
   
    if popular_hour==12:
        answer = 'noon'
    elif popular_hour > 12:
        answer = '{} pm'.format(popular_hour-12)
    else:
        answer = '{} am'.format(popular_hour)
    print('The most popular hour for travel is {}.'.format(answer))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station_list = df['Start Station'].value_counts()[:1].index.tolist()
    common_start_station = common_start_station_list[0]
    print('The most popular start station is {}.'.format(common_start_station))

    # display most commonly used end station
    common_end_station_list = df['End Station'].value_counts()[:1].index.tolist()
    common_end_station = common_end_station_list[0]
    print('The most popular end station is {}.'.format(common_end_station))

    # display most frequent combination of start station and end station trip
    df['Station Pair'] = df['Start Station'] + " to " + df['End Station']
    common_station_pair_list = df['Station Pair'].value_counts()[:1].index.tolist()
    common_station_pair = common_station_pair_list[0]
    print('The most popular route (start station to end station) is {}.'.format(common_station_pair))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Travel Time'] = df['End Time'] - df['Start Time']
    #print(df.head())
    total_travel_time = df['Travel Time'].sum()
    print('The total travel time for all rides is ')
    print(total_travel_time)
    print()

    # display mean travel time
    mean_travel_time = df['Travel Time'].mean()
    print('The average time for a single trip is ')
    print(mean_travel_time)
    print()

    # display the longest trip
    long_travel = df['Travel Time'].max()
    print('The longest trip took ')
    print(long_travel)
    print()

    #display the shortest trip
    short_travel = df['Travel Time'].min()
    print('The shortest trip took ')
    print(short_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('The following shows how many users of each type there are in the data sample you selected. ')
    print()
    users_dict = dict(zip(df['User Type'].value_counts().index.tolist(), df['User Type'].value_counts().tolist()))
    for item, value in users_dict.items():
        print("{}   {}".format(item,value))
    print()

    # Display counts of gender
    if city.lower() != 'washington':
        print('The following shows how many users of each gender there are in the date sample you selected. ')
        print()
        gender_dict = dict(zip(df['Gender'].value_counts().index.tolist(), df['Gender'].value_counts().tolist()))
        for item, value in gender_dict.items():
            print("{}   {}".format(item,value))
        print()


    # Display earliest, most recent, and most common year of birth
    if city.lower() != 'washington':
        # find the oldest rider
        earliest_year_raw = str(df['Birth Year'].min())
        earliest_year_shorter = earliest_year_raw[:4]
        earliest_year = int(earliest_year_shorter)
        oldest_age = 2017 - earliest_year
        if oldest_age > 90:
            print('The oldest rider in the data set you selected was {} years old at the time of the ride. That\'s hard to believe!'.format(oldest_age))
            print()
        else:
            print('The oldest rider in the data set you selected was {} years old at the time of the ride.'.format(oldest_age))
            print()

        #find the youngest rider
        latest_year_raw = str(df['Birth Year'].max())
        latest_year_shorter = latest_year_raw[:4]
        latest_year = int(latest_year_shorter)
        youngest_age = 2017 - latest_year
        if youngest_age < 5:
            print('The youngest rider in the data set you selected was {} years old at the time of the ride. They were probably a rider on a parent\'s bike.'.format(youngest_age))
            print()
        else:
            print('The youngest rider in the data set you selected was {} years old at the time of the ride.'.format(youngest_age))
            print()

        # find the most common year of birth
        df['Birth Year'] = df['Birth Year'].astype(str)
        common_year_list = df['Birth Year'].value_counts()[:1].index.tolist()
        common_year_str = common_year_list[0]
        common_year_short_str = common_year_str[:4]
        common_year = int(common_year_short_str)
        common_age = 2017 - common_year
        print('Most of the riders in the data set you selected were {} years old at the time of the ride.'.format(common_age))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Shows raw data five lines at a time according to user request."""
     
    print('\nRetrieving raw data...\n')
    start_time = time.time()

    # ask the user if they want to see raw data
    request = input('\nWould you like to see 5 rows of raw data? Enter yes or no.\n')
    
    start = 0
    end = 5
    while request.lower() == 'yes':
        print(df.iloc[start:end])
        request = input('\nWould you like to see 5 more rows? Enter yes or no.\n')
        if request == 'yes':
            start += 5
            end += 5
        else:
            break


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        global repeat
        if repeat == False:
            city, month, day = get_filters()
            data = select_data()
            df = load_data(city, month, day, data)

        if data == 1 or data == 6:
            time_stats(df, month, day)

        if data == 2 or data == 6:
            station_stats(df)

        if data == 3 or data == 6:
            trip_duration_stats(df)

        if data == 4 or data == 6:
            user_stats(df, city)

        if data == 5 or data == 6:
            display_data(df)

        choose_again = input('\nWould you like to see another type of data? Enter yes or no.\n')
        if choose_again.lower() == 'yes':
            repeat = True
            data = select_data()
        else:
            repeat = False
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()