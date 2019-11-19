import datetime
import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'nyc':'new_york_city.csv',
              'new york':'new_york_city.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
              #reading the city bikeshare data


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print("-"*50)
    print('\nHello! Let\'s explore some US bikeshare data!')

    city = input('''Would you like to look at the data for Chicago, New York or Washington from the US Bikeshare data?\n''')
    city = city.lower()
    city = city.replace(" ", "")
    # Taking the user input for city (chicago, new york city, washington)
    while city not in ['chicago','newyorkcity','newyork','nyc','washington'] :
    	city = input("You have entered an invalid input.\nCheck the correct spelling of the city and enter here ")
    	city = city.lower()
    	city = city.replace(" ", "")

    # Taking the user input for month of the year starting from January to June
    month = input("\nSince we only have the bikesharing data starting from the month of January till the June,\nEnter a month from 'January to June' in case you want to filter by a specific month or enter 'all' to apply no filter\n")
    month = month.lower()
    while month not in ['january','february','march','april','may','june','all']:
    	month = input("\nYou have entered an invalid input.\nCheck the correct spelling of the month and enter month only from 'January to June' or 'all' :  ")
    	month = month.lower()

    # Taking the user input for the day of the week
    day = input("\nWould you want us to filter the data by any particular day of the week?\nIf yes, enter the day you want to filter your data by and if you do not want to filter the data by day, enter 'all' :\n")
    day = day.lower()
    while  day.lower() not in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']:
    	day = input("\nYou have entered an invalid input.\nCheck the correct spelling of the day and enter here :  ")
    	day = day.lower()
    print('-'*50)
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

    #converts the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracts month ,day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filters by month if user asks to
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filters by month to create the new dataframe
        df = df[df['month'] == month]

    # filters by day of week if user asks to
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

    print('\nCalculating The Most common Time of Travel.\n')
    start_time = time.time()

    # displays the most common month
    popular_month = df['month'].mode()[0]
    months=["January","February","March","April","May","June"]
    if month == "all" :
    	print("The most popular month is : ",months[popular_month-1])
    else:
    	print("The data has been filtered by the month of {}".format(month))

    # displays the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    if day == "all" :
    	print("The most popular day of the week is : ",popular_day)
    else :
    	print("The data has been filtered by the day of {}".format(day))
    # displays the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular hour is : ",popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating the in & out stations and the route with the highest number of subscribers.\n')
    start_time = time.time()

    # displays most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The start station with the maximum influx is the :",popular_start_station)

    # displays most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The end station with the maximum outflow is the :",popular_end_station)

    # displays most frequent round trip
    df['Station'] = df['Start Station'].str.cat(df['End Station'],sep="  --  ")
    popular_trip=df['Station'].mode()[0]
    print("The route with maximum number of subscribers is :",popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration.\n')
    start_time = time.time()

    # Displays the total travel time
    total_travel_time = df['Trip Duration'].sum()
    days,hours,minutes,seconds=convert_seconds(int(total_travel_time))
    print("The total duration of travel of all the users is : {} days, {} hours, {} minutes, {}seconds ".format(days,hours,minutes,seconds))

    # Displays the mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    days,hours,minutes,seconds=convert_seconds(int(mean_travel_time))
    print("The mean duration of travel of all the users is : {} days, {} hours, {} minutes, {}seconds ".format(days,hours,minutes,seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Statistics.\n')
    start_time = time.time()

    # Displays the counts of user types
    user_types = df['User Type'].value_counts()
    print("The type of user and their respective counts are ")
    print(user_types)

    if city != "washington" :

    	# Displays the count of gender
    	gender_count = df['Gender'].value_counts()
    	print("\n\nThe Genders\' of users and their respective counts are ")
    	print(gender_count)

    	# Displays the earliest, most recent, and most common year of births of the Users
    	oldest_birth = df['Birth Year'].min()
    	recent_birth = df['Birth Year'].max()
    	common_birth = df['Birth Year'].mode()[0]
    	oldest_birth , recent_birth , common_birth = int(oldest_birth),int(recent_birth),int(common_birth)
    	print("\n\nThe year of birth of the Oldest user is : {} \nThe year of birth of the youngest user is : {} \nThe most common year of birth of the users is : {}  ".format(oldest_birth,recent_birth,common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nIf you\'d like to start all over again, please enter yes else enter a no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
