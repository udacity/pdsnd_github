import time
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

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

    Validations:
        -Asks user to input which city data he/she would like to analyze
          -Keeps validating the input for valid city Chicago or New York City or washington
          -If wrong city is entered, error is prompted to enter valid city until correct city is entered
        -Asks user to input which month data he/she would like to analyze
         -Keeps validating the input for valid month January, February, March,April,May,june
         -If wrong month is entered, error is prompted to enter valid month
        -Asks user to input which day of the week he/she would like to analyze
         -Keeps validating the input for valid day of the week Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
         -If wrong day of the week is entered, error is prompted to enter valid day of the week until correct city is entered

    """
    print()
    print('Hello! Let\'s explore some US bikeshare data!')
    print()

    while True:
        # get user input for city (chicago, new york city, washington).
        city = input('\nWhich city\'s data would you like to analyze? Please enter Chicago or New York City or Washington\n')

        try:
            #Strip the before and after white spaces from the city entered
            if city.lower().lstrip().rstrip() not in ('chicago','new york city','washington'):
                print('Please enter valid city. Chicago or New York City or Washington\n')
            else:
                break
        except ValuError:
            print('Value Error')
        except KeyboardInterrupt:
            print("Pressed Control key")
            break

    #return the city entered after converting it to lower case and stripping before and after whitespaces
    city = city.lower().lstrip().rstrip()



    while True:

        # get user input for month (all, january, february, ... , june)

        month = input('\nWould you like to analyze data by month? Please enter January, February, March, April, May, June OR all for no time filter\n')

        try:
            #Strip the before and after white spaces from the month entered
            if month.lower().lstrip().rstrip() not in ('all','january','february', 'march','april','may','june'):
                print('Please enter valid month OR all for no month filter\n')
            else:
                break
        except ValuError:
            print('Value Error')
        except KeyboardInterrupt:
            print("Pressed Control key")
            break

    #return the month entered after converting it to lower case and stripping before and after whitespaces
    month = month.lower().lstrip().rstrip()


    while True:
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('\nWould you like to analyze data by day of week? Please enter Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday OR all for no day filter \n')

        try:
            #Strip the before and after white spaces from the day of the week entered
            if day.lower().lstrip().rstrip() not in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
                print('Please enter valid day of the week or all for no day filter\n')
            else:
                break
        except ValuError:
            print('Value Error')
        except KeyboardInterrupt:
            print("Pressed Control key")

    #return the day of the week entered after converting it to lower case and stripping before and after whitespaces
    day = day.lower().lstrip().rstrip()

    print('-'*100)
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

    Validations:
       -Check if the file for requested city is found, if not print error message
       -If file is present, creates DataFrame with specified city and filters by month and day if applicable
    """
    try:
        df = pd.read_csv(CITY_DATA[city])
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        df['day'] = df['Start Time'].dt.weekday_name

        if month != 'all':
            months = ['january','february','march','april','may','june']
            month = months.index(month) + 1
            df = df[df['month'] == month]

        if day != 'all':
            df = df[df['day'] == day.title()]

    except FileNotFoundError:
        print('Data file {} not found'.format(CITY_DATA[city]))
        df = pd.DataFrame()

    return df


def time_stats(df):

    """Displays statistics on the most frequent times of travel.

    Args:
        (df) -Pandas DataFrame containing city data filtered by month and day
    Returns:
        Nothing
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = (df['month']).mode()[0]
    months = ['January','February','March','April','May','June']

    print("\nThe most common month of travel is:", months[common_month-1])

    # display the most common day of week
    common_day = (df['day']).mode()[0]
    print("\nThe most common day of week for travel is:", common_day)

    # display the most common start hour
    common_hour = (df['Start Time'].dt.hour).mode()[0]
    print('\nThe most common start hour for travel is: {} hours'.format(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (df) -Pandas DataFrame containing city data filtered by month and day
    Returns:
        Nothing
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    common_start_station = (df['Start Station']).mode()[0]
    print('\nThe most common start station of travel is:', common_start_station)

    # display most commonly used end station
    common_end_station = (df['End Station']).mode()[0]
    print("\nThe most common end station of travel is:", common_end_station)

    # display most frequent combination of start station and end station trip

    df['Trip Station'] = df['Start Station'] + '-' +  df['End Station']
    common_trip = (df['Trip Station']).mode()[0]
    print('\nThe most common trip of travel between Start Station and End Station is:')
    print(common_trip.split('-'))

    #display the maximum duration for the most frequent combination of start station and end station trip
    common_trip_max = df.groupby(['Trip Station'])['Trip Duration'].max()

    if common_trip in common_trip_max:
        duration_max = common_trip_max[common_trip]
        print('\nThe maximum duration for the most common trip is:',duration_max)

    #display the maximum duration for the most frequent combination of start station and end station trip
    common_trip_min = df.groupby(['Trip Station'])['Trip Duration'].min()

    if common_trip in common_trip_min:
        duration_min = common_trip_min[common_trip]
        print('\nThe minimum duration for the most common trip is:',duration_min)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (df) -Pandas DataFrame containing city data filtered by month and day
    Returns:
        Nothing
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_duration_sum = df['Trip Duration'].sum()
    print('\nTotal Travel Time is:',trip_duration_sum)

    # display mean travel time
    trip_duration_mean = df['Trip Duration'].mean()
    print('\nAverage Travel Time is:', trip_duration_mean)

    # display longest duration of the trip
    trip_longest_duration = df['Trip Duration'].max()
    print('\nThe longest duration of all the trip is:', trip_longest_duration)

    # display shortest duration of the trip
    trip_shortest_duration = df['Trip Duration'].min()
    print('\nThe shortest duration of all the trip is:', trip_shortest_duration)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def user_stats(df):
    """Displays statistics on bikeshare users.
    Args:
        (df) -Pandas DataFrame containing city data filtered by month and day
    Returns:
        Nothing
    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('\nThe counts of user types:')
    print(user_types_count)


    # Display counts of gender
    # washington.csv file does not have gender and birth year column, so need to check for KeyError

    try:
        user_gender_count = df['Gender'].value_counts()
        print('\nThe counts of user gender types:')
        print(user_gender_count)
    except KeyError:
        print('\nThere is no Gender data.')

    # Display earliest, most recent, and most common year of birth

    try:
        earliest_birth_year = int(df['Birth Year'].min())
        print('\nThe earliest birth year:',earliest_birth_year)

        recent_birth_year = int(df['Birth Year'].max())
        print('\nThe most recent birth year:',recent_birth_year)

        common_birth_year = int(df['Birth Year'].mode()[0])
        print('\nThe most common year of birth:',common_birth_year)

        #display the total trips by earliest birth year
        trip_by_year = df['Birth Year'].value_counts()
        print('\nThe counts of trip by Birth Year:')
        print(trip_by_year)

    except KeyError:
        print('\nThere is no Birth Year data.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)

def print_data(df):
    """ Displays Data from the the DataFrame

    Args:
        (df) -Pandas DataFrame containing city data filtered by month and day
    Returns:
        Nothing

    Validations:
      - Asks User if they need to see raw data. If User enters 'yes' or presses Enter' 5 rows of data is displayed at a time.
      - Continues these prompts and displays until the user says 'no'.

    """

    n = 0

    raw_data = input('\nWould you like to see data? Press enter or type yes to display data OR type no to skip data display.\n')
    while True:

        if raw_data.lower().lstrip().rstrip() == 'no':
            break
        else:
            df_next = df.iloc[n: n+5]
            if df_next.empty:
                print('There is no more data to display')
                break
            else:
                print(df_next)
                n+=5
                raw_data = input('\nWould you like to see next 5 rows of data? Press enter or type yes to display data OR type no to skip data display.\n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        #Check if the DataFrame contains data for the specified city, month and day
        
        if df.empty:
            print('There is no data for combination of city: {}, month: {}, day: {}'.format(city,month,day))
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            print_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower().lstrip().rstrip() == 'no':
            break


if __name__ == "__main__":
	main()
