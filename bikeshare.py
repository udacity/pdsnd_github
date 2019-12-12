import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
   # Asks user to specify a city, month, and day to analyze.
   ask_1=input("")

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city=input("Enter name city  ").lower() 
    
    while(city!="chicago" and city!="new york city" and city!="washington"):
        city=input("Enter a valid city name   ").lower() 
    print(city)    
    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("Enter a month EX.(All ,January ,February, March, April , May ,June ,July ,August ,September , October , November,December"  ).capitalize() 
    while(month!="All" and month!="January" and month!="February" and month!="March" and month!= "April" and month!= "May"and month!="June" and month!="July"and month!="August" and month!="September" and month!="October" and month!="November" and month!="December"):
       month=input("Enter a valid month name  ").capitalize()
    print(month)
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Enter a day  ").capitalize()
    while(day!="All" and day!="Sunday" and day!="Monday" and day!="Tuesday" and day!="Wednesday" and day!="Thursday" and day!="Friday" and day!="Saturday"):       
        day=input("Enter a valid day name   ").capitalize()
    print(day)
   
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
    # filtered by the city
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the start and end times from strings to dates, so we can extract the day/month from them
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract the day and month into their separate columns
    df['day'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month_name()
    
     # filter by month if applicable
    if month != 'All':
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'All': 
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
        
    print("Most common start month:\n{} \n".format(popular_month))

    # TO DO: display the most common day of week
    popular_week = df['day'].mode()[0]
        
    print("Most common start day:\n{} \n".format(popular_week))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most common start hour:\n{} \n".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station= df['Start Station'].mode()[0]
    print("Most common start station:\n{} \n".format(start_station))

    # TO DO: display most commonly used end station
    end_station= df['End Station'].mode()[0]
    print("Most common start station:\n{} \n".format(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['route']=df['Start Station']+['End Station']
    rote_cover=df['route'].mode()[0]
    print("Most common start station:\n{} \n".format(rote_cover))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

   # TO DO: display total travel time
    total=df['Trip Duration'].sum()
    print(total)
    # TO DO: dispp mean travel time
    start=0
    end=4
    user=input("Do you want view data")
    
    while(user=="yes"):
        print(df.iloc[start:end+1])
        start+=5
        end+=5
        user=input("Do you want view data ,agin")

    
   
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
    # TO DO: Display counts of gender
    
    try: 
      print(df['Gender'].value_counts())
    except KeyError:
        print("The city of Washington has no gender")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Birth_Year=df['Birth Year'].min()
      Birth_Year1=df['Birth Year'].max()
      Birth_Year2=df['Birth Year'].mode()[0]
      print(Birth_Year)
      print(Birth_Year1)
      print(Birth_Year2)
    except KeyError:
        print("The city of Washington has no Birth Year")

    
    
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
# file_1.close()
# file_2.close()
# file_3.close()