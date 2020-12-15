import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']   
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def month_filter():
    month = input("\nWhich month? January, February, March, April, May, or June? Please type out the full month name.. ").lower().strip()
    if month not in months:
        print("\nPlease make sure to type the month name correctly!") 
    else:
        return month

def day_filter():
    day = input("\nWhich day? Please type out the full day name.. ").lower().strip()
    while day not in days:
       day =  print("\nPlease make sure to type the day correctly!")
    return day        

def get_filters():
    filter = ''
    month, day = 'none', 'none'
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input ("\nWould you like to see data for Chicago, New York, or Washington? ").lower().strip()
        if city in CITY_DATA.keys():
            print(f"\nLooks like you want to hear about {format(city)}")
            break
        else:
            print("\nPlease make sure to type the city correctly!")
    # Give all the choices in a series of print statements.
    while filter != 'q':
        print("\n[1] Enter 1 to filter by Month. ")
        print("[2] Enter 2 to filte by Day. ")
        print("[3] Enter 3 to filter by both. ")
        print("[4] Enter 4 to not use any filter. ")
        print("[q] Enter q to quit.")
        filter = input("\nWhat would you like to do? ")
        # Respond to the user's choice.
        if filter == '1':
            month = month_filter()
            day = 'none'
            print(f"\nWe will make sure to filter the data by {month.title()}! ")
            break
        elif filter == '2':
            day = day_filter()
            month = 'none'
            print(f"\nWe will make sure to filter the data by {day.title()}! ")
            break
        elif filter == '3':
            month = month_filter()
            day = day_filter()
            print(f"\nWe will make sure to filter the data by both {month.title()} and {day.title()}! ")
            break
        elif filter == '4':
            month = 'none'
            day = 'none'
            print("\nWe will not use any filter! ")
            break
        elif filter == 'q':
            print("\nThanks You. See you later.\n")
            import sys
            sys.exit(0)
        else:
            print("\nI don't understand that choice, please try again.\n")

    print('-'*40)
    #print(city,'-', month,'-',day)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    if month != 'none':
        month = months.index(month)-1
        df = df[df['month'] == month]

    if day != 'none':
        df = df[df['day'] == day]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print("\n------------------ Fetching Data ------------------ ")
    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # TO DO: display the most common month
    print("\nMost Popular Month is ", months[df['month'].mode()[0]-1])
    
    # TO DO: display the most common day of week
    print("\nMost Popular Day is", df['day'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hr = df['hour'].mode()[0]
    print(f"\nMost Popular hour is {common_hr}. ")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\nMost Used Start Staion is The", df['Start Station'].mode()[0], "Station")

    # TO DO: display most commonly used end station
    print("\nMost Used End Staion is The", df['End Station'].mode()[0], "Station")

    # TO DO: display most frequent combination of start station and end station trip
    df['Route'] = df['Start Station'] + ' to ' + df['End Station']
    print("\nMost Frequent Route used is from ", df['Route'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # TO DO: display total travel time
    duration = df['Trip Duration'].sum()
    dur_details = datetime.timedelta(seconds = duration.item())
    print(f"\nTotal Travel Time is {format (dur_details)} ")

    # TO DO: display mean travel time
    mean_dur = round(df['Trip Duration'].mean())
    mean_details = datetime.timedelta(seconds = mean_dur)
    print(f"\nAverage Travel Time is {format(mean_details)} ")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\nCount of user Types:\n", df['User Type'].value_counts())

    # This Try block is to catch any errot if user choses a city thatn doesnt not the gender column
    if 'Gender' in df.columns:
        genders = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{format(genders)}")
    else:
        print("\nGender information are not avilable for this city.")

 # This Try block is to catch any errot if user choses a city thatn doesnt not the birth date column
    if 'Birth Year' in df.columns:
        earliest_by = int(df['Birth Year'].min())
        recent_by = int(df['Birth Year'].max())
        common_by = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest birth year: {format(earliest_by)}")
        print(f"\nThe most recent birth year: {format(recent_by)}")
        print(f"\nThe most common birth year: {format(common_by)}")
    else:
        print("\nBirth year information are not avilable for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def all_data(df):
    """
    Asks if the user would like to see some lines of data from the filtered dataset.
    Displays 5 (show_rows) lines, then asks if they would like to see 5 more.
    Continues asking until they say stop.
    """
    start_row = 0
    end_row = 5
    row_num = 5
    answer = input("\nWould you like to see some raw data from this dataset? (Y or N). ").lower().strip()

    while answer == "y":
        print("\nDisplaying rows {} to {}:".format(start_row + 1, end_row))
        print("\n", df.iloc[start_row : end_row + 1])
        start_row += row_num
        end_row += row_num
        print('\n-------------------------------------------------------------------\n')
        answer = input("Would you like to see the next {row_num} rows?(Y or N). ".lower().strip())


def main():
    while True:
        city, month, day = get_filters()
        #print(city,month,day)
        df = load_data(city, month, day)
        #print(df.columns.values.tolist())

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        all_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()