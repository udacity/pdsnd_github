import time
import pandas as pd
import numpy as np
import math
days=['all', 'monday','tuesday', 'wednesday', 'thursday', 'Friday',  'saturday', 'sunday']
months=['all', 'january', 'february','march','april','may',  'june']


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
    cities=('chicago', 'new york city', 'washington')
    while True:
        city =input("what the city you want chicago, new york city or washington ")
        city=city.lower()
        if city in cities :
            break
    

    # TO DO: get user input for month (all, january, february, ... , june)
    months=('all', 'january', 'february','march','april','may',  'june')
    while True:
        month=input("which month you want (all, january, february, ... , june) ")
        month=month.lower()
        if month in months :
            break
    


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=('all', 'monday','tuesday', 'wednesday', 'thursday', 'Friday',  'saturday', 'sunday')
    while True:
        day=input("which day  you want (all, monday, tuesday, ... sunday) ")
        day=day.lower()
        if day in days :
            break
   
     



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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.weekday_name
  
    if month !='all':
        month=months.index(month)
        df=df[df['month']==month]
    
 
   
    if(day !='all'):
        day=day.title()
        df=df[df['day']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    monthFrequent=df['month'].mode()[0]
    print("display the most common month is "+months[monthFrequent])
    


    # TO DO: display the most common day of week
    frqday=df['day'].mode()[0]
    print("display the most common day of week is ",frqday)
    

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    frqhour=df['hour'].mode()[0]
    print("display the most common start hour is ",frqhour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    frqstart=df['Start Station'].mode()[0]
    
    print("most common start station is "+frqstart)
    
    # TO DO: display most commonly used end station
    frqend=df['End Station'].mode()[0]
    
    print("most common End station is "+frqend)


    # TO DO: display most frequent combination of start station and end station trip
    df['trip']=df['Start Station']+' to '+df['End Station']
    frqtrip=df['trip'].mode()[0]
    print("most frequent combination of start station and end station trip "+frqtrip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
     
    print("total travel time is: ",df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print("mean travel time is: ",df['Trip Duration'].mean())

    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types is: ",df['User Type'].value_counts())
   
    if city!= 'washington' :
        # TO DO: Display counts of gender
        print("counts of gender is: \n",df['Gender'].value_counts())


        # TO DO: Display earliest, most recent, and most common year of birth
        temp=np.sort(df['Birth Year'])
        print("earliest birth year ", int(np.sort(df['Birth Year'])[0]))
        i= -1
        while math.isnan(temp[i]):
            i-= 1

        print("recent birth year ", int(temp [i]))


        print(" most common year of birth",df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    start=0
    limite=5
    while True:
        choix=input("do you want to see 5 raw of data? enter 'yes' or 'no' ")
        
        

        if choix=='yes':
            while start<limite:
                print(df.iloc[start])
                start+=1
            limite+=5
                
                
            #print(df[start:start+5])
            #start+=5
             
        else :
            break
            
            

def main():
    #df = load_data('chicago', 'all', 'all')
    
    
    #user_stats(df)

    #trip_duration_stats(df)
    #station_stats(df)
    #time_stats(df)
    
    
    #exit()
    while True:
        city, month, day = get_filters()
        
        
        df = load_data(city, month, day)

        
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
