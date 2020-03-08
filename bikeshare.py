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
    cities = ["chicago","new york city", "washington"]
    months = ["all","january","february","march","april","may","june"]
    days = ["all", "sunday","monday","tuesday","wednesday","thrusday","friday","saturday"]
    while(1):
        city = input("Which city you want to choose among chicago, new york city, washington: ")
        city = city.lower()
        
        if city in cities: break

        else: print("Ooops! Enter the correct city name ")


    # TO DO: get user input for month (all, january, february, ... , june)
    while(1):
        print("option = [january, february, march, april ,may,june]")
        month = input("Enter name of the month to filter by, or \"all\" to apply no month filter: ")
        month =  month.lower()
        if(month in months): break
        else: print("Oops! Enter the month name correctly")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while(1):
        print("option = [sunday, monday, tuesday, wednesday ,thrusday,friday,saturday]")
        day = input(" name of the day of week to filter by, or \"all\" to apply no day filter: ")
        day = day.lower()
        if day in days:
            break
        else: print("Oops! Enter correct day")


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
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
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
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['day'] = df['Start Time'].dt.day
    df['month'] = df['Start Time'].dt.month
                     
    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("Most common month ", most_common_month)


    # TO DO: display the most common day of week
    day_of_week = df['day'].mode()[0]
    print("Most common day of week ", day_of_week)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print("Most common hour ",most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts(sort = 'True').keys().tolist()[0]
    print("Most popular start station",popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts(sort = 'True').keys().tolist()[0]
    print("Most Popular end startion",popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    popular_combination = df.groupby(['Start Station','End Station']).count().sort_values(by=['Start Station','End Station']).iloc[0]
    print("Most popular combination of start station and end statioin")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df["Trip Duration"].sum()
    print("Total travel time",total_time)
    


    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Total average travel time",mean_travel_time)

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
    gender = df['Gender'].value_counts()
    print(gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year'].value_counts(sort = 'True').keys().tolist()[0]
    print(birth_year)


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
