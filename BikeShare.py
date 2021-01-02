import time
import pandas as pd
import numpy as np
#from tabulate import tabulate

CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv' }

MONTHS_TO_INDEX = {'JAN': '1','FEB': '2','MAR': '3','APR': '4','MAY': '5','JUN': '6' ,'ALL': 'ALL'}

INDEX_TO_MONTH = {1 : 'January', 2 : 'February', 3 : 'March', 4 : 'April', 5 : 'May', 6 : 'June'}

DAY_TO_INDEX = {'MON': 0,'TUE': 1,'WED': 2,'THU': 3,'FRI': 4,'SAT': 5,'SUN': 6,'ALL':'ALL'}

INDEX_TO_DAY = {0: 'Monday',1: 'Tuesday',2: 'Wednesday',3: 'Thursday',4: 'Friday',5: 'Saturday',6: 'Sunday'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    
    city_found, month_found, day_found = False, False, False

    while True:
        #get user input (chicago, new york city, washington). HINT: Use a while loop to handle invalid input
        if not city_found:
            city = input("we have 3 cities available to explore: Chicago, Washington, New York City. Please select one: ")
            city = city.lower()
            if city not in CITY_DATA:
                print("Invalid city or data data not available, please choose one of the 3 : Chicago, Washington, New York City")
                continue
            else:
                city_found = True
        print('\n')
   
    
        # get user input for month (all, january, february, ... , june)
        if not month_found:
            month = input("Enter month you want to explore. Choose one of: JAN, FEB, MAR, APR, MAY, JUN, ALL. ALL denotes data for all months:")
            month = month.upper()
            if month not in MONTHS_TO_INDEX:
                print("Invalid month entered!!! Enter a valid month!!!!")
                continue
            else:
                month_found = True
        print('\n')

        # get user input for day of week (all, monday, tuesday, ... ,sunday)
        day = input("Enter day you want to explore. Choose one of: MON, TUE, WED, THU, FRI, SAT, SUN, ALL. ALL denotes data for all days:")
        day = day.upper()
        if day not in DAY_TO_INDEX:
            print("invalid day entered!!! Enter a vlaid day!!!")
            continue
        else:
            break

    print('-' *40)
    print('/n')
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
    start_time = time.time()
    print("Begin data processing !!!") 

    df = pd.read_csv(CITY_DATA.get(city))

    # extract start month from the Start time column to create Start month column
    df['Start Month'] = pd.to_datetime(df['Start Time']).dt.month

    # extract start hour from the Start Time column to create an Start Hour column
    df['Start Day'] = pd.to_datetime(df['Start Time'], format = '%Y-%m-%d %H:%M:%S').dt.dayofweek

    # extract Start Hour from the Start Time column to create an Start Hour column
    df['Start Hour'] = pd.to_datetime(df['Start Time']).dt.hour

    # filter on month, if month is specified
    if month != MONTHS_TO_INDEX.get('ALL'):
        df = df[df['Start Month'] == int(MONTHS_TO_INDEX.get(month))]

    # filter on day, if day is specified
    if day != DAY_TO_INDEX.get('ALL'):
        df = df[df['Start Day'] == int(DAY_TO_INDEX.get(day))]

    print("Data processing completed !!!")
    print("This took %s seconds." % (time.time() - start_time))    
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == MONTHS_TO_INDEX.get('ALL'):
        popular_month = df['Start Month'].dropna()
        if popular_month.empty:
            print("No popular month for for the filter specified!! Please adjust your filter!!")
        else:
            popular_month = popular_month.mode()[0]
            print("Most popular month for renting is :{}".format(INDEX_TO_MONTH.get(popular_month)))
    else:
        print("As you have chosen month: {} as filter, most popular month fot renting won\'t be calculated".format(month))

    # display the most common day of week
    if day == DAY_TO_INDEX.get('ALL'):
        popular_day = df['Start Day'].dropna() #.mode()[0]
        if popular_day.empty:
            print('No popular day found for the filters specified!! Please adjust your filter!!!')
        else:
            popular_day = popular_day.mode()[0]
            print('Most popular day for renting is : {}'.format(INDEX_TO_DAY.get(popular_day)))
    else:
        print('As you have chosen {} day as filter, most day for renting won\'t be calculated'.format(day.title()))

    # display the most common start hour
    popular_start_hour = df['Start Hour'].dropna()
    if popular_start_hour.empty:
        print('No popular start hour found for the filter specified!! Please adjust your filter !!!')
    else:
        popular_start_hour = popular_start_hour.mode()[0]
        print('Most popular renting start hour is: {}:00 hrs'.format(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    
def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Args:
        param1 (df): The data frame you wish to work with.
        
    Returns:
        None.    
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station: {common_start_station}")
    
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"\nThe most commonly used end station: {common_end_station}")
              
    # display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep = ' to ')
    combo = df['Start To End'].mode()[0]
    
    print(f"\nThe most frequent combination of trips are from {combo}.")
              
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    
    Args:
        param1 (df): The data frame you wish to work with
        
        
    Returns:
        None.    
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print(f"The total trip duration is {hour} hours, {minute} minutes and {second} seconds.")

    # display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    mins, sec = divmod(average_duration, 60)
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average trip dusration is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average trip duration is {mins} minutes and {sec} seconds.")
        
    print(f"\nThis took {(time.time() - start_time)} seconds")
    print('-'*80)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].dropna()

    if user_type.empty:
        print('No data available for specified filter, please adjust your filter!!')
    else:
        user_type = user_type.value_counts()
        print('User type details for the filter specified : {}'.format(user_type))

    # Display counts of gender
    if 'Gender' in df:
        user_gender = df['Gender'].dropna()
        if user_gender.empty:
            print('No data available for specified filter, please adjust your filter!!')
        else:
            user_gender = user_gender.value_counts()
            print('User gender count : {}'.format(user_gender))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        birth_years = df['Birth Year'].dropna()
        if birth_years.empty:
            print('No data available for specified filter, please adjust your filter!!')
        else:
            user_birth_year = df['Birth Year'].dropna()
            if user_birth_year.empty:
                print('No data available for specified filter, please adjust your filter!!')
            else:
                oldest_user = user_birth_year.min()
                print('Earliest year ofbirth for the selected filter : {}'.format(int(oldest_user)))
            
                youngest_user = user_birth_year.max()
                print('Most recent year of birth for the selected filter : {}'.format(int(youngest_user)))
            
                most_common_year_of_birth = user_birth_year.mode()[0]
                print('Most common year of birth for the selected filter : {}'.format(int(most_common_year_of_birth)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def show_raw_data(df):
    """method to print the selected data frame, 5 at a time"""

    BIN_RESPONSE_LIST = ['yes', 'no']
    rdata = ''
    counter = 0
    while rdata not in BIN_RESPONSE_LIST:
        print("\nDo you wish to view the raw data? Enter yes or no")
        rdata = input().lower()
        if rdata == "yes":
            print(df.head())
        elif rdata not in BIN_RESPONSE_LIST:
            print("\nPlease check your input.")
            print("Input does not match any of accepted responses.")
            print("\nRestarting...\n")
            
    while rdata == "yes":
        print("Do you wish to view more raw data?")
        counter += 5
        rdata = input().lower()
        
        if rdata == "yes":
            print(df[counter: counter + 5])
        elif rdata != "yes":
            break
            
        print('-'*80) 

def main():
    while True:
        city, month, day = get_filters()
        print("Input to be proecessed -> City : {}, Month : {}, Day : {}".format(city, month, day))
        
        df = load_data(city, month, day)

        if df.empty:
            print("No data found for specified filter, please adjust your filters!!!")
            continue
        
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
