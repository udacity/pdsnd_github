import time
import pandas as pd
import numpy as np
#get data from 3 cities
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
    global city
    city = input('Hi! Which of these cities do you want to get data from: Chicago, New York City, or Washington?\n').lower()
   
    
    while city not in CITY_DATA.keys() :
        print('Sorry, the city is not among the options listed. Try again')
        city = input('Which of these cities do you want to get data from: Chicago, New York City, or Washington?\n').lower()

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which of these months are you interested in: January, February, March, April, May, June or all?\ntype in your option\n').lower()
        month_value=['january', 'february', 'march', 'april', 'may', 'june', 'all']
        
        if month not in month_value :
            print('Invalid month selection. Please choose a month from the options or type all')
            month = input('Which of these months are you interested in: January, February, March, April, May, June or all?\ntype in your option\n').lower()
            
        else :
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_values=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
        day = input("Which of the following weekdays are you looking at: Sunday, Monday, Tuesday,\nWednesday, Thursday, Friday, Saturday or all the days?").lower()
        if day not in day_values:
            print("Invalid! Please type in a valid day of the week or type all to see all")
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
    df['Start Time'] = df['Start Time'].astype('datetime64')
    df['Month'] = df['Start Time'].dt.month_name()
    df['Week Day'] = df['Start Time'].dt.day_name()
    
    if month != 'all' :
        df = df[df['Month'] == month.title()]
    
    if day != 'all' :
        df = df[df['Week Day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_count = df['Month'].value_counts()
    highest_month_count = month_count.max()
    most_common_month = month_count.idxmax()
    print('\nCalculating The Most Frequent Month of Travel...\n')
    print('The Most Common Month is: {}, And Count is: {}'.format(most_common_month,highest_month_count))


    # display the most common day of week
    count_week_day = df['Week Day'].value_counts()
    max_week_day_count = count_week_day.max()
    most_common_week_day = count_week_day.idxmax()
    print('\nCalculating The Most Frequent Day of Travel...\n')
    print('The Most Common Day is: {}, With Count of: {}.'.format(most_common_week_day,max_week_day_count))



    # display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    count_start_hour = df['Start Hour'].value_counts()
    max_count_start_hour = count_start_hour.max()
    most_common_start_hour = count_start_hour.idxmax()
    
    print('\nCalculating The Most Frequent Hour of Travel...\n')
    print('The Most Common Start Hour is: {}, With a Count of: {}.'.format(most_common_start_hour,max_count_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    count_start_station = df['Start Station'].value_counts()
    max_start_station_count = count_start_station.max()
    most_common_start_station = count_start_station.idxmax()
    
    print('\nCalculating The Most Start Station...\n')
    print('The Most Common Start Station: {}, With Count of: {}'.format(most_common_start_station,max_start_station_count))

    # display most commonly used end station
    count_end_station = df['End Station'].value_counts()
    max_end_station_count = count_end_station.max()
    most_common_end_station = count_end_station.idxmax()
    
    print('\nCalculating The Most Popular End Station...\n')
    print('The Most Common End Station is: {}, With Count of: {}'.format(most_common_end_station,max_end_station_count))

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ', ' + df['End Station']
    trip_count = df['Trip'].value_counts()
    max_trip_count = trip_count.max()
    most_common_trip = trip_count.idxmax()
    
    print('\nCalculating The Most Popular Trip...\n')
    print('The Most Common Trip: {}, With Count: {}'.format(most_common_trip,max_trip_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total Travel Time:', df['Trip Duration'].sum())


    # display mean travel time
    print('Mean Travel Time:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('The Earliest year of Birth:', df['Birth Year'].min())
        print('The Most Recent year of Birth:', df['Birth Year'].max())
        print('The Most Common year of Birth:', df['Birth Year'].value_counts().idxmax())

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
        display_data()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
#Adding the display data function as instructed by last reviewer. :)
def display_data():
    global city
    df = pd.read_csv(CITY_DATA[city])
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 0
    while (view_data=='yes'):
        print(df.iloc[0:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        if view_data!='yes':
            break
if __name__ == "__main__":
	main()

#Credits to Pandas .dt Series which helped access date values and idxmax for frequency
#https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.html
#https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.month_name.html
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html
