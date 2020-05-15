import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities=['chicago','new york city','washington']

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
    city=input("Which city would you like to filter : ").lower()
    while(city not in cities):
        print("Please enter the valid city")
        city=input("Which city would you like to filter : ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months=['all','january', 'february', 'march', 'april', 'may', 'june']
    month=input("Which month would you like to filter : ").lower()
    while(month not in months):
        print("Please enter the valid month")
        city=input("Which month would you like to filter : ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
    day=input("Which day of the week would you like to filter : ").lower()
    while(day not in days):
        print("Please enter the valid day")
        city=input("Which day of the week would you like to filter : ").lower()

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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['combination name'] = df['Start Station']+" "+df['End Station']

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

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
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    
    print("The most common month : ",popular_month)
    
    # TO DO: display the most common day of week
    popular_day=df['day'].mode()[0]
    
    print("The most common day of week : ",popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    
    print("The most common start hour : ",popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    popular_startstation = df['Start Station'].mode()[0]
    print("Popular start station : ",popular_startstation)
    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]
    print("Popular end station : ",popular_endstation)

    # TO DO: display most frequent combination of start station and end station trip
   
   # name=df.groupby(['Start Station','End Station']).count().sort_values(by=['Start Station','End Station'],axis=0).iloc[-1]
    combination = df['combination name'].mode()[0]
    print("Most frequent combination of start station and end station : ",combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    
    print("Total travel time:",total_duration)
    
    # TO DO: display mean travel time

    mean_duration = df['Trip Duration'].mean()
    
    print("Mean travel time:",mean_duration)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    
    print("The count of user types :\n",user_types)
    
    # TO DO: Display counts of gender
    if('Gender' in df):
        gender_count = df['Gender'].value_counts()
        print("Gender count: \n",gender_count)
    #else:
     #   print("This city did not provide any data regarding gender")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    
    if('Birth Year' in df):
        earliestyear = df['Birth Year'].min()
        recentyear = df['Birth Year'].max()
        mostcommonyear = df['Birth Year'].mode()[0]
        print("Earliest year of birth : ",earliestyear)
        print("Most recent year of birth : ",recentyear)
        print("Most common year of birth : ",mostcommonyear)
    #else:
     #   print("This city did not provide any data regarding year of birth")
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    check=input("do you want to see raw data? : ").lower()
    while(check not in ['yes','no']):
        print("Enter yes or no to see the raw data ")
        check=input("do you want to see raw data? : ").lower()
    i=0
    k=len(df.index)
    while(check == "yes" and i<k):
        print(df.iloc[i:i+5])
        check=input("do you want to see  Another 5 rows raw data? : ").lower()
        i+=5
        
        
   


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
