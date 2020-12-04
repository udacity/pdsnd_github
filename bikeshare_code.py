import time
import pandas as pd
import numpy as np


CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input('1. Which city would you like to explore? Chicago, New york  City or Washington?').title().strip()
        if city != 'Chicago' and city != 'New York City' and city != 'Washington':
            print("Data type not found, try again.")
        else:
            break

    while True:
        month = input('2. What month? (Type from Ja, Fe, Ma, Ap, My, Ju  or All)')
        month = month.title().strip()
        if month != 'Ja' and month != 'Fe' and month != 'Ma' and month != 'Ap' and month != 'My' and month != 'Ju' and month != 'All':
            print("Please use the specified format.")
        else:
            break

    while True:
        day = input('3. And which day? (Type from Saturday, Sunday, Monday, Tuesday, Wednesday Thursday, Friday or All)')
        day = day.title().strip()
        if day != 'Sunday' and day != 'Monday' and day != 'Tuesday' and day != 'Wednesday' and day != 'Thursday' and day != 'Friday' and day != 'Saturday' and day != 'All':
            print("Please use the specified format.")
        else:
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'All':
        months = ['Ja', 'Fe', 'Ma', 'Ap', 'My', 'Ju']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):

    print('\n 1.Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    pop_m = df['month'].mode()[0]
    print('a) Popular Month - ', pop_m)
    pop_d= df['day_of_week'].mode()[0]
    print('b) Popular Day - ', pop_d)
    pop_h = df['hour'].mode()[0]
    print('c) Popular Hour - ', pop_h)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    print('\n 2.Calculating The Most Popular Stations and Trips...\n')
    start_time = time.time()
    pop_ss = df['Start Station'].mode()[0]
    print("a) Popular Start Station - ", pop_ss)
    pop_es = df['End Station'].mode()[0]
    print("b) Popular End Station - ", pop_es)
    grouped = df.groupby(['Start Station','End Station'])
    pop_combo = grouped.size().nlargest(1)
    print("c) Popular Combined Statitons - ", pop_combo)
    print('-'*40)


def trip_duration_stats(df):
    print('\n 3.Calculating Trip Duration...\n')
    start_time = time.time()

    tt = df['Trip Duration'].sum()
    print('a) Total Time Travelled - ', tt)
    mean_tt = df['Trip Duration'].mean()
    print('b) Mean of Time Travelled - ', mean_tt)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    print('\n 4.Calculating User Stats...\n')
    start_time = time.time()
    print('a) Stats According to User Type - ')
    print(df['User Type'].value_counts())
    if city == 'Washington':
        print("No Gender or Birth Data for this city.")
    else:
        gender = df['Gender'].value_counts()
        print(gender)
        print('b) Stats according to Birth Years - ')
        pop_yr = df['Birth Year'].mode()[0]
        print('c) Popular Date of Births - ',pop_yr)
        rec_year = df['Birth Year'].max()
        print('d) Recent Year - ', rec_year)
        ear_year = df['Birth Year'].min()
        print('e) Earliest Year - ', ear_year)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    return df,city

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        print('-'*40)
        raw = input('Would you like to view the raw data? yes/no').lower().strip()
        raw_data = 0
        y = 5
        while (raw == 'yes'):
            x = df.iloc[raw_data : y]
            print(x)
            raw_data += 5
            y += 5
            raw = input('Would you like to view some more?').lower().strip()

#this should be wrapped in a seperate funtion than the main for better seamlessness of the code and ease of eyes. 

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

 
