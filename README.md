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
    cities = ('chicago', 'new york city', 'washington', )
    while True:
        city = input("\n which of these cities do you want to explore? {}".format(cities)).lower()
        if city not in cities:
            print("\n Incorrect Selection")

        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    # Updated word in input area for simplicity
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', ]
    while True:
        month = input("\n Please select a month from - {}".format(months)).lower()
        if month not in months:
            print("\n Incorrect Selection")

        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Upated word in input to make it consistent with the above  
    days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',  ]
    while True:
        day = input('\n Please select a day of the week from - {}'.format(days)).lower()
        if day not in days:
            print("\n Incorrect Selection")

        else:
            break

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

    # Create new columns in dataframe for month and day of week to filter by    
    df['month'] = pd.to_datetime(df['Start Time'], errors='coerce').dt.month
    df['day_of_week'] = pd.to_datetime(df['Start Time'], errors='coerce').dt.weekday_name

    # filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june'  ]
        filter_month = months.index(month)+1
        df = df[df['month']==filter_month]

    # filter by day
    if day != 'all':
        df = df[df['day_of_week'].str.lower()==day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print("Most common month is :", common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("Most common day of the week is :", common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = pd.to_datetime(df['Start Time'], errors='coerce').dt.hour
    common_hour = df['hour'].value_counts().idxmax()
    print("Most commmon hour is :", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_used_start = df['Start Station'].mode()[0]
    print("most used start station is :", commonly_used_start)

    # TO DO: display most commonly used end station
    commonly_used_end = df['End Station'].mode()[0]
    print("most used end station :", commonly_used_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    frequent_combination = df['combination'].mode()[0]
    print("most popular trip combination is :", frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("total travel time :", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("mean time :", mean_travel)

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
      print("no gender information available")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Year_of_Birth' in df:
      earliest = df['Year_of_Birth'].min()
      print("earliest year of birth :", earliest)
      most_recent = df['Year_of_Birth'].max()
      print("most recent births :", most_recent)
      common_birth_year = df['Year_of_Birth'].mode()[0]
      print("most common year of bith is : ", common_birth_year)
    else:
     print("no birth details avaiable.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)   


def data(df):
    """Display 5 lines of raw data."""
    user_input = input('would you like to display 5 rows of raw data? Enter yes or no.\n ')
    raw_data = 0

    while 1 == 1 :
        if user_input.lower() != 'no':
            print(df.iloc[raw_data:raw_data + 5])
            raw_data += 5
            user_input = input('\n would you like to display 5 more rows of raw data? Enter yes or no.\n')
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
        data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
