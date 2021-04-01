"""
Description:
This python code allows the user to filter data related to usage of a bike share program in on of three cities (Chicago, New York or Washington).
The filter can also select a specific month and or day of the week.
The program then displays summery statistics for:
    popular time of Travel
    popular stations
    trip Duration
    user details
The user is then offered the chance to view the raw data.
"""


import time
#import pandas as pd
#import numpy as np

def get_city(city_dict):
    """
    This definition asks the user to specify a city to analyze.
    The definition requires a dictionary of citys, with the city as the key and their file names as the value.
    """
    while True:
        city = str(input('\nPlease enter the name of the city to analyse: Chicago, New York or Washington? ')).title()
        if city in city_dict:
            return city
        print('\nO dear, please check your spelling and try again')

def get_month(months):
    """
    This definition asks the user to specify if they would like to filter the data by month.
    The definition requires a dictionary or list of months which are contained within the data.
    The test to check which months are within the data file chosen has not been applied,
    this review was completed prior to setting up the question for all of the data files.
    This definition returns the month to use as a filter.
    """
    while True:
        month_filter = str(input('\nWould you like to filter the results by a spesific month? Please answer yes or no: ')).capitalize()
        if month_filter == 'No':
            month = 'NaN'
            return month
        elif month_filter =='Yes':
            while True:
                month = str(input('\nwhich month between January and June would you like to analyse? ')).capitalize()
                if month in months:
                    return month
                else:
                    print('\nO dear, please check your spelling and try again')
        else:
            print('\nO dear, please check your spelling and try again')


def get_day(days):
    """
    This definition asks the user to specify if they would like to filter the data by a spsific day.
    The definition requires a dictionary or list of days which are contained within the data.
    The test to check which dayss are within the data file has not been applied. This definition returns the day to use as a filter.
    """
    while True:
        day_filter = str(input('\nWould you like to filter the results by a spesific day? Please answer yes or no: ')).capitalize()
        if day_filter == 'No':
            day = 'NaN'
            return day
        elif day_filter =='Yes':
            while True:
                day = str(input('\nwhich day would you like to analyse? ')).capitalize()
                if day in days:
                    return day
                else:
                    print('\nO dear, please check your spelling and try again')
        else:
            print('\njanuaryO dear, please check your spelling and try again')

def get_filters(city_dict, months, days):
    """
    This definition runs the definitions to choose the city and the month and day filters to apply to the database.
    It returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')

    city = get_city(city_dict)
    month = get_month(months).split()
    day = get_day(days).split()
    print('-'*40)
    return city, month, day


def load_data(city_dict, city, month, day):
    """
    This definition loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    filename = city_dict[city]


    df = pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month_travel'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour_start'] = df['Start Time'].dt.hour

    df = df[df.month_travel.isin(month) & df.day_of_week.isin(day)]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel. Requires a datafram input argument."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    try:
        print('\nthe most common month for travel in this data set is {}.'.format( df['month_travel'].mode().item()))

        print('\nthe most common day for travel in this data set is {}.'.format(df['day_of_week'].mode().item()))

        print('\nthe most common hour for travel in this data set is {}:00.'.format(df['hour_start'].mode().item()))
    except Exception:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip. Requires a datafram input argument."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    try:
        print('\nthe most common start station is {}.'.format(df['Start Station'].mode().item()))

        print('\nthe most common end station is {}'.format(df['End Station'].mode().item()))

        station_from_to = df['End Station']
        df['station_from_to'] = df['Start Station'].str.cat(station_from_to, sep=" to ")
        print('\nthe most common journey is {}.'.format(df['station_from_to'].mode().item()))
    except Exception:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Converts trip duration to minutes then displays statistics on the total and average trip duration.

    Requires a datafram input argument."""

    df['Trip Duration'] = (df['Trip Duration']/60).round()
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    try:
        print('\nThe combined total travel time of all users is {} minutes'.format(df['Trip Duration'].sum().round()))

        print('\nThe average travel time is {} minutes '.format(df['Trip Duration'].mean().round()))
    except Exception:
        pass
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users. Requires a datafram input argument."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        print('\nthe number of different user types are: \n', df['User Type'].value_counts())

        print('\nthe gender split is: \n', df['Gender'].value_counts())

        print('\nthe oldest user was borne in {} and is {} years old '.format(df['Birth Year'].min(), 2021-df['Birth Year'].min()))

        print('\nThe youngest user was borne in {} and is {} years old'.format(df['Birth Year'].max(), 2021-df['Birth Year'].max()))

        print('\nThe most common age of user is {}'.format(2021-df['Birth Year'].mode().item()))
    except Exception:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view(df):
    """
    This definition offers the view the option to displays a 5 row subsed of the database.
    It then provides the option to keep seeing the next 5 lines untill the end of the database is reached,
    or the useer no longer asks to see more rows.

    Requires a datafram input argument.
    """
    pd.set_option('display.max_columns', None)
    to_view = str(input('\nWoul you like to view a sample of 5 rows of the database? Please answer yes or no: ').title())
    counter = 0
    no_rows = len(df.index)
    try:
        while counter < no_rows-5:
            if to_view == 'Yes':
                to_show = df[['Start Time', 'station_from_to','Trip Duration','User Type', 'Gender', 'Birth Year']]
                print(to_show[counter:counter+5])
                counter+=5
                to_view = str(input('\nWoul you like to view a sample of 5 rows of the database? Please answer yes or no: ').title())
                if to_view == 'No':
                    return
            elif to_view == 'No':
                return
            else:
                print('\n O dear, please check your spelling and try again')
                to_view = str(input('\nWoul you like to view a sample of 5 rows of the database? Please answer yes or no: ').title())
    except Exception:
            if to_view == 'Yes':
                print(df[counter:counter+5])
                counter+=5
                to_view = str(input('\nWoul you like to view a sample of 5 rows of the database? Please answer yes or no: ').title())
                if to_view == 'No':
                    return
            elif to_view == 'No':
                return
            else:
                print('\n O dear, please check your spelling and try again')
                to_view = str(input('\nWoul you like to view a sample of 5 rows of the database? Please answer yes or no: ').title())


def compare_city():
    """
    This definition allows the user to compare statistics for multiple cities.
    This definition returns the filters (compare_citys) to be applied to city_compare_stats definition .
    """
    while True:
        compare = str(input('\nWould you like to compare summary data from multiple cities? Please answer yes or no: ').title()):
        if compare =="Yes":
            while True:
                compare_citys = int(input('\nIf you would like to compare Chicago with New York, please enter 1 \n If you would like to compare Chicago with Washington, please enter 2\n If you would like to compare New York with Chicago, please enter 3\n If you would like to compare New York with Washington, please enter 4\n if you would like to compare Chicago, New York and Washington, please enter 5').title())
                if compare_citys >= 1 and compare_citys <=5:
                    return compare_citys
                else:
                    print('\nO dear, you entered an invalid number, please try again.').title())
        elif compare =="No":
            return
        else:
            print('\nO dear, please check your spelling and try again ').title())

#to do: build city_compare_stats definition and load into main definition.#


def main():
    """
    This definition runs the desired definitions to choose the data and filters,
    load the data file into a data fram and returns summery statistics for the filtered data.
    It then gives the user an option to restart the program or exit.
    Does not require an input argument.
    """
    city_file = {'Chicago':'chicago.csv', 'New York':'new_york_city.csv', 'Washington':'washington.csv'}
    month_w_data = {'January':0,'February':1,'March':2,'April':3,'May':4,'June':5}
    day_in_week = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
    while True:
        city,month,day = get_filters(city_file,month_w_data, day_in_week)
        if 'NaN' in month:
            month = ['January','February','March','April','May','June']
        else:
            pass
        if 'NaN' in day:
            day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        else:
            pass

        df = load_data(city_file, city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view(df)
        compare_city(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'no':
            break
        elif restart.lower() == 'yes':
            pass
        else:
            print('\n O dear, please check your spelling and try again')
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() == 'no':
                break


if __name__ == "__main__":
    main()
