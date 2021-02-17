import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        print("\nWould you like to see data for Chicago, New York, or Washington? \n")
        city = input().lower()
        
        if city not in CITY_DATA.keys():
            print("\nInvalid City! Please check your input and try again.")
                 
    
    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nWhich month would you like to filter the data by? January through June, or type \"All\" for no filter.\n")
        month = input().lower()
        
        if month not in MONTH_DATA.keys():
            print("\nInvalid Month! Please check your input and try again.")
           
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY_LIST:
        print("\nWhich day of the week would you like to filter the data by? (Type \"All\" for no filter.)\n")
        day = input().lower()
        
        if day not in DAY_LIST:
            print("n\Invalid Day! Please check your input and try again.")
      
   
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
    # load data for city
    print("\nLoading Data...")
    df = pd.read_csv(CITY_DATA[city])
            
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month
    if month != 'all':
          months = ['january','february','march','april','may','june']
          month = months.index(month) + 1
          
          df = df[df['month'] == month]
     
    # filter by day
    if day != 'all':
          # filter by day of week to create the new dataframe
          df = df[df['day_of_week'] == day.title()] 
          
          
    return df
          
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mode_month = df['month'].mode()[0]
    print("\n The most common month is (1 = January, 2 = February, 3 = March, ...):",mode_month)

    # TO DO: display the most common day of week
    mode_day_of_week = df['day_of_week'].mode()[0]
    print("\n The most common day of the week is:",mode_day_of_week)

    # TO DO: display the most common start hour
    df['Start_Hour'] = df['Start Time'].dt.hour
    mode_start_hour = df['Start_Hour'].mode()[0]
    print("\n The most common start hour is:",mode_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mode_Start_Station = df['Start Station'].mode()[0]
    print("\n The most common Start Station is:",mode_Start_Station)

    # TO DO: display most commonly used end station
    mode_End_Station = df['End Station'].mode()[0]
    print("\n The most common End Station is:",mode_End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    mode_combo_start_and_end = df['Start Station'].str.cat(df['End Station'],sep=" to ").mode()[0]
    print("\n The most common combination of Start and End Station is:",mode_combo_start_and_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute,60)
    print(f"\n The total trip time was {hour} hours, {minute} minutes, and {second} seconds.")

    # TO DO: display mean travel time
    mean_duration = round(df['Trip Duration'].mean())
    minute2, second2 = divmod(mean_duration, 60)
    hour2, minute2 = divmod(minute2, 60)
    print(f"\n The average trip time was {hour2} hours, {minute2} minutes, and {second2} seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f"The types of users by number are given below:\n\n{user_type}")
    
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe type of genders by number are given below:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in this file.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        print(f"\nThe earliest birth year is: {earliest}")
        most_recent = int(df['Birth Year'].max())
        print(f"\nThe most recent birth year is: {most_recent}")
        most_common = int(df['Birth Year'].mode()[0])
        print(f"\nThe most common birth year is: {most_common}")
    except:
        print("There is no birth year information in this file!")
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
               
        
#To display raw data  
#def rawdata(df):
 #   valid_responses = ["yes","no"]
  #  A1 = ''
   # while A1 not in valid_responses:
    #    print("\nWould you like to see the raw data? Yes or No")
     #   A1 = input().lower()
      #  if A1 == "yes":
       #     print(rawdata(df).head())
        #elif A1 not in valid_responses:
         #   print("\nInvalid Input! Please try again.")
        #else:
        #   print("Okay...Continuing")


        
def raw_data(df):
#show raw data
    start_line = 0
    end_line = 5

    show_data = input("Would you like to see raw data?: (yes)(no) ").lower()
    if show_data == 'yes':
        while end_line <= df.shape[0] - 1:
            print(df.iloc[start_line:end_line,:])
            start_line += 5
            end_line += 5
            show_data_end = input("More?: ").lower()
            if show_data_end == 'no':
                break
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
		raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

