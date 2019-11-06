import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york', 'washington']
cal_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

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
    
    while True :
        city = input('You need to select a city: Chicago, New York City or Washington\n').lower()
        if city.lower() not in cities:
            print("Please try again")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True :    
        month = input('You need to select Which month would you like to explore?\n').lower()
        if month.lower() not in cal_months:
            print("Please try again or type - all.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input('You need to select a weekday that you are interested in analyzing?\n').lower()
        if day.lower() not in weekdays:
            print("Please try again or type - all.")
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = cal_months
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
            df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)


    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('Most Common day:', common_day)


    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most popular start station is :  ",popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most popular end station is :  ",popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Station'] = df['Start Station'].str.cat(df['End Station'],sep="  --  ")
    popular_trip=df['Station'].mode()[0]
    print("The most popular trip  is :  ",popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum(skipna=True)
    count=df['Trip Duration'].count()
    print('Total travel time:', total_travel_time/86400, " Days")


    # TO DO: display mean travel time

    mean_travel_time = total_travel_time/(count)
    print("Mean Travel Time:",mean_travel_time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    count=df['User Type'].value_counts(dropna=True)
    subscriber=count['Subscriber']
    customer=count['Customer']
    print("Subscriber:",subscriber," Customer:",customer)
    
    if city != "washington" :
    # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("Gender counts are\n{}\n".format(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
   
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        earliest , recent , common_year = int(earliest),int(recent),int(common_year)
        print("\n\nEarliest Birth Year :  {} \nMost Recent Birth Year :  {} \nMost Common Birth Year :  {}  ".format(earliest,recent,common_year))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    row_index = 1
    view_data = input("\nWould you like to view the raw data? Type 'Yes' or 'No' \n").lower()
    
    while True:
        if view_data == 'no':
            return
        if view_data == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5
        view_data = input("\n Would you like to see an extra 5 rows of the raw data? Type 'Yes' or 'No' \n").lower()     
        
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)
               
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            

if __name__ == "__main__":
    main()



