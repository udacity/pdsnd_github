import datetime 
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'newyorkcity': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city = input('''\nwhich city you want to explore its data Chicago, New York, or Washington?\n''') 
    city = city.lower()
    city = city.replace(" ", "")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in ['chicago','newyorkcity','washington'] :
    	city = input("Please enter either chicago, new york city or washington \n ")
    	city = city.lower()
    	city = city.replace(" ", "")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter the month to filter from 'January to June' or 'all' to apply no filter  :  ")
    month = month.lower()
    month = month.replace(" ", "")
    #to handle invalid inputs
    while month not in ['january','february','march','april','may','june','all']:
    	month = input("Please select month from 'January to June' or 'all' to apply no filter  :  ")
    	month = month.lower()
    	month = month.replace(" ", "")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the day of week to filter or 'all' to apply no filter  :  ")
    day = day.lower()
    day = day.replace(" ", "")
    #to handle invalid inputs
    while  day.lower() not in ['sunday','monday','tuesday','wednesday','thursday','saturday','all']:
    	day = input("Please select a valid day of the week or 'all' to apply no filter  :  ")
    	day = day.lower()
    	day = day.replace(" ", "")
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
    #load data into pandas dataframe 
    df = pd.read_csv(CITY_DATA[city])
    print(df.head()) 
    n   = 2
    while True:
        answer  = input('\n Would you like to display 5 more row of the raw data ? Press [yes/no] ')
        if answer == 'y' :
            print(df.head(5 * n))
            n += 1
        else :
            break
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month ,day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

   
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def convert_seconds(sec):
	"""Converts seconds into days,hours,minutes and seconds
	Args:
		 (int)sec: seconds in float
	Returns:
			days,hours,miuntes,seconds
	"""
	#computes days,hours and minutes
	d = datetime.timedelta(seconds=sec)
	minutes = d.seconds//60
	hour = minutes//60
	minutes=minutes%60
	hour=hour%60
	seconds = d.seconds
	seconds = seconds%60
	return d.days,hour,minutes,seconds


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    months=["January","February","March","April","May","June"]
    if month == "all" :
    	print("The most popular month is :  ",months[popular_month-1])
    else:
    	print("The filter for {} month is applied".format(month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    if day == "all" :
    	print("The most popular day of the week is :  ",popular_day)
    else :
    	print("The filter for {} day is applied".format(day))  
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular hour is :  ",popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most popular start station is :  ",popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most popular end station is :  ",popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Station'] = df['Start Station'].str.cat(df['End Station'],sep="  --  ")
    popular_trip=df['Station'].mode()[0]
    print("The most popular trip  is :  ",popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    days,hours,minutes,seconds=convert_seconds(int(total_travel_time))
    print("The total travel time is : {} days, {} hours, {} minutes, {}seconds ".format(days,hours,minutes,seconds))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    days,hours,minutes,seconds=convert_seconds(int(mean_travel_time))
    print("The mean travel time is : {} days, {} hours, {} minutes, {}seconds ".format(days,hours,minutes,seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Type and count are ")
    print(user_types)

    if city != "washington" :

    	# TO DO: Display counts of gender
    	gender_count = df['Gender'].value_counts()
    	print("\n\nGenders and  count are ")
    	print(gender_count)

    	# TO DO: Display earliest, most recent, and most common year of birth
    	oldest_birth = df['Birth Year'].min()
    	recent_birth = df['Birth Year'].max()
    	common_birth = df['Birth Year'].mode()[0]
    	oldest_birth , recent_birth , common_birth = int(oldest_birth),int(recent_birth),int(common_birth)
    	print("\n\nOldest Birth Year :  {} \nYoungest Birth Year :  {} \nMost Frequent Birth Year :  {}  ".format(oldest_birth,recent_birth,common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()