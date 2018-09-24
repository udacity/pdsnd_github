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
# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("enter name of the city (all lower case): {}, {}, {}\n".lower().format('chicago', 'new york city', 'washington'))
        if city not in ["chicago", "new york city", "washington"]:
            print("this input is invalid, please select cities from the aforementioned list")
        else:
            break

# get user input for month (all, january, february, ... , june)
    while True:
        month = input("enter name of the city (all lower case): {}, {}, {}, {}, {}, {}\n or {}\n".lower().format('january', 'february', 'march', 'april', 'may', 'june', 'all'))
        if month not in ["january", "february", "march", "april", "may", "june", "all"]:
            print("this input is invalid, please select months from the aforementioned list", month)
        else:
            break

# get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("enter the days of the week from the list (all lower case): {}, {}, {}, {}, {}, {}, {} or {}\n".lower().format('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'))
        if day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
            print("this input is invalid, please select months from the aforementioned list")
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

    # extract month, day of week from Start Time and hour to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour

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

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("the most popular month of travel is: \n{}".format(popular_month))

    # display the most common day of week
    popular_week = df['day_of_week'].mode()[0]
    print("the most popular week day of travel is: \n{}".format(popular_week))

    # display the most common start hour
    popular_start_hour = df['start_hour'].mode()[0]
    print("the most popular start hour of travel is: \n{}".format(popular_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print("the most commonly used start station is: \n{}".format(common_start_station))
    # display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("the most commonly used end station is: \n{}".format(common_end_station))

    # display most frequent combination of start station and end station trip
    highest_combination_start_End_station = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).head(1)
    print("the most frequent combination of start station and end station trip is: \n{}".format(highest_combination_start_End_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("the total travel time is: \n{}".format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("the mean travel time is: \n{}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_type = df['User Type'].value_counts()
    print("the count of specific user types are: \n{}".format(counts_of_user_type))
    # Display counts of gender
    if 'Gender' in df.columns:
        counts_of_gender = df['Gender'].value_counts()
        print("the count of gender is: \n{}".format(counts_of_gender))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].sort_values(ascending=True).head(1).astype(dtype=int)
        print("the earliest year of birth is: \n{}".format(earliest_birth_year))

    elif 'Birth Year' in df.columns:
        most_recent_birth_year = df['Birth Year'].sort_values(ascending=False).head(1).astype(dtype=int)
        print("the most recent year of birth is: \n{}".format(most_recent_birth_year))

    elif 'Birth Year' in df.columns:
        most_common_year_of_birth = df['Birth Year'].mode()[0].astype(dtype=int)
        print("the most common year of birth is: \n{}".format(most_common_year_of_birth))

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
