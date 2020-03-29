import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#definition of input month function.
def get_month():
    month_option=['january','february','march','april','may','june','july','august','september','october','november','december']
    while True:
        month =input('\nWhich month? Choose junuary, february, march, april, may, june, july, august, september, october, november or december\n') 
        month=month.lower()
        if(month in month_option):
            break
    return month
#definition of input day function.
def get_day():
    days_option=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    while True:
        day =input('\nWhich day? Choose sunday, monday, tuesday, wednesday, thursday, friday or saturday\n') 
        day=day.lower()
        if(day in days_option):
            break
    return day
#definition of filters function
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, New York City, Washingon)
    city_option=['chicago','new york city','washington']
    while True:
        city =input('\nPlease choose one of the following cities (chicago, new york city, washington)\n')
        city=city.lower()
        if(city in city_option):
            break
    # get user input for filters (month, New day, both, not at all)
    while True:
        filter_option=[1,2,3,4]
        filter =input('\nWould you like to filter using\n1:month\n2:day\n3:both\n4:not at all\nType 1, 2, 3, or 4\n')
        filter=int(filter)
        if(filter in filter_option):
            break
    if(filter==1):
        # get user input for month (Junuary, february, ...etc)
        month=get_month()
        day='all'
    elif(filter==2):
        day=get_day()
        month='all'
    elif(filter==3):
        # get user input for month and day
        month=get_month()
        day=get_day()
    elif(filter==4):
        day='all'
        month='all'
    
    print('-'*40)
    return city, month, day
#definition of load data function
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
    df['day'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month) + 1
        # filter by month to create the neyesw dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
    return df
#definition of most common month function
def common_month(df):
    df['month'] = df['Start Time'].dt.month_name()
    popular_month=df['month'].mode()[0]
    print('Most Popular Start Month:',popular_month)
#definition of most common day function
def common_day(df):
    df['day'] = df['Start Time'].dt.day_name()
    popular_day=df['day'].mode()[0]
    print('Most Popular Day:',popular_day)
#definition of most common start hour function
def common_start_hour(df):
    df['hour'] = df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('Most Popular Start Hour:',popular_hour)
#definition of most frequent times of travel function
def time_stats(df, month, day):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if(month=='all' and day=='all'):
        # display the most common month
        common_month(df)
        # display the most common day of week
        common_day(df)
        # display the most common start hour
        common_start_hour(df)
    elif(month!='all' and day=='all'):
        # display the most common day of week
        common_day(df)
        # display the most common start hour
        common_start_hour(df)
    elif(month=='all' and day!='all'):
        # display the most common start hour
        common_start_hour(df)
        # display the most common month
        common_month(df)
    elif(month!='all'and day!='all'):
        common_start_hour(df)
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#definition of the most popular stations and trip function
def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('Most Popular Start Station:',popular_start_station)
    # display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('Most Popular End Station:',popular_end_station)
    # display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'].map(str) + '&' + df['End Station']
    popular_start_end = df['Start End'].value_counts().idxmax()
    print('Most Popular most frequent combination of start station and end station: ',popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#definition of trip duration stats function
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total Travel Time:',total_travel_time)
    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean Travel Time:',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#definition of the statistics on bikeshare users function
def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print('User Type:\n',user_types)
    if city=='new york city' or city=='chicago':
          # Display counts of gender
          gender_types = df['Gender'].value_counts()
          print('Gender Type:\n',gender_types)
          # Display earliest, most recent, and most common year of birth
          earliest_year_birth = int(df['Birth Year'].min())
          print('Earliest Year Birth: ',earliest_year_birth)
          most_recent_year_birth =int(df['Birth Year'].max())
          print('Most Recent Year Birth: ',most_recent_year_birth)
          most_common_year_birth = int(df['Birth Year'].mode()[0])
          print('Most common Year Birth: ',most_common_year_birth)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def main():
    while True:
        city, month, day = get_filters()
        load_data(city, month, day)
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        flag=1
        start=0
        end=5
        while(flag ==1):
            flag=int(input('\nWould you like to view individual trip data? \nType 1 or 2 \n1:True\n2:False\n'))
            while((flag != 1) and (flag!=2)):
                flag=int(input('\nPlease enter available input: '))
            print(df.iloc[start:end])
            start+=5
            end+=5
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        restart = restart.lower()
        while((restart != 'yes') and (restart !='no')):
            restart=input('\nPlease enter available input: ')
        if restart == 'no':
            break
        elif restart =='yes':
            continue


if __name__ == "__main__":
	main()
