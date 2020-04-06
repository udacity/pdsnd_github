import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    month = ""
    day = ""
    city_list = ['Chicago', 'New York City', 'Washington']
    city_check = False
    while city_check == False:
        city = input("Please select a city name from this list: chicago, new york city, washington: ").title()
        if city in city_list:
            break
        else:
            print("City entered is incorrect!")
            continue
        
   
    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['All','January','February','March','April','May','June']
    month_check = False
    while month_check == False:
        month = input("Please select a month from this list [January,February,March,April,May,June] or select All for all the months: ").title()
        if month in month_list :
            break
        else:
            print("Month entered is incorrect!")
            continue
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_week_list = ['All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day_of_week_check = False
    while day_of_week_check == False:
        day = input("Please select a day from this list: All,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday : ").title()
        if day in day_of_week_list:
            break
        else:
            print("Day of Week entered is incorrect!")
            continue
        

    print('-'*150)
    #print(city,month,day)
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January','February','March','April','May','June']
    print("The most common month is {} ".format(months[df['month'].mode()[0]-1]))


    # TO DO: display the most common day of week
   
    print("The most common day of week is {} ".format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print("The most common hour is {} ".format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*150)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_counts = df['Start Station'].value_counts()
    
    print("The most commonly used start station is {} and the count is {}".format(df['Start Station'].mode()[0], start_station_counts[0]))


    # TO DO: display most commonly used end station
    end_station_counts = df['End Station'].value_counts()
    
    print("The most commonly used end station is {} and the count is {}".format(df['End Station'].mode()[0], end_station_counts[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station']+df['End Station']
    combo_station_counts = df['combo'].value_counts()
    
    print("The most commonly used combination of stations is {} and the count is {}".format(df['combo'].mode()[0], combo_station_counts[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*150)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is {}".format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print("The mean travel time is {}".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*150)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types is \n {}".format(user_types))

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print("The count of gender is \n {}".format(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    print("The earliest year of birth is {}".format(int(df['Birth Year'].min())))
    print("The most recent year of birth is {}".format(int(df['Birth Year'].max())))
    print("The most common year of birth is {}".format(int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*150)

def user_stats_washington(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types is \n {}".format(user_types))

    # TO DO: Display counts of gender

    print("The count of gender is not available for washington City.")

    # TO DO: Display earliest, most recent, and most common year of birth
    print("The earliest year of birth is not available for washington City.")
    print("The most recent year of birth is not available for washington City.")
    print("The most common year of birth is not available for washington City.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*150)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
 
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city == 'Washington':
            user_stats_washington(df)
        else:
            user_stats(df)
        # ask user for seeing raw data
        n = 0 #default rows for the user
        view_data = input('\n Would you like to see the raw data? Enter yes or no. \n')
        while view_data == 'yes':
            print(df.loc[n:n+4,:])
            view_data = input('\n Would you like to see the raw data? Enter yes or no. \n')
            if view_data == 'yes':
                n +=5
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
