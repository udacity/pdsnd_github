#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all','january', 'february', 'march', 'april', 'may','june','july','august','september','october','november','december']

days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
cities    = [ "new york city", "chicago", "washington" ]
#filtros = ['month','day','none']



def validar_parametros (valor,rango):
    if valor in rango:
        return True
    else:
        return False
    
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle     invalid inputs
    
    ciudad=' '
    while ciudad not in CITY_DATA:
        ciudad = str(input('Would you like to see data for Chicago, New York, or Washington?')).lower()
        if validar_parametros(ciudad,cities) is True:
            city = CITY_DATA[ciudad.lower()]
            #print (city)
        else:
            print ('Try again')
    # TO DO: get user input for month (all, january, february, ... , june)

    #Mes
    mes=' '
    while mes not in months:
        mes=str(input('Which month? January, February, March, April, May or June? Type "all" for no month filter \n')).lower()
        if validar_parametros(mes,months)is True:
            month=mes.lower()
        else:
            print ('Try again')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    dia=' '    
    while dia not in days:
        dia = str(input('Which day? Please type your response as an string e.g., sunday, Type "all" for no day filter \n')).lower()
        if validar_parametros(dia,days)is True:
            day=dia.lower()
        else:
            print ('Try again')  
   
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
    # Name of the city
    df = pd.read_csv(city)
    #print(df)
    # start Time 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # End Time 
    
    # Trip Duration
   
    # End Station
    # User Type
    
    # Month
    df['m'] = df['Start Time'].dt.month
    # Day of the week
    df['d'] = df['Start Time'].dt.weekday
    # Hour
    df['h'] = df['Start Time'].dt.hour
    
    print (df)
    #Filtro mes del año
    if validar_parametros(month,months) is True:
        month=months.index(month)
        print (month)
        df = df.loc[df['m'] == month]
        print(df)
    #Filtro día de la semana
    if validar_parametros(day,days) is True:
        day=days.index(day)
        #df = df.loc[df['d'] == day.title()]
    

    return df
#QUESTIONS

#1 Popular times of travel (i.e., occurs most often in the start time)
    #most common month
    #most common day of week
    #most common hour of day

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    cm=df['m'].mode()[0]
    print ('most common month: ',cm)

    # TO DO: display the most common day of week
    c_day=df['d'].mode()[0]
    print ('most common day of week: ',c_day)

    # TO DO: display the most common start hour
    c_hour=df['h'].mode()[0]
    print ('most common start hour: ',c_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#2 Popular stations and trip
    #most common start station
    #most common end station
    #most common trip from start to end (i.e., most frequent combination of start station and end station)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    cs_station=df['Start Station'].mode()[0]
    print ('most common Start Station: ',cs_station)
    
    # TO DO: display most commonly used end station
    ce_station=df['End Station'].mode()[0]
    print ('most common End Station: ',ce_station)

    
    # TO DO: display most frequent combination of start station and end station trip

    c_combination=df['Start Station'] +'and'+ df['End Station'].mode()[0]
    print ('most frequent combination: ',c_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
#3 Trip duration
    #total travel time
    #average travel time
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    t_travel=df['Trip Duration'].sum()
    print ('total travel time: ',t_travel)
    
    # TO DO: display mean travel time
    m_time=df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#4 User info
    #counts of each user type
    #counts of each gender (only available for NYC and Chicago)
    #earliest, most recent, most common year of birth (only available for NYC and Chicago)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    u_types=df['User Type'].value_counts()
    print ('counts of user types: ',str(u_types))

    # TO DO: Display counts of gender
    if city != 'washington.csv':
        counts_g=df['Gender'].value_counts()
        print ('counts of gender: ',str(counts_g))
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest= df['Birth Year'].min()
        print ('earliest year of birth: ',earliest)
        most_recent=  df['Birth Year'].max()
        print ('most recent year of birth: ',most_recent)
        common_year= df['Birth Year'].mode()[0]
        print ('common recent year of birth: ',common_year)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    view_data = input('nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    
    while view_data.lower()=='yes':
        print(df.iloc[start_loc:start_loc+4])
        start_loc += 5
        view_display = input('Do you wish to continue?: ').lower()
        if view_display.lower() != 'yes':
            break

def main():
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


# In[ ]:





# In[ ]:




