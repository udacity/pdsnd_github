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
        print('\nPlease choose one of the following cities to analyze by typing the full city name\n')
        city = input('Chicago, New York City, Washington: ').lower()
        print('\nYou have requested: ',city.capitalize())
        if city not in ('chicago', 'new york city', 'washington'):
            print('\nWARNING: This is not an appropriate choice, please choose again.\n\n')
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    print('\nPlease choose a month to filter, or type in "all" for all months\n')
    while True:
        month = input('January, February, March, April, May, June, or all: ').lower()
        print('\nYou have requested: ',month.capitalize())
        if month not in ('january','february','march','april','may','june','all'):
            print('\nWARNING: This is not an appropriate month/filter, please choose again.\n\n')
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('\nPlease choose a day to filter or "all" for no filters\n')
    while True:
        day = input('Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, All: ').lower()
        print('\nYou have requested: ',day.capitalize())
        if day not in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
            print('\nWARNING: This is not an appropriate day/filter, please choose again.\n\n')
        else:
            break
    input('\nPress Enter to Start the various calculations...')
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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    input('\nPress Enter to display The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most Common Month was: ', common_month)
              

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most Common Day was: ', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most Common Hour was: ',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    input('\nPress Enter to display The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station was: ',common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station was: ',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    Combo_Start_stop_station = df.groupby(['Start Station', 'End Station']).count()
    print('The most commonly used combination of Start and End Station was: ', common_start_station, " & ", common_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    input('\nPress Enter to display Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total Travel Time: ',round(Total_Travel_Time/86400,2)," Days")

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('The Mean travel time is: ', round(Mean_Travel_Time/60,2), " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    input('\nPress Enter to display User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of User Types: ', user_types)

    # TO DO: Display counts of gender
    try:
        gender_type = df['Gender'].value_counts()
        print('\nGender Types:\n', gender_type)
    except KeyError:
        print('\nGender Types: SORRY, this data was not available based on your requested filters')
        

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earliest_Year = df['Birth Year'].min()
        print('\nEarliest Year of Birth: ', round(Earliest_Year,0))
    except KeyError:
        print('\nEarliest Year of Birth: SORRY, this data was not available based on your requested filters')
    
    try:
        Most_Recent_Year = df['Birth Year'].max()
        print('\nMost Recent Year of Birth: ', round(Most_Recent_Year,0))
    except KeyError:
        print('\nMost Recent Year of Birth: SORRY, this data was not available based on your requested filters')
        
    try:
        Most_Common_Year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year of Birth: ', round(Most_Common_Year,0))
    except KeyError:
        print('\nMost Common Year of Birth: SORRY, this data was not available based on your requested filters')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_raw_data(df):
    """ This function is created to display upon request by the user in this manner: 
        Script should prompt the user if they want to see 5 lines of raw data.
        If the answer is "Yes", continue this prompt and display the raw data until the user says "No"
    """
    start_row = 0
    end_row = 5
    
    Show_5 = input('Would you like to see 5 lines of raw data? (Y/N): ').lower()  
    if Show_5.lower() =='y':
        while True:
            print(df.iloc[start_row:end_row,:])
            start_row += 5
            end_row += 5
            Stop_5 = input('\nWould you like to see 5 more? (Y/N): ').lower()
            if Stop_5.lower() == 'n':
                break
            else:
                continue

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        get_raw_data(df)

        restart = input('\nWould you like to restart? Enter "yes" or "no": ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
