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
        print('Please enter a city below')
        city = input(' ')
        city = city.lower()
        if city not in ('chicago','new york city', 'washington'):
            print('Your choice is not valid')
            break
        else:
            print('Please enter a month below')
            month = input(' ')
            month = month.lower()
            if month not in ('all', 'january', 'febuary', 'march', 'april', 'may', 'june'):
                print('Your choice is not valid')
                break
            else:
                print('Please enter a day of the week')
                day = input(" ")
                day = day.lower()
                if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday'):
                     print('Your choice is not valid')
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

    # load data file into a dataframe
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

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month is ' , most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day is' , most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour is', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is', most_common_start_station)
    


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is', most_common_end_station)
   
    # TO DO: display most frequent combination of start station and end station trip
    print('Below is the most frequent combination of the start and end station. I have also included how many times this combincation has occured in the dataframe')
    df_count = df.groupby(['Start Station'])['End Station'].value_counts().reset_index(name="Count")
    max_freq = df_count["Count"].max()
    df_count = df_count[df_count["Count"] == max_freq]
    print(df_count)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    total_time = str(total_time)
    print('The total travel time is ' + total_time + ' seconds')
    
    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    avg_time = str(avg_time)
    print('The average travel time is ' + avg_time + ' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Below are the number of different type of users')
    user_type_count = df['User Type'].value_counts()
    print(user_type_count)

    # TO DO: Display counts of gender
    try:
        
        gender = df['Gender'].value_counts()
        print('Below are the number of different genders')
       
        print(gender)
        
    except KeyError:
        print('Gender data not found')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print(df['Birth Year'].min())
        print('The earliest year that someone was born in this dataframe is')
        print('The most recent  year that someone was born in this dataframe is')
        print(df['Birth Year'].max())
        print('The most common year that people were born in this dataframe is')
        print(df['Birth Year'].mode()[0])
    except KeyError:
        print('Year Information is not found')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_data(df):
#This function asks the user if they wish to see 5 rows of raw data. As long as they enter yes you will get more 
#raw data each time in rows of 5. 
    first_row_iteration = 0
    
    print('Do you wish to see 5 rows of raw data? If so please respond yes or no')
    while True:
        response = input('')
        response = response.lower()
        if response == 'yes':
            print(df[first_row_iteration: first_row_iteration + 5])
            first_row_iteration += 5
            print('Do you wish to see more rows')
            continue
        else:
            break

def main():
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
