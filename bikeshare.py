import time
import pandas as pd
import numpy as np

VALID_DAYS = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'all']
VALID_MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']
LST_CITY=["Chicago","New york city","Washington"]
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
    """
    Gets city , month , day information from customer
    """
    print('Welcome to Bikeshare data Analysis...')
    try:
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        while True:
            try:
                cit_num = int(input('Enter city you would like to analyze \n1 : Chicago\n2 : Newyork\n3 : Washington :\n'))
            except ValueError:
                print("Please enter a number value\n")
                continue
            if cit_num not in (1,2,3):
                 print("Please enter a valid number that refers to cities\n")
                 continue
            else:
                 break

        city = LST_CITY[cit_num - 1].lower()
        # TO DO: get user input for month (all, january, february, ... , june)
        while True:
            try:
                month_num = int(input('Enter month of the year  you would like to analyze \n1 : JAN\n2 : FEB\n3 : MAR\n4 : APR\n5 : MAY\n6 : JUN\n7 : WHOLE WEEK\n'))
            except ValueError:
                print("Please enter a num value\n")
                continue
            if month_num not in range(1,8):
                print("Please enter a valid month...\n")
                continue
            else:
                break
        month = VALID_MONTHS[month_num-1]
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            try:
                day_num = int(input('Enter day of the week  you would like to analyze \n1 : MON\n2 : TUE\n3 : WED\n4 : THU\n5 : FRI\n6 : SAT\n7 : SUN\n8 : ALL MONTHS\n'))
            except ValueError:
                print("Please enter a num value\n")
                continue
            if day_num not in range(1, 9):
                print("Please enter a valid month number...\n")
                continue
            else:
                break
        day = VALID_DAYS[day_num-1]

        print('\n'+'*'*20)
        print('Your selections are stated below\nCity : {} , Month : {} , Day : {} '.format(city.title(),month.title(),day.title()))
        print('*'*20)
        
        return city, month, day ,cit_num , month_num , day_num
        
    except Exception as e:
        print('An exception has been occurred : {}'.format(e))
    

        

def load_data(city, month, day ,city_num, month_num, day_num):
    """
    Applies month,date,city filters and loads the appropriate csv file
    """
    try:
        df = pd.read_csv(CITY_DATA[city])
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        df['hour'] = df['Start Time'].dt.hour

        # filter by month if applicable
        if month != 'all':
            df = df[df['month'] == month_num]
        # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe

            df = df[df['day_of_week'].str.contains(day.title())]
        return df
    except Exception as e:
        print('An exception has been occurred during loading data: {}'.format(e))

def time_stats(df, city):
    """Displays statistics on the most frequent times of travel."""
    print("\n"*2+'*' * 20)
    print('Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    try:
        fav_month_num = df['Start Time'].dt.month.mode()[0]
        fav_month = VALID_MONTHS[fav_month_num-1].title()
        print('Most frequent month for ', city.title(), 'is:', fav_month.title())
    except Exception as e:
        print('An exception has been occurred while displaying most common month : {}'.format(e))

    # TO DO: display the most common day of week
    try:
        fav_day = df['day_of_week'].mode()[0]
        print('Most frequent weekday for ', city.title(), 'is:',fav_day.title())
    except Exception as e:
        print('An exception has been occurred while displaying most common moth day of week: {}'.format(e))


    # TO DO: display the most common start hour
    try:
        fav_hour = df['hour'].mode()[0]
        print('Most frequent starthour for ', city.title(), 'is:',fav_hour)
    except Exception as e:
        print('An exception has been occurred while displaying most common start hour: {}'.format(e))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*20)

def station_stats(df, city):
    """Displays statistics on the most common stations and trip."""

    print("\n" * 2 + '*' * 20)
    print('Calculating The Most common Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        fav_start_position = df['Start Station'].mode()[0]
        fav_start_position_amount = df['Start Station'].value_counts()[0]
        print('Most frequent departure point for ', city.title(), 'is:',fav_start_position, 'and was used', fav_start_position_amount, 'times.')
    except Exception as e:
        print('An exception has been occurred while displaying most frequent departure point : {}'.format(e))
        
    # TO DO: display most commonly used end station
    try:
        fav_end_station = df['End Station'].mode()[0]
        fav_end_station_amount = df['End Station'].value_counts()[0]
        print('Most frequent arrival point for ', city.title(), 'is:',fav_end_station, 'and was used', fav_end_station_amount, 'times.')
    except Exception as e:
        print('An exception has been occurred while displaying frequent arrival point: {}'.format(e))
    
    # TO DO: display most frequent combination of start station and end station trip
    try:
        print(df)
        df["trips"]=df['Start Station']+':'+df["End Station"]
        fav_trip=df["trips"].value_counts().idxmax()
        fav_trip_amt = df["trips"].value_counts()[0]
        print('Most frequent roundtrip stations are:\n', fav_trip, '\n and was driven', fav_trip_amt,'times')
    except Exception as e:
        print('An exception has been occurred while displaying most frequent combination of start station and end station trip : {}'.format(e))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*' * 20)
    

def trip_duration_stats(df, city):
    """Displays statistics on the total and average trip duration."""

    print("\n" * 2 + '*' * 20)
    print('Calculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    try:
        df['Time Delta'] = df['End Time'] - df['Start Time']
        total_time_delta = df['Time Delta'].sum()
        print('The total travel time :', total_time_delta)
    except Exeption as e:
        print('An exception has been occurred while displaying total travel time: {}'.format(e))
        
    # TO DO: display mean travel time
    try:
        total_mean = df['Time Delta'].mean()
        print('The mean travel time :', total_mean)
    except Exception as e:
        print('An exception has been occurred while displaying mean travel time: {}'.format(e))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*' * 20)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print('The counts of user types in', city.title(), 'are as follows:\n', df['User Type'].value_counts())
    except Exception as e:
        print('An exception has been occurred while displaying counts of user type: {}'.format(e))
        
    # TO DO: Display counts of gender
    try:
        print('The counts of gender in', city.title(), 'are as follows:\n',df['Gender'].value_counts())
    except Exception as e:
        print('An exception has been occurred while displaying counts of gender: {}'.format(e))
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()
        print('The earliest, most recent, and most common year of birth in', city.title(), 'is:\n' 'The earliest birth date is:', int(earliest_year),'\n' 'The most recent birth date is:', int(most_recent_year),'\n' 'The most common year of birth is:', int(most_common_year))
    except Exception as e:
        print('An exception has been occurred while displaying earliest, most recent, and most common year of birth: {}'.format(e))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    raw_data = 0

    try:

        while True:
            answer = input("Do you want to see the raw data? Please type Yes or No : ").lower()
            if answer not in ['yes', 'no']:
                print('\nInvalid answer!\n')
                continue
            elif answer == 'yes':
                print(df.iloc[raw_data : raw_data + 5])
                raw_data += 5
                while True :
                    again = input("Do you want to see more 5 lines of raw data? Please type Yes or No : ").lower()
                    if again not in ['yes', 'no']:
                        print('\nInvalid answer!\n')
                        continue
                    elif again == 'yes':
                        print(df.iloc[raw_data : raw_data + 5])
                        raw_data += 5
                    else:
                        break
                break
            else:
                break

           
    except Exception as e:
        print('An exception has been occurred while displaying raw data : {}'.format(e))
    
    

def main():
    while True:
        city, month, day ,cit_num , month_num , day_num = get_filters()
        df = load_data(city, month, day,cit_num , month_num , day_num)
        time_stats(df, city)
        station_stats(df, city)
        trip_duration_stats(df, city)
        user_stats(df,city)
        
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()