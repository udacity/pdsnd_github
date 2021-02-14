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
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    cities = ['chicago','new york','washington']
    days = ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']  
    valid_city_input=False
    while valid_city_input == False:
          city=input('Would like to filter the data based on city(chicago, new york,washington)?\n Please Enter the City Name : ')
          if city != '' and city.lower() in cities:
            valid_city_input=True
          else:
            valid_city_input=False  
    
    valid_month_input=False
    while valid_month_input == False:
          month=input('Would you like to filter the data based on the month (January,February,March,April,May,June)?\n Please enter the month name or type all : ')
          if month != '' and month.lower() in months:
            valid_month_input=True
          else:
            valid_month_input=False 
            print('Please provide a valid month ')
     
    valid_day_input=False
    while valid_day_input == False:
          day=input('Would you like to filter the data based on the day (sunday, monday,tuesday,wednesday,thursday,friday saturday)?\n Please enter the day name or type all : ')
          if day != '' and day.lower() in days:
            valid_day_input=True
          else:
            valid_day_input=False 
            
    

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
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month']= df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        df= df.loc[df['month'] == month.title()]
    if day != 'all':
        df= df.loc[df['day_of_week'] == day.title()]
       
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    
    popular_month=df['month'].mode()[0]
    print("Most Popular month %s" %popular_month)

    # TO DO: display the most common day of week
    
    #find the most popular day
    popular_day = df['day_of_week'].mode()[0]
    print("Most Popular day %s" %popular_day)
    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print("Most Popular Hour %s" %popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    popular_start_station= df['Start Station'].value_counts().idxmax()
   
    print('Most Popular Start Station  %s'%popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station= df['End Station'].value_counts().idxmax()
   
    print('Most Popular End Station  %s'%popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station=str(df.groupby(['Start Station','End Station'] ).size().idxmax())
    print('Most Popular Start Station and End Station %s '%popular_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration'].sum()
    print('Total Trip Duration %s'%trip_duration)
    
    trip_average=  df['Trip Duration'].mean()
    print('Average Travel Time %s' %trip_average)


    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of each User Type %s'%df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('Counts of Each Gender Type %s'%df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('Earliest, most recent and most common  year of birth %s %s %s'%(int(df['Birth Year'].min()),int(df['Birth Year'].max()),int(df['Birth Year'].mode()[0])))
       

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        start=0
        end=5
        while True:
            prompt = input('Would you like to look at the Raw Data(yes or no)?')
            if prompt.lower() != 'yes':
                break             
            print(df.iloc[start:end])
            start=end
            end = start + 5               
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
