#import time the calcutulate the run time 
import time
#import pandas to use the pandas series and pandas dataframe
import pandas as pd
#import numpy to use numpy nd array
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
        #Create variable ci to hold input answer 
        city = input("Which city would you like to filter by? chicago, new_york_city, washington /n ").lower() #user should input the city name like this
        if city not in ("chicago", "new_york_city", "washington"):
            print("Sorry its invalid input ")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        #Create variable mon to hold input answer 
        month = input("Which month would you like to filter by? january, february, ... , june or all to display all months  /n ").lower() 
        if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print("Sorry its invalid input ")
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        #Create variable day to hold input answer 
        day = input("Which day would you like to filter by? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or 'all' display all days /n ").lower() 
        if day not in ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"):
            print("Sorry its invalid input ")
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
    #using panda dataframe to load the data
    df =pd.read_csv(CITY_DATA[city])
    #converting to datatime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # access month and day of week from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filtering by month
    if month != 'all':
        Months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = Months.index(month) + 1
        df = df[df['month'] == month]
    # filtering by day 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    Most_common_month = df['month'].mode()[0]
    print('Most Common Month:', Most_common_month)

    # TO DO: display the most common day of week
    Most_common_day = df['day_of_week'].mode()[0]
    print('Most Common Month:', Most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    Most_common_starthour = df['hour'].mode()[0]
    print('Most Common Hour:', Most_common_starthour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    startstation = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', startstation)
    # TO DO: display most commonly used end station
    endstation = df['End Station'].value_counts().idxmax()
    print('Most Commonly used end station:', endstation)
    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = df.groupby(['Start Station', 'End Station']).count()
    print('Most frequent combination of start station and end station trip:', startstation, " & ", endstation)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time:', total_travel_time/86400, " Days")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user = df['User Type'].value_counts()
    print('User Types:\n', counts_user)
    # TO DO: Display counts of gender
    #we should use try and expect function
    try:
      counts_gender = df['Gender'].value_counts()
      print('\nGender Types:\n', counts_gender)
    except KeyError:
      print("Error:No data available now .")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest = df['Birth Year'].min()
      print('Earliest Year:', earliest)
    except KeyError:
      print("Error:No data available now.")
    try:
      recent = df['Birth Year'].max()
      print('Most Recent Year:', recent)
    except KeyError:
      print("Error:No data available now.")
    try:
      common = df['Birth Year'].value_counts().idxmax()
      print('Most Common Year:', common)
    except KeyError:
      print("Error:No data available now.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    userinput = input('Do you want to see raw data? Enter yes or no.\n')
    number = 0

    while True : #True to make it readable
        if userinput.lower() != 'no':
            print(df.iloc[number : number + 5])
            number += 5
            userinput = input('\nDo you want to see more raw data? [please Enter yes or no.\n')
        else:
            break    
def main():
# the final function which can run all function above
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
