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
    while True: 
           
        city = str(input("\nType a city name from Chicago, New York City, Washington: ").strip().lower())

        if city not in ("chicago", "new york city", "washington"):
            print("\nUnexpected input, please try again")
            continue
        else:
            print("\nYou will get data for: '{}' ".format(city.title()))
            validity_check()
            break

    while True:
    # get user input for month (all, january, february, ... , june)
        month = str(input("\nType name of monnth like January or all to get every month): ").strip().lower())

        if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print("\nUnexpected input, please type name of the month or all to get every month)")
            continue
        else:
            print("\nYou will get data for: '{}' ".format(month.title()))
            validity_check()
            break

    while True:
    # get user input for day of week (all, monday, tuesday, ... sunday)
        day = str(input("\nType day of week like Monday or all to get every day: ").strip().lower())

        if day not in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday" , "sunday", "all"):
            print("Unexpected input, please type name of the day or all to get every day")
            continue
        else:
            print("\nYou will get data for: '{}' ".format(day.title()))
            validity_check()
            break

    print("\nYou have filtered '{}' as city, '{}' as month, and '{}' as day. \nCollecting and filtering your data....".format(city.title(), month.title(), day.title()))
    print()

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
    df = pd.read_csv(CITY_DATA[city])

    # Start Time column is converted to datetime type
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Month, Hour and Day_of_Week is gathered from Start Time as new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_Week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour

    # Month input is defined from month list
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    # Day input is defined from month list
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        df = df[df['Day_of_Week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # look_up dictionary 
    look_up = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
        '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}

    # display the most common month
    popular_month = df['Month'].mode()[0]
    month_in_string = look_up[str(popular_month)]
    print("Most common month: ", month_in_string)

    # display the most common day of week
    popular_day = df['Day_of_Week'].mode()[0]
    print("Most common day of the week: {}".format(popular_day))

    # display the most common start hour
    popular_hour = df['Hour'].mode()[0]
    print('Most common start hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("Most common start station: '{}'".format(start_station))

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("Most common used end station: '{}'".format(end_station))
    
    # display most frequent combination of start station and end station trip
    startend_station = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).reset_index(name="counts")
    
    frequent_start_pair = startend_station['Start Station'][0]
    frequent_end_pair = startend_station['End Station'][0]

    print("Start station for most frequent combination: '{}' and end station for most frequent combination: '{}'".format(frequent_start_pair, frequent_end_pair))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    duration = total_travel_time.astype('float64', copy=False)
    time_in_duration = timedelta(seconds=duration)
    print("The total travel time: '{}' secs, it's '{}' as duration. ".format(total_travel_time, time_in_duration))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time : '{}' secs ".format(mean_travel_time))

    print("\nThis took %s secs." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    userType_cnt = df["User Type"].value_counts()
    print(userType_cnt)

    # Display counts of gender
    gender_cnt = df["Gender"].value_counts()
    print(gender_cnt)

    # Display earliest, most recent, and most common year of birth
    earliest_birth = df['Birth Year'].min()
    most_recent_birth = df['Birth Year'].max()
    most_common_birth = df['Birth Year'].mode()[0]
    print("\nEarliest birth: '{}'. \nMost recent birth: '{}'. \nMost common birth: '{}'.".format(earliest, most_recent, most_common))

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
	
#refactor: performance utilization
#refactor: User warnings updated
