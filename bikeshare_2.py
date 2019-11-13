import time
import pandas as pd


CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAYS_OF_WEEK = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' 'sunday']


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
    city = input("\nPlease enter a city name (options are: chicago, new york city and washington):\n").lower()
    while city not in CITY_DATA.keys():
        city = input("\nPlease enter a city name (options are: chicago, new york city and washington):\n").lower()

    # get user input for month (all, january, february, ... , june)
    month = input("\nPlease enter a month name (choose between january to june or all for no month):\n").lower()
    while month not in MONTHS:
        month = input("\nPlease enter a month name (choose between january to june or all for no month):\n").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nPlease enter a day name (choose between monday to sunday or all for no day):\n").lower()
    while day not in DAYS_OF_WEEK:
        day = input("\nPlease enter a day name (choose between monday to sunday or all for no day):\n").lower()

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

    # load csv file
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime data type
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracting month and day_of_week and adding columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        month_index = MONTHS.index(month)
        df = df[df['month'] == month_index]

    # filter by day of week if applicable and save the new dataframe
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def display_raw_data(df):
    """Display the five first rows if the user wants by answering yes to the main question"""

    show = 5
    assertion = input("\nWould you like to see 5 rows from the raw data (answer must be yes or no)?\n").lower()

    while assertion not in ('yes', 'no'):
        assertion = input("\nWould you like to see 5 rows from the raw data (answer must be yes or no)?\n").lower()

    while True:
        if assertion == 'no':
            break
        else:
            print(df.head(5))
            break

    if assertion == 'yes':
        assertion_2 = input("\nWould you like to see more 5 rows (answer must be yes or no)?\n").lower()

        while assertion_2 not in ('yes', 'no'):
            assertion_2 = input("\nWould you like to see more 5 rows (answer must be yes or no)?\n").lower()

        while True:
            if assertion_2 == 'no':
                break
            else:
                show += 5
                print(df.head(show))
                assertion_2 = input("\nWould you like to see more 5 rows (answer must be yes or no)?\n").lower()

    print('-' * 40)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime data type
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracting month and day_of_week and starting hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour

    # display the most common month
    most_common_month = df['month'].mode().tolist()[0]
    print("The most common month is: {}".format(MONTHS[most_common_month].capitalize()))

    # display the most common day of week
    most_common_week = df['day_of_week'].mode().tolist()[0]
    print("The most common day of week is: {}".format(most_common_week))

    # display the most common start hour
    most_common_hour = df['start_hour'].mode().tolist()[0]
    print("The most common starting hour is: {}h".format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start_station = df['Start Station'].mode().tolist()[0]
    print("The most common used start Station is: {}".format(most_used_start_station.title()))

    # display most commonly used end station
    most_used_end_station = df['End Station'].mode().tolist()[0]
    print("The most common used end Station is: {}".format(most_used_end_station.title()))

    # create station_combination column to store from start station to end station data
    df['station_combination'] = df['Start Station'].str.cat(df['End Station'], sep=' -> ')

    # display most frequent combination of start station and end station trip
    most_used_combination = df['station_combination'].mode().tolist()[0]
    print("The most common used combination Stations is: {}".format(most_used_combination.title()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum(skipna=True)
    print("The total travel time is: {}".format(total_travel_time))

    # display mean travel time
    travel_time_mean = df['Trip Duration'].mean(skipna=True)
    print("The overall travel time mean is: {}".format(travel_time_mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts(dropna=True)
    print(user_types_count)

    if city != 'washington':
        # Display counts of gender
        genders_count = df['Gender'].value_counts(dropna=True)
        print("\n", genders_count)

        # Display earliest, most recent, and most common year of birth
        most_common_birth_year = df['Birth Year'].mode()[0]
        most_recent_birth_year = df['Birth Year'].max()
        earliest_birth_year = df['Birth Year'].min()

        print("\nThe most common birth year is: {}".format(most_common_birth_year))
        print("The most recent birth year is: {}".format(most_recent_birth_year))
        print("The earliest birth year is: {}".format(earliest_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city=city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

