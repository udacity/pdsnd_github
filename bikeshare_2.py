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
        print(pd.__version__)
        city = input('\nPlease input the city you wish to filter by\nChicago, New York City, Washington\n')
        city = city.capitalize()
        if city not in ('Chicago', 'New york city', 'New York', 'Washington'):
            print('Your input is wrong, make sure the spelling is correct. Please try again')
            continue
        else:
            print('\nYou have chosen {} \n'.format(city))
            city = city.lower()
            break

    # get user input for month (all, january, february, ... , june)

    while True:
        month = input('\nPlease input the month you wish to filter by\nJanuary, February, March, April, May, June.\nYou can type all if you wish to use all the months\n')
        month = month.capitalize()
        if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
            print('\nYour input is wrong, make sure the spelling is correct. Please try again\n')
            continue
        else:
            print('\nYou have chosen {} \n'.format(month))
            month = month.lower()
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('\nPlease input the day you wish to filter by\nMonday, Tuesday, Wedesday, Thursday, Friday, Saturday, Sunday.\nYou can type all if you wish to use all the days\n')
        day = day.capitalize()
        if day not in ('Monday', 'Tuesday', 'Wedesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All'):
            print('Your input is wrong, make sure the spelling is correct. Please try again')
            continue
        else:
            print('\nYou have chosen {} \n'.format(day))
            day = day.lower()
            break

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
    city = city.lower()

      # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time']  = pd.to_datetime(df['Start Time'])
    df['End Time']    = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")
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
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nMost frequent time of travel calculated...\n')
    start_time = time.time()


    # find the most popular month

    common_month = df['month'].mode().values[0]

    print('Most Popular month:', common_month)
    # display the most common day of week

    common_day = df['day_of_week'].mode().values[0]
    print(f"Most common day: {common_day}")

    # find the most popular hour
    common_hour = df['hour'].mode().values[0]

    print(f"Most Popular Hour is: {common_hour}")

    # display the most common start hour
    common_start = df['Start Time'].mode().values[0]
    print(f"The Most Common Start Hour is: {common_start}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commmon End Station:', common_end_station)

    # display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station'] + " " + df['End Station']
    combo = df['combo'].mode()[0]
    print('Most Commmon combination of Start and End Stations is:', combo)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Duration'] = df['End Time'] - df['Start Time']
    # display total travel time
    print("The total travel time is : {}".format(str(df['Duration'].sum())))
    # display mean travel time
    print("The average travel time is : {}".format(str(df['Duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print(f"These are the counts of user types:{user_type_count}")
    # Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print(f"Here are the gender counts: {gender_counts}")
    except:
        print("Sorry, there are no gender details here.")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = int(df['Birth Year'].min())
        recent_birth = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest birth year here is: {earliest_birth}\n And the most recent birth year is: {recent_birth}\n And the most common birth year is: {most_common}")
    except:
        print("Sorry, the birth year information cannot be accessed.")


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
