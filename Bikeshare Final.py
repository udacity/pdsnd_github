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
        city = input('Please enter city you like to filter by (chicago, new york city or washington): ')
        if city in ('chicago', 'new york city', 'washington'):
             break 
        else:
             print('Invalid city name')
             continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
        month = input('Please enter specific month to filter by: ')
        if month in ('all','january', 'february','march','april','may','june'):
            print
            break
        else:
            print('Invalid month input') 
            continue
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        day = input('Please enter day of week to filter by: ')
        if day in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
         break
        else:
         print('Invalid day input')
         continue
        
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
                                     
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.weekday_name
                                     
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month)+1

        df = df[df['Month'] == month]
    
    if day != 'all':
        df = df[df['Day'] == day.title()]

    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    Popular_Month = df['Month'].mode()[0]
    print('Most Popular Start Month: ',Popular_Month)
    # TO DO: display the most common day of week
    Popular_Day_of_Week = df['Day'].mode()[0]
    print('Most Popular Day of Week: ', Popular_Day_of_Week)

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    Popular_Hour = df['Hour'].mode()[0]
    print('Most Popular Hour: ', Popular_Hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Common_Start_Station = df['Start Station'].mode()[0]
    print('Most Popular Start Station: ', Common_Start_Station)

    # TO DO: display most commonly used end station
    Common_End_Station = df['End Station'].mode()[0]
    print('Most Popular End Station: ', Common_End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_to_end'] = df['Start Station'].astype(str) + 'and' + df['End Station']
    Frequent_Combination = df['Start_to_end'].mode()[0]
    print('Most Frequent Combination of Start Station and End Station: ',Frequent_Combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()
    print('Total Travel Time: ',Total_Travel_Time)
    

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean Travel Time: ', Mean_Travel_Time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    Count_of_User_Type = df['User Type'].value_counts()
    print('Counts of User Types: ', Count_of_User_Type)
    
    # TO DO: Display counts of gender
    Count_of_Gender = df['User Type'].value_counts()
    print('Counts of User Types: ', Count_of_Gender)

    # TO DO: Display earliest, most recent, and most common year of birth
 
    try:
        Oldest= df['Birth Year'].max()
        Youngest= df['Birth Year'].min()
        Popular_Year = df['Birth Year'].mode()
        print('Oldest, Youngest, Popular Birth Year: ', Oldest, Youngest, Popular_Year)
    except KeyError:
        print('No data Available')

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

