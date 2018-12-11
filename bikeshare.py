import pandas as pd
import datetime
import time
import collections as clct

# Filenames
# chicago: 'chicago.csv'
# new_york_city: 'new_york_city.csv'
# washington: 'washington.csv'

def get_city():

    city_list = {'chicago': 'chicago.csv','new york': 'new_york_city.csv', 'washington': 'washington.csv'}
    city_input = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New york, or Washington?\n')

    while(True):
        if city_input.lower() in city_list.keys():
            city = pd.read_csv(city_list[city_input.lower()])
            break

        else:
           city_input = input('\nPlease enter the correct city. (e.g: Chicago, New York, or Washington)\n')

    return city, city_input.lower()


def get_time_period():

    time_period_list = ['month', 'day', 'none']
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')

    while (True):
        if time_period.lower() in time_period_list:
            return time_period.lower()
            break
        else:
            time_period = input("\nPlease enter the correct filter. (e.g: month, day or none)\n")


def get_month():

    month_list = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6}
    month_input = input('\nWhich month? January, February, March, April, May, or June?\n')

    while(True):
        if month_input.title() in month_list.keys():
            month = month_list[month_input.title()]
            break
        else:
            month_input = input("\nPlease enter the correct month. (e.g: January, February, March, April, May, or June)\n")

    return month


def get_day():

    day_list = {'m': 0, 'tu': 1, 'wed': 2, 'th': 3, 'fr': 4 , 'sat': 5, 'sun': 6}
    day_input = input('\nWhich day? M, Tu, Wed, Th, Fr, Sat or Sun.\n')

    while(True):

        if day_input.lower() in day_list.keys():
            day = day_list[day_input.lower()]
            break
        else:
            day_input = input('\nPlease enter the correct day. (e.g: M, Tu, Wed, Th, Fr or Sat)\n')

    return day


def start_time_data_format(city_file):
    #converting Start Time dates in table (Day | month | year).
    year_list = []
    month_list = []
    day_list = []
    hour_list = []
    minut_list = []
    sec_list = []
    week_list = []

    for index in range(len(city_file)):
        year_list.append(int(city_file.loc[index, 'Start Time'].split()[0].split("-")[0]))
        month_list.append(int(city_file.loc[index, 'Start Time'].split()[0].split("-")[1]))
        day_list.append(int(city_file.loc[index, 'Start Time'].split()[0].split("-")[2]))
        hour_list.append(int(city_file.loc[index, 'Start Time'].split()[1].split(":")[0]))
        minut_list.append(int(city_file.loc[index, 'Start Time'].split()[1].split(":")[1]))
        sec_list.append(int(city_file.loc[index, 'Start Time'].split()[1].split(":")[2]))

    for year, month, day in zip(year_list, month_list, day_list):
        week_list.append(datetime.date(year,month,day).weekday())

    start_time_df = pd.DataFrame({ 'Sec': sec_list, 'Year': year_list, 'Month': month_list,'Minute': minut_list,'Hour': hour_list, 'Day': day_list, 'Week': week_list})

    return start_time_df


def popular_month(filter_for,time_period, start_time_df):
    '''
    Question: What is the most popular month for start time?
    '''
    month_list = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June"}
    months_in_df = start_time_df['Month']

    # Applying filter
    if time_period == 'month':
        f_month_list = months_in_df[start_time_df['Month'] == filter_for]

    elif time_period == 'day':
        f_month_list = months_in_df[start_time_df['Week'] == filter_for]

    else:# Flitering data for 'none' means no filter
        f_month_list = months_in_df

    month_count_list = clct.Counter(f_month_list.values).most_common()
    month_count_df = pd.DataFrame(month_count_list)
    row_index = month_count_df[1].idxmax()
    month = month_count_df.loc[row_index, 0]

    print("***************************************************************************")
    print("Most popular month for start time.\n")
    if month in month_list.keys():
        print("Month: {}\n".format(month_list[month]))


def popular_day(time_period, start_time_df, filter_for):
    '''
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    week_list = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    week_in_df = start_time_df['Week']

    # Applying filter
    if time_period == 'month':
        f_week_list = week_in_df[start_time_df['Month'] == filter_for]

    elif time_period == 'day':
        f_week_list = week_in_df[start_time_df['Week'] == filter_for]

    else:# Flitering data for 'none' means no filter
        f_week_list = week_in_df

    week_count_list = clct.Counter(f_week_list.values).most_common()
    week_count_df = pd.DataFrame(week_count_list)
    row_index = week_count_df[1].idxmax()
    week = week_count_df.loc[row_index, 0]


    print("***************************************************************************")
    print("Most popular day of week for start time.\n")
    if week in week_list.keys():
        print("Day: {}\n".format(week_list[week]))


def popular_hour(time_period, start_time_df, filter_for):
    '''
    Question: What is the most popular hour of day for start time?
    '''
    hour_in_df = start_time_df['Hour']

    #Applying filter..
    if time_period == 'month':
        #Filtring hours according to month which is given by user.
        f_hours = hour_in_df[start_time_df['Month'] == filter_for]

    elif time_period == 'day':
        #Filtring hours according to week which is given by user.
        f_hours = hour_in_df[start_time_df['Week'] == filter_for]

    else:# Flitering data for 'none' means no filter
        f_hours = hour_in_df

    #Counting..
    hour_count_list = clct.Counter(f_hours.values).most_common()
    hour_count_df = pd.DataFrame(hour_count_list)
    row_index = hour_count_df[1].idxmax()
    hour = hour_count_df.loc[row_index, 0]


    print("***************************************************************************")
    print("Most popular hour of day for start time.\n")
    print("Hour: {}\n".format(hour))


def trip_duration(city_file, time_period, start_time_df, filter_for):
    '''
    Question: What is the total trip duration and average trip duration?
    '''
    trip_duration_in_df = city_file['Trip Duration']

    #Applying filter..
    if time_period == 'month':
        #Filtring hours according to month which is given by user.
        f_trip_duration_list = trip_duration_in_df[start_time_df['Month'] == filter_for]

    elif time_period == 'day':
        #Filtring hours according to week which is given by user.
        f_trip_duration_list = trip_duration_in_df[start_time_df['Week'] == filter_for]

    else:# Flitering data for 'none' means no filter
        f_trip_duration_list = trip_duration_in_df

    #Calculating...
    total_trip_duration = sum(f_trip_duration_list)
    avg_trip_duration = f_trip_duration_list.mean()


    print("***************************************************************************")
    print("Total trip duration and average trip duration.\n")
    print("Total Trip Duration: {} seconds\nAverage Trip Duration: {} seconds\n".format(total_trip_duration, avg_trip_duration))


def popular_stations(city_file, time_period, filter_for, start_time_df):
    '''
    Question: What is the most popular start station and most popular end station?
    '''
    #Geting start stations, end station from city_file int to start_stations, end_stations.
    start_station_in_df = city_file['Start Station']
    end_station_in_df = city_file['End Station']

    #Applying filter...
    if time_period == 'month':
        f_start_stations = start_station_in_df[start_time_df['Month'] == filter_for]
        f_end_stations = end_station_in_df[start_time_df['Month'] == filter_for]

    elif time_period == 'day':
        f_start_stations = start_station_in_df[start_time_df['Week'] == filter_for]
        f_end_stations = end_station_in_df[start_time_df['Week'] == filter_for]

    else:# flter for none means no filter
        f_start_stations = start_station_in_df
        f_end_stations = end_station_in_df

    #Counting..
    ss_count_list = clct.Counter(f_start_stations.values).most_common()
    es_count_list = clct.Counter(f_end_stations.values).most_common()

    ss_count_df = pd.DataFrame(ss_count_list)
    es_count_df = pd.DataFrame(es_count_list)

    ss_row_index = ss_count_df[1].idxmax()
    es_row_index = es_count_df[1].idxmax()

    start_station = ss_count_df.loc[ss_row_index, 0]
    end_station = es_count_df.loc[es_row_index, 0]

    print("***************************************************************************")
    print("Most popular start station and most popular end station.\n")
    print("Start Station: {}\nEnd Station: {}\n".format(start_station, end_station))

    return f_start_stations, f_end_stations


def users(city_file, time_period, start_time_df, filter_for):
    '''
    Question: What are the counts of each user type?
    '''
    user_types_list = city_file['User Type']

    if time_period == 'month':
        user_type = user_types_list[start_time_df['Month'] == filter_for]

    elif time_period == 'day':
        user_type = user_types_list[start_time_df['Week'] == filter_for]

    else: # Filter for none means no filter.
        user_type = user_types_list

    user_type_count_list = clct.Counter(user_type.values).most_common()
    user_type_count_df = pd.DataFrame(user_type_count_list)


    print("***************************************************************************")
    print("Counts of each user type.\n")
    print("{}: {}\n{}: {}\n".format(user_type_count_df.loc[0,0], user_type_count_df.loc[0,1], user_type_count_df.loc[1,0], user_type_count_df.loc[1,1]))


def gender(city_file, time_period, filter_for, start_time_df):
    '''
    Question: What are the counts of gender?
    '''
    gender_list = city_file['Gender']

    if time_period == 'month':
        gender = gender_list[start_time_df['Month'] == filter_for]

    elif time_period == 'day':
        gender = gender_list[start_time_df['Week'] == filter_for]

    else:
        gender = gender_list

    gender_count_list = clct.Counter(gender.values).most_common()
    gender_count_df = pd.DataFrame(gender_count_list)

    print("***************************************************************************")
    print("Counts of gender.\n")
    print("{}: {}\n{}: {}\n".format(gender_count_df.loc[0,0], gender_count_df.loc[0,1], gender_count_df.loc[1,0], gender_count_df.loc[1,1]))


def birth_years(city_file, time_period, filter_for, start_time_df):
    '''
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
    birth_year_list = city_file['Birth Year']

    if time_period == 'month':
        f_birth_year = birth_year_list[start_time_df['Month'] == filter_for]

    elif time_period == 'day':
        f_birth_year = birth_year_list[start_time_df['Month'] == filter_for]

    else:
        f_birth_year = birth_year_list

    #Popular birth year..
    f_birth_year_count_list = clct.Counter(f_birth_year.values).most_common()
    f_birth_year_count_df = pd.DataFrame(f_birth_year_count_list)
    row_index = f_birth_year_count_df[1].idxmax()
    popular_year = int(f_birth_year_count_df.loc[row_index, 0])
    #youngest year..
    youngest_year = int(f_birth_year.max())
    #oldest year..
    oldest_year = int(f_birth_year.min())

    print("***************************************************************************")
    print("Oldest, youngest and most popular birth years.\n")
    print("Oldest Year: {}\nYoungest Year: {}\nMost Popular: {}\n".format(oldest_year, youngest_year, popular_year))


def popular_trip(filtered_start_station, filtered_end_station, time_period):
    '''
    Question: What is the most popular trip?
    '''
    # Adding start station & end station in one data panda Series.
    trips = 'Start: ' + filtered_start_station + ' | End: ' + filtered_end_station
    #Counting trips and storing trip_count_list.
    trip_count_list = clct.Counter(trips.values).most_common()
    #Converting trip_count_list in data frame.
    trip_count_df = pd.DataFrame(trip_count_list)
    #Getting row index of trip_count_df for max trip count in column 1.
    max_index_row = trip_count_df[1].idxmax()

    print("***************************************************************************")
    print("Most popular trip.\n")

    print("{}\nCount:{}\n".format(trip_count_df.loc[max_index_row, 0], trip_count_df.loc[max_index_row, 1]))


def display_data(city_file):

    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    n = 0
    while(display.lower() == 'yes'):
        n += 5
        print("***************************************************************************")
        print(city_file.head(n))
        print("***************************************************************************")

        display = input('\nwould like to see five more?'
                        'Type \'yes\' or \'stop\'.\n')


def statistics():

    # Filter by city (Chicago, New York, Washington)
    city_file, city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    if time_period == 'month':
        filter_for = get_month()
    elif time_period == 'day':
        filter_for = get_day()
    else:
        filter_for = 'none'

    print('\nJust one moment... loading data, after that it will go fast.')
    start_time_df = start_time_data_format(city_file)


    print('\nCalculating the first statistic...')

    # What is the most popular month for start time?
    start_time = time.time()

    popular_month(filter_for, time_period, start_time_df)

    print("That took %s seconds." % (time.time() - start_time))
    print("***************************************************************************")
    print("\nCalculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    start_time = time.time()

    popular_day(time_period, start_time_df, filter_for)

    print("That took %s seconds." % (time.time() - start_time))
    print("***************************************************************************")
    print("\nCalculating the next statistic...")

    start_time = time.time()

    # What is the most popular hour of day for start time?
    popular_hour(time_period, start_time_df, filter_for)

    print("That took %s seconds." % (time.time() - start_time))
    print("***************************************************************************")

    print("\nCalculating the next statistic...")

    start_time = time.time()

    # What is the total trip duration and average trip duration?
    trip_duration(city_file, time_period, start_time_df, filter_for)

    print("That took %s seconds." % (time.time() - start_time))
    print("***************************************************************************")
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    filtered_start_station, filtered_end_station = popular_stations(city_file, time_period, filter_for, start_time_df)

    print("That took %s seconds." % (time.time() - start_time))
    print("***************************************************************************")
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    users(city_file, time_period, start_time_df, filter_for)

    print("That took %s seconds." % (time.time() - start_time))
    print("***************************************************************************")
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    if city != 'washington':
        gender(city_file, time_period, filter_for, start_time_df)

    else:
        print("***************************************************************************\n")
        print("Sorry! no gender data to share.")

    print("That took %s seconds." % (time.time() - start_time))
    print("***************************************************************************")
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    if city != 'washington':
        birth_years(city_file, time_period, filter_for, start_time_df)
    else:
        print("***************************************************************************\n")
        print("Sorry! no birth year data to share.")

    print("That took %s seconds." % (time.time() - start_time))
    print("***************************************************************************")
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    popular_trip(filtered_start_station, filtered_end_station, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("***************************************************************************\n")

    # Display five lines of data at a time if user specifies that they would like to
    display_data(city_file)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
