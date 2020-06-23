import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = [ "new york city", "chicago", "washington" ]
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days   = [ "monday", "tuesday", "wednesday", "thursday",
                        "friday", "saturday", "sunday", 'all']




def user_choice(options, user_input):
    while True:
        result = input(user_input).strip().lower()
        if result in options:
            return result
        else:
            print("Please follow the input guidance!")

def raw_data(df):
    x = 0
    user_input = input('\nWould you like to see the raw data? Enter yes or no. ')
    while True:
        if user_input.lower() == 'yes':
            df_5 = df.iloc[x: x+5]
            print(df_5)
            x += 5
            user_input = input('\nDo you want to continue to visualize data? Enter yes or no. ')
        else:
            print('\nThanks and Good Bye!')
            break
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

    city = user_choice(cities, "Please select the City you want to display data for 'Chicago', 'New York City', 'Washington' in lowercase ")

    # TO DO: get user input for month (all, january, february, ... , june)

    month = user_choice(months, "Please enter the month you want to display in lowercase 'Month date is available from January to June. ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = user_choice(days, "Please enter the day you want to display the data for in lowercase 'Monday to Sunday' ")


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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day'] = df['Start Time'].dt.weekday_name

    df["hour"] = df['Start Time'].dt.hour

    df["Start_End"] = df['Start Station'] + ' - to - ' + df['End Station']

    if month != 'all':

        month_index = months.index(month) + 1

        df = df[df["month"] == month_index]

    if day != 'all':

        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_index = df["month"].mode()[0] -1
    common_month = months[month_index].title()
    print('The most common month is : ', common_month)
    # TO DO: display the most common day of week

    common_day =  df['day'].mode()[0]
    print('The most common day to travel is: ', common_day)

    # TO DO: display the most common start hour

    common_hour = df["hour"].mode()[0]
    print('The busiest hour of travel is: ', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_station = df['Start Station'].mode()[0]
    print('The most common start station is: ', common_station )


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = df['Start_End'].mode()[0]
    print('The most common start to end station is: ', common_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel = df['Trip Duration'].sum()
    print('Total travel time is: ', tot_travel)

    # TO DO: display mean travel time
    avg_travel = df['Trip Duration'].mean()
    print('Average travel time is: ', avg_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users = df['User Type'].count()
    print('Based on your search there are currently {} users'.format(users))

    # TO DO: Display counts of gender
    if "Gender" in df:
        print("Males: ", df.query("Gender == 'Male'").Gender.count())
        print("Females: ", df.query("Gender == 'Female'").Gender.count())

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        print("\nEarliest year of birth: ", int(df["Birth Year"].min()))
        print("Most recent year of birth: ", int(df["Birth Year"].max()))
        print("Most common year of birth: ", int(df["Birth Year"].value_counts().idxmax()))

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
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
