import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    User must specify a city, month, and day to analyze.
    Returns:
        (str) city - Filter by city
        (str) month - Filter by month or all months
        (str) day - Filter by day of the week or all days of the week
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = input("\nPlease input the name of the city you would like to view bikeshare data for? New York City, Chicago or Washington.\n")
      if city not in ('New York City', 'Chicago', 'Washington'):
        print("Sorry, that's not one of the choices. Please try again.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nPlease input the month you would like to view bikeshare data for? January, February, March, April, May, June... or all.\n")
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print("Sorry, that's not one of the choices. Please try again.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nPlease input the day of the week you would like to view bikeshare data for: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all.\n")
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        print("Sorry, that's not one of the choices. Please try again.")
        continue
      else:
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data and filters as specified by the user
    Arguments:
        (str) city - specified city
        (str) month - specified month or all months
        (str) day - specified day of week or all days of the week
    Returns:
        df - Pandas DataFrame containing data filtered by city, month, and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Shows the most popular times of travel."""

    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print('In this city, the most popular month for bikeshare use is:', popular_month)


    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('In this city, the most popular day for bikeshare use is:', popular_day)



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('In this city, the most popular time of day for bikeshare is:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Shows the most popular stations and trips."""

    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('In this city, the most popular bikeshare start station is:', Start_Station)


    # TO DO: display most commonly used end station

    End_Station = df['End Station'].value_counts().idxmax()
    print('\nThe most popular end station is:', End_Station)


    # TO DO: display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nThe most popular bikeshare trip with the same start station and end station trip is:', Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Shows on the total and average trip duration."""

    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('In this city, the total days bikeshare was used is:', Total_Travel_Time/86400, " Days")


    # TO DO: display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('The average trip duration was:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n',user_types)

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n',gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:',Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:',Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:',Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    When user inputs y, displays 10 rows from the filtered dataset, then asks if user would like to see 10 more.
    Continues asking until user inputs n.
    """
    show_rows = 10
    rows_start = 0
    rows_end = show_rows - 1    # use index values for rows

    print('\nWould you like view raw data from the current dataset?')
    while True:
        raw_data = input('      (y or n):  ')
        if raw_data.lower() == 'y':

            print('\n    Displaying rows {} to {}:'.format(rows_start + 1, rows_end + 1))

            print('\n', df.iloc[rows_start : rows_end + 1])
            rows_start += show_rows
            rows_end += show_rows

            print('\nWould you like to see the next 10 rows?'.format(show_rows))
            continue
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to view data for another city? Enter y or n.\n')
        if restart.lower() != 'y':
            break

if __name__ == "__main__":
	main()
