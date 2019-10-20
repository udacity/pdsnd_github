import time
import pandas as pd
import numpy as np


#filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def pick_city():
    '''Asks the user to request city and return
    that city's bike share data.
    Args:
        none.
    Returns:
        (str) Display city's bikeshare data.
    '''
    
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 '\nWould you like to see data for Chicago (CH), New York (NY), or Washington (WA)?\n')



    city = city.lower()

    while True:
        if city == "ny" or city == "new york":
            print('\nYou requested New York City! We\'re going to explore NY bikeshare data\n')
            return new_york_city
        if city == "ch" or city == "chicago":
            print('\nYou requested Chicago! We\'re going to explore CH bikeshare data\n')
            return chicago
        elif city == "wa" or city == "washington":
            print('\nYou requested Washington! We\'re going to explore WA bikeshare data\n')
            return washington
        city = input("Please pick cities between Chicago (CH), New York (NY), or Washington (WA)")
        city = city.lower()


def pick_time_period():
    '''Asks the user to request a time period and returns the info.
    Args:
        none.
    Returns:
        (str) Time period information.
    '''

    time_period = input('\nWould you like to view the data by month (m) , day of the week (d), or not at all? Type "none" for no time filter.\n')

    time_period = time_period.lower()

    while True:
        if time_period == 'm' or time_period == "month":

            while True:
                filterByDayOfMonth = input("\n Do you wish to view by day of the month too? Type 'YES' or 'NO'\n").lower()

                if filterByDayOfMonth == "no":
                    print('\n We are viewing data by month...\n')

                    return 'month'

                elif filterByDayOfMonth == "yes":
                   print ('\n We are viewing data by month and day of the month...\n')
                   return 'day_of_month'

        if time_period == "d" or time_period == "day":
            print('\n We are viewing data by day of the week...\n')
            return 'day_of_week'
        elif time_period == "none" or time_period == "n":


            return "none"
        time_period = input("\n Please request a time between month (M), day of the week (d), or none (n) \n").lower()

# get user input for month (all, january, february, ... , june)
def pick_month(month_):
    '''Asks the user to request a month and returns the info.
    Args:
        month_ - the output from pick_time_period()
    Returns:
        (str) Month information.
    '''
    if month_ == 'month':

        month = input('\nWhich month? January, February, March, April, May, or June? Please type the full month name.\n')
        while month.strip().lower() not in ['january', 'february', 'march', 'april', 'may', 'june']:
            month = input('\nPlease pick between January, February, March, April, May, or June? Please type the full month name.\n')
        return month.strip().lower()
    else:
        return 'none'

def day_of_month(df, dayOfMonth_):
    """Asks the user to request a month and a day of month, and return info for both
    Args:
        dayOfMonth_ - the ouput of pick_time_period()
        df - the dataframe with all bikedata
    Returns:
        list with Month and day information
    """
    monthAndDay = []

    if dayOfMonth_ == "day_of_month":

        month = pick_month("month")
        monthAndDay.append(month)

        maxDayOfMonth = max_day_of_month(df, month)

        while (True):

            promptString = """\n Which day of the month? \n
            Please type  response as an integer between 1 and """


            promptString  = promptString + str(maxDayOfMonth) + "\n"

            dayOfMonth = input(promptString)

            try:

                dayOfMonth = int(dayOfMonth)

                if 1 <= dayOfMonth <= maxDayOfMonth:
                    monthAndDay.append(dayOfMonth)
                    return monthAndDay

            except ValueError:

                print("That's not an integer")

    else:
        return 'none'

#  get user input for day of week (all, monday, tuesday, ... sunday)

def pick_day(day_):
    '''Asks the user to request a day and returns the info.
    Args:
        day_ - string - should data be viewed by day
    Returns:
        (str) Day information.
    '''
    if day_ == 'day_of_week':
        day = input('\nWhich day of the week? Please type a day M, Tu, W, Th, F, Sa, Su. \n')
        while day.lower().strip() not in ['m', 'tu', 'w', 'th', 'f', 'sa', 'su']:
            day = input('\nPlease pick a day from M, Tu, W, Th, F, Sa, Su. \n')
        return day.lower().strip()
    else:
        return 'none'


def load_data(city):
    """
    Reads the city file name and loads it to a dataframe
    INPUT:
    city - path to the file as a string
    OUTPUT:
    df - dataframe to be used to calculate all stats
    """
    print('\nLoading the data...\n')
    df = pd.read_csv(city)

    #add datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #add auxiliary columns

    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    df["day_of_month"] = df["Start Time"].dt.day

    return df

def apply_time_filters(df, time_period, month, dayOfWeek, monthAndDay):
    '''
    Filters the data according to the criteria specified by the user.
    INPUT:
    df           - city dataframe
    time_period  - string indicating the specified time period (either "month", "day_of_month", or "day_of_week")
    month        - string indicating the month used to filter the data
    dayOfWeek    - string indicating the week day used to filter the data
    dayOfMonth   - list indicating the month (at index [0]) used to filter the data
                    and the day number (at index [1])
    OUTPUT:
    df - dataframe to be used to calculate all aggregates that is filtered according to
         the specified time period
    '''


    print('Data loaded. Now computing stats... \n')

    if time_period == 'month':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]


    if time_period == 'day_of_week':
        days = ['Monday', 'Tuesday',
        'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday']
        for d in days:
            if dayOfWeek.capitalize() in d:
                day_of_week = d
        df = df[df['day_of_week'] == day_of_week]

    if time_period == "day_of_month":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = monthAndDay[0]
        month = months.index(month) + 1
        df = df[df['month']==month]
        day = monthAndDay[1]
        df = df[df['day_of_month'] == day]

    return df

 #  display the most common month
def popular_month(df):
    '''What is the most popular month for start time?
    INPUT:
        df - dataframe returned from apply_time_filters
    OUTPUT:
        most_popular_month - string of most frequent month
    '''
    print('\n * What is the most popular month for bikeshare traveling?')
    mnth = df.month.mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_popular_month = months[mnth - 1].capitalize()
    return most_popular_month

#  display the most common day of week
def popular_day(df):
    '''What is the most popular day of week for start time?
    INPUT:
        df - dataframe returned from apply_time_filters
    OUTPUT:
        popular_day - string with name of day with most rides
    '''
    print('\n * What is the most popular day of the week (Monday to Sunday) for bikeshare traveling?')

    return df['day_of_week'].value_counts().reset_index()['index'][0]

 #  display the most common start hour

def popular_hour(df):
    '''What is the most popular hour of day for start time?
    INPUT:
        df - dataframe returned from apply_time_filters
    OUTPUT:
        popular_hour - int of the most popular hour
    '''
    print('\n * What is the most popular hour of the day for bike traveling?')
    df['hour'] = df['Start Time'].dt.hour
    return df.hour.mode()[0]


def trip_duration(df):
    '''What is the total trip duration and average trip duration?
    INPUT:
        df - dataframe returned from apply_time_filters
    OUTPUT:
        tuple = total trip duration, average trip durations
        each is a pandas._libs.tslib.Timedelta objects
    '''
    print('\n * What was the total traveling done for 2017 through June, and what was the average time spent for each travel?')
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']

#  display total travel time
    total_travel_time = np.sum(df['Travel Time'])

    totalDays = str(total_travel_time).split()[0]

    print ("\nThe total travel time on 2017 through June was " + totalDays + " days \n")

  #  display mean travel time
    average_travel_time = np.mean(df['Travel Time'])

    averageDays = str(average_travel_time).split()[0]

    print("The average travel time on 2017 through June was " + averageDays + " days \n")

    return total_travel_time, average_travel_time

  #  display most frequent combination of start station and end station trip
def popular_stations(df):
    '''What is the most popular start station and most popular end station?
    INPUT:
        df - dataframe returned from apply_time_filters
    OUTPUT:
        tuple - indicating most popular start and end stations
    '''

    #  display most commonly used start station
    print("\n* What is the most popular start station?\n")
    start_station = df['Start Station'].value_counts().reset_index()['index'][0]
    print (start_station)

    #  display most commonly used end station
    print("\n* What is the most popular end station?\n")
    end_station = df['End Station'].value_counts().reset_index()['index'][0]
    print(end_station)
    return start_station, end_station


def popular_trip(df):
    '''What is the most popular trip?
    INPUT:
        df - dataframe returned from apply_time_filters
    OUTPUT:
        result -pandas DataFrame - with start, end, and number of trips for most popular trip
    '''
    result = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\n* What was the most popular trip from start to end?')
    return result

#  Display counts of user types
def users(df):
    '''What are the counts of each user type?
    INPUT:
        df - dataframe returned from apply_time_filters
    OUTPUT:
        users - pandas series with counts for each user type
    '''
    print('\n* Are users subscribers, customers?\n')

    return df['User Type'].value_counts()

#  Display counts of gender
def gender(df):
    '''What are the counts of gender?
    INPUT:
        df - dataframe returned from apply_time_filters
    OUTPUT:
        gender pandas.series.Series counts for each gender
    '''
    try:
        print('\n* What is the breakdown of gender among users?\n')

        return df['Gender'].value_counts()
    except:
        print('There is no gender data.')

 #  Display earliest, most recent, and most common year of birth
def birth_years(df):
    '''What is the earliest, latest, and most frequent birth year?
    INPUT:
        df - dataframe returned from apply_time_filters
    OUTPUT:
        tuple of earliest, latest, and most frequent year of birth
    '''
    try:
        print('\n* What is the earliest, latest, and most frequent year of birth?')
        earliest = np.min(df['Birth Year'])
        print ("\nThe earliest year of birth is " + str(earliest) + "\n")
        latest = np.max(df['Birth Year'])
        print ("The latest year of birth is " + str(latest) + "\n")
        most_frequent= df['Birth Year'].mode()[0]
        print ("The most frequent year of birth is " + str(most_frequent) + "\n")
        return earliest, latest, most_frequent
    except:
        print('No available birth date data.')

def compute_stat(f, df):
    """
    Calculates the time it takes to commpute a stat
    INPUT:
      f  - the applied stats function
      df - the dataframe with all the data
    OUTPUT:
        prints to console, doesn't return a value
    """

    start_time = time.time()
    statToCompute = f(df)
    print(statToCompute)
    print("Computing this stat took %s seconds." % (time.time() - start_time))

def max_day_of_month(df, month):
    """
    Gets the max day of the month
    INPUT:
      df - the city dataframe
      month - string of the selected month
    OUTPUT:
       maxDay - integer with the max day of the month
    """
    months = {"january": 1, "february": 2, "march": 3, "april":4, "may": 5, "june":6}
    df = df[df["month"] == months[month]]

    maxDay = max(df["day_of_month"])
    return maxDay

#display additional lines of data upon request

def display_raw_data(df):
    """
    Displays the data used to compute the stats
    Input:
        the dataframe with all the bikeshare data
    Returns:
       none
    """

    df = df.drop(['month', 'day_of_month'], axis = 1)

    rowIndex = 0

    seeData = input("\n Would you like to see multiple rows of the data for computing the stats? Please write 'yes' or 'no' \n").lower()

    while True:

        if seeData == 'no':
            return

        if seeData == 'yes':
            print(df[rowIndex: rowIndex + 5])
            rowIndex = rowIndex + 5


        seeData = input("\n Would you like to see five additional rows of the data for computing the stats? Please write 'yes' or 'no' \n").lower()

#Display requested data per city
def stats():
    '''Calculates and prints out the descriptive statistics about a city
    and time period specified by the user via raw input.
    Args:
        none.
    Returns:
        none.
    '''
    city = pick_city()

    df = load_data(city)

    time_period = pick_time_period()

    month = pick_month(time_period)
    day = pick_day(time_period)
    monthAndDay = day_of_month(df, time_period)

    df = apply_time_filters(df, time_period, month, day, monthAndDay)

    display_raw_data(df)

    stat_function_list = [popular_month,
     popular_day, popular_hour,
     trip_duration, popular_trip,
     popular_stations, users, birth_years, gender]

    for func in stat_function_list:
        compute_stat(func, df)

    #request restart or end
    restart = input("\n * Would you like to restart and request another analysis? Type \'yes\' or \'no\'.\n")
    if restart.upper() == 'YES' or restart.upper() == "Y":
        stats()

if __name__ == '__main__':
    stats()
