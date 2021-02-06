import time
import pandas as pd
import numpy as np

#i used https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html for finding df methods

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv'}

FILTER_NAME = {'month', 'day', 'both', 'none'}

MONTHS = {'january', 'february', 'march', 'april', 'may', 'june'}

DAYS = {'1', '2', '3', '4', '5', '6', '0'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) filter - filter to choose, by month, by day both or none
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    #Get the city to analyze later
    while True:
        city = input('Whould you like to see the data for Chicago, New York, or Washington?\n').lower()
        if city in CITY_DATA:
            city
            break
        else:
            print("\nOops! Looks like you didn't type in one of the stored cities! Try again!")
    
    print('-'*40)
    
    #Get the time filters to analyze later
    while True:
        filtername = input('Whould you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.\n').lower()
        if filtername in FILTER_NAME:
            filtername
            break
        else:
            print("\nOops! Looks like you didn't type in one of the stored months! Try again!")  

    print('-'*40)
    
    days=""
    months=""
    
    #Filter by month if user asks for it
    if filtername=='month' or filtername=='both':
        months =isMonth()     

    #Filter by month if user asks for it
    if filtername=='day' or filtername=='both':
        days=isDay()

            
    return city, months, days


def isMonth():
    """
    Function to ask input from user to choose which month

    Returns:
        (str) month - name of the month to filter by
    """
    while True:
        month = input('Which month? January, Februrary, March, April, May, or June?\n').lower()
        if month in MONTHS:
           month
           break
        else:
            print("\nNo data available for " + month)  
    print('-'*40)
    return month
    
def isDay():
    """
    Function to ask input from user to choose which day

    Returns:
        (str) day - name of the day to filter by
    """
    while True:
        day = input('Which day?\n').lower()
        if day in DAYS:
            day
            break
        else:
            print("\n No data available for day " + day)  
    print('-'*40)
    return day
    
def load_data(city, month, day):
    """new york
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
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.dayofweek
    
    
    #Filter by month if user choose
    if month != '':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]
        
    #Filter by day if user choose
    if day != '':
        day = int(day)
        df = df[df['Day of Week'] == day]
        
    return df
    
def time_stats(df, month, day):
    """
    gets filtered dataframe and give popularity statistics
    Args:
        (df) dataframe - filtered dataframe according to filters
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (int) day - number of the day beginning from monday
    Print:
        Popular, day, month and hour
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #According to filters give corresponding popular day, month and hour.
    if day == '' and month == '':
        commonMonth(df)
        commonDay(df)
        commonHour(df)
    elif month == '':
       commonMonth(df)
       commonHour(df)
    elif day == '':
       commonDay(df)
       commonHour(df)
    else:
        commonHour(df)        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def commonMonth(df):
    """
    calculates popular month from filtered data

    Args:
        (df) dataframe - filtered dataframe according to filters
    Print:
        Popular month
    """
    all_month= {0: 'January', 1: 'February', 2: 'March',
                 3: 'April', 4: 'May', 5: 'June'}
    popular_month = df['Month'].mode()[0]
    print("The Most Common Month: " + str(all_month.get(popular_month)))

def commonDay(df):
    """
    calculates popular day from filtered data

    Args:
        (df) dataframe - filtered dataframe according to filters
    Print:
        Popular day
    """
    all_day= {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
                 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6:'Sunday'}
    popular_day = df['Day of Week'].mode()[0]

    print("The Most Common Day: " + all_day.get(popular_day))
    
def commonHour(df):
    """
    calculates popular hour from filtered data

    Args:
        (df) dataframe - filtered dataframe according to filters
    Print:
        Popular hour
    """
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    print("The Most Common Hour: " + str(popular_hour))

def station_stats(df):
    """
    calculates station statistics from filtered data

    Args:
        (df) dataframe - filtered dataframe according to filters
    Print:
        Most popular start station, end station and most popular combination
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # gives most popular start station
    startStation = df['Start Station'].mode()[0]
    print('The Most Popular Start Station is ' + startStation)

    # gives most popular end station
    endStation = df['End Station'].mode()[0]
    print('The Most Popular End Station is '+ endStation)
    
    # gives most frequently used combination of start station and end station
    comboStations = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).reset_index(name="combo")
    
    popStartStation = comboStations['Start Station'][0]
    popEndStation = comboStations['End Station'][0]
    print('The Most Frequent Combination: ' + popStartStation + ' - ' + popEndStation)   
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """
    Calculates duration statistics from filtered data

    Args:
        (df) dataframe - filtered dataframe according to filters
    Print:
        Average and total time
    """
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    #gives average travel time
    averageTime = str(df['Trip Duration'].mean())
    print('Average Travel Time is ' + averageTime + ' seconds' )

    #gives total travel time in seconds
    totalDuration = str(df['Trip Duration'].sum())
    print('The total trip duration is ' + totalDuration + ' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """    
    Calculates User based statistics from filtered data
    Args:
        (df) dataframe - filtered dataframe according to filters
    Print:
        Counts of user types, counts of gender, earliest, most recent, and most common year of birt
    """
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    countUserType = df['User Type'].value_counts()  
    printer(countUserType)
    print('-'*40)

    # TO DO: Display counts of gender
    try:
        countGender= df['Gender'].value_counts()
        printer(countGender)
    except:
        print("\nGender data is not available")
    print('-'*40)
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        minBirth = int(df['Birth Year'].min())
        recentBirth = int(df['Birth Year'].max())
        commonBirth = int(df['Birth Year'].mode()[0])
        print("\nThe earliest year of birth: " + str(minBirth));
        print("\nThe most recent year of birth: " + str(recentBirth));
        print("\nThe most common year of birth: " + str(commonBirth));

    except:
        print("Birthdate data is not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def printer(df):
    counter=0
    for x in df:
        label = list(df.keys())[counter]
        print("Count of " + label + " is " + str(df[counter]))
        counter += 1
    
def printRows(df):
    """
    print results from filtered data

    Args:
        (df) dataframe - filtered dataframe according to filters
    Print:
       5 row a time
    """
    row = 0
    filteredResult = input("\nWould you want to see results? Write 'yes' to see first 5 rows or 'no' to turn back \n").lower()
    while True:
        if filteredResult == 'no':
            return
        if filteredResult == 'yes':
            print(df[row: row + 5])
            row = row + 5
        filteredResult = input("\n Would you want to see five more rows? Write 'yes' or 'no' turn back\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        printRows(df)
        
        
        
if __name__ == "__main__":
    main()
