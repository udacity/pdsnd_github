import time  #used for datetime manipulation
import pandas as pd  #used for data handling
import numpy as np #used for numerical and statistical analysis

CHICAGO = 'Chicago'
NYC = 'New York City'
WASHINGTON = 'Washington'

CITY_DATA = { CHICAGO: 'chicago.csv',
              NYC: 'new_york_city.csv',
              WASHINGTON: 'washington.csv' }

days_in_week = [ 'Monday' , 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday' , 'Sunday' ]
months_in_year = [ 'January' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December' ]
hours = [ '11 PM' , '10 PM' , '9 PM' , '8 PM' , '7 PM' , '6 PM' , '5 PM' , '4 PM' , '3 PM' , '2 PM' , '1 PM' , '12 PM' , '11 AM' , '10 AM' , '9 AM' , '8 AM', '7 AM' , '6 AM' , '5 AM' , '4 AM' , '3 AM' , '2 AM' , '1 AM' , '12 AM' ]

seconds_in_minute = 60
seconds_in_hour = 60 * seconds_in_minute
seconds_in_days = 24 * seconds_in_hour
seconds_in_week = 7 * seconds_in_days

#print(CITY_DATA)
START_TIME = 'Start Time'
END_TIME = 'End Time'
BIRTH_YEAR = 'Birth Year'
START_STATION = 'Start Station'
END_STATION = 'End Station'
TRIP_DURATION = 'Trip Duration'
GENDER = 'Gender'

#colums that are added
START_MONTH = 'Start Month'
START_DAY_OF_WEEK = 'Start Day of Week'

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    ALL = 'all'
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print("Select the number of the city that you would like to choose ")
        print("1 - Chicago, 2 - New York, 3 - Washington")
        location = input("> ")
        if location == '1' :
            city = CHICAGO
            print("You have selected the city of Chicago")
            break
        elif location == '2' :
                city = NYC
                print("You have selected the city of New York")
                break
        elif location == '3' :
                city = WASHINGTON
                print("You have selected the city of Washington")
                break
        else :
                print("Sorry, you have entered an invalid choice")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        print("Select the number of the month that you want to explore or \"{}\": ".format(ALL))
        print("1 as January, 2 as February, 3 as March, 4 as April, 5 as May and 6 as June")
        m = input("> ")
        if m == ALL :
            month = None
            break
        try :
            month = int(m)
        except ValueError :
            print("Sorry, you have entered an invalid choice")
            continue
        else :
            if month >= 1 and month <= 6 :
                print("You have selected " + months_in_year[month - 1])
                break
            elif month <= 12 :
                print("You just have to select from January to June")
                print("Sorry, you have entered an invalid choice")
                continue
            else :
                  print("Sorry, you have entered an invalid choice")
                  continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print("Select the number of the month you would like to explore or \"{}\": ".format(ALL))
        print("1 as Monday, 2 as Tuesday, 3 as Wednesday, 4 as Thursday, 5 as Friday, 6 as Saturday and 7 as Sunday")
        d = input("> ")
        if d == ALL :
            day = None
            break
        try :
            day = int(d)
        except ValueError :
            print("Sorry, you have selected an invalid option")
            continue
        else :
            if day >= 1 and day<= 7 :
                day -= 1
                print("You have selected " + days_in_week[day])
                break
            else :
                print("Sorry, you have selected an invalid option")
                continue


    return city, month, day

#added extra

def convert_date_time_columns(df) :
                    df[START_TIME] = df[START_TIME].apply(pd.to_datetime)
                    df[END_TIME] = df[END_TIME].apply(pd.to_datetime)
                    df[START_MONTH] = df[START_TIME].dt.month
                    df[START_DAY_OF_WEEK] = df[START_TIME].dt.dayofweek

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
    convert_date_time_columns(df)

    if month is not None :
                    df = df[df[START_MONTH] == month]
    if day is not None :
                    df = df[df[START_DAY_OF_WEEK] == day]

    return df


def time_stats(df, display_month, display_day_in_week):
    """Displays statistics on the most frequent times of travel.
    Args:
        df - Pandas DataFrame containing city data filtered by month and day
        (bool) display_month - if already filtered by month, don't display it
        (bool) display_day_in_week - same as above for day of week
    Returns:
        month, day_of_week, hour (tuple of ints) -
            Most frequent times of travel - day_of_week and/or hour may be None if already filtered by these
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    month, day_of_week, hour = None, None, None

    # TO DO: display the most common month
    if display_month :
        month = df[START_MONTH].mode()[0]
        print("This tells us that the most common start month {}".format(months_in_year[month - 1]))

    # TO DO: display the most common day of week
    if display_day_in_week :
        day_of_week = df[START_DAY_OF_WEEK].mode()[0]
        print("This tells that the most common start day in the whole week {}".format(days_in_week[day_of_week]))

    # TO DO: display the most common start hour
    hour = df[START_TIME].dt.hour.mode()[0]
    print("This tells us that the most common time {}".format(hours[hour]))
    print("\nThis took %s seconds." % (time.time() - start_time))


    return month, day_of_week, hour


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    top_start = df['Start Station'].mode()[0]
    common_start_station = (df['Start Station'] == top_start).sum()
    print("The Common Start Station is {} ({} trips)".format(top_start, common_start_station))

    # TO DO: display most commonly used end station
    top_end = df[END_STATION].mode()[0]
    common_end_station = (df[END_STATION] == top_end).sum()
    print('The Common End Station is {} ({} trips)'.format(top_end, common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    by_start_and_end = df.groupby([START_STATION, END_STATION]).size()
    common_start_end_station = by_start_and_end.idxmax()
    print('The Most Popular Combination Station is \n{}, {} ({} trips)'.format(common_start_end_station[0], common_start_end_station[1], by_start_and_end[common_start_end_station]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    return top_start, top_end, common_start_end_station


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df[TRIP_DURATION].sum()
    print('We find the total travelled time is found to be\n', total_travel_time)

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('We find the average travel time is found to be\n', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.

    Returns:
        user_dict - key type of user, value is count
        gender_dict - same as above, for gender
        earliest_year (int) of birth
        the_most_recent_year (int) "
        the_most_common_year (int) "
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df.groupby('User Type').count()
    user_dict = {}
    for index, row in user_type.iterrows():
        user_dict[index] = row[0]
        print("{}: {}".format(index, row[0]))

    gender_dict = {}
    if GENDER in df.columns:

    # TO DO: Display counts of gender
        gender = df.groupby(GENDER).count()
        print()
        for index, row in gender.iterrows():
            gender_dict[index] = row[0]
            print("{}: {}".format(index, row[0]))

    the_earliest_year = None
    the_most_recent_year = None
    the_most_common_year = None
    if BIRTH_YEAR in df.columns:

    # TO DO: Display earliest, most recent, and most common year of birth
        birth_year = df[BIRTH_YEAR].dropna()
        the_earliest_year = int(birth_year.min())
        the_most_recent_year = int(birth_year.max())
        the_most_common_year = int(birth_year.mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    return user_dict, gender_dict, the_earliest_year, the_most_recent_year, the_most_common_year
    print('-'*40)

def main():
    line_number = 0

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month is None, day is None)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'no':
            print(df.iloc[line_number : line_number + 5])
            line_number += 5

        if restart.lower() != 'yes':
            print("Have a great day. Goodbye!")
            break


if __name__ == "__main__":
	main()
