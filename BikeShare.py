import pandas as pd
import datetime
import calendar

#After all data is viewed, prompts to restart from the begining
def reset_everthing():

    """
    After all the data is viewed, this will let you restart from the begining.

    Input: restart desire.

    Returns: ends function or starts over
    """

    desire = input('\nDo you want to start over?\nYes or no:\n').lower()
    if desire == 'yes' or desire == 'y':
        return bike_data()
    elif desire == 'no' or desire == 'n':
        return
    else:
        print('{} is not reconized, please try again.'.format(desire.title()))

#Set the filters that will be used. City, month, or day
def data_set():

    """
    This is to set the city, and month, day, or no filter.

    Inputs: City, filter, month or day.

    Returns: Selected city, selected filter, specific month or day
    """
    #Select the city to view data for
    while True:
        city = input('There is bikeshare data for Chicago, New York, and Washington.\n'
                     'Please select as city or press "O" for city accepted input options.\n').title()
        if city == 'Chicago' or city == 'C' or city == 'Chi-Town':
            city = 'Chicago'
            print('\n{} accepted.'.format(city))
            city_file = 'chicago.csv'
            break
        elif city == 'New York' or city == 'New York City' or city == 'N' or city == 'Nyc':
            city = 'New York City'
            print('\n{} accepted.'.format(city))
            city_file = 'new_york_city.csv'
            break
        elif city == 'Washington' or city == 'W' or city == "Dc" or city == 'Washington Dc':
            city = 'Washington'
            print('\n{} accepted.'.format(city))
            city_file = 'washington.csv'
            break
        elif city == 'O':
            print('\nYour options are:')
            print("Chicago, Chi-Town, C,\n"
                  "New York, NYC, N, New York City,\n"
                  "Washington, Washington DC, DC, or W.")
        else:
            print('\n{} is not reconized, please try again.'.format(city))

    #Set if no filter or filter by month or day will be used
    while True:
        date_narrow = input('The data can be sorted by month or day or not at all.\n'
                            'Please select month, day, or no filter.\n').lower()
        if date_narrow == 'month' or date_narrow == 'm':
            date_narrow = 'month'
            break
        elif date_narrow == 'day' or date_narrow == 'd':
            date_narrow = 'day'
            break
        elif date_narrow == 'no' or date_narrow == 'none' or date_narrow == 'no filter' or date_narrow == 'n':
            date_narrow = 'no filter'
            break
        else:
            print('{} is not reconized, plese select month, day, or no filter.'.format(date_narrow))

    #Verify city and no time filter
    while date_narrow == 'no filter':
        reset = input('You selected {} with {}, is this correct?\n'.format(city,date_narrow)).lower()
        if reset == 'yes' or reset == 'y':
            print('Thank you\n')
            return city_file, date_narrow, 'none'
            break
        elif reset == 'no' or reset == 'n':
            print('Back to the top')
            return data_set()
        else:
            print('{} is not reconized, please try again.'.format(reset))

    #Specify the month that will be used
    while date_narrow == 'month':
        reset = input('Please select a month:\n'
                      'January, February, March, April, May, or June:\n').title()
        if reset == 'January':
            print('January accepted')
            month_num = '01'
            break
        elif reset == 'February':
            print('February accepted')
            month_num = '02'
            break
        elif reset == 'March':
            print('March accepted')
            month_num = '03'
            break
        elif reset == 'April':
            print('April accepted')
            month_num = '04'
            break
        elif reset == 'May':
            print('May accepted')
            month_num = '05'
            break
        elif reset == 'June':
            print('June accepted')
            month_num = '06'
            break
        else:
            print('{} is not reconized, please try again.'.format(reset))

    #Specify the day that will be used
    while date_narrow == 'day':
        reset = input('Please select a day:\n'
                      'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday:\n').title()
        if reset == 'Monday':
            print('Monday accepted')
            day = 1
            break
        elif reset == 'Tuesday':
            print('Tuesday accepted')
            day = 2
            break
        elif reset == 'Wednesday':
            print('Wednesday accpeted')
            day = 3
            break
        elif reset == 'Thursday':
            print('Thursday accepted')
            day = 4
            break
        elif reset == 'Friday':
            print('Friday accepted')
            day = 5
            break
        elif reset == 'Saturday':
            print('Saturday accepted')
            day = 6
            break
        elif reset == 'Sunday':
            print('Sunday accepted')
            day = 7
            break
        else:
            print('{} is not reconized, please try again.'.format(reset))

    #Verify selections for month
    while date_narrow == 'month':
        print('')
        print('\nYou selected {} with filtering by {} for {}.'.format(city,date_narrow,reset))
        f_reset = input('Is this correct?\n').lower()
        if f_reset == 'y' or f_reset == 'yes':
            print('Thank you\n')
            return city_file, date_narrow, month_num
            break
        elif f_reset == 'n' or f_reset == 'no':
            print('Back to the top.')
            return data_set()
        else:
            print('{} is not reconized, please try again.'.format(f_reset))

    #Verify selections for day
    while date_narrow == 'day':
        print('')
        print('\nYou selected {} with filtering by {} for {}.'.format(city,date_narrow,reset))
        f_reset = input('Is this correct?\n').lower()
        if f_reset == 'y' or f_reset == 'yes':
            print('Thank you\n')
            return city_file, date_narrow, day
            break
        elif f_reset == 'n' or f_reset == 'no':
            print('Back to the top.')
            return data_set()
        else:
            print('{} is not reconized, please try again.'.format(f_reset))

#Return raw data based on filters
def more(city_file, line):

    """
    Prompts if you want to see the raw data based on the filters five lines at a time.

    Input: Yes or no

    Returns: The raw data or none
    """
    want = input('\nDo you want to see more data?\n'
                 'Yes or no?\n')
    if want == 'yes' or want == 'y':
        print()
        print(city_file.iloc[line:line+5])
        line += 5
        return more(city_file, line)
    elif want == 'no' or want == 'n':
        return reset_everthing()
    else:
        print('{} is not valid, plase try again.'.format(want))
        return more(city_file, line)


#Return calulated with the filters
def bike_data():

    """
    Get min, max, and average values for trips, start times, stations.
    Also shows what days and or months are the most popular based off the filters
    that have been set.

    Input: Preselected filters

    Returns: Filterd data specific to the city selected
    """

    data_extract = data_set()
    city_file_name = data_extract[0]
    city_file = pd.read_csv(city_file_name)

    #Convert specific date to its weekday
    #Followed by extracting specfic information from the specified file
    def pick_day_of_week(str_date):
        date_obj = datetime.date(int(str_date[0:4]), int(str_date[5:7]), int(str_date[8:10]))
        return date_obj.weekday()
    city_file['Date'] = city_file['Start Time'].str[0:10]
    city_file['Day'] = city_file['Start Time'].apply(pick_day_of_week)
    city_file['Month'] = city_file['Start Time'].str[5:7]
    city_file['Year'] = city_file['Start Time'].str[0:4]
    city_file['Start Hour'] = city_file['Start Time'].str[11:13]
    city_file['Duration'] = city_file['Trip Duration']
    city_file['Start Point'] = city_file['Start Station']
    city_file['End Point'] = city_file['End Station']

    date_filt = data_extract[1]
    month_day = data_extract[2]

    if date_filt == 'no filter':
        city_filter = city_file
    elif date_filt == 'month':
        city_filter = city_file.loc[city_file['Month'] == month_day]
    elif date_filt == 'day':
        city_filter = city_file.loc[city_file['Day'] == month_day]

    #Trip Times
    total_trip_duration = city_filter['Duration'].sum()
    mean_trip_duration = city_filter['Duration'].mean()
    minute, second = divmod(total_trip_duration, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    year, day = divmod(day, 365)
    print('\nUsers rode for a total of\n'
    '{} years {} days {} hours {} minutes {} seconds'.format(year, day, hour, minute, second))
    minute, second = divmod(mean_trip_duration, 60)
    hour, minute = divmod(minute, 60)
    mean_trip_duration = '{} hours {} minutes and {} seconds'.format(hour, minute, second)
    print('with an average of {} per trip.'.format(mean_trip_duration))

    #Trip Count
    trip_count = city_filter['Start Time'].count()
    print('This is based off data for {} trips with no filter.\n'.format(trip_count))

    #Most common hour
    common_hour = city_filter.groupby('Start Hour')['Start Time'].count()
    common_hour_s = common_hour.sort_values(ascending=False)
    common_hour_num = str(common_hour_s[0])
    print('The most common ride start hour is ' + common_hour_s.index[0] + ':00\n'
          '  with a total of ' + common_hour_num + ' trips.')

    #The most popular month
    if date_filt == 'no filter' or date_filt == 'day':
        common_month = city_filter.groupby('Month')['Start Time'].count()
        common_month_s = common_month.sort_values(ascending=False).index[0]
        common_month_num = str(common_month.sort_values(ascending=False)[0])
        month = calendar.month_name[int(common_month_s)]
        print('The most common month for ridership is ' + month + '\n with a total of ' + common_month_num + ' trips.')

    #Most common day
    if date_filt == 'no filter' or date_filt == 'month':
        common_day = city_filter.groupby('Day')['Start Time'].count()
        common_day_s = common_day.sort_values(ascending=False).index[0]
        common_day_num = str(common_day.sort_values(ascending=False)[0])
        day = calendar.day_name[common_day_s]
        print('The most common day for ridership is ' + day + '\n  with a total of ' + common_day_num + ' trips.')

    #Common Start
    start_point = city_filter.groupby('Start Point')['Start Station'].count()
    start_point_s = start_point.sort_values(ascending=False)
    start_point_num = str(start_point_s[0])
    print('The most common starting point is ' + start_point_s.index[0] + '\n  with a total of ' + start_point_num + ' trips.')

    #Common End
    end_point = city_filter.groupby('End Point')['End Station'].count()
    end_point_s = end_point.sort_values(ascending=False)
    end_point_num = str(end_point_s[0])
    print('The most common ending point is ' + end_point_s.index[0] + '\n  with a total of ' + end_point_num + ' trips.')

    #Common Trip
    trip_count = city_filter.groupby(['Start Point', 'End Point'])['Start Time'].count()
    trip_count_s = trip_count.sort_values(ascending=False)
    start_station = str(trip_count_s.index[0][0])
    end_station = str(trip_count_s.index[0][1])
    trip_total = trip_count_s[0]
    print('The most common trip starts at ' + start_station + 'and ends at ' + end_station + '.')
    print('  With a total of {} trips.'.format(trip_total))

    #User Type
    user_type = city_filter.groupby('User Type')['User Type'].count()
    user_type_s = user_type.sort_values(ascending=False)
    user_type_1 = str(user_type_s.index[0])
    user_type_2 = str(user_type_s.index[1])
    user_type_c1 = str(user_type_s[0])
    user_type_c2 = str(user_type_s[1])
    print()
    print('There were {} {} riders and {} {} riders.'.format(user_type_c1, user_type_1, user_type_c2, user_type_2))

    if city_file_name == 'new_york_city.csv' or city_file_name == 'chicago.csv':
        #Birth Years
        birth_year_count = city_filter.groupby('Birth Year')['Birth Year'].count()
        sorted_age = birth_year_count.sort_values(ascending=False)
        sorted_ages = sorted_age.index[0]
        print()
        print('The most common birth year is: {}'.format(int(sorted_ages)))
        earliest_birth_year = str(int(city_filter['Birth Year'].min()))
        newest_birth_year = str(int(city_filter['Birth Year'].max()))
        print('The oldest rider was born: ' + earliest_birth_year)
        print('The youngest rider was born: ' + newest_birth_year)
        #Gender
        gender = city_filter.groupby('Gender')['Gender'].count()
        gender_s = gender.sort_values(ascending=False)
        gender_1 = str(gender_s.index[0])
        gender_2 = str(gender_s.index[1])
        gender_c1 = str(gender_s[0])
        gender_c2 = str(gender_s[1])
        print()
        print('There were {} {} riders and {} {} riders.'.format(gender_c1, gender_1, gender_c2, gender_2))
    else:
        print()
        print('Washington has no gender or age data.')

    more(city_filter, 0)


if __name__ == "__main__":
    bike_data()
