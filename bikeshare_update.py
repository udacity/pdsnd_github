import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Tells the user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello and welcome to this fantastic experience. \n\
Let\'s explore some data over the US bike shares!\n")

    cities = ['Chicago', 'New York', 'Washington']
    while True:
        city = input("Do you want to see Chicago, New York, or Washington: ").title()
        if city in cities:
            break
        else:
            print('That is not one of Chicago, New York and Washington')
    
    # Import the data and make a month and weekday column
    df = pd.read_csv(CITY_DATA[city])

    df["month"] = pd.DatetimeIndex(df["Start Time"]).month # Will be month in numbers
    df["day"] = pd.DatetimeIndex(df["Start Time"]).weekday # Will be weekday in numbers
   
    # Only input Month, Day, Both or NO!
    filters = ['Month', 'Day', 'Both', 'No']
        
    while True:
        filt = input('\nExcellent choice, now, how do would you want to filter\n\
Month, Day, Both or not at at all, type "No" if no filter: ').title()
        if filt in filters:
            break
        else:
            print('Please only write Month, Day, Both or NO!')
    
    # Filter months if the chosen alternative is both or month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    if filt == "Month" or filt == "Both":
        while True:
            month = input("\nEnter a month between January to June: ").title()
            if month in months:
                break
            else:
                print('Please insert a valid month: ')
        m = {
            'January': 1,
            'February': 2,
            'March': 3,
            'April': 4,
            'May': 5,
            'June': 6  
        }
        month_m = m[month]
        df = df[df["month"] == month_m]
    elif filt == "No" or filt == "Day":
        month = "No month selected"


    # Filter Weekdays if the chosen alternative is Week or Both
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday', 'Sunday']
    if filt == "Day" or filt == "Both":
        while True:
            day = input("\nEnter a weekday: ").title()
            if day in weekdays:
                break
            else:
                print('Please input a valid weekday')
        d = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday' : 6
        }
        day_n = d[day]
        df = df[df['day'] == day_n]
    elif filt == "Month" or filt == "No":
        day = "No day selected"


    print("\nYou have chosen to search for information for \n{} \n{} \n{}"\
        .format(city, month, day))

    print('-'*40)
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # The most common month
    month = df["month"].mode()[0]
    m = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June' 
        }
    month_M = m[month]
    count_mo = df['month'].value_counts()[:1].nlargest(n=1).values[0]
    print("The most common month is {}, Count: {}".format(month_M, count_mo))

    # The most common day
    weekday = df["day"].mode()[0]
    d = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
        }
    day_N = d[weekday]
    count_da = df['day'].value_counts()[:1].nlargest(n=1).values[0]
    print("The most common weekday is {}, Count: {}".format(day_N, count_da))

    # The most common start hour
    df["start_hour"] = pd.DatetimeIndex(df["Start Time"]).hour    # Will be weekday in numbers
    hour = df["start_hour"].mode()[0]
    count_h = df['start_hour'].value_counts()[:1].nlargest(n=1).values[0]
    print("The most common hour is: {}, Count: {}".format(hour, count_h))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # The most commonly used start station
    s_station = df["Start Station"].mode()[0]
    s_count = df["Start Station"].value_counts().nlargest(n=1).values[0]
    print("The most popular start station is: {}, Count: {}".format(s_station, s_count)) 
    

    # The most commonly used end station
    e_station = df["End Station"].mode()[0]
    e_count = df["End Station"].value_counts().nlargest(n=1).values[0]
    print("The most popular end station is: {}, Count: {}".format(e_station, e_count)) 

    # The most common trip
    combination = df.groupby(['Start Station','End Station']).size().idxmax()
    print("The most popular trip is {}".format(combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Displays the travel duration
    duration= df['Trip Duration'].sum()
    d_Count = df["Trip Duration"].value_counts().sum()
    d_Average = df['Trip Duration'].mean()
    print("Total duration is: {}, Count {}, Average {}".format(duration, d_Count, d_Average))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    s_count = (df["User Type"] == "Subscriber").sum()
    c_count = (df["User Type"] == "Customer").sum()
    print("The user types are Subscriber: {}, Costumer: {}".format(s_count, c_count))

    # No Gender Column in Washington so only do if the column exist
    if 'Gender' in df.columns:
        m_count = (df["Gender"] == "Male").sum()
        f_count = (df["Gender"] == "Female").sum()
        ns_count = (df["Gender"] == "").sum()
        print("\nThe genders are Male: {}, Female: {}, NotSpec: {}".format(m_count, f_count, ns_count))

    # No Birth Year Column in Washington so only do if column exists
    if 'Birth Year' in df.columns:
        df['Birt Year'] = pd.to_datetime(df['Birth Year'])
        early = (df['Birth Year']).min()
        common = df['Birth Year'].mode()[0]
        count_common = df['Birth Year'].value_counts().nlargest(n=1).values[0]
        recent = (df['Birth Year']).max()

        print("The Earliest Date of Birth is: {}\n\n Most recent birth date: {} \
        \n\nMost common year of birth: {}, Count: {}".format(early, recent, common, count_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_request(df):
    """Show data on User Request, 5 lines"""
    print('\nCalculating User Request...\n')
    start_time = time.time()

    s = 0 
    request = input('\nSo, Dear User, do you want to see \
    individual data?').title()
    while request == 'Yes':
        for i in range(6):
            df['Start Station'].slice = df['Start Station'].iloc[s+i-1: s+i]
            df['End Station'].slice = df['End Station'].iloc[s+i-1: s+i]
            df['Start Time'].slice = df['Start Time'].iloc[s+i-1: s+i]
            df['End Time'].slice = df['End Time'].iloc[s+i-1: s+i]
            df['Trip Duration'].slice = df['Trip Duration'].iloc[s+i-1: s+i]

            print("\n Person {} \n".format(s+i))
            start_station = df['Start Station'].slice.values
            end_station = df['End Station'].slice.values
            start_time2 = df['Start Time'].slice.values
            end_time = df['End Time'].slice.values
            duration = df['Trip Duration'].slice.values
            print\
            ("Start_Station: {} \n End_Station: {}\nStart_Time: {}\
             \nEnd_Time: {} \n Duration: {}".format(start_station, end_station, \
             start_time2, end_time, duration))
        s += 5
        request= input('\nSo, Dear User, do you want to see \
        individual data:').title()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def main():
    while True:
        df = get_filters()
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        user_request(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()