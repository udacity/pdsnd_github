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
    city = input("Would you like to see the data for Chicago, New york City, Washington or all? : ").lower()
    while city not in ['chicago', 'new york city', 'washington', 'all']:
        city = input("City is name you entered is invalid! Please input another name: ").lower()
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Select a month.. January, February, March, April, May, June or all?: ").lower()
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter a day or all?: ").lower()
    
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
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df.loc[df['month'] == month,:]
    if day != 'all': 
        df = df.loc[df['day_of_week'] == day,:]

    print(df.head())
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Displaying the most common month: {}".format(str(df['month'].mode().values[0])))

    # TO DO: display the most common day of week
    print("Displaying the most common day of the week: {}".format(str(df['day_of_week'].mode().values[0])))


    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("Displaying the most common start hour: {}".format(str(df['start_hour'].mode().values[0])))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Displaying most commonly used start station is: {}".format(df['Start Station'].mode().values[0]))
    
    # TO DO: display most commonly used end station
    print("Displaying the most commonly used end station is: {}".format(df['End Station'].mode().values[0]))


    # TO DO: display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station']+ " " + df['End Station']
    print("Displaying the most common combination of start and end station: {}".format(df['combo'].mode().values[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    df['duration'] = df['End Time'] - df['Start Time']
    
    # TO DO: display total travel time
    print("Displaying the total travel time: {}".format(str(df['duration'].sum())))
    

    # TO DO: display mean travel time
    print("Displaying the mean travel time: {}".format(str(df['duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("There is no gender information in this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print(earliest)
        recent = df['Birth_Year'].max()
        print(recent)
        common_birth = df['Birth Year'].mode()[0]
        print(common_birth)
    else:
        print("There is no birth year information in this city.")

  
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
