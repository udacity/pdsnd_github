import calendar
import datetime
import pandas as pd
import time


def requested_city():
    '''Asks user to specify a city to analyze.

    Args:
        none.
    Returns:
        (str) Filename of the city to analyze
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago (CHI), New York City (NYC), or Washington D.C. (DC)?\n').title().lower()
    if city == city == 'chicago' or city == 'chi':
        return 'chicago.csv'
    elif city =='new york city' or city == 'nyc':
        return 'new_york_city.csv'
    elif city == 'washington' or city == 'washington dc' or city == 'washington d.c.' or city == 'dc':
        return 'washington.csv'
    else:
        print("\nI'm sorry, I did not catch that.")
        return requested_city()


def requested_filters():
    '''Asks user to specify if they want month or day to analyze.

    Args:
        none.
    Returns:
        (list) with two str values:
            First value: the type of filter period (i.e. month, day or none)
            Second value: the specific filter period (e.g. March, Tuesday)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or no filter? Enter M for month, D for day, and N for no filter.\n').lower()
    
    if time_period == 'month' or time_period == 'm':
        return ['month', requested_month()]
    elif time_period == 'day' or time_period == 'd':
        return ['day', requested_day()]
    elif time_period == 'none' or time_period == 'n':
        return ['none', 'no filter']
    else:
        print("\nI'm sorry, I did not catch that.")
        return requested_filters()


def requested_month():
    '''Asks user to specify a month to analyze.

    Args:
        none.
    Returns:
          (str) month - name of the month to filter by
    '''
    month = input('\nWhich month? (1)January, (2)February, (3)March, (4)April, (5)May, or (6)June?\
                    Enter 1 for January, 2 for February, 3 for March, 4 for April,\
                    5 for May, or 6 for June.\n').title().lower()
    if month == 'january' or month == '1':
        return '01'
    elif month == 'february' or month == '2':
        return '02'
    elif month == 'march' or month == '3':
        return '03'
    elif month == 'april' or month == '4':
        return '04'
    elif month == 'may' or month == '5':
        return '05'
    elif month == 'june' or month == '6':
        return '06'
    else:
        print("\nI'm sorry, I did not catch that.")
        return requested_month()

def requested_day():
    '''Asks user to specify a  day to analyze.

    Args:
        none.
    Returns:
        (int) Integer of day of week to filter by
    '''
    day_of_week = input('\nWhich day of the week? (1)Monday, (2)Tuesday, (3)Wednesday, (4)Thursday,\
                        (5)Friday, (6)Saturday, or (7)Sunday? Enter 1 for Monday, 2 for Tuesday,\
                         3 for Wednesday, 4 for Thursday, 5 for Friday, 6 for Saturday, or 7 for Sunday.\n').title().lower()
    if day_of_week == 'monday' or day_of_week == '1':
        return 0
    elif day_of_week == 'tuesday' or day_of_week == '2':
        return 1
    elif day_of_week == 'wednesday' or day_of_week == '3':
        return 2
    elif day_of_week == 'thursday' or day_of_week == '4':
        return 3
    elif day_of_week == 'friday' or day_of_week == '5':
        return 4
    elif day_of_week == 'saturday' or day_of_week == '6':
        return 5
    elif day_of_week == 'sunday' or day_of_week == '7':
        return 6
    else:
        print("\nI'm sorry, I did not catch that.")
        return requested_day()

def common_month(df):
     """Displays statistics on the most frequent times of travel."""
     trips_per_month = df.groupby('Month')['Start Time'].count()
     # returns the most common month
     return "Most common month: " + calendar.month_name[int(trips_per_month.sort_values(ascending=False).index[0])]


def common_day(df):
     """Displays statistics on the most frequent times of travel."""

     trips_per_day_of_week = df.groupby('Day of Week')['Start Time'].count()
     # display the most common day of week
     return "Most common day of the week: " + calendar.day_name[int(trips_per_day_of_week.sort_values(ascending=False).index[0])]


def common_hour(df):

    """Displays statistics on the most frequent times of travel."""

    trips_per_hour = df.groupby('Hour of Day')['Start Time'].count()
    # display the most common start hour
    most_common_hour_int = trips_per_hour.sort_values(ascending=False).index[0]
    d = datetime.datetime.strptime(most_common_hour_int, "%H")
    return "Most common hour: " + d.strftime("%I %p")

def common_stations(df):
    """Displays statistics on the most popular stations and trip."""

    start_station_count = df.groupby('Start Station')['Start Station'].count()
    end_station_count = df.groupby('End Station')['End Station'].count()
    sorted_start_station_counts = start_station_count.sort_values(ascending=False)
    sorted_end_station_counts = end_station_count.sort_values(ascending=False)
    total_trips = df['Start Station'].count()
    # display most commonly used start station
    most_common_start_station = "\nMost common start station: " + sorted_start_station_counts.index[0] + " (" + str(sorted_start_station_counts[0]) + " trips, " + '{0:.2f}%'.format(((sorted_start_station_counts[0]/total_trips) * 100)) + " of trips)"
    # display most commonly used end station
    most_common_end_station = "Most common end station: " + sorted_end_station_counts.index[0] + " (" + str(sorted_end_station_counts[0]) + " trips, " + '{0:.2f}%'.format(((sorted_end_station_counts[0]/total_trips) * 100)) + " of trips)"
    return [most_common_start_station, most_common_end_station]


def common_trip(df):
     """Displays statistics on the most popular stations and trip."""

     # display most frequent combination of start station and end station trip
     trip_count = df.groupby(['Start Station', 'End Station'])['Start Time'].count()
     sorted_trip_station_counts = trip_count.sort_values(ascending=False)
     total_trips = df['Start Station'].count()
     return "Most common trip: " + "\n  Start station: " + str(sorted_trip_station_counts.index[0][0]) + "\n  End station: " + str(sorted_trip_station_counts.index[0][1]) + "\n  (" + str(sorted_trip_station_counts[0]) +  " trips, " + '{0:.2f}%'.format(((sorted_trip_station_counts[0]/total_trips) * 100)) + " of trips)"

def trip_duration(df):
    """Displays statistics on the total and average trip duration."""

    total_trip_duration = df['Trip Duration'].sum()
    avg_trip_duration = df['Trip Duration'].mean()
    m, s = divmod(total_trip_duration, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)
    # display total travel time
    total_trip_duration = "\nTotal travel time: %d years %02d days %02d hrs %02d min %02d sec" % (y, d, h, m, s)
    m, s = divmod(avg_trip_duration, 60)
    h, m = divmod(m, 60)
    # display mean travel time
    avg_trip_duration = "Average travel time: %d hrs %02d min %02d sec" % (h, m, s)
    return [total_trip_duration, avg_trip_duration]



def users(df):
    """Displays statistics on bikeshare users."""
    # Display counts of user types
    user_type_count = df.groupby('User Type')['User Type'].count()
    return user_type_count


def gender(df):
    """Displays statistics on bikeshare users."""
    # Display counts of gender
    gender_count = df.groupby('Gender')['Gender'].count()
    return gender_count


def birth_year(df):
    """Displays statistics on bikeshare users."""
    # Display earliest, most recent, and most common year of birth
    earliest_birth_year = "Earliest birth year: " + str(int(df['Birth Year'].min()))
    most_recent_birth_year = "Most recent birth year: " + str(int(df['Birth Year'].max()))
    birth_year_count = df.groupby('Birth Year')['Birth Year'].count()
    sorted_birth_year_counts = birth_year_count.sort_values(ascending=False)
    total_trips = df['Birth Year'].count()
    most_common_birth_year = "Most common birth year: " + str(int(sorted_birth_year_counts.index[0])) + " (" + str(sorted_birth_year_counts.iloc[0]) + " trips, " + '{0:.2f}%'.format(((sorted_birth_year_counts.iloc[0]/total_trips) * 100)) + " of trips)"
    return [earliest_birth_year, most_recent_birth_year, most_common_birth_year]

def display_data(df, current_line):
    """Displays raw data."""

    display = input('\nWould you like to see the trip data used for these calculations? Enter Y for yes or N for no.\n').lower()
    display = display.lower()
    if display == 'yes' or display == 'y':
        print(df.iloc[current_line:current_line+5])
        current_line += 5
        return display_data(df, current_line)
    if display == 'no' or display == 'n':
        return
    else:
        print("\nWould you like to see more trip data?\ Enter Y for yes or N for no.")
        return display_data(df, current_line)


def main():

    city = requested_city()
    city_df = pd.read_csv(city)

    def get_day_of_week(str_date):

        date_obj = datetime.date(int(str_date[0:4]), int(str_date[5:7]), int(str_date[8:10]))
        return date_obj.weekday()

    city_df['Day of Week'] = city_df['Start Time'].apply(get_day_of_week)
    city_df['Month'] = city_df['Start Time'].str[5:7]
    city_df['Hour of Day'] = city_df['Start Time'].str[11:13]

    time_period = requested_filters()
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

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if filter_period == 'none' or filter_period == 'day':
        print(common_month(filtered_df))

    if filter_period == 'none' or filter_period == 'month':
        print(common_day(filtered_df))

    print(common_hour(filtered_df))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    most_common_station = common_stations(filtered_df)
    print(most_common_station[0])
    print(most_common_station[1])

    print(common_trip(filtered_df))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    trip_duration_stats = trip_duration(filtered_df)
    print(trip_duration_stats[0])
    print(trip_duration_stats[1])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print('')
    print(users(filtered_df))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        print('')
        print(gender(filtered_df))

        birth_year_data = birth_year(filtered_df)
        print('')
        print(birth_year_data[0])
        print(birth_year_data[1])
        print(birth_year_data[2])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    display_data(filtered_df, 0)

    def restart_question():

        restart = input('\nWould you like to restart? Enter Y for yes or N for no.\n').lower
        if restart() == 'yes' or restart() == 'y':
            main()
        elif restart() == 'no' or restart() == 'n':
            return
        else:
            print("\nPlease re-enter your response.")
            return restart_question()

    restart_question()

if __name__ == "__main__":
    main()
