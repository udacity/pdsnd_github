import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city,month,day):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        print('Please slect the city for explore Bikeshare data!')
        city = input('Select the city name from "chicago","new york city" and "washington" :').lower()
        if city not in ("chicago","new york city", "washington"):
            print("\nPlease check the city name")
            continue
        else:
            break

    print("Please select how to filter data ")

    user_input = input('"month","day" or "both": ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)

    while True :
        if user_input not in ("month","day","both" ):
            print('\nPlease check again how to filter data :')
            user_input = input('"month","day",or "both": ').lower()
        elif user_input == 'month':
            print('Please select the month to explore :')
            month = input('"all", "january", "february","march","april","may" ,"june":').lower()

            day = 'all'
            while True:
                if month not in ["all", "january", "february","march","april","may" ,"june"]:
                    print("Please insert the month like to explore!: ")
                    month = input('"all", "january", "february","march","april","may" ,"june":').lower()
                else:
                    break
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

        elif user_input == 'day':
            print('Please select the day to explore :')
            day = input('"monday", "tuesday", "wednesday", "thursday", "friday", "saterday", "sunday" or "all":').lower()
            month = 'all'
            while True:
                if day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saterday", "sunday","all"]:
                    print("Please insert the day like to explore!: ")
                    day = input('"monday", "tuesday", "wednesday", "thursday", "friday", "saterday", "sunday" or "all":').lower()
                else:
                    break
            break


        elif user_input == 'both':
            print('Please select the month to explore :')
            month = input('"all", "january", "february","march","april","may" ,"june":').lower()

            while True:
                if month not in ["all", "january", "february","march","april","may" ,"june"]:
                    print("Please insert the month like to explore!: ")
                    month = input('"all", "january", "february","march","april","may" ,"june":').lower()
                else:
                    break

            print('Please select the day to explore :')
            day = input('"monday", "tuesday", "wednesday", "thursday", "friday", "saterday", "sunday" or "all":').lower()

            while True:
                if day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saterday", "sunday","all"]:
                    print("Please insert the day like to explore!: ")
                    day = input('"monday", "tuesday", "wednesday", "thursday", "friday", "saterday", "sunday" or "all"').lower()
                else:
                    break

            break

    print('Selected City Name: ', city)
    print('Selected Month Name: ',month)
    print('Selected day: ', day)


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA [city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month']== month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]

    print('Most Popular Month is: ',popular_month)


    # TO DO: display the most common day of week
    df['week'] = df['Start Time'].dt.weekday_name
    popular_day_week = df['week'].mode()[0]

    print('Most Popular Day of week: ',popular_day_week)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour: ',popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Used Start station is :',popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Used End Station is: ',popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['combined_station'] = df['Start Station'] + ' to ' +df['End Station']
    popular_combined_station = df['combined_station'].mode()[0]
    print('Most frequent combined station is: ',popular_combined_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total Travel Time: ',total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Average Travel Time: ',mean_travel_time)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print('User Types :', user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('Count of Gender: \n',gender)
    else:
        print ('No gender information avilable for your selected city!')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest Birth Year: ',earliest_birth_year)

        recent_birth_year = df['Birth Year'].max()
        print ('Recent Birth Year: ',recent_birth_year)

        common_birth_year = df['Birth Year'].mode()[0]
        print('Most Common Birth Year: ',common_birth_year)

    else:
        #print('Birth information is not avilable for your select city !!')
        print('no birth information avilable for selcted city!!')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):

    dis_data = input('\nDo you want to display csv data? \nPlease select "yes" or "no": ').lower()
    if dis_data in ("yes"):
        i = 0
        while True:
            print(df.iloc[i:i+5])
            i += 5
            display_more = input('\nDo you want to display more data? \nPlease select "yes" or "no": ').lower()
            if display_more not in ("yes"):
                break





def main():

    city = ""
    month = 0
    day = 0

    while True:
        city, month, day = get_filters(city,month,day)
        df = load_data(city, month, day)

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
