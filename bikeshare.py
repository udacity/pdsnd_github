# ----------------------------------------------------------------------
#                          bikeshare.py
# ----------------------------------------------------------------------
# Author:   Josh Batchelor
# Date:     5 October 2019
# Purpose:  Interactively return statistics about US Bikeshare Data
#           Completed for Udacity Project: Explore US Bikeshare Data
#
# ----------------------------------------------------------------------
# Usage:    Cmd:\>python bikeshare.py
# ----------------------------------------------------------------------


import time
import datetime
import contextlib
import pandas as pd

city_data = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user for input in selecting a city from predefined list, a month and a day
    :return city: lowercase string either 'chicago', 'new york' or 'washington'
    :return month: month of year (jan to june): integer in range 0 - 6 where 0 represents user selecting all months
    :return day: day of week: integer in range 0 - 7 where 0 represents user selecting all days of week, monday is 1
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington).
    print('We have bikeshare data available from Chicago, New York City and Washington.')
    city = ''
    while city[:8] not in ['chicago', 'new york', 'washingt']:
        city = input('Which city\'s data would you like to explore?: ').lower()

    # tidy up user input
    if city[:8] == 'chicago':
        city = 'chicago'
    elif city[:8] == 'new york':
        city = 'new york city'
    elif city[:8] == 'washint':
        city = 'washington'

    # get user input for month (all, january, february, ... , june)
    # start with dictionary of month names and their index
    months = {}
    month = ''
    for i in range(1, 7):
        months[i] = datetime.date(2019, i, 1).strftime('%B')

    # get input from users as either month number, month name or as all
    # store month as integer where 0 is all and 1-6 is Jan-Dec
    while month not in months.keys() and month != 0:
        try:
            month = input('Which month (January to June) are you interested in? (enter all for all months): ')
            month = int(month)
        except ValueError:
            for k, v in months.items():
                if month.lower() == 'all':
                    month = 0
                    break
                elif v.lower()[:3] == str(month).lower()[:3]:
                    month = k
                    break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    # start with dictionary of weekday names and their index
    # store day of week as integer where 0 is all and 1-7 is Mon-Sun
    days = {}
    day = ''
    for i in range(1, 8):
        days[i] = datetime.date(2019, 4, i).strftime('%A')
    # get input from users as either weekday number, weekday name or as all
    while day not in days.keys() and day != 0:
        try:
            day = input('Which day of the week\'s data would you like to view? (enter all for all days): ')
            day = int(day)
        except ValueError:
            for k, v in days.items():
                if day.lower() == 'all':
                    day = 0
                    break
                elif v.lower()[:3] == str(day).lower()[:3]:
                    day = k
                    break

    print('-'*40)

    # Print a message to the user showing the input they entered.
    if month == 0 and day == 0:
        print('Great, returning data for {} for all months and all days'.format(city.title()))
    elif month == 0:
        print('Great, returning data for {} for {}s from all months'.format(city.title(), days[day]))
    elif day == 0:
        print('Great, returning data for {} from {} for all days'.format(city.title(), months[month]))
    else:
        print('Great, returning data for {} from {} for {}s'.format(city.title(), months[month], days[day]))
    return city, month, day


def load_data(city, month=0, day=0):
    """
    Takes user-supplied inputs, reads in csv datasets to pandas dataframes and filters on parameters
    :param city: lowercase string either 'chicago', 'new york' or 'washington'
    :param month: month of year: integer in range 0 - 12 where 0 represents user selecting all months
    :param day: day of week: integer in range 0 - 7 where 0 represents user selecting all days of week
    :return:
    """

    # Specify source data depending on city input
    try:
        city_csv = city_data[city]
    except KeyError:
        raise NameError('no data available for city {}'.format(city))

    # create pandas dataframe from csv, rename columns and cast dates to Timestamp objects
    df = pd.read_csv('source_data\\{}'.format(city_csv))
    df = df.rename(columns={'Unnamed: 0': 'trip_id',
                            'Start Time': 'start_time',
                            'End Time': 'end_time',
                            'Trip Duration': 'trip_duration',
                            'Start Station': 'start_station',
                            'End Station': 'end_station',
                            'User Type': 'user_type',
                            'Gender': 'gender',
                            'Birth Year': 'birth_year'})
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])

    # check for valid month and day inputs
    if not isinstance(month, int) and month not in range(0, 13):
        raise ValueError('invalid month value: must be integer between 0 and 12')
    elif not isinstance(day, int) and day not in range(0, 8):
        raise ValueError('invalid day value: must be integer between 0 and 7')

    # filter based on combination of day and month input
    if day == 0 and month == 0:
        pass
    elif month == 0:
        df = df[df['start_time'].dt.dayofweek == day - 1]
        pass
    elif day == 0:
        df = df[df['start_time'].dt.month == month]
        pass
    else:
        df = df[df['start_time'].dt.month == month]
        df = df[df['start_time'].dt.dayofweek == day - 1]

    return df


def time_stats(df, month=0, day=0):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = []
    for i in range(1, 13):
        months.append(datetime.date(2019, i, 1).strftime('%B'))
    if month == 0:
        common_month = months[int(df['start_time'].dt.month.mode().values[0])]
        print('The most common month for starting trips is ' + common_month)

    # display the most common day of week
    days = []
    for i in range(1, 8):
        days.append(datetime.date(2019, 4, i).strftime('%A'))
    if day == 0:
        common_day = days[int(df['start_time'].dt.dayofweek.mode().values[0])]
        print('The most common day for starting trips is ' + common_day)

    # display the most common start hour
    common_start = int(df['start_time'].dt.hour.mode().values[0])
    if 0 <= common_start < 12:
        start_interval = ('between ' +
                          str(common_start).zfill(2) + ':00 am and ' +
                          str(common_start + 1).zfill(2) + ':00 am')
    elif common_start == 23:
        start_interval = ('between ' +
                          str(common_start - 12).zfill(2) + ':00 pm and ' +
                          str(common_start - 11).zfill(2) + ':00 am')
    else:
        start_interval = ('between ' +
                          str(common_start - 12).zfill(2) + ':00 pm and ' +
                          str(common_start - 11).zfill(2) + ':00 pm')
    print('The most common start period is ' + start_interval)

    print("\nThis took %s seconds." % round(time.time() - start_time, 3))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trips...\n')
    start_time = time.time()

    # display most commonly used start stations
    print('Top 5 Start Stations by Trip Count\n' + '-'*40)
    print(df['start_station'].value_counts().head().reset_index().to_string(header=None, index=None))

    # display most commonly used end stations
    print('\nTop 5 End Stations by Trip Count\n' + '-'*40)
    print(df['end_station'].value_counts().head().reset_index().to_string(header=None, index=None))

    # display most frequent journeys (combination of start station and end station trips)
    print('\nTop 5 Journeys by Trip Count\n' + '-'*40)
    print((df['start_station'].map(str) + ' to ' + df['end_station']).value_counts().head().to_string(header=None))

    print("\nThis took %s seconds." % round(time.time() - start_time, 3))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    def stat_str(stat_sec):
        if stat_sec < 60:
            return str(round(stat_sec)) + ' seconds'
        elif stat_sec < 3600:
            minutes, seconds = divmod(stat_sec, 60)
            return '{} minutes, {} seconds'.format(int(minutes), int(round(seconds)))
        elif stat_sec < 86400:
            hours, minutes = divmod(stat_sec, 3600)
            minutes, seconds = divmod(minutes, 60)
            return '{} hours, {} minutes, {} seconds'.format(int(hours),
                                                             int(minutes),
                                                             int(round(seconds)))
        else:
            days, hours = divmod(stat_sec, 86400)
            hours, minutes = divmod(hours, 3600)
            minutes, seconds = divmod(minutes, 60)
            return '{} days, {} hours, {} minutes, {} seconds'.format(int(days),
                                                                      int(hours),
                                                                      int(minutes),
                                                                      int(round(seconds)))

    # Calculate trip statistics
    duration_sum = stat_str(df['trip_duration'].sum())
    duration_mean = stat_str(df['trip_duration'].mean())
    duration_std = stat_str(df['trip_duration'].std())
    duration_min = stat_str(df['trip_duration'].min())
    duration_25 = stat_str(df['trip_duration'].describe()['25%'])
    duration_50 = stat_str(df['trip_duration'].describe()['50%'])
    duration_75 = stat_str(df['trip_duration'].describe()['75%'])
    duration_max = stat_str(df['trip_duration'].max())

    # Print trip statistics
    print('Trip Duration Statistics\n' + '-' * 40)
    text_width = 17
    print('Mean:'.ljust(text_width) + duration_mean.rjust(42))
    print('Standard Dev:'.ljust(text_width) + duration_std.rjust(42))
    print('Maximum:'.ljust(text_width) + duration_max.rjust(42))
    print('Minimum:'.ljust(text_width) + duration_min.rjust(42))
    print('25th Percentile:'.ljust(text_width) + duration_25.rjust(42))
    print('50th Percentile:'.ljust(text_width) + duration_50.rjust(42))
    print('75th Percentile:'.ljust(text_width) + duration_75.rjust(42))
    print('All Trips Sum:'.ljust(text_width) + duration_sum.rjust(42))

    print("\nThis took %s seconds." % round(time.time() - start_time, 3))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Calculate counts of user types
    if 'user_type' in df:
        user_counts = df['user_type'].dropna(axis=0).value_counts().rename('Count')
        user_percent = df['user_type'].dropna(axis=0).value_counts(normalize=True).rename('Percentage')
        df_user = pd.concat([user_counts, user_percent], axis=1)
        df_user['Percentage'] = pd.Series(["{0:.2f}%".format(val * 100) for val in df_user['Percentage']],
                                          index=df_user.index)
        print('User Statistics by Type of User\n' + '-'*40)
        print(df_user)
        print()

    else:
        print('Sorry, no user type data available for this city')

    # Calculate gender statistics
    if 'gender' in df:
        gender_counts = df['gender'].dropna(axis=0).value_counts().rename('Count')
        gender_percent = df['gender'].dropna(axis=0).value_counts(normalize=True).rename('Percentage')
        df_gender = pd.concat([gender_counts, gender_percent], axis=1)
        df_gender['Percentage'] = pd.Series(["{0:.2f}%".format(val * 100) for val in df_gender['Percentage']],
                                            index=df_gender.index)
        print('\nGender Statistics\n' + '-'*40)
        print(df_gender)
        print()
    else:
        print('Sorry, no gender data available for this city')

    # Calculate earliest, most recent, and most common year of birth
    if 'birth_year' in df:
        birthyear_max = int(df['birth_year'].dropna(axis=0).max())
        birthyear_min = int(df['birth_year'].dropna(axis=0).min())
        birthyear_mode = int(df['birth_year'].dropna(axis=0).mode()[0])
        print('\nBirth Year Statistics\n' + '-'*40)
        print('Oldest Birth Year is     : {}'.format(str(birthyear_min)))
        print('Youngest Birth Year is   : {}'.format(str(birthyear_max)))
        print('Most Common Birth Year is: {}'.format(str(birthyear_mode)))
    else:
        print('Sorry, no birth year data available for this city')

    print("\nThis took %s seconds." % round(time.time() - start_time, 3))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        def print_stats(df, month, day):
            time_stats(df, month, day)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        print_stats(df, month, day)

        # Optional output of screen text to text file
        f_out = input('\nWould you like to write these statistics to a text file? Enter yes or no.\n')
        if f_out.lower() == 'yes':

            # Create Filename based on user input
            output_file = city + '_' + str(month).zfill(2) + '_' + str(day).zfill(2) + '.txt'
            with open(output_file, 'w+') as f:
                with contextlib.redirect_stdout(f):  # Redirects output to file

                    # Create Descriptive File Header
                    days = {}
                    for i in range(1, 8):
                        days[i] = datetime.date(2019, 4, i).strftime('%A')
                    months = {}
                    for i in range(1, 7):
                        months[i] = datetime.date(2019, i, 1).strftime('%B')
                    if month == 0 and day == 0:
                        print('Bikeshare Data for {} for all months and all days'.format(city.title()))
                    elif month == 0:
                        print('Bikeshare Data for {} for {}s from all months'.format(city.title(),
                                                                                     days[day]))
                    elif day == 0:
                        print('Bikeshare Data for {} from {} for all days'.format(city.title(),
                                                                                  months[month]))
                    else:
                        print('Bikeshare Data for {} from {} for {}s'.format(city.title(),
                                                                             months[month],
                                                                             days[day]))
                    print_stats(df, month, day)

        # Optional restart
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
