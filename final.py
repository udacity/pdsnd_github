import time
import pandas as pd
import numpy as np
import calendar
from datetime import datetime

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
           try:
              city= input("\nChoose a city to analyze; chicago, washington, new york city: \n")
              if city.lower() in list(CITY_DATA.keys()):
                  print('Hello there,lets analyze '+city+' city data!!')
                  break
              else:
                  print("\nPlease enter any of the cities below:.\n")
                  for city in list(CITY_DATA.keys()):
                      print(city)
           except Exception as e:
               print("please enter the right city")
    while True:
        try:
            month=input("\nChoose month to filter the data by(January, February,March,April,May,June) or 'all' for no month filter:\n")
            if month != 'all':
                if month in calendar.month_name[1:7]:
                    break
                else:
                    print("please choose one of the months below")
                    for k in calendar.month_name[:7]:
                        print(k)
            else:
                break
        except Exception as e:
            print("please input the right month")

    while True:
        try:
            day=input("\nChoose A DAY to filter the data by(Monday,Tuesday,Wednesday,Thursday,Friday,Saturday, Sunday) or 'all' for no month filter:\n")
            if day != 'all':
                if day in calendar.day_name[:7]:
                    break
                else:
                    print("please choose one of the days below")
                    for k in calendar.day_name[:7]:
                        print(k)
            else:
                break
        except Exception as e:
            print("please enter the right day")

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

    df=pd.read_csv(CITY_DATA[city])
    try:
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month']=df['Start Time'].dt.month
        df['day']=df['Start Time'].dt.weekday_name
        if month != 'all':
            month=calendar.month_name[:7].index(month)
            df=df[df['month']==month]
        if day != 'all':
            df = df[df['day'] == day.title()]
        return df

    except Exception as e:
        print("The load_data function has a problem...")

def view_data_stats(df):
    """

    Displays raw data from the dataframe  and descriptive statistics

    """
    try:
        while True:
            view_data = input('\nWould you like to view the raw data? Enter yes or no...\n')
            if view_data.lower() =='yes':

                print(df.head())
                print(df.describe())
                print(df.info())
            else:
                break
    except Exception as e:
        print("The view_data_stats function has a problem...")


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    try:
        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # display the most common month
        df['month']=df['Start Time'].dt.month
        common_month=df['month'].mode()[0]
        print("\nThe most common month was:\n")
        print(common_month)


        # display the most common day of week
        df['day']=df['Start Time'].dt.weekday_name
        common_day=df['day'].mode()[0]
        print("\nThe most common day was:\n")
        print(common_day)


        # display the most common start hour
        df['hour']=df['Start Time'].dt.hour
        common_hour=df['hour'].mode()[0]
        print("\nThe most common hour was:\n")
        print(common_hour)


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    except Exception as e:
        print("The time_stats function has a problem..")


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    try:
        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # display most commonly used start station
        common_station=df['Start Station'].mode()[0]
        print("\nThe most common start station was:\n" +  common_station)


        # display most commonly used end station
        common_end_station=df['End Station'].mode()[0]
        print("\nThe most common end station was:\n" + common_end_station)



        # display most frequent combination of start station and end station trip
        df['comb']=df['Start Station'] +' and '+ df['End Station']
        common_comb=df['comb'].mode()[0]
        print("\nThe most frequent combination of start station and end station respectively:\n" + common_comb)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    except Exception as e:
        print("The station_statsfunction has a problem..")


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    try:
        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # display total travel time
        df['End Time']=pd.to_datetime(df['End Time'])
        df['time_diff']=df['End Time']-df['Start Time']
        df['time_diff']=df['time_diff']/np.timedelta64(1,'s')
        total_travel_time=df['time_diff'].sum()
        print("\nThe total travel time in seconds was:\n")
        print(total_travel_time)



        # display mean travel time
        mean_travel_time=df['time_diff'].mean()
        print("The mean travel time was {} seconds.".format(mean_travel_time))
        #print()


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    except Exception as e:
        print("The trip_duration_stats function has a problem")



def user_stats(df):
    """Displays statistics on bikeshare users."""
    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        count_user_type=df['User Type'].value_counts()
        print("\nBelow are the counts of user types:\n")
        print(count_user_type)


        # Display counts of gender
        if 'Gender' in df:
            count_gender =df['Gender'].value_counts()
            print("\nBelow are the gender counts:\n")
            print(count_gender)
        else:
            print("The dataframe has no gender column")



        # Display earliest, most recent, and most common year of birth
        if 'Birth Year' in df:
            common_birth_year =int(df['Birth Year'].mode()[0])
            print("\nThe most common year of birth was {} \n".format(common_birth_year))
            #print()


            earliest_birth_year =int(df['Birth Year'].min())
            print("\nThe earliest year of birth was {}\n". format(earliest_birth_year))
            #print()


            most_recent_birth_year = int(df['Birth Year'].max())
            print("\nThe most recent year of birth was:\n")
            print(most_recent_birth_year)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)



    except Exception as e:
        print("The user_stats function has a problem..")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        view_data_stats(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
