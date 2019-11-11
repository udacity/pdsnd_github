import time
import pandas as pd
import numpy as np

##Adding Data
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

# List for accepted month values and day of the week values.
accepted_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
accepted_days_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']


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
    city = input('Enter the city name to analyze:')
    while city.lower() not in CITY_DATA:
        print('Not a recognized city. Please check.')
        city = input('Enter the city name to analyze:')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter the month name (from January until June) or enter 'all' to analyze:")
    while month.lower() not in accepted_months:
        print('Not a recognized month value.')
        month = input(
            "Enter the correct month to analyze (from January until June) or enter 'all' to analyze everything:")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the name of the day of the week or enter 'all' to analyze:")
    while day.lower() not in accepted_days_week:
        print('Not a recognized day of the week. Please check.')
        day = input(
            "Enter the correct day of the week to analyze (between Sunday until Saturday) or enter 'all' to analyze everything:")

    print('-' * 40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    try:
        # load data file into a dataframe and parse the 'Start Time' column.
        df = pd.read_csv(CITY_DATA[city], parse_dates=['Start Time'])

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

    except ValueError as e:
        print(e.args)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    try:
        # TO DO: display the most common month
        print('Most frequent month is ', df['month'].value_counts().idxmax())

        # TO DO: display the most common day of week
        print('Most frequent day of the week is ', df['day_of_week'].value_counts().idxmax())

        # TO DO: display the most common start hour
        print('Most frequent start hour is ', df['Start Time'].dt.hour.value_counts().idxmax())

    except ValueError as e:
        print(e.args)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    try:
        # TO DO: display most commonly used start station
        print('Most common start station is ', df['Start Station'].value_counts().idxmax())

        # TO DO: display most commonly used end station
        print('Most common end station is ', df['End Station'].value_counts().idxmax())

        # TO DO: display most frequent combination of start station and end station trip
        print('Most common combinations of stations are ', df.groupby(['Start Station', 'End Station']).size().idxmax())
    except Exception as e:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    try:
        # TO DO: display total travel time
        print('Total travel time is ', sum(df['Trip Duration']))

        # TO DO: display mean travel time
        print('Mean travel time is ', df.loc[:, "Trip Duration"].mean())
    except ValueError as e:
        print(e.args)
    except Exception as e:
        print(e.args)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
        # TO DO: Display counts of user types
        print('User Type Data -> ', df['User Type'].value_counts())

        # TO DO: Display counts of gender

        print('Gender Type Stats -> ', df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth

        print('Earlier Birth Year, Most recent Birth Year, Most common Birth Year -> ', df['Birth Year'].min(),
              df['Birth Year'].max(), df['Birth Year'].value_counts().idxmax())
    except KeyError as e:
        print(e.args)
    except Exception as e:
        print(e.args)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_raw_data(df):
    """
        Displays filtered data - 5 rows at a time depending on user input.

        Args:
            (str) df - pandas DataFrame with the filtered data (filtered in the load_data method).
    """
    display5=True
    start=0
    end=5
    while display5:
        display5 = input('\nWould you like to print 5 rows of the spreadsheet? Enter yes or no.\n')
        while display5.lower() not in ['yes', 'no']:
            display5 = input('\nPlease enter either yes or no.Would you like to print 5 rows of the spreadsheet? Enter yes or no.\n')
        if display5.lower() != 'yes':
            break
        print(df[start:end])
        start+=5
        end+=5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
