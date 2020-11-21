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
      cities = ('new york city', 'chicago', 'washington')
      city = input("Pleae choose on the following cities (washington, new york city, chicago): " ).strip().lower()
      if city not in cities:
        print("This is not a valid city, please pick another city: ")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month = input("Please choose one month between january - june inclusive or all for all months: ").strip().lower()
        if month not in months: 
            print("This is not a valid month, please pick another month: ")
            continue 
        else: 
            break 
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'] 
        day = input("Please pick one day of the week or all days (i.e. sunday, monday...): ").strip().lower()
        if day not in days: 
            print("This is not a valid month, please pick another month: ")
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month 
    popular_month = df['month'].mode()[0]
    print("Most popular month is ", popular_month)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['week_day'] = df['Start Time'].dt.weekday_name 
    popular_day = df['week_day'].mode()[0]
    print("Most popular day is ", popular_day)


    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour 
    popular_hour = df['hour'].mode()[0]
    print("Most popular hour is ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().sort_values(ascending=False).index[0]
    print("The most common start station is ", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().sort_values(ascending=False).index[0]
    print("The most common end station is ", most_common_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    df["start_end"] = df["Start Station"] + df["End Station"]
    most_common_start_end = df["start_end"].value_counts().sort_values(ascending=False).index[0]
    print("The most common start_end situation is: ", most_common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: ", total_travel_time)
                         
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("This is the count for the different user types:\n", user_types)

    # TO DO: Display counts of gender
    try: 
        gender = df['Gender'].value_counts()
        print("This is the count for gender :\n", gender)
    except: 
        print("There is no gender information for this city\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print("The earlier year is: ", earliest_year)
        print("The most recent year is: ", most_recent_year) 
        print("The most common year is: ", most_common_year)
    except:
        print("There is no birth year information for this city\n")


                         
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
                         
        raw_data_display = input("Do you want to see raw data?").lower().strip()
        counter_start = 0
        counter_end = 5
        while raw_data_display == 'yes': 
            raw_data = df[counter_start:counter_end]
            print(raw_data)
            counter_start += 5
            counter_end += 5
            raw_data_display = input("Do you want to see more raw data?").lower().strip()
               
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
