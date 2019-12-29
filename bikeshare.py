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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
while True:
      city = input("\nWhich city would you like to filter by? New York City, Chicago or Washington?\n")
      if city not in ('New York City', 'Chicago', 'Washington'):
        print("please enter one of these cities.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
while True:
      month = input("\nWhich month would you like to filter by? January, February, March, April, May, June or 'all' if you need to see all months?\n")
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print("please enter one of the above month options.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
while True:
      day = input("\nPlease enter the day you look for as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you wish to see data of all days.\n")
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        print("Please enter one of the day options shown above.")
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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The Most Common Month is:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print('The Most Common day is:', common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The Most Common Hour is:',  common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('The Most Commonly used start station is:', Start_Station)

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('The Most Commonly used end station is:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    Combination_of_Stations = df.groupby(['Start Station', 'End Station']).count()
    print('The Most Commonly used combination of start station and end station trip is:', Start_Station, " & ", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('The Total travel time is:', Total_Travel_Time)

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('The Mean travel time is:', Mean_Travel_Time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
     if 'Gender' in df.columns:
     gender_count = df['Gender'].value_counts()
     print(gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
        if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("\nEarliest year of birth is: " , earliest_birth_year)
        print("\nMost recent year of birth is: " , most_recent_birth_year)
        print("\nMost common year of birth is: " , common_birth_year)

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
