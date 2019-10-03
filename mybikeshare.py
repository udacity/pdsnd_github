import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

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
    city = input("""\n\nPlease enter Chicago, New York, or Washington: """).title()
    while True:
        if city in ["Chicago", "New York", "Washington"]:
            break
        else:
            print("\nInvalid entry. Please type Chicago, New York, or Washington")
            city = input("""\nPlease enter Chicago, New York City, or Washington: """).title()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("""\n\nPlease enter for which month of the year you would like data: """).title()
    while True:
        if month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "All"]:
            break
        else:
            print("\nInvalid entry. Please enter a valid month of the year")
            month = input("""\nPlease enter for which month of the year you would like data. If you would like data for all days please enter 'all': """).title()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("""\n\nPlease enter for which day of the week you would like data. If you would like data for all days please enter 'all': """).title()
    while True:
        if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "All"]:
            break
        else:
            print("\nInvalid entry. Please enter the day of the week.")
            day = input("""\nPlease enter for which day of the week you would like data. If you would like data for all days please enter 'all': """).title()
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
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])

    df["year"] = pd.DatetimeIndex(df["Start Time"]).year
    df["month"] = df["Start Time"].dt.month_name()
    df["day_week"] = df["Start Time"].dt.weekday_name
    df["hour"] = df["Start Time"].dt.hour

    if month != "All":
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "All"]
        #month = months.index(month) + 1
        df = df[df["month"] == month]


    if day != "All":
        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","All"]
        df = df[df["day_week"] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mode_month = df["month"].mode()[0]
    print("\n\nThe bikes were rented most frequently in the month of {}.".format(mode_month))

    # TO DO: display the most common day of week
    mode_week = df["day_week"].mode()[0]
    print("\nThe bikes were rented most frequently on {}s.".format(mode_week))

    # TO DO: display the most common start hour
    mode_hour = df["hour"].mode()[0]
    print("\nThe bikes were rented most frequently at {}:00.".format(mode_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mode_start_station = df["Start Station"].mode()[0]
    print("\n\nThe most frequent starting station was {}.".format(mode_start_station))

    # TO DO: display most commonly used end station
    mode_end_station = df["End Station"].mode()[0]
    print("\nThe most frequent ending station was {}.".format(mode_end_station))
    # TO DO: display most frequent combination of start station and end station trip
    df["combination"] = df["Start Station"] + " to " + df["End Station"]
    mode_combination = df["combination"].mode()[0]
    print("\nThe most frequent route was from {}.".format(mode_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("\n\nThe total travel time for your selected period was {} hours.".format(*divmod(total_travel_time, 60)))


    # TO DO: display mean travel time
    average_travel_time = df["Trip Duration"].mean()
    print("\nThe average total travel time for your selected period was {} mintues.".format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df["User Type"].value_counts()
    print("\n\nThere were the following numbers of users for your selected time period:\n{}".format(user_type_count))

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        sex = df["Gender"].value_counts()
        print("\nDuring your selected time period, the breakdown of the users by sex was:\n{}".format(str(sex)))
    else:
        print("""\n\nDemographic information on the users' sex was not collected.""")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        b_y_earliest = int(df["Birth Year"].min())
        b_y_latest = int(df["Birth Year"].max())
        b_y_mode = int(df["Birth Year"].mode()[0])
        print("\nThe oldest user was born in {}, and the youngest user was born in {}. \nThe most common year of birth was {}.".format(b_y_earliest, b_y_latest, b_y_mode))
    else:
        print("""\n\nDemographic information on the users' year of birth was not collected.""")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):

    raw_data = input('Do you want to view five rows of raw data? Please enter Yes or No.')
    next_row = 0
    blocksize = 10 #display rows in blocks of 10

    while raw_data == 'y':
        next_slice = df[next_row : next_row + blocksize]
        if len(next_slice) == 0:
            print ('No more raw data to print.')
            break
        next_row = next_row + blocksize
        print (next_slice)
        raw_data = input('Do you want to view more raw data (y/n)?')
        #print next 10 rows if there are no more rows to display else exit.
#end of function



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
