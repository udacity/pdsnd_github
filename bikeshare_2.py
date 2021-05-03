import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input("Please input the city that you want to filter by (New York City, Chicago, Washington).\n").title()
      if city not in ('New York City', 'Chicago', 'Washington'):
        print("Sorry! I cant recognize the city you want! Give it another try.\n")
        continue
      else:
        break

                    
            # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("Please enter which month you would like to filter by? January, February, March, April, May or June? And if you dont want to filter by a specific month, enter 'all'.\n").title()
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
        print("Sorry! I cant recognize the month you want to filter by! Give it another try.\n")  
        continue
      else:
        break
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("Which day of the week you would like to filter by? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday? And if you dont want to filter by a specific day, enter 'all'.\n").title()
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
        print('Sorry! I cant recognize the day of the week that you entered! Give it another try.\n')
        continue
      else:
        break

    print('-'*40) 
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:Z
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

    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        df = df[df['month'] == month]

        if day != 'All':
            df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month that people travelled in is " , most_common_month)

        # TO DO: display the most common day of week
    most_common_dow = df['day_of_week'].mode()[0]
    print("The most common day that people travelled in is " , most_common_dow)

        # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("The most common hour that people travelled in is " , most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used station to travel from is ' + start_station)

        # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used station to travel to is ' + end_station)
        # TO DO: display most frequent combination of start station and end station trip
    combination_station = df.groupby(['Start Station', 'End Station']).size().idxmax()

    print('The most commonly used combination of starting and ending stations is ' , combination_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Sum_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Sum_Travel_Time/86400, " Days")
        
        
        # TO DO: display mean travel time
    Average_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Average_Travel_Time/60, " Minutes")
        
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('Count of User Types is ', user_types_count)

        # TO DO: Display counts of gender
    try:
       gender_types = df['Gender'].value_counts()
       print('Gender Types: ', gender_types)
    except KeyError:
       print("Gender Types: No data available for this month.")

        # TO DO: Display earliest, most recent, and most common year of birth
    try:
       Earliest_Year = df['Birth Year'].min()
       print('Earliest Year is ', Earliest_Year)
    except KeyError:
       print("Earliest Year: No data available for this month.")

    try:
       Most_Recent_Year = df['Birth Year'].max()
       print('Most Recent Year is ', Most_Recent_Year)
    except KeyError:
       print("Most Recent Year: No data available for this month.")

    try:
       Most_Common_Year = df['Birth Year'].value_counts().idxmax()
       print('Most Common Year is ', Most_Common_Year)
    except KeyError:
       print("Most Common Year: No data available for this month.")

    print("/nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc : start_loc + 5])
        start_loc += 5
        view_data = input('Do you wish to continue?: ').lower()

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