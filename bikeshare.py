import time
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# declare global variables for months and days to use throughout program
months = ['january','february','march','april','may','june','july','august','september','october','november','december']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

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
    city = input("Choose a city (Chicago, New York City, or Washington): \n>>> ").lower()
    # error message to handle incorrect inputs
    error_msg = "That's not an option.\n"

    while city not in CITY_DATA.keys():
        print(error_msg)
        city = input("Choose a city (Chicago, New York City, or Washington): \n>>> ").lower()

    # get user input for month (all, january, february, ... , june)
    month = input("Choose a month (or \'all\'): \n>>> ").lower()
    while month not in months and month != 'all':
        print(error_msg)
        month = input("Choose a month (or \'all\'): \n>>> ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Choose a day of the week (or \'all\'): \n>>> ").lower()
    while day not in days and day != 'all':
        print(error_msg)
        day = input("Choose a day of the week (or \'all\'): \n>>> ").lower()

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
    df['Start Time']  = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
       # use the index of the months list to get the corresponding int
        df = df[df['month'] == months.index(month) + 1]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def raw_data_prompt(df):
    """Allow user to choose to see raw data 5 lines at a time."""
    # get user input to see raw data output
    print_raw_data = \
    input("""Would you like to see 5 lines of your selection?
    \nEnter yes or no.\n>>> """)

    # loop to add 5 lines of data every time the user chooses to continue
    n = 5
    # print data based on user input
    while print_raw_data.lower() == 'yes':
        print(df.iloc[:n])
        n += 5
        print_raw_data = input("""
        \nWould you like to see 5 more lines of your selection?
        \nEnter yes or no.\n>>> """)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("Most common month: ",months[common_month-1].title())

    # display the most common day of week
    print("Most popular day of the week: {}"\
    .format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print("Most popular start hour: {}".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most popular start station: {}"\
    .format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print("\nMost popular end station: {}".\
    format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    pop_combo = df.groupby(['Start Station','End Station'])\
    .size().sort_values(ascending=False)
    # isolate most popular start station from pair
    pop_combo_start = pop_combo.idxmax()[0]
    # isolate most popular end station from pair
    pop_combo_end = pop_combo.idxmax()[1]

    print("\nMost Popular Trip:\nFrom {} to {}."\
    .format(pop_combo_start,pop_combo_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print("Total time of all trips in seconds: {}".format(total_time))
    # break total time into days, hours, minutes, and seconds
    total_days = int(total_time / (3600 * 24))
    total_hours = int(total_time % (3600 * 24) / 3600)
    total_minutes = int((total_time % 3600) / 60)
    total_seconds = int(total_time % 60)
    print("\nThat is approximately {} days, {} hours, {} minutes, and {} seconds"
    .format(total_days, total_hours,total_minutes,total_seconds))

    # display mean travel time
    average_time = df['Trip Duration'].mean()
    print("\nAverage Trip Duration in seconds: {}".format(average_time))
    # break average time into hours, minutes, and seconds
    average_hours = int(average_time / 3600)
    average_minutes = int((average_time % 3600) / 60)
    average_seconds = int(average_time % 60)
    print("\nThat is approximately {} hours, {} minutes, and {} seconds"
          .format(average_hours,average_minutes,average_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Total of each type of user:\n{}"\
    .format(df['User Type'].value_counts()))

    # Display counts of gender
    try:
        print("\nTotal of each gender:\n{}"\
        .format(df['Gender'].value_counts()))
    except KeyError:
        pass

    # Handles errors due to missing age & gender data from Washington file
    try:
        # Display earliest, most recent, and most common year of birth
        print("\nThe oldest rider was born in: ",int(df['Birth Year'].min()))
        print("\nThe youngest rider was born in: ",int(df['Birth Year'].max()))
        print("\nThe most common birthyear is: ",int(df['Birth Year'].mode()[0]))
    except KeyError:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stat_plot(df):
    start_time = time.time()
    # Request user input for custom module
    trip_distance_input = input("""
    \nWould you like to see a plot of user data?
    \n(Requires an installation of matplotlib)
    \nEnter yes or no.
    \n>>> """)

    # Only run custom module based on user input
    if trip_distance_input.lower() == 'yes':
        # Handles errors for missing data in Washington file
        try:
            # convert birth year to current age
            x = datetime.datetime.now().year - df['Birth Year']
            # convert trip duration to minutes
            y = df['Trip Duration'] / 60

            plt.scatter(x, y)
            plt.xlabel('Age (Years)')
            plt.ylabel('Trip Duration (Minutes)')

            plt.title("Trip Duration v. Rider Age Plot")
            plt.legend()
            plt.show()

            print("\nThis took %s seconds." % (time.time() - start_time))

        except:
            print("Data is not available for this selection")
    else:
        return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data_prompt(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        user_stat_plot(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n>>> ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
