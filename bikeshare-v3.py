import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday' ]
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city = input('Please select from the following cities: Chicago, New York or Washington? \n>').lower()
        #lower is used to get input in any format\n",
    "\n",
    while(True):
            if(city == 'chicago' or city == 'new york' or city == 'washington' or city == 'all'):
                break
            else:
                city = input('Enter Correct city:\n>').lower()
                 #lower is used to get input in any format\n",
        # get user input for month (all, january, february, ... , june)\n",
    month = input('Which month? January, February, March, April, May, or June?\n').lower()
         #lower is used to get input in any format\n",
    while(True):
            if(month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all'):
                break
            else:
                month = input('Enter valid month\n>').lower()
        # get user input for day of week (all, monday, tuesday, ... sunday)\n",
    day =  input('Which day ? monday, tuesday, wednesday, thursday, friday, saturday , sunday or all to display data of all days?\n>').lower()
         #lower is used to get input in any format\n",
    while(True):

            if(day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all'):
                break
            else:
                day = input('Enter Correct day:\n>').lower()
                 #lower is used to get input in any format\n",

        #return day\n",

    print('-'*40)
    return city, month, day


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


    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]


    if day != 'all':

        df = df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month:", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week:", most_common_day)

    # TO DO: display the most common start hour
    most_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour:", most_start_hour)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_start_station)

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].value_counts().idxmax()
    print("The most used end station:", most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most used start and end station: {}, {}"\
            .format(most_start_end_station[0], most_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time= df['Trip Duration'].sum()
    print("Total travel time:", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time= df['Trip Duration'].mean()
    print("Mean travel time:", mean_travel_time)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()

    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))

    print()

    if 'Gender' in df.columns:
        user_stats_gender(df)

    if 'Birth Year' in df.columns:
        user_stats_birth(df, start_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: Display counts of gender
def user_stats_gender(df):
    """Displays statistics of analysis based on the gender of bikeshare users."""


    print("Counts of gender:\n")
    gender_counts = df['Gender'].value_counts()

    for index,gender_count   in enumerate(gender_counts):
        print("  {}: {}".format(gender_counts.index[index], gender_count))

    print()




def user_stats_birth(df, start_time):
    """Displays statistics of analysis based on the birth years of bikeshare users."""

    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year']

    most_common_year = birth_year.value_counts().idxmax()
    print("The most common birth year:", most_common_year)

    most_recent = birth_year.max()
    print("The most recent birth year:", most_recent)

    earliest_year = birth_year.min()
    print("The most earliest birth year:", earliest_year)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def table_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating Dataset Stats...\n')

    # counts the number of missing values in the entire dataset
    number_of_missing_values = np.count_nonzero(df.isnull())
    print("The number of missing values in the {} dataset : {}".format(city, number_of_missing_values))

    # counts the number of missing values in the User Type column
    number_of_nonzero = np.count_nonzero(df['User Type'].isnull())
    print("The number of missing values in the \'User Type\' column: {}".format(number_of_missing_values))


def display_data(df):
    i = 0
    while (True):
        q = input('\n Do you want to see raw data? Enter yes or no.\n>')
        if (q == 'yes'):
            print (df.iloc[i:i+5])
            i+=5
        elif (q == 'no'):
            break
    return



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        table_stats(df, city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
