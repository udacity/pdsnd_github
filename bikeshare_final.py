import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago' 'chicago.csv',
              'new york city' 'new_york_city.csv',
              'washington' 'washington.csv' }

def get_filters()
    
    Asks user to specify a city to analyze.

    Returns
        (str) city 'Birth Year' in df1 - name of the city to analyze
    
    print('nTime to explore some US bikeshare data!')
    # TO DO get user input for city (chicago, new york city, washington). HINT Use a while loop to handle invalid inputs
    
    
    
    city = input(To view BikeShare information please choose one of the following cities Chicago, New York City, or Washington  ).lower()
    while city not in ('chicago', 'new york city', 'washington')
        print(nPlease choose Chicago, New York City, or Washington)
        city = input(To view BikeShare information please choose one of the following cities Chicago, New York City, or Washington  ).lower()
    print(nThank you for choosing {}..format(city).title())
    return city


    print('-'40)
    return city


def load_data(city)
    
    Loads data for the specified city.

    Args
        (str) city - name of the city to analyze
     
    Returns
        df1 - Pandas DataFrame containing city data
    
    df1 = pd.read_csv(CITY_DATA[city])

    return df1


def time_stats(df1)
    Displays statistics on the most frequent times of travel.

    print('nCalculating The Most Frequent Times of Travel...n')

    start_time = time.time()

    # TO DO display the most common month

#extract month from datetime
    df1['month'] = pd.DatetimeIndex(df1['Start Time']).month

#Calculate most popular month - it will be a number
    monthnum = df1['month'].mode().values[0]

#convert most popular month number to month name
    monthnum = 1

    if monthnum == 1
         monthname = Jan
    elif monthnum == 2
        monthname = Febr
    elif monthnum == 3
        monthname = Mar  
    elif monthnum == 4
       monthname = Apr
    elif monthnum == 5
       monthname = May
    elif monthnum == 6
       monthname = Jun


        
    print(nThe most popular month is {}..format(
        monthname))


    print(nThis took %s seconds. % (time.time() - start_time))
    print('-'40)

    # TO DO display the most common day of the week

#extract day of the week from datetime
    df1['dayofweek'] = pd.DatetimeIndex(df1['Start Time']).day

      
#Calculate most popular day - it will be a number
    daynum = df1['dayofweek'].mode().values[0]


#convert most popular day number to month name
    daynum = 1

    if daynum == 1
        dayname = Sun
    elif daynum == 2
        dayname = Mon
    elif daynum == 3
        dayname = Tue 
    elif daynum == 4
        dayname = Wed
    elif daynum == 5
        dayname = Thu
    elif daynum == 6
        dayname = Fri
    elif daynum == 7
        dayname = Sat
     
#print(dayname) tested and dayname is correct!

    print(nThe most popular day of the week is {}..format(
        dayname))

#extract day of the week from datetime
    df1['hourofday'] = pd.DatetimeIndex(df1['Start Time']).hour
      
#Calculate most popular day - it will be a number
    hournum = df1['hourofday'].mode().values[0]


#convert most popular day number to month name

    if hournum == 1
        hourname = 1am
    elif hournum == 2
        hourname = 2am
    elif hournum == 3
        hourname = 3am  
    elif hournum == 4
        hourname = 4am
    elif hournum == 5
        hourname = 5am
    elif hournum == 6
        hourname = 6am
    elif hournum == 7
        hourname = 7am
    elif hournum == 8
        hourname = 8am
    elif hournum == 9
        hourname = 9am
    elif hournum == 10
        hourname = 10am  
    elif hournum == 11
        hourname = 11am
    elif hournum == 12
        hourname = 12pm
    elif hournum == 13
        hourname = 1pm
    elif hournum == 14
        hourname = 2pm
    elif hournum == 15
        hourname = 3pm  
    elif hournum == 16
        hourname = 4pm
    elif hournum == 17
        hourname = 5pm
    elif hournum == 18
        hourname = 6pm
    elif hournum == 19
        hourname = 7pm
    elif hournum == 20
        hourname = 8pm
    elif hournum == 21
        hourname = 9pm
    elif hournum == 22
        hourname = 10pm  
    elif hournum == 23
        hourname = 11pm
    elif hournum == 24
        hourname = 12am

  
#print(hourname) tested and hourname is correct!

    print(nThe most popular hour of the day is {}..format(
        hourname))


def station_stats(df1)
    Displays statistics on the most popular stations and trip.

    print('nCalculating The Most Popular Stations and Trip...n')
    start_time = time.time()

    # TO DO display most commonly used start station
    print(nThe most popular starting station is {}..format(
        str(df1['Start Station'].mode().values[0])))

    # TO DO display most commonly used end station
    print(nThe most popular ending station is {}..format(
        str(df1['End Station'].mode().values[0])))

    # TO DO display most frequent combination of start station and end station trip
    df1['startendstation'] = df1['Start Station']+  to  +df1['End Station']
    print(nThe most popular trip from start station to end station is {}..format(
        str(df1['startendstation'].mode().values[0])))

    print(nThis took %s seconds. % (time.time() - start_time))
    print('-'40)


def trip_duration_stats(df1)
    Displays statistics on the total and average trip duration.

    print('nCalculating Trip Duration...n')
    start_time = time.time()

    # TO DO display total travel time
    print(nThe total travel time is {} years..format(
        str(df1['Trip Duration'].sum()31536000)))

    # TO DO display mean travel time
    print(nThe average travel time is {} minutes..format(
        str(df1['Trip Duration'].mean().astype(int)60)))

    print(nThis took %s seconds. % (time.time() - start_time))
    print('-'40)


def user_stats(df1)
    Displays statistics on bikeshare users.

    print('nCalculating User Stats...n')
    start_time = time.time()

    # TO DO Display counts of user types
##Old version that showed two columns of pandas table subcust and count
    #print(nThe number of Subscribers or Customers are)
    #print(df1['User Type'].value_counts())

    if 'User Type' in df1
        print(nThe number of Subscribers and Customers are)
        #print(df1['Gender'].value_counts()) old version that was pandas table
        utype_vals = [] 
        utype_vals = str(df1['User Type'].value_counts()).split()
        #print(utype_vals)  test of utype_vals
        print(nSubscriber    {}.format(utype_vals[1]))
        print(Customer       {}.format(utype_vals[3]))
    
    # TO DO Display counts of gender
#Old version that showed two columns of pandas table gender and count
#    if 'Gender' in df1
#       print(nThe number of Male and Female customers are)
#        print(df1['Gender'].value_counts())

    if 'Gender' in df1
        print(nThe number of Male and Female customers are)
        #print(df1['Gender'].value_counts()) old version that was pandas table
        gender_vals = [] 
        gender_vals = str(df1['Gender'].value_counts()).split()
        #print(gender_vals) test of gender_vals
        print(nMale     {}.format(gender_vals[1]))
        print(Female    {}.format(gender_vals[3]))

        
        
        
    # TO DO Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df1
        print(nThe earliest year of birth is {}..format(
            str(df1['Birth Year'].min().astype(int))))

        
        print(nThe most recent year of birth is {}..format(
            str(df1['Birth Year'].max().astype(int))))

        by = (nThe most common year of birth is {}..format(
            str(df1['Birth Year'].value_counts().head(1).astype(int))))
        print(by.split(.)[0]+'.')


    print(nThis took %s seconds. % (time.time() - start_time))
    print('-'40)


def main()
    while True
        city = get_filters()
        df1= load_data(city)

        time_stats(df1)
        station_stats(df1)
        trip_duration_stats(df1)
        user_stats(df1)

        
        dorestart = True
        doquestion = True
        while(doquestion)
            restart = input('nWould you like to restart Enter yes or no.n')
            if restart.lower() == 'yes'
                dorestart = True
                doquestion = False
                continue
            elif restart.lower() == 'no'
                dorestart = False
                doquestion = False
                break
            else
                print(Please answer Yes or No.)
                doquestion = True
         
        #End of Yes No question loop
        if dorestart == False
            break
    #end of restart for script
    
    
if __name__ == __main__
	main()