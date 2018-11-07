import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# list of months and their associated index values to drive computation logic
LIST_OF_MONTHS = {
                    'january': 1, 
                    'february': 2, 
                    'march': 3, 
                    'april': 4, 
                    'may': 5, 
                    'june': 6, 
                    'july': 7, 
                    'august': 8, 
                    'september': 9, 
                    'october': 10, 
                    'november': 11, 
                    'december': 12, 
                    'all': 0
                }

# list of days and their associated index values to drive computation logic
LIST_OF_DAYS = {
                'monday' : 1, 
                'tuesday': 2, 
                'wednesday': 3, 
                'thursday': 4, 
                'friday': 5, 
                'saturday': 6, 
                'sunday': 7, 
                'all': 0
                }

FILE_EXT = '.csv'

""" Allows us to enter a city, month, or day. Each of these inputs will be trimmed and lowered to match the keys in the dictionary.
    The values will be used for computation. 
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    print('Here are a list of valid cities: ', ', '.join(CITY_DATA.keys()))
    city = input('Enter a valid city to get data from: ')
    city = city.lower().strip()
    while city not in CITY_DATA.keys():
        city = input('Uh Oh! Your city choice was invalid... Choose between the valid cities: ')
        city = city.lower().strip()
    
    # get user input for month (all, january, february, ... , june)

    print('Here are a list of valid months: ', ', '.join(LIST_OF_MONTHS.keys()))
    month = input('Enter a month or all: ')
    month = month.lower().strip()
    while month not in LIST_OF_MONTHS.keys():
        month = input('Uh Oh! Your choice of months was invalid, Choose between a valid month: ')
        month = month.lower().strip()

    # # get user input for day of week (all, monday, tuesday, ... sunday)
    print('Here are a list of valid days: ', ', '.join(LIST_OF_DAYS.keys()))
    day = input('Enter a day or all: ')
    day = day.lower().strip()
    while day not in LIST_OF_DAYS.keys():
        day = input('Uh Oh! Your choice of days was invalid, Choose a valid day: ')
        day = day.lower().strip()
    
    print('-'*40)
    return city, month, day

""" given a city name, we load the data for the city... since we can have cities separated by space, we are expecting the file name to be separated by underscores. 
INPUT: 
city: for now we have data for new york city, washington, and chicago.
month: The month to gather stats off of. All is optional to gather stats from all the months.
day: The day to gather stats off of. All is optional to gather stats from all the days.
OUTPUT:
Df: the data frame to compute the stats off of.
"""
def load_data(city, month, day):
    file_name = city.replace(' ', '_') # match file name :D
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv('{0}.csv'.format(file_name))
    if month == 'all' and day == 'all':
        # no filters applied so we just return the loaded data frame
        return df

    elif month == 'all' and day != 'all':
        # filter by day
        dayIndex = LIST_OF_DAYS[day]
        filteredDataByDay = filter_by_day(df, 'Start Time', dayIndex)
        return filteredDataByDay

    elif month != 'all' and day == 'all':
        # filter by month 
        numMonth = LIST_OF_MONTHS[month]
        filteredDataByMonth = filter_df_by_month(df, 'Start Time', numMonth)
        return filteredDataByMonth

    else: 
        #filter by month and day
        dayIndex = LIST_OF_DAYS[day]
        numMonth = LIST_OF_MONTHS[month]
        filteredDataByMonth = filter_df_by_month(df, 'Start Time', numMonth)
        month_day_filter = filter_by_day(filteredDataByMonth, 'Start Time', dayIndex)
        return month_day_filter
    
""" Calculates the most frequent time of travel for: month, day of week, and start hour

INPUT: 
df - DataFrame to collect stats off of.
"""

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    propName = 'Start Time'
    # all of the stats below are calculated off of the Start Time index.
    # check to see if that index exists before computing stats
    if propName in df.columns: 
        df[propName] = pd.to_datetime(df[propName])

        # find the month, day of week and calculate mode
        df['month'] = df[propName].dt.month
        df['weekday'] = df[propName].dt.dayofweek + 1 # day of week is 0 indexed
        df['start hour'] = df[propName].dt.hour
        # display the most common month
        commonMonthIndex = df['month'].mode().iloc[0]
        print('MOST COMMON MONTH FROM THE REQUESTED DATA: ')
        print_dict_key_given_value(LIST_OF_MONTHS, commonMonthIndex)

        # display the most common day of week 
        print('MOST COMMON DAY OF THE WEEK FROM THE REQUESTED DATA: ')
        commmonDayOfWeekIndex = df['weekday'].mode().iloc[0]
        print_dict_key_given_value(LIST_OF_DAYS, commmonDayOfWeekIndex)

        # display the most common start hour

        print('MOST COMMON START HOUR FROM THE REQUESTED DATA: ')
        print(df['start hour'].mode().iloc[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

""" Calculates the most popular station: start, end, and most common combination of start and end. 
INPUT: 
df - DataFrame to collect stats off of.
"""

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    startStationIndex = 'Start Station'
    endStationIndex = 'End Station'
    startEndCombIndex = 'Start And End Station'
    
    if startStationIndex in df.columns:
        # display most commonly used start station 
        print('The most commonly used start station is: ')
        print(df[startStationIndex].mode().iloc[0])

    # display most commonly used end station
    if endStationIndex in df.columns:
        print('The most commonly used end station is: ')
        print(df[endStationIndex].mode().iloc[0])
    
    if (endStationIndex in df.columns) and (startStationIndex in df.columns):
        # display most frequent combination of start station and end station trip
        print('The most common start and end station is: ')
        df[startEndCombIndex] = 'FROM: ' + df[startStationIndex] + ' TO: ' + df[endStationIndex]
        print(df[startEndCombIndex].mode().iloc[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

""" Display trip duration stats for a dataframe. The trip duration stats include total time travelled in seconds and average time travelled in seconds
INPUT: 
df - DataFrame to collect stats off of.
"""

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    tripDurationIndex = 'Trip Duration'
    # display total travel time
    if tripDurationIndex in df.columns:
        totalTimeTravelledInSeconds = df[tripDurationIndex].sum()
        print('TOTAL TRAVEL TIME IN SECONDS: ' + str(totalTimeTravelledInSeconds))

    # display mean travel time
        avgTravelTime = df[tripDurationIndex].mean()
        print('AVERAGE TRAVEL TIME IN SECONDS: ' + str(avgTravelTime))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

""" Displays the following user statistics:
    Counts of each type of user
    Counts of each type of gender
INPUT: 
df: DataFrame to collect user data off of.
"""

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('HERE ARE THE COUNTS FOR EACH TYPE OF USER: ')
    indexName = 'User Type' # check if index exists.
    if indexName in df.columns:
        print(df[indexName].value_counts())

    # Display counts of gender
    print('HERE ARE THE COUNTS FOR EACH TYPE OF GENDER: ')
    indexName = 'Gender' # check if index exists 
    if indexName in df.columns:
        print(df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    print('HERE ARE THE MOST COMMON, MOST RECENT, AND EARLIEST BIRTH YEARS')
    
    birthYearIndex = 'Birth Year'

    if birthYearIndex in df.columns:
        sortedBirthYear = df.sort_values(birthYearIndex)
        print('Earliest Birth Year: ')
        print(sortedBirthYear[birthYearIndex].iloc[0])

        print('Most Recent Birth Year: ')
        print(sortedBirthYear.loc[sortedBirthYear[birthYearIndex].notnull()][birthYearIndex].iloc[-1])

        print('Most Common Birth Year: ')
        print(sortedBirthYear[birthYearIndex].mode().iloc[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# ----- util functions 


""" given a certain value and a dictionary
    this function prints out all the keys tied to that value
INPUT:
dictionary: dictionary that holds the key and value
targetValue: value that we need to look up to find the key.
"""

def print_dict_key_given_value(dictionary, targetValue):
     for key, value in dictionary.items():
        if value == targetValue:
            print(key)


""" Allows us to filter a dataframe by a property name which contains a date time as string, by a specific day index (indexed from 1 -> 7)
INPUT:
df : DataFrame used as the collection of data we need.
propName: index in the data frame
dayIndex: index of the day that we're looking for 1.. Monday, 2.. Tuesday, etc.
OUTPUT:
dayFilter: DataFrame filtered by day.
"""

def filter_by_day(df, propName, dayIndex):
    df[propName] = pd.to_datetime(df[propName])
    dayFilter = df[df[propName].dt.dayofweek + 1 == dayIndex]
    return dayFilter


""" Allows us to filter a data frame by a property name which contains a date time as a string. We filter this data frame by a specific month index.
INPUT:
df : DataFrame used as the collection of data we need.
propName: index in the data frame
monthindex: index of the day that we're looking for 1.. January, 2.. February, etc.
OUTPUT:
monthFilter: DataFrame filtered by the month index.
"""

def filter_df_by_month(df, propName, monthIndex):
    df[propName] = pd.to_datetime(df[propName])
    monthFilter = df[df[propName].dt.month == monthIndex]
    return monthFilter



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df.empty:
            print('Uh Oh! There is no data for {0} on {1} the month of {2}'.format(city, day, month))
        else: 
            copyDF = df.copy() # copying so that I can modify the copy instead of the original object.
            time_stats(copyDF)
            station_stats(copyDF)
            trip_duration_stats(copyDF)
            user_stats(copyDF)

            rawDataRequested = input('\n Would you like to see the first 5 entires in the data set? Enter yes or no. \n')
            rowStartIndex = 0 #starts at 0 and prints every 5 rows upon users request
            while rawDataRequested.lower().strip() == 'yes':
                print(df[rowStartIndex:rowStartIndex + 5])
                rowStartIndex = rowStartIndex + 5
                rawDataRequested = input('\n Would you like to see the next 5 entires in the data set? Enter yes or no. \n')
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
