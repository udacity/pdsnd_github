import datetime
import pandas as pd
import calendar

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.
   Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n').title()
    if city == 'Chicago' or city == 'C':
        return 'chicago.csv'
    elif city == 'New York' or city == "N":
        return 'new_york_city.csv'
    elif city == 'Washington' or city == 'W':
        return 'washington.csv'
    else:
        print("\nSorry I do not understand your input. Please select a city.")
        return get_city()

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.
    Args:
        none.
    Returns:
        (list) with two str values:
            First value: the type of filter period
            Second value: the specific filter period
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n').lower()
    if time_period == 'month' or time_period == 'm':
        return ['month', get_month()]
    elif time_period == 'day' or time_period == 'd':
        return ['day', get_day()]
    elif time_period == 'none' or time_period == 'n':
        return ['none', 'no filter']
    else:
        print("\nSorry I do not understand your input. Please select a time period.")
        return get_time_period()

def get_month():
    '''Asks the user for a month and returns the specified month.
    Args:
        none.
    Returns:
        (str) String represents month number, e.g. January returns '01'
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n').title()
    if month == 'January':
        return '01'
    elif month == 'February':
        return '02'
    elif month == 'March':
        return '03'
    elif month == 'April':
        return '04'
    elif month == 'May':
        return '05'
    elif month == 'June':
        return '06'
    else:
        print("\nSorry I do not understand your input. Please select a month.")
        return get_month()

def get_day():
    '''Asks the user for a day of the week and returns the specified day.
    Args:
        none.
    Returns:
        (int) Integer represents the day of the week, e.g. Monday returns 0
    '''
    day_of_week = input('\nWhich day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').title()
    if day_of_week == 'Monday':
        return 0
    elif day_of_week == 'Tuesday':
        return 1
    elif day_of_week == 'Wednesday':
        return 2
    elif day_of_week == 'Thursday':
        return 3
    elif day_of_week == 'Friday':
        return 4
    elif day_of_week == 'Saturday':
        return 5
    elif day_of_week == 'Sunday':
        return 6
    else:
        print("\nSorry I do not understand your input. Please select a day of the week.")
        return get_day()

def popular_month(df):
    '''Finds and displays the most popular month for start time.
    Args:
        df: dataframe of bikeshare data
    Returns:
        (str) String that displays the month with the most trips
    '''
    #Count the rows that have a specific month.
    trips_by_month = df.groupby('Month')['Start Time'].count()
    #Sort the results highest to lowest and then return the month that with the highest count
    return "Most popular month for start time: " + calendar.month_name[int(trips_by_month.sort_values(ascending=False).index[0])]

def popular_day(df):
    '''Finds and displays the most popular day of the week for start time (e.g. Monday, Tuesday)
    Args:
        df: dataframe of bikeshare data
    Returns:
        (str) String that displays the day with the most trips
    '''
    #Count the rows that have a specific Day of Week value.
    trips_by_day_of_week = df.groupby('Day of Week')['Start Time'].count()
    #Sort the results highest to lowest and return the day of the week that was highest
    return "Most popular day of the week for start time: " + calendar.day_name[int(trips_by_day_of_week.sort_values(ascending=False).index[0])]

def popular_hour(df):
    '''Finds and prints the most popular hour of day for start time.
    Args:
        df: dataframe of bikeshare data
    Returns:
        (str) String that displays hour of the day with the most trips
    '''
    #Count the rows which have a particular Hour of Day value.
    trips_by_hour_of_day = df.groupby('Hour of Day')['Start Time'].count()
    #Sort the results highest to lowest and return the hour of the day that was highest
    most_pop_hour_int = trips_by_hour_of_day.sort_values(ascending=False).index[0]
    d = datetime.datetime.strptime(most_pop_hour_int, "%H")
    return "Most popular hour of the day for start time: " + d.strftime("%I %p")

def trip_duration(df):
    '''Finds and prints the total trip duration and average trip duration in hours, minutes, and seconds.
    Args:
        df: dataframe of bikeshare data
    Returns:
        (list) with two str values:
            First value: String that lists the total trip duration in years, days, hours, minutes, and seconds
            Second value: String that lists the average trip duration in hours, minutes, and seconds
    '''
    total_trip_duration = df['Trip Duration'].sum()
    avg_trip_duration = df['Trip Duration'].mean()
    m, s = divmod(total_trip_duration, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)
    total_trip_duration = "\nTotal trip duration: %d years %02d days %02d hrs %02d min %02d sec" % (y, d, h, m, s)
    m, s = divmod(avg_trip_duration, 60)
    h, m = divmod(m, 60)
    avg_trip_duration = "Average trip duration: %d hrs %02d min %02d sec" % (h, m, s)
    return [total_trip_duration, avg_trip_duration]

def popular_stations(df):
    '''Finds and prints the most popular start station and most popular end station.
    Args:
        df: dataframe of bikeshare data
    Returns:
        (list) with two values:
            First value: String displaying the name of the most popular start station
                and the number of trips that started there and the percentage of trips
                that are accounted for
            Second value: String displaying the name of the most popular ending station
                and the number trips that started there and the percentage of trips
                that are accounted for
    '''
    start_station_counts = df.groupby('Start Station')['Start Station'].count()
    end_station_counts = df.groupby('End Station')['End Station'].count()
    sorted_start_stations = start_station_counts.sort_values(ascending=False)
    sorted_end_stations = end_station_counts.sort_values(ascending=False)
    total_trips = df['Start Station'].count()
    most_popular_start_station = "\nMost popular start station: " + sorted_start_stations.index[0] + " (" + str(sorted_start_stations[0]) + " trips, " + '{0:.2f}%'.format(((sorted_start_stations[0]/total_trips) * 100)) + " of trips)"
    most_popular_end_station = "Most popular end station: " + sorted_end_stations.index[0] + " (" + str(sorted_end_stations[0]) + " trips, " + '{0:.2f}%'.format(((sorted_end_stations[0]/total_trips) * 100)) + " of trips)"
    return [most_popular_start_station, most_popular_end_station]

def popular_trip(df):
    '''Finds and prints the most popular trip.
    Args:
        df: dataframe of bikeshare data
    Returns:
        (str) String that lists the most popular combination of start and end
        stations and the number of trips that are accounted for and the
        percentage of trips that are accounted for
    '''
    trip_counts = df.groupby(['Start Station', 'End Station'])['Start Time'].count()
    sorted_trip_stations = trip_counts.sort_values(ascending=False)
    total_trips = df['Start Station'].count()
    return "Most popular trip: " + "\n  Start station: " + str(sorted_trip_stations.index[0][0]) + "\n  End station: " + str(sorted_trip_stations.index[0][1]) + "\n  (" + str(sorted_trip_stations[0]) +  " trips, " + '{0:.2f}%'.format(((sorted_trip_stations[0]/total_trips) * 100)) + " of trips)"

def users(df):
    '''Finds and prints the counts of each user type.
    Args:
        df: dataframe of bikeshare data
    Returns:
        (pandas series) the index for each row is the type of user and
        the value is how many trips the user completed
    '''
    user_type_counts = df.groupby('User Type')['User Type'].count()
    return user_type_counts

def gender(df):
    '''Finds and prints the counts of gender.
    Args:
        df: dataframe of bikeshare data
    Returns:
        (pandas series) the index of each row is the gender and the value
            is the number of trips that gender made
    '''
    gender_counts = df.groupby('Gender')['Gender'].count()
    return gender_counts

def birth_years(df):
    '''Finds and prints the earliest (i.e. oldest user), most recent (i.e.
        youngest user), and most popular birth years.
    Args:
        df: dataframe of bikeshare data
    Returns:
        (list) with three values:
            First value: String stating the earliest birth year
            Second value: String stating the most recent birth year
            Third value: String stating the most common birth year
    '''
    earliest_birth_year = "Earliest birth year: " + str(int(df['Birth Year'].min()))
    most_recent_birth_year = "Most recent birth year: " + str(int(df['Birth Year'].max()))
    birth_year_counts = df.groupby('Birth Year')['Birth Year'].count()
    sorted_birth_years = birth_year_counts.sort_values(ascending=False)
    total_trips = df['Birth Year'].count()
    most_common_birth_year = "Most common birth year: " + str(int(sorted_birth_years.index[0])) + " (" + str(sorted_birth_years.iloc[0]) + " trips, " + '{0:.2f}%'.format(((sorted_birth_years.iloc[0]/total_trips) * 100)) + " of trips)"
    return [earliest_birth_year, most_recent_birth_year, most_common_birth_year]

def display_data(df, current_line):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.
    Args:
        df: dataframe of bikeshare data
    Returns:
        If the user selects yes then this function returns the next five lines
            of data and then asks the user again by calling this
            function again
        If the user says no then this function returns without any values
    '''
    display = input('\nWould you like to view individual trip data?'
                    ' Type \'yes\' or \'no\'.\n')
    display = display.lower()
    if display == 'yes' or display == 'y':
        print(df.iloc[current_line:current_line+5])
        current_line += 5
        return display_data(df, current_line)
    if display == 'no' or display == 'n':
        return
    else:
        print("\nSorry I do not understand your input. Please type 'yes' or 'no'")
        return display_data(df, current_line)

def statistics():
    '''Calculates and prints out the descriptive statistics about a city and
    time period specified by the user via raw input.
    Args:
        none.
    Returns:
        none.
    '''

    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    print('Loading data...')
    city_df = pd.read_csv(city)

    def get_day_of_week(str_date):
        '''Takes a date in the format yyyy-mm-dd and returns an integer
            for the day of the week, e.g. Monday returns 0
        Args:
            str_date: date in the format yyyy-mm-dd
        Returns:
            (int) Integer represention of the day of the week,
                e.g. for Monday it returns 0
        '''
    #parse string in format yyyy-mm-dd and create date based on those values.
        date_obj = datetime.date(int(str_date[0:4]), int(str_date[5:7]), int(str_date[8:10]))
        return date_obj.weekday() #return the day of the week
    #store day, month, and hour values
    city_df['Day of Week'] = city_df['Start Time'].apply(get_day_of_week)
    city_df['Month'] = city_df['Start Time'].str[5:7]
    city_df['Hour of Day'] = city_df['Start Time'].str[11:13]

    # Filter by time period that the user specifies (month, day, none)
    time_period = get_time_period()
    filter_period = time_period[0]
    filter_period_value = time_period[1]
    filter_period_label = 'No filter'

    if filter_period == 'none':
        filtered_df = city_df
    elif filter_period == 'month':
        filtered_df = city_df.loc[city_df['Month'] == filter_period_value]
        filter_period_label = calendar.month_name[int(filter_period_value)]
    elif filter_period == 'day':
        filtered_df = city_df.loc[city_df['Day of Week'] == filter_period_value]
        filter_period_label = calendar.day_name[int(filter_period_value)]

    #Prints heading that specifies the city this data represents and any filters that are applied
    print('\n')
    print(city[:-4].upper().replace("_", " ") + ' -- ' + filter_period_label.upper())
    print('Calculating data...')

    #Print the total number of trips for this city and filter
    print('Total trips: ' + "{:,}".format(filtered_df['Start Time'].count()))

    # What is the most popular month for start time?
    if filter_period == 'none' or filter_period == 'day':
        print(popular_month(filtered_df))

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if filter_period == 'none' or filter_period == 'month':
        print(popular_day(filtered_df))

    # What is the most popular hour of day for start time?
    print(popular_hour(filtered_df))

    # What is the total trip duration and average trip duration?
    trip_duration_stats = trip_duration(filtered_df)
    print(trip_duration_stats[0])
    print(trip_duration_stats[1])

    # What is the most popular start station and most popular end station?
    most_popular_stations = popular_stations(filtered_df)
    print(most_popular_stations[0])
    print(most_popular_stations[1])

    # What is the most popular trip?
    print(popular_trip(filtered_df))

    # What are the counts of each user type?
    print('')
    print(users(filtered_df))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        # What are the counts of gender?
        print('')
        print(gender(filtered_df))
        # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
        # most popular birth years?
        birth_years_data = birth_years(filtered_df)
        print('')
        print(birth_years_data[0])
        print(birth_years_data[1])
        print(birth_years_data[2])

    # Display five lines of data at a time if user specifies that they would like to
    display_data(filtered_df, 0)

    # Restart?
    def restart_question():
        '''Restarts the interactive program based on the user's input
        Args:
            none.
        Returns:
        '''
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'. (If you say no it will end the program.)\n')
        if restart.lower() == 'yes' or restart.lower() == 'y':
            statistics()
        elif restart.lower() == 'no' or restart.lower() == 'n':
            return
        else:
            print("\Sorry I do not understand your input. Please type 'yes' or 'no'")
            return restart_question()

    restart_question()

if __name__ == "__main__":
    statistics()
