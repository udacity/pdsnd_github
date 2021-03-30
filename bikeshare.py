import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#
#
#
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    print()
    #  Get user input for city -- chicago, new york city, washington.
    city = ''
    print('Please select one of the cities below for which you would like to explore the bikeshare data:')
    print()
    print('Chicago')
    print('New York City')
    print('Washington D.C.')
    print()
    print('Enter city:')
    city = input().lower()
    if city == 'chicago':
        city = 'Chicago'
    elif city == 'new york city':
        city = 'New York City'
    elif city == 'washington d.c.':
        city = 'Washington D.C.'
    else:
        print('You have not entered a valid city')
        city = 'Chicago by default'
    print()
    print('Data will be analyzed for: {}'.format(city))

    #  Get user input for month

    print()
    month = ''
    print("Which month would you like to filter by?")
    print("Please enter the month from the list below, or enter 'all' to select all months")
    print()
    print('January -- February -- March -- April -- May -- June')
    print()
    print('Enter month (or "all"):')
    month = input().lower()
    if month == 'january':
       month = 'January'
       mm = 1
    elif month == 'february':
       month = 'February'
       mm = 2
    elif month == 'march':
       month = 'March'
       mm = 3
    elif month == 'april':
       month = 'April'
       mm = 4
    elif month == 'may':
       month = 'May'
       mm = 5
    elif month == 'june':
       month = 'June'
       mm = 6
    elif month == 'all':
       month = 'all'
       mm = 13
    else:
        print('You have not choosen a valid month.')
        print('Default value is all months.')
        month = 'all months by default'
        mm = 13
    print()
    #
    if month == 'all' or month == 'all months by default':
        print('Data will be analyzed for all available months.')
    else:
        print('Data will be analyzed for the month of: {}'.format(month))
    #
    #  Get user input for day
    print()
    day = ''
    print("Which days would you like to filter by?")
    print("Please select a day as follows, or enter 'all' to select all days")
    print()
    print('Monday -- Tuesday -- Wednesday -- Thursday -- Friday -- Saturday -- Sunday')
    print()
    print('Enter day (or "all"):')
    day = input().lower()
    if day == 'monday':
       day = 'Monday'
       dd = 1
    elif day == 'tuesday':
       day = 'Tuessday'
       dd = 2
    elif day == 'wednesday':
       day = 'Wednesday'
       dd = 3
    elif day == 'thursday':
       day = 'Thursday'
       dd = 4
    elif day == 'friday':
       day = 'Friday'
       dd = 5
    elif day == 'saturday':
       day = 'Saturday'
       dd=6
    elif day == 'sunday':
       day = 'Sunday'
       dd = 7
    elif day == 'all':
       day = 'all'
       dd = 8
    else:
        print('You have not choosen a valid day.')
        print('Default value is all days.')
        day = 'all days by default'
        dd = 8

    print()
    #
    if day == 'all' or day == 'all days by default':
        print('Data will be analyzed for all days.')
    else:
        print('You have choosen to analyze data for: {}'.format(day))

    return city, mm, dd, month, day

# print a report heading
def report_heading(city,month,day):
    print()
    print('*'*50)
    print()
    print('City: ',city)
    print('Month: ',month)
    print('Day: ',day)
    print()
#
# load data based on user filter input
# data to pandas df called 'city-data'
def load_data(city, mm, dd):
    city = city.lower()
    if city == 'chicago' or city == 'chicago by default':
        city_data = pd.read_csv(CITY_DATA['chicago'])
    elif city == 'new york city':
        city_data = pd.read_csv(CITY_DATA['new york city'])
    else:
        city_data = pd.read_csv(CITY_DATA['washington'])

    #

    # convert Start Time to date_time format
    city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
    if mm != 13:
        index = city_data[city_data['Start Time'].dt.month != mm].index
        city_data.drop(index, inplace=True)
    if dd != 8:
        index = city_data[city_data['Start Time'].dt.day != dd].index
        city_data.drop(index, inplace=True)

    return city_data

# calculate time stats
def time_stats(city_data,mm,dd):

    if mm == 13:
        #CALCULATE MOST COMMON MONTH
        max_month = city_data['Start Time'].dt.month.value_counts().idxmax()
        print('Month with maximum rides: ',max_month)
    if dd == 8:
        #calculate the most common day
        max_day = city_data['Start Time'].dt.day.value_counts().idxmax()
        print('Day with maximum rides: ',max_day)
    #calculate the most common hour based on Start Time
    max_hour = city_data['Start Time'].dt.hour.value_counts().idxmax()
    print('Hour with maximum rides: ',max_hour)
    print()
#
# calculate station stats
def station_stats(city_data):
   # find most frequent starting station
   max_start_station = city_data['Start Station'].value_counts().idxmax()
   print('Most frequent starting statiion: ', max_start_station)
   # find most common end station
   max_end_station = city_data['End Station'].value_counts().idxmax()
   print('Most frequent end station: ', max_end_station)
   # most common trip from start to end (i.e., most frequent combination of start station and end station)
   # do this by creating a new field, 'Trip', that combines start and end stations into a trip
   city_data['Trip'] = city_data['Start Station'] +' '+ 'TO '+ city_data['End Station']
   max_trip = city_data['Trip'].value_counts().idxmax()
   print('Most frequent trip: ', max_trip)
   print()

def trip_duration_stats(city_data):
    total_travel_time_ss = city_data['Trip Duration'].sum()
    total_travel_time_mm = total_travel_time_ss/60
    total_travel_time_hh = total_travel_time_mm/60
    print('Total trvel time (s): ',total_travel_time_ss)
    print('Total travel time (m): ',total_travel_time_mm)
    print('Total travel time (h): ',total_travel_time_hh)
    print()

    print()

# calculate user stats
def user_stats(city_data,city):
    city = city.lower()
    user_type_trips = city_data['User Type'].value_counts(dropna = False)
    print('User type    number of rides')
    print(user_type_trips)
    print()
    if city == 'new york city' or city == 'chicago' or city == 'chicago by default':
        sex_type = city_data['Gender'].value_counts(dropna = False)
        early_yob = city_data['Birth Year'].min()
        latest_yob = city_data['Birth Year'].max()
        most_common_yob = city_data['Birth Year'].value_counts().idxmax()
        print('Sex     number of rides')
        print(sex_type)
        print()
        print('Earliest year-of-birth: ', int(early_yob))
        print('Lates year-of-birth: ', int(latest_yob))
        print('Most common year-of-birth: ', int(most_common_yob))
        print()

# create csv file to inspect results data frame
#def create_file(city_data):
#    city_data.to_csv('final_city_data.csv')


# function to print 5 lines raw data
def five_lines(city_data):
    ans = ''
    c = 5
    print('Enter "y" to see raw data (5 lines), other to continue.')
    ans = input().lower()
    if ans == 'y':
        print(city_data.iloc[0:c])
        print('Enter "y" to see more raw data (5 lines), other to continue.')
        ans = input().lower()
        while ans == 'y':
            d = c + 5
            print(city_data.iloc[c:d])
            print('Enter "y" to see more raw data (5 lines), other to continue.')
            ans = input().lower()
            c = c + 5


def main():
    while True:
        city, mm, dd, month, day = get_filters() #return city, mm, dd, month, day
        report_heading(city,month,day)           #none
        city_data = load_data(city, mm, dd)      #return city_data
        time_stats(city_data,mm,dd)              #none
        station_stats(city_data)                 #none
        trip_duration_stats(city_data)           #none
        user_stats(city_data,city)               #none
  #      create_file(city_data)                   #none
        five_lines(city_data)
        restart = input('\nEnter "y" to continue, other to end.\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
