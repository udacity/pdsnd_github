
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
"""
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to be analyzed
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
"""

print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). 

def get_city():
    city = ' '
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('What city data would you like to explore, New York, Chicago or Washington? \n')
        if city.lower() == 'new york':
            return 'new york city'
        elif city.lower() == 'chicago':
            return 'chicago'
        elif city.lower() == 'washington':
            return 'washington'
        else:
             print('Enter correct City name\n')
    return city

def get_filter():
    filter = ''
    while filter.lower() not in ['day', 'month', 'none']:
        filter = input('How would you like to filter the data - day or month or no filter. Type \'none\' for no filter\n')
        if filter.lower() not in ['day', 'month', 'none']:
            print('Please enter a valid selection\n')
    return filter

            # TO DO: get user input for month (all, january, february, ... , june)
def get_month():
    month = ' '
    month_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    while month.lower() not in month_dict.keys():
        month = input('\n Which month data are you interested in - January, February, March, April, May, or June?\n')
        if month.lower() not in month_dict.keys():
            print('\nPlease enter the correct month\n')
    month = month_dict[month.lower()]
    return month


        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

def get_day():
    day = ' '
    day_dict = {'m': 'Monday', 't': 'Tuesday', 'w': 'Wednesday', 'th': 'Thursday', 'f': 'Friday', 'sa': 'Saturday', 's': 'Sunday'}
    while day.lower() not in day_dict.keys():
        day = input('\nWhich day would you like to see - M, T, W, Th, F, Sa, S\n')
        if day.lower not in day_dict.keys():
            print('\nPlease enter a day of the week\n')
    day = day_dict[day.lower()]
    return day




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    months = ['January', 'February', 'March', 'April', 'May', 'June']
    ref = int(df['Start Time'].dt.month.mode())
    pop_month = months[ref - 1]
    print('\nThe most popular month is {}'.format(pop_month))

    # TO DO: display the most common day of week

    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ref = int(df['Start Time'].dt.dayofweek.mode())
    pop_day = day[ref]
    print('\nThe most popular day is {}'.format(pop_day))


    # TO DO: display the most common start hour

    ref = int(df['Start Time'].dt.hour.mode())
    print('\nThe most popular hour for start time in 24-hour format is {}'.format(ref))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    ref_start = df['Start Station'].mode().to_string(index = False)
    print('\nThe most commonly used start station is {}'.format(ref_start))
    # TO DO: display most commonly used end station
    ref_end = df['End Station'].mode().to_string(index = False)
    print('\nThe most commonly used end station is {}'.format(ref_end))

    # TO DO: display most frequent combination of start station and end station trip

    df['trip'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    ref = df['trip'].mode().to_string(index = False)
    print('\nThe most frequent combination of start station and end station is {}'.format(ref))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    mins, sec = divmod(total_time, 60)
    hour, mins = divmod(mins, 60)
    print('The total travel time is {} hours {} minutes and {} seconds'.format(hour, mins, sec))


    # TO DO: display mean travel time

    mean_time = round(df['Trip Duration'].mean())
    mins, sec = divmod(mean_time, 60)
    #if mins > 60:
    hour, mins = divmod(mins, 60)
    print('The average travel time is {} hours {} minutes and {} seconds'.format(hour, mins, sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # print value counts for each user type

    sub = (df['User Type'] == 'Subscriber').sum()
    cust = (df['User Type'] == 'Customer').sum()
    print('\nThe count of subscriber is {} and Customer is {}'.format(sub, cust))


    user_types = df['User Type'].value_counts()

    print(user_types)
    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        male = (df['Gender'] == 'Male').sum()
        female = (df['Gender'] == 'Female').sum()
        print('\nThe count of male is {} while female is {}'.format(male, female))


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        early_yb = int(df['Birth Year'].min())
        recent_yb = int(df['Birth Year'].max())
        common_yb = int(df['Birth Year'].mode())
        print('\nThe most earliest year of birth is {}'.format(early_yb))
        print('\nThe most recent year of birth is {}'.format(recent_yb))
        print('\nThe most common year of birth is {}'.format(common_yb))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    selection = input('Would you like to read some of the raw data? Yes/No ').lower()
    print()
    if selection=='yes' or selection=='y':
        selection=True
    elif selection=='no' or selection=='n':
        selection=False
    else:
        print('Please enter a valid choice. Try again.')
        display_data(df)
        return


    if selection:
        while 1:
            for i in range(5):
                print(df.iloc[i])
                print()
            selection = input('Another five? Yes/No ').lower()
            if selection=='yes' or selection=='y':
                continue
            elif selection=='no' or selection=='n':
                break
            else:
                print('Please enter a valid choice.')
                return





def main():
     while True:
        # Read city name (Either New York, Chicago or Washington)
        city = get_city()
        print('Retrieving data from {} for you...'.format(city))


        # Read csv file for the city selected
        df = pd.read_csv(CITY_DATA[city], parse_dates = ['Start Time', 'End Time'])


        df['Start Time'] = pd.to_datetime(df['Start Time'])
        # Read month and day
        filter = get_filter()
        if filter == 'month':
            month = get_month()
            df['month'] = df['Start Time'].dt.month
            df = df[df['month'] == month]

        elif filter == 'day':
            day = get_day()
            df['day'] = df['Start Time'].dt.weekday_name
            df = df[df['day'] == day]



        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()




 #References: github.com,google
