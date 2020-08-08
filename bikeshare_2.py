import time
import pandas as pd
import datetime

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or
                      "all" to apply no month filter
        (str) day - name of the day of week to filter by, or
                    "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Select a city to explore the bike share data. ' +
                     'Chicago, New York City, or Washington?\n')
        if city.lower() in CITY_DATA.keys():
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Specify the month of data to explore. All, January ' +
                      'February, March, April, May, or June?\n')
        if month.lower() in ['all', 'january', 'february', 'march',
                             'april', 'may', 'june']:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Specify the day of data to explore. ' +
                    'All, Monday, Tuesday, Wednesday, Thursday, Friday, ' +
                    'Saturday, Sunday?\n')
        if day.lower() in ['all', 'monday', 'tuesday', 'wednesday', 'thursday',
                           'friday', 'saturday', 'sunday']:
            break

    print('-'*50)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month
    and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all"
                      to apply no month filter
        (str) day - name of the day of week to filter by, or "all"
                    to apply no day filter
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

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # display the most common month
    print('\nMost Common Month of Travel:')
    print(df['month'].mode()[0])

    # display the most common day of week
    print('\nMost Common Day of Travel:')
    print(df['day_of_week'].mode()[0])

    # display the most common start hour
    print('\nMost Common Start Hour of Travel:')
    print(df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # display most commonly used start station
    print('\nMost Common Start Station:')
    print(df['Start Station'].mode()[0])

    # display most commonly used end station
    print('\nMost Common End Station:')
    print(df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print('\nMost Frequency Start & Stop Combination')
    print(df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...')
    start_time = time.time()

    # display total travel time
    print('\nTotal Travel Time:')
    print(datetime.timedelta(seconds=int(df['Trip Duration'].sum())))

    # display mean travel time
    print('\nMean Travel Time:')
    print(datetime.timedelta(seconds=int(df['Trip Duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...')
    start_time = time.time()

    # Display counts of user types
    print('Counts of User Types:')
    print(df['User Type'].value_counts())

    # Display counts of gender
    print('\nCounts of Genders:')
    try:
        print(df['Gender'].value_counts())
    except:
        print('Data does not include genders')

    # Display earliest, most recent, and most common year of birth
    print('\nEarliest, Latest & Most Common Date of Birth:')
    try:
        print('Earliest: {}\nLatest: {}\nMost Common: {}'
              .format(df['Birth Year'].min(), df['Birth Year'].max(),
                      df['Birth Year'].mode()[0]))
    except:
        print('Data does not include date of birth')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_data(df):
    """
    Iterate through 5 entries at a time.

    Returns:
        Print five row entries of data to terminal
    """

    show_more = 'yes'
    while show_more == 'yes':
        for i in df.iterrows():
            count = 0
            while count < 5:
                print(i)
                count += 1
            response = input('\nView 5 more data entries? Yes or No?\n')
            if response.lower() == 'no':
                show_more = 'no'
                break


def main():
    """Main body of program"""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Yes or No?\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
