import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = 'None'
    while city not in CITY_DATA:
        city = input('Please, input a valid city: ').lower()
        if city in CITY_DATA:
            print('valid city !')
            city_file = CITY_DATA[city]
        else: 
            city = 'chicago'
            city_file = CITY_DATA[city]
            print('The city is unregistered or does not exist. Defining Chicago as default value')
            
    city = city_file
    # TO DO: get user input for month (all, january, february, ... , june)
    months_valid = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input ('Enter a month or all: ').lower()
    if month not in months_valid:        
        print('No data for this month or does not exist. Placed to all by default')
        month = 'all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_valid = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
    day = input ('Enter a week day or all: ').lower()
    if day not in days_valid:        
        print('No data for this day or does not exist. Placed to all by default')
        day = 'all'

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
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
# filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    try:
        # TO DO: display the most common month
        month_clist = df['month'].value_counts()
        #print (month_clist)
        month_max = month_clist.max()
        month_id = month_clist[month_clist == month_max].index[0]
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        mc_month = months[month_id-1]
        print('The most common month is {}\n'.format(mc_month.title()))

        # TO DO: display the most common day of week
        day_clist = df['day_of_week'].value_counts()
        #print(day_clist)
        day_max = day_clist.max()
        mc_day = day_clist[day_clist == day_max].index[0]
        print('The most common day is {}\n'.format(mc_day))

        # TO DO: display the most common start hour
        df['Hour'] =  df['Start Time'].dt.hour
        hour_clist = df['Hour'].value_counts()
        #print(hour_clist)
        hour_max = hour_clist.max()
        mc_Hour = hour_clist[hour_clist == hour_max].index[0]
        print('The most common start hour is {}h\n'.format(mc_Hour))
    except:
      print('ERROR: Data for times of travel missing or corrupted !\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    try:
        # TO DO: display most commonly used start station    
        sstation_clist = df['Start Station'].value_counts()
        #print(sstation_clist)
        sstation_max = sstation_clist.max()
        mc_sstation = sstation_clist[sstation_clist == sstation_max].index[0]
        print("The most common used start station is '{}'\n".format(mc_sstation))

        # TO DO: display most commonly used end station
        estation_clist = df['End Station'].value_counts()
        #print(estation_clist)
        estation_max = estation_clist.max()
        mc_estation = estation_clist[estation_clist == estation_max].index[0]
        print("The most common used end station is '{}'\n".format(mc_estation))

        # TO DO: display most frequent combination of start station and end station trip
        df['Duo Station'] = df['Start Station']+df['End Station']
        dstation_clist = df['Duo Station'].value_counts()
        #print(dstation_clist)
        dstation_max = dstation_clist.max()
        mc_dstation = dstation_clist[dstation_clist == dstation_max].index[0]
        mc_sdstation = df[df['Duo Station']==mc_dstation]['Start Station'].values[0]
        mc_edstation = df[df['Duo Station']==mc_dstation]['End Station'].values[0]
        print("The most common used duo of stations is '{}' (start) and '{}' (end)\n".format(mc_sdstation,mc_edstation))
    except:
        print('ERROR: Data for stations missing or corrupted !\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
   
    try:
    # TO DO: display total travel time        
        total_travel_time = df['Trip Duration'].sum()          
        total_travel_time_h = int(total_travel_time // 3600)
        total_travel_time_res =int(total_travel_time % 3600)
        total_travel_time_min = int(total_travel_time_res // 60)
        total_travel_time_sec = int(total_travel_time_res % 60)
        print("The total travel time is {} hours, {} minutes, {} seconds (total: {} seconds)\n".format(total_travel_time_h, total_travel_time_min, total_travel_time_sec,total_travel_time))

        # TO DO day mean travel time
        mean_travel_time =  df['Trip Duration'].mean()
        mean_travel_time_h =  int(mean_travel_time // 3600)
        mean_travel_time_res = int(mean_travel_time % 3600)
        mean_travel_time_min = int(mean_travel_time_res // 60)
        mean_travel_time_sec = int(mean_travel_time_res % 60)
        print("The mean travel time is {} hours, {} minutes, {} seconds (total: {} seconds)\n".format(mean_travel_time_h, mean_travel_time_min, mean_travel_time_sec, mean_travel_time))

    except:
        print('ERROR: Data for travel time missing or corrupted !\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    try:
        usertypes = df['User Type'].value_counts()
        print("The counts of user types is the following: \n\n{} \n".format(usertypes.to_string()))
    except:
        print('ERROR: Data for user type missing or corrupted !\n')
    # TO DO: Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print("The counts of genders  is the following: \n\n{} \n".format(genders.to_string()))
    except:
        print('ERROR: Data for gender missing or corrupted !\n')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_by = int(df['Birth Year'].min())
        recent_by = int(df['Birth Year'].max())
        common_by = int(max(df['Birth Year'].mode()))
        print("The earliest, most recent and most common years of birth are respectively {}, {} and {}\n".format(earliest_by, recent_by, common_by))
    except:
        print('ERROR: Data for Birth Year missing or corrupted !\n')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_df(df):
    try:
        i = int(input ('Do you want to access the first 5 data of the dataframe (0 = yes) ? '))
    except:
        i = 1
    k = 0
    while i == 0:
        try:
            print (df[k:k+5])
            k+= 5
            i = int(input ('Do you want to display the following 5 data (0 = yes) ? '))
        except:
            break
    print ('\nEnd of dataframe verification')
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_df(df)
        time_stats(df)
        display_df(df)
        station_stats(df)
        display_df(df)
        trip_duration_stats(df)
        display_df(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
