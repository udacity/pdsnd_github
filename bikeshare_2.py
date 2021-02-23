import time
import pandas as pd
import numpy as np
import calendar

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid input
    cities = ["chicago", "new york city", "washington"]
    months = ["january", "february", "march", "april", "may", "june", "all"]
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
       
    while True:
        city =  input("What city would you like to view- Chicago, New York City or Washington:").strip().lower()
        if city not in CITY_DATA:
            print("That is not a valid city. Please try again.")
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("Would you like to view data on a specific month between January through June, or all: ").lower()
        if month not in months:
            print("That is not a valid month. Please try again")
            continue
        else:
            print(month)
            break
        
      # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Would you like to view a specific day of the week. Enter 'all' for all: ").lower()
        if day not in days:
            print("That is not a valid day. Please try again")
            continue
        else:
            print(day)
            break
      
    print('-'*40)
    
    return city, month, day   

def load_data(city, month, day):
    
    """Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day"""
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday
    df['hour']=df['Start Time'].dt.hour
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df=df[df['month'] == month]
        
    if day != 'all':
        days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
        day= days.index(day) + 1
        df['day'] = df['Start Time'].dt.day_name()
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    month = df['Start Time'].dt.month
    day_of_week = df['Start Time'].dt.weekday_name
    hour = df['Start Time'].dt.hour
    
    # TO DO: display the most common month
   
    df['month']=df['Start Time'].dt.month
    common_month= df['month'].mode()[0]
    common_month = calendar.month_name[common_month]
    print("\nThe most common month bikeshare is used is:\n",common_month)

    # TO DO: display the most common day of week
    
    common_day=df['day_of_week'].mode()[0]
    common_day = calendar.day_name[common_day]
    print("\nThe day that has the greatest amount of users is:\n",common_day)

    # TO DO: display the most common start hour
    popular_start=df['hour'].mode()[0]
    popular_start_count=hour.value_counts().max()
    print("\nThe most common start time riders begin is {} and the number of riders with this time is {}\n".format(popular_start, popular_start_count))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("\nThe most common start station is: {}\n".format(common_start))

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("\nThe most common end station is: {}\n".format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['common_trip']=df['Start Station'] + ' to  ' + df['End Station']
    trip=df['common_trip'].mode()[0]    
    print("The most common start to end trip is:\n {}".format(trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Trip Duration']=df['Trip Duration'].mode()[0]
    travel_time=df['Trip Duration'].sum()/60/60/24
    print('The total travel time in hours was: {}'.format(travel_time))
    
    # TO DO: display mean travel time
    mean_travel=(df['Trip Duration'].mean())/60
    print('The average travel time in hours was: {}'.format(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    print('The number of users by type are:\n{}'.format(user_type))


      # TO DO: Display counts of gender
    if 'Gender' not in df.columns:
        print('Gender column unavailable')
    else:
        gender=df['Gender'].value_counts()
        print('The number of users by gender are:\n{}'.format(gender))
    
    

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print('Birth Year column unavailable')
    else:
        oldest_birth_year=df['Birth Year'].min()
        youngest_birth_year=df['Birth Year'].max()
        common_birth_year=df['Birth Year'].mean()
        print('The oldest  riders were  born {},\nthe youngest were born {},\nthe most common were born {}'.format(oldest_birth_year, youngest_birth_year, common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
'''to request if the user would like to see the raw data'''

def raw_data(df):
    b = 0
    e = 5
    data = input('\nWould you like to see the first 5 rows of data?:\n').lower()
    pd.set_option('display.max_columns',200)
    while True:
        if data.lower() == 'no':
            break
        if data.lower() == 'yes':
            print(df.iloc[b:e])
            more = input('\nWould you like to see the next 5 rows?\n').lower()
            if more.lower() == 'no':
                break
            if more.lower() == 'yes':
                b+=5
                e+=5
                print(df.iloc[b:e])
            

def main():
    city = ""
    month = ""
    day = ""
    
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
