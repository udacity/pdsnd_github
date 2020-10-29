import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
	     
              'new york city': 'new_york_city.csv',
	     
              'washington': 'washington.csv' }

# a comment for refactoring the code for github


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
	
	
    global city, month, day
    print('\n')
    print('\n')
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\n(1) Which city would you like to Explore its data? [new york city , chicago , washington]\n")
        if city not in ('new york city', 'chicago', 'washington'):
            print("The city name you entered is invalid, please try again")
            continue
        else:
            break
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\n(2) Please enter the Month name your want to filter by, [January , February , March , April , May , June] or enter 'all'\n")
        if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
            print("The month name you entered is invalid, please try again")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n(3) Please eneter a day of the week to filter by, or enter 'all'\n")
        if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
            print("The day name you entered is invalid, please try again")
            continue
        else:
            break
   
    print('-'*40)
    print('-'*40)
    print('-----CALCULATING STATISTICS FOR YOU-----')
    print('-'*40)
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
    
    #[1] LOAD DATA GIVEN THE CITY NAME 
    df = pd.read_csv(CITY_DATA[city])
    
    
    #[2]CHANGE START COLUMNS TO DATETIME DATA TYPE
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #[3] CREATE NEW COLUMNS FOR TRIP START WEEKDAY AND START MONTH 
    df['start_weekday']=df['Start Time'].dt.strftime('%A')
    df['start_month']=df['Start Time'].dt.strftime('%B')
    
    
    #[4] EXTARC FILTERED DATA GIVEN USER SELECTIONS
    #[4.1] Filter data given month name selection 
    if month != 'all':
        #months_list = ['January', 'February', 'March', 'April', 'May', 'June']
        #month = months_list.index(month) + 1
        df = df[df['start_month'] == month]
        
    #[4.2] Filter data given day name selection 
    if day != 'all':
        df = df[df['start_weekday'] == day]
        
    return df







#[5] CALCULATE TIME STATS

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The Most common month is {} with count value equlas to{}.'.format(([df['start_month'].value_counts().idxmax()])                                                                ,df['start_month'].value_counts().max()))


    # TO DO: display the most common day of week
    print('The Most common day of the week is {} with count value equlas to {}.'.format(([df['start_weekday'].value_counts().idxmax()])                                                     ,df['start_weekday'].value_counts().max()))

    # TO DO: display the most common start hour
    df['start_hour']=df['Start Time'].dt.hour
    print('The Most common start hour is {} with count value equlas to {}.'.format(([df['start_hour'].value_counts().idxmax()])
                                                      ,df['start_hour'].value_counts().max()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('-'*40)
    print('\n')


    
    
    
#[6] CALCULATE STATIONS STATS
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
   
    print('\n')
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(' Most commonly used start station is {} with count value equlas to {}.'.format(([df['Start Station'].value_counts().idxmax()]) ,df['Start Station'].value_counts().max()))

    # TO DO: display most commonly used end station
    print(' Most commonly used end station is {} with count value equlas to {}.'.format(([df['End Station'].value_counts().idxmax()]) ,df['End Station'].value_counts().max()))

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_stations'] = df['Start Station'] +' '+ df['End Station']
    print(' Most frequent combination f start station and end station trip is {} with count value equlas to {}.'.format(([df['start_end_stations'].value_counts().idxmax()]) ,df['start_end_stations'].value_counts().max()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('-'*40)
    print('\n')
   

    
    
    
    
    
    
    
    
#[7] CALCULATE TRIP STATS

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n')
    print('\n')
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time in Hours is:', sum(df['Trip Duration'])/3600, " Hours")

    # TO DO: display mean travel time
    duration_sec = df['Trip Duration']/3600    
    print('Total travel time in Hours is:', duration_sec.mean(), " Hours")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('-'*40)
    print('\n')
    

    
    
    
    
#[8] CALCULATE USERS STATS
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n')
   
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Types:\n', df['User Type'].value_counts())
    print('\n')
    
    
    # TO DO: Display counts of gender
    if city != 'washington':
        print('Users Gender:\n', df['Gender'].value_counts())
        print('\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print('Most earliest Birthday is: {}.' .format(df['Birth Year'].min()))
        print('Most Recent Birthdays: {}.' .format(df['Birth Year'].max()))
        print('Most common Birthday is: {} with count value equlas to {}.'.format(([df['Birth Year'].value_counts().idxmax()]) ,df['Birth Year'].value_counts().max()))

  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('-'*40)
    print('\n')
   

    
    
#[9] GET RAW DATA
 
def fetch_raw(df):
    #pd.set_option('display.max_colwidth', None)
    print('\n Displaying raw data')
    rows = 5
    start_i = 0
    end_i = rows-1
    loop_ind = True
    print_data = True
    
    while loop_ind == True:       
        if print_data == True:
            print('\n', df.iloc[start_i:end_i+1, :])
            temp = df.shape[0] - 5
            if temp > 5:
                start_i += rows
                end_i += rows
              
        answer2 = input('\n Would you like to see the next set of rows? (Y/N)\n')
        answer2 = answer2.lower()
        if answer2 not in ('y', 'n'):
            print("The entered value is invalid, please try again")
            print_data = False
            continue
        elif answer2 == 'y':
            print_data = True
            continue
        elif answer2 == 'n':
            loop_ind = False
            print("Okie Thank you!")
            break
    
    
   

def display_raw_data(df):
    
    print('-'*40)
    print('-'*40)
    print('----------DISPLAYING RAW DATA-----------')                                                  
    print('-'*40)
    print('-'*40)
   
    
    while True:
        answer = input('\n Would you like to see 5 lines of the raw data? (Y/N)\n')
        answer = answer.lower()
        if answer not in ('y', 'n'):
            print("The entered value is invalid, please try again")
            continue
    
        elif answer == 'y':
            fetch_raw(df)
            break
        elif answer == 'n':
            print("Okie Thank you!")
            break
            
            

  
            
  
    
def main():
    while True:
        city, month, day= get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('-'*40)
            print('-'*40)
            print('----------THANK YOU, BYE-----------')                                                  
            print('-'*40)
            print('-'*40)
            print('\n')
            print('\n')
    
            break


if __name__ == "__main__":
	main()
