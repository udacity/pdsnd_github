import time
import pandas as pd
import numpy as np
#Change 1

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list = ["january", "feburary", "march", "april","may","june","all"]
day_list = ["sunday", "monday", "tuesday", "wednesday","thursday","friday","saturday","all"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid 
    
    city = input("what city would you like to select to see its data,New York City, Chicago or Washington?").lower().strip()
    while (city not in CITY_DATA.keys()) : 
        city = input("what city would you like to select to see its data,New York City, Chicago or Washington?").lower().strip()
        
    
 # get user input for month (all, january, february, ... , june)
    month = input("which month From January to June you would like to select or you choose?").lower().strip() 
    while (month not in month_list): 
          month = input("which month From January to June you would like to select or you choose").lower().strip()
# get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(" what weekday you want to do filter bikeshare data ?").lower().strip()
    while (month not in month_list): 
          day = input(" what weekday you want to do filter bikeshare data ?").lower().strip()
#make sure filters entered by user are correct 
           
        
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
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"]= pd.to_datetime(df["Start Time"])
    df["Month"]= df["Start Time"].dt.month_name()
    df["day"] = df["Start Time"].dt.day_name()

    if (month != "all"):
         df = df [df["Month"] == month.capitalize()]
    if (day != "all"):
         df = df [df["day"]== day.capitalize()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['Month'].mode()[0]
    print("Most Common month according to the selected filters: " , common_month)

    # display the most common day of week
    common_day = df['day'].mode()[0]
    print("Most Common day according to the selected  filter: " , common_day)

    # display the most common start hour
    df['Start Hour']= df['Start Time'].dt.hour
    common_hour = df['Start Hour'].mode()[0]
    print("Most Common Start Hour according to the selected filter : " , common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start station according to Selected filter:' , common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Common End station according to Selected filter:' , common_end_station)

    # display most frequent combination of start station and end station trip
    df['Combination'] = (df['Start Station'] + ' - ' + df['End Station'])
    common_combination = (df['Combination'].mode()[0])
    print('Most Common Start-End Combination according to Selected filter:' , common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(" the total travel time  according to the selcted filter : " , total_travel_time )

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("the mean travel time according to the selected filter : " , mean_travel_time  )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts for each user types according to filter: " , user_types )

    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print("Counts for each gender according to filter: " , gender_count ) 
    except:
        print(" There is no data of user genders for  the selected city.")
              
# Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        print(" the oldest person according to selected filter was born in : " , earliest_birth_year)
        most_recent_birth_year = df['Birth Year'].max()
        print(" the youngest person according to selected filter was born in: " , most_recent_birth_year)
        most_common_birth_year = df['Birth Year'].mode()[0]
        print(" the most common birth year according to selected filter is : "  , most_common_birth_year)
    except:
        print("There is no data for birth year for the Selected city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        raw_data = input("DO you wanna take a look for raw data ?" ).lower().strip()
        begining = 0 
        Last = 5
        while True:
             tp = df.iloc[begining:Last]
             begining+= 5
             Last+= 5
             print(tp)
             raw_data = input("DO you wanna take a look for  more raw data ?" ).lower().strip()
             if(raw_data == "no"):
                break 
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)       
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower().strip()
        if restart != 'yes':
            break

if __name__ == "__main__":
	main()
