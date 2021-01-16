import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']



# cd Documents\Udacity\DSPWP\python_project
"""
code from the following two O'Reilly books were used in this script:
1) Intoducing Python, by Bill Lubanovic
2) Python for Data Analysis, by Wes McKinney
"""

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to
    # handle invalid inputs
    city = input("Would you like to see data for Chicago, Washington or New York?\n")
    city = city.lower()
    if city == "new york":
        city += " city"

    while city != 'chicago' and city != 'new york city' and city != 'washington':
        city = input("Please enter the correct spelling for Chicago, New York or Washington:\n")
        city = city.lower()
        if city == "new york":
            city += " city"

    # need to set a global variable as washington has no gender or birth data
    global data_city
    data_city = city

    # get user input for month (all, january, february, ... , june)
    months.append('all')
    print("")
    print("We have data for the months of January, February, March, April, May and June. ")
    month = input("Please enter the name of the month you would like to filter the data for, or all: ")
    month = month.lower()
    while month not in months:
        month = input("Please enter the correct spelling of one of the available months, or all: ")
        month = month.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days.append('all')
    print("")
    day = input("Please enter the name of the day of a week to filter on, or 'all' to apply no day filter: ")
    day = day.lower()
    while day not in days:
        day = input("Please enter the correct spelling of the day to filter on, or 'all': ")
        day = day.lower()

    print("Here is the data for {}, month(s): {}, days: {}.".format(city, month, day))

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
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        monthi = months.index(month)
        # filter by month to create the new dataframe
        # datetime month number starts with 1, my months list index is zero based
        df = df[df['month']==monthi+1]
        """
        print(monthi)
        print(month)
        print(df)
        """

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == days.index(day)]
        # teacher's solution
        # df = df[df['day_of_week'] == day.title()]
        """
        print(day)
        print(df)
        """

    return df




def display_data(df):
    """displays the filtered DataFrame 5 rows at a time if user wants to see it"""
    print("Before we display summary statistics...")

    # let's not show the user our derived collumns (month and day_of_week)
    col_list = ['Start Time', 'End Time', 'Trip Duration',
       'Start Station', 'End Station', 'User Type']
    if data_city != 'washington':
        col_list.append('Gender')
        col_list.append('Birth Year')

    view_data = input('\nWould you like to view the first 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data != 'no'):
        print(df[col_list].iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input('\nWould you like to continue with the next 5 rows? Enter no to view the summary statistics\n')




def get_most_common(df, field):
    """gets the value counts for field of dataframe in series, sort desc and convert to frame"""
    mc = (df[field].value_counts())
    mc.sort_values(ascending=False, inplace=True)
    mc = mc.to_frame()
    return mc

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month  -----------------------------
    # get the value counts for month, sort desc and convert to frame
    cm = get_most_common(df, 'month')

    # month number will be the index of the cm frame
    # get the month name from the months list (zero based, so subtract 1)
    month = months[cm.index[0]-1]
    # number of bikeshares with be the first value (0,0) of the frame
    shares = cm.iat[0,0]

    msg = "Most popular month for bikeshares was {}, with {} shares that month."
    print(msg.format(month.title(), shares))

    # display the most common day of week  ----------------------------
    # get the value counts of most common day of week
    dw = get_most_common(df, 'day_of_week')

    # day number will be the index of the cm frame
    # get the day name from the months list
    day = days[dw.index[0]]
    # number of bikeshares with be the first value (0,0) of the frame
    shares = dw.iat[0,0]

    msg = "Most popular day for bikeshares was {}, with {} shares that day."
    print(msg.format(day.title(), shares))

    # display the most common start hour  ------------------------------
    df['hour'] = df['Start Time'].dt.hour
    ch = get_most_common(df, 'hour')

    # hour will be the index of the ch frame
    hour = ch.index[0]
    # convert to 12 hour clock
    if hour > 12:
        hour = str(hour - 12) + " PM"
    else:
        hour = str(hour) + " AM"

    # number of bikeshares with be the first value (0,0) of the frame
    shares = ch.iat[0,0]

    msg = "Most popular hour for bikeshares was {}, with {} shares that hour."
    print(msg.format(hour, shares))
    """
    df1 = df[df['hour']>12]
    print(df1[['Start Time', 'hour']])
    """

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station   --------------------------
    ss = get_most_common(df, 'Start Station')

    # Start Station will be the index of the ss frame
    station = ss.index[0]
    # number of trips with be the first value (0,0) of the frame
    trips = ss.iat[0,0]

    msg = "Most popular Starting Station was {}, with {} trips from that station."
    print(msg.format(station, trips))

    # display most commonly used end station   ----------------------------
    es = get_most_common(df, 'End Station')

    # End Station will be the index of the es frame
    station = es.index[0]
    # number of trips with be the first value (0,0) of the frame
    trips = es.iat[0,0]

    msg = "Most popular End Station was {}, with {} trips to that station."
    print(msg.format(station, trips))

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' To ' + df['End Station']
    ct = get_most_common(df, 'Trip')

    # Trip will be the index of the es frame
    trip = 'From ' + ct.index[0]
    # number of trips with be the first value (0,0) of the frame
    trips = ct.iat[0,0]

    msg = "Most popular combination of start station and end station was {}, with {} trips involving those stations."
    print(msg.format(trip, trips))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    ttd = df['Trip Duration'].sum()
    msg = "The total travel time for this data is {}"
    print(msg.format(ttd))

    # display mean travel time
    mtt = df['Trip Duration'].mean()
    msg = "The mean travel duration for this data is {}"
    print(msg.format(mtt))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Here is a list of User Types and counts for each:")
    print((df['User Type'].value_counts()))

    #no gender or birth date data for washington
    if data_city == 'washington':
        print("There is no gender or birth date data for Washington")
    else:
        # Display counts of gender
        print("\nHere is a count of our users by Gender:")
        print((df['Gender'].value_counts()))

        # Display earliest, most recent, and most common year of birth
        eb = df['Birth Year'].min()
        rb = df['Birth Year'].max()
        cb = df['Birth Year'].mean()

        msg = "\nThe earliest year of birth of our users is {}"
        print(msg.format(int(eb)))  # Data issue here - 1899 not possible

        msg = "The most recent year of birth of our users is {}"
        print(msg.format(int(rb)))

        msg = "The most common birth year of our users is {}"
        print(msg.format(int(cb)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        print("Thank you for using my app.")
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
