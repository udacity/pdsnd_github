import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

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
        city = input("\nWhich city would you like to choose from? New York, Chicago or Washington?\n").title()
        if city not in ('New York', 'Chicago', 'Washington'):
            print("Sorry, wrong input. Try again.")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            "\nWhich month would you like to choose from? January, February, March, April, May, June or type 'all' for all months?\n").title()
        if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
            print("Sorry, wrong input. Try again.")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
            "\nwhich day are you looking into? kindly enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' for all days.\n").title()
        if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
            print("Sorry, wrong input. Try again.")
            continue
        else:
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
    print("\nplease wait...")

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df["day_of_month"] = df["Start Time"].dt.day

    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]


    if day != 'All':
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        day = days.index(day) + 1
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(df['month'])
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common day:', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mostcommon_Start = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', mostcommon_Start)

    # display most commonly used end station
    mostcommon_End = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', mostcommon_End)

    # display most frequent combination of start station and end station trip
    mostcommon_Combination = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', mostcommon_Start, " & ",
          mostcommon_End)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Time / 86400, " Days")

    # display mean travel time
    Mean_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Time / 60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print('\nGender Types:\n', gender_counts)
    except KeyError:
        print("\nGender Types:\nNo data.")


    # Display earliest, most recent, and most common year of birth
    try:
        Earliest_birth = df['Birth Year'].min()
        print('\nEarliest Year:', Earliest_birth)
    except KeyError:
        print("\nEarliest Year:\nNo data.")

    try:
        Most_Recent_birth = df['Birth Year'].max()
        print('\nMost Recent Year:', Most_Recent_birth)
    except KeyError:
        print("\nMost Recent Year:\nNo data.")

    try:
        Most_Common_birth = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', Most_Common_birth)
    except KeyError:
        print("\nMost Common Year:\nNo data.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    show_data = input('\nWould you like to see 5 rows of raw data? yes or no:\n').title()
    if show_data == 'Yes':
        i = 0
        while (i < df['Start Time'].count() and show_data != 'no'):
            print(df.iloc[i:i+5])
            i += 5
            more_data = input('\nWould you like to see 5 more rows of data? yes or no:\n').title()
            if more_data == 'Yes':
                continue
            elif more_data == 'No':
                    break
            else:
                print('wrong input')
                return
    elif show_data == 'No':
                return
    else:
                print('wrong input')
                return


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
