import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

####

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities =('chicago','washington', 'new york city')
    while True:
        try:
            city = input('\nWhat city would you like to discover? choice from (chicago, new york city, washington)\n').lower()
            if city in cities:
                break
            else:
                print('YOUR  CITY INPUT IS WRONG!!choes from: chicago, new york city, washington')
        except KeyError:
            print('YOUR  CITY INPUT IS WRONG!!choes from: chicago, new york city, washington')
            
        
    # TO DO: get user input for month (all, january, february, ... , june)
    months =('january', 'february', 'march', 'april', 'may', 'june','all')
    while True:
        try:
            month = input('\nWhat month would you like to check? choice from (all, january, february, ... , june)\n')
            if month in months:
                break
            else:
                print('YOUR MONTH INPUT IS WRONG!! you should choes from january, february, march, april, may, june,all')
        except:
            print('YOUR MONTH INPUT IS WRONG!! you should choes from january, february, march, april, may, june,all')
      
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days =('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')

    while True:
        try:
            day = input('\nWhich day? choice from (all, monday, tuesday, ... sunday)\n')
            if day in days:
                break
            else:
                print('YOUR MONTH INPUT IS WRONG!! you should choes from january, february, march, april, may, june,all')
        except:
            print('YOUR MONTH INPUT IS WRONG!! you should choes from january, february, march, april, may, june,all')

    print('-'*40)
    return city, month, day

#end of the user input

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df
#i copied this part from the practice solution#3

#start on the most frequent times of travel:

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    
    print('\nThe most common Month is:', common_month)


    # TO DO: display the most common day of week
    day_of_week = df['day_of_week'].mode()[0]
    
    print('\nThe most common day of the week is:',day_of_week)


    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
        
    print('\nThe most common start hour is:',common_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#end of the most frequent times of travel



# start on the most popular stations and trip
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = df['Start Station'].mode()[0]
    
    print('\nThe most commonly used start station: ',commonly_start_station)

    # TO DO: display most commonly used end station
    commonly_end_station = df['End Station'].mode()[0]
    
    print('\nThe most commonly used end station: ',commonly_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    commonly_start_end_station= df.groupby(["Start Station", "End Station"]).count()
    
    print('\nThe most frequent combination of start station and end station trip is:',commonly_start_end_station)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#end of the most popular stations and trip


#start on the total and average trip duration

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    
    print('\nThe total travel time:', total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    
    print('\nThe mean travel time:', mean_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#end of the total and average trip duration.


#start of bikeshare users:
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = pd.value_counts(df['User Type'])  
    print('\nUser types:',user_type)
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("\nno gender information")
    
        # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        most_common_year= df['Birth Year'].mode()[0] 
        print('\n The most common year:',most_common_year)

        recent_year= df['Birth Year'].min()
        print('\n The most recent year:',recent_year)

        earliest_year= df['Birth Year'].max()
        print(gender)
    else:
        print("No information")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# end of bikeshare users:

#Display 5 line of sorted raw data each time
def raw_date(df):
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
            
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc +=5
        view_display = input('Do you wish to continue?:Enter yes or no.\n' ).lower()
        if view_display != 'yes':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
       
        raw_date(df)          
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)  
          
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
                
if __name__ == "__main__":
         main()

    
