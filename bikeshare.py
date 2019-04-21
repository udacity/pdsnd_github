import csv
import itertools
import pandas as pd
import time

city_to_file = {'chicago':'chicago.csv','new york':'new_york_city.csv','washington':'washington.csv'}
month_to_index = {'january':1,'february':2,'march':3,'april':4,'may':5,'june:':6}
day_to_index = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5,'sunday':6}
time_range_to_letters = {'month':'M','day':'D','both':'B','none':'N'}

def get_file_name():

    '''Asks the user to enter a city name and returns the corressponding file name to analyze the bike share data from.
    Args:
        None.
    Returns:
        (str) filename for which the bike share data shall be analyzed.
    '''

    city_name = input('Would you like to see data for Chicago, New York, or Washington?\n')
    city_name = city_name.strip().lower()

    while city_name not in list(city_to_file.keys()):
        city_name = input('\nInvalid city name. Please enter a valid city name from the three given options.\n'
            'i.e. Chicago, New York, or Washington\n')
        city_name = city_name.strip().lower()

    return city_name

def get_time_range_filter():

    '''Asks the user to enter a range and returns the respective time range filter.
    Args:
        None.
    Returns:
        (str) month, day, both or none time range to filter the results for.
    '''
    time_range = input('\nWould you like to filter the data by month, day, both or not apply a filter at all? Type'
                       ' "both" to filter by month as well as day and "none" for no time filter.\n')
    time_range = time_range.strip().lower()

    while time_range not in list(time_range_to_letters.keys()):
        time_range = input('\nSorry, the time range entered is not recognized. Please enter a valid time range from the given options.'
                            '\ni.e. month, day, both or no filter at all.\n')
        time_range = time_range.strip().lower()

    return time_range_to_letters.get(time_range)

def get_month_filter():

    '''Asks the user to enter a month and returns the respective month filter.
    Args:
       None.
    Returns:
       (str) month to filter the results for.
    '''
    month = input('\nWhich month you want to filter the data for; January, February, March, April, May, or June?\n')
    month = month.strip().lower()

    while month not in list(month_to_index):
        month = input('\nSorry there is not data for {}.\n Pick a month from January, February, March, April, May, or June?\n'.format(month))
        month = month.strip().lower()

    return month_to_index.get(month)

def get_day():

    '''Asks the user to enter an integer for the day of the week and returns the corressponding day.
    Args:
        None.
    Returns:
        (int) day of the month
    '''
    day = input('\nWhich day? Pick a day from monday, tuesday, wednesday, thursday, friday, saturday, or sunday?\n')
    day = day.strip().lower()

    while day not in list(day_to_index):
        day = input('\nInvalid day {}.\n Pick a day from monday, tuesday, wednesday, thursday, friday, saturday, or sunday.\n'.format(day))
        day = day.strip().lower()

    return day_to_index.get(day)

def get_most_common_month(df):
    '''Finds the most common month in a dataframe.
    Args:
        (dataframe) df, having valid data.
    Returns:
        (str) name of the most common month in the given dataframe.
    '''

    valid_months = list(month_to_index.keys())
    month_index = df['month'].mode()[0]

    return valid_months[month_index-1]

def get_most_common_day(df):
    '''Finds the most common day of the week in a dataframe.
    Args:
        (dataframe) df, having valid data.
    Returns:
        (str) name of the most common day of the week in the given dataframe.
    '''
    valid_days = list(day_to_index.keys())
    day_index = df['day_of_week'].mode()[0]
    return valid_days[day_index]

def get_most_common_hour(df):
    '''Finds the most common hour in a dataframe.
    Args:
        (dataframe) df, having valid data.
    Returns:
        (str) name of the most common hour in the given dataframe.
    '''
    hour_index = df['hour'].mode()[0]

    if hour_index == 0:
        return '12 a.m.'
    elif hour_index == 12:
        return '12 p.m.'
    elif hour_index <= 11:
        return '{} a.m.'.format(hour_index)
    elif hour_index > 12:
        hour_index -= 12
    return '{} p.m.'.format(hour_index)

def get_common_stations(df):
    '''Finds the most common start and end stations in a dataframe.
    Args:
        (dataframe) df, having valid data.
    Returns:
        (tuple(str,str)) names of the most common start and end stations respectively.
    '''
    common_start = df['Start Station'].mode()[0]
    common_end = df['End Station'].mode()[0]
    return(common_start, common_end)

def get_common_trip(df):
    '''Finds the most common trip in a dataframe.
    Args:
        (dataframe) df, having valid data.
    Returns:
        (str) the most common trip route in the given dataframe.
    '''
    get_common_trip = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().idxmax()
    return get_common_trip

def get_trip_duration(df):
    '''Calculates total and average trip duration in a dataframe.
    Args:
        (dataframe) df, having valid data.
    Returns:
        (tuple(float,float)) total and average trip duration in hours for the given dataframe.
    '''
    total_trip_duration = df['Trip Duration'].sum()
    avg_trip_duration = df['Trip Duration'].mean()

    total_hours = total_trip_duration / 3600.00
    avg_hours = avg_trip_duration / 60.00

    return (total_hours, avg_hours)

def get_birth_years(df):
    '''Finds the earliest (oldest user), most recent (youngest user) and most common birth year in a dataframe.
    Args:
        (dataframe) df, having valid data.
    Returns:
        (tuple (int, int, int)) the most common, oldest and youngest birth years respectively.
    '''
    df_birth_years = df['Birth Year']
    most_common_year = str(int(df_birth_years.mode()[0]))
    youngest = str(int(df_birth_years.max()))
    oldest = str(int(df_birth_years.min()))

    return (most_common_year, oldest, youngest)

def print_column_count(df,column_name):
    '''Prints the count for each unique value present in the column of a dataframe.
    Args:
        (dataframe) df, having valid data.
        (str) column_name, name of the column for which the count of each type should be returned.
    Returns:
        Nothing
    '''
    types = df[column_name].value_counts().index.tolist()
    values = df[column_name].value_counts().values.tolist()

    print('Here is the count for all unique values in {}'.format(column_name))
    for i in range(0,len(types)):
        print("{} ---> {}".format(types[i],values[i]))
    print("\n")

def get_filters():
    """Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (int) month - respective digit of the month to filter by, or -1 to apply no month filter
        (int) day - respective digit of the day of week to filter by, or -1 to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_file_name()

    time_range = get_time_range_filter()
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    if time_range == 'M':
        month = get_month_filter()
        day= -1
    elif time_range == 'D':
         day = get_day()
         month = -1
    elif time_range == 'B':
        month = get_month_filter()
        day = get_day()
    elif time_range == 'N':
        month = -1
        day = -1

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    '''Loads data from respective csv file into a dataframe and applies month or day filter to it.
    Args:
        (str) city - name of the city to analyze.
        (int) month - respective digit of the month to filter by.
        (int) day - respective digit of the day of week to filter by.
    Returns:
        (dataframe) dataframe with applied filters and city data.
    '''

    # load data file into pandas dataframe
    df = pd.read_csv(city_to_file.get(city))

    # convert the Start Time to a dataframe
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
    df['day'] = df['Start Time'].dt.day

    # filter df by month/day/both or none
    if month != -1 and day == -1:
        df = df[df['month'] == month]
    elif day != -1 and month == -1:
        df = df[df['day_of_week'] == day]
    elif month != -1 and day != -1:
        df = df[df['month'] == month]
        df = df[df['day_of_week'] == day]

    return df

def display_raw_data(city):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        (str) city, for which raw data is required.
    Returns:
        raw data.
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    display = display.strip().lower()

    inputs = ['yes','no']

    while display not in inputs:
        print("I don't understand that.")
        display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
        display = display.strip().lower()

    # used for slicing the raw data to 5 rows.
    start = 1
    end = 6

    while display == 'yes':
        with open(city_to_file.get(city), newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in itertools.islice(reader, start, end):
                print(row)
                start +=5
                end +=5
        display = input('\nWould you like to continue to view individual trip data?\n'
                    'Type \'yes\' or \'no\'.\n')
        display = display.strip().lower()
        while display not in inputs:
            print("I don't understand that.")
            display = input('\nWould you like to continue to view individual trip data?\n'
                    'Type \'yes\' or \'no\'.\n')
            display = display.strip().lower()

def time_stats(df):
    """Displays statistics on the most frequent    times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    get_most_common_month(df)

    # display the most common day of week
    get_most_common_day(df)

    # display the most common start hour
    get_most_common_hour(df)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most common stations and trip."""

    print('\nCalculating The Most common Stations and Trip...\n')
    start_time = time.time()
    stations = get_common_stations(df)

    # display most commonly used start station
    print("The most commonly used start station is {}.\n".format(stations[0]))

    # display most commonly used end station
    print("The most commonly used end station is {}.\n".format(stations[1]))

    # display most frequent combination of start station and end station trip
    trip = get_common_trip(df)
    print("The most frequent combination of start station and end station trip is from {} to {}.\n".format(trip[0],trip[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    durations = get_trip_duration(df)

    # display total travel time
    print('The total duration is {} hours.\n'.format(durations[0]))

    # display mean travel time
    print('The mean travel duration is {} minutes.\n'.format(durations[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print_column_count(df,'User Type')

    # because washington.csv does not have gender and birth year
    if city != 'washington':
        # counts of each gender
        print_column_count(df,'Gender')

        # most popular birth years
        years = get_birth_years(df)
        print("The most common birth year is {}.\nThe oldest rider was born in the year {}.\nThe youngest rider was born in the year {}.".format(years[0],years[1],years[2]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
