import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['january', 'february', 'march','april','may','june','all']

DAY_DATA = ['monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday','all']

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
    
    
    city_n=''
    while city_n.lower() not in CITY_DATA:
        city_n = input("Please chose one of the following cities: chicago, new york city, washington: anywhere here would be fine...\n")
        if city_n.lower() in CITY_DATA:
            city= CITY_DATA[city_n.lower()]
        else:
            print("Let's try this again - one of the cities in the list please: chicago, new york city, washington \n")         
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month_n=''
    while month_n.lower() not in MONTH_DATA:
        month_n = input("And month of choice? january through june or 'all' are available  \n")
        if month_n.lower() in MONTH_DATA:
            month=month_n.lower()
        else:
            print("that month is not in the data buddy, please pick another \n") 
            
  # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_n=''
    while day_n.lower() not in DAY_DATA:
        day_n = input("And the day of the week you are interested in is...? ")
        if day_n.lower() in DAY_DATA:
            day=day_n.lower()
        else:
            print("did you check your spelling? perhaps lets try this again... \n")
    print ('\n \n You have chosen the following selection: city file: {}, month: {}, day: {} '.format(city, month, day))       
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
    df = pd.read_csv(city)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
   

    if month != 'all':
            month = MONTH_DATA.index(month) +1
            df = df[df['month'] == month]
       
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]
      
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    c_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    c_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    c_hour = df['hour'].mode()[0]
    
    print("the most common month: " + MONTH_DATA[c_month].title())
    print("the most common day of week: " + c_day)
    print("the most common start hour: " + str(c_hour) + " oclock")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_ss = df['Start Station'].mode()[0]
    # TO DO: display most commonly used end station
    common_es = df['End Station'].mode()[0]
    # TO DO: display most frequent combination of start station and end station trip
    f_combo = (df['Start Station'] + " AND " + df['End Station']).mode()[0]
    
    print("most commonly used start station: " + common_ss)
    print("most commonly used end station: " + common_es)
    print("most frequent combination of start station and end station trip: " + f_combo) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()

    print("Total travel time: " + str(total_travel))
    print("The mean travel time: " + str(mean_travel))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("counts of user types:  \n" + str(user_types))
    
    
    # TO DO: Display counts of gender
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender = df['Gender'].value_counts()
        print("counts of gender:  " + str(gender))
    

        # TO DO: Display earliest, most recent, and most common year of birth
        e_birth = df['Birth Year'].min()
        print('Earliest birth year: {}\n'.format(e_birth))
        r_birth = df['Birth Year'].max()
        print('Most recent birth year: {}\n'.format(r_birth))
        c_birth = df['Birth Year'].mode()[0]
        print('Most common birth year: {}\n'.format(c_birth) )
    else:
        print('\n Please note: there is no data on GENDER or BIRTH dates available for the city of washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def raw_data(df):
    print(df.head())
    data = 0
    while True:
        raw_data = input('\n would you like to see more data? \n')
        if raw_data.lower() != 'yes':
            return
        data = data + 5
        print(df.iloc[data:data+5])



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()