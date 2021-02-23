import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS_DATA = [
              'january',    
              'february', 
              'march', 
              'april',
              'may' , 
              'june' ,
              'june' , 
              'july', 
              'august', 
              'september', 
              'october', 
              'november',
              'december',
              'all']

DAYS_OF_WEEK = ['all', 
              'monday', 
              'tuesday', 
              'wednesday', 
              'thursday',
              'friday' , 
              'saturday',
              'sunday',
               'all']

def view_data(df):
    
#to show the first 5 rows of user filtered data
    user_input = input('Would you like to the first 5 rows of your selection? enter yes or no \n').lower()
    i = 0
    while user_input != 'no':
        print(df.iloc[i:i+5])
        i+=5
        user_input = input("Would you like to continue next 5 rows?").lower()
        if user_input == 'yes':
           print(df.iloc[i:i+5]) 
           i+=5
        else:
           break
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
    
    city = input("Please enter City: ")
    while city.lower() not in {
            'chicago',
            'new york city',
            'washington'}:
        city = input("Please try again\nEnter City: ")
        print("City is: " + city)

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("Enter Month (eg. all, january, february ..) : ")
    while month.lower() not in MONTHS_DATA:
        month = input("Please try again.\nEnter Month (eg. all, january, february ..) : ")
        print("Month is: " + month)
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Please enter day of the week (eg. all, monday, tuesday ..) : ")
    while day.lower() not in DAYS_OF_WEEK:
            
        day = input("Please try again.\nEnter day of the week (eg. all, monday, tuesday ..) : ")
        print("Day of the week is: " + day)

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
    df=pd.read_csv(CITY_DATA[city]) 
    
# adding new columns to the data frame
    df['start_time']=pd.to_datetime(df['Start Time'])
    
    df['month'] = df['start_time'].dt.month
    df['day'] = df['start_time'].dt.weekday_name
    
    if month != 'all':
       month = MONTHS_DATA.index(month) + 1
       df=df[df['month']==month]
                
    if day != 'all':
       df = df[df['day'] == day.title()]
    print(df.head())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #pd.to_datetime(df['Start Time'], format='%Y-%m-%d %H:%M:%S')
    #df['month'] = pd.to_datetime(df['Start Time']).dt.month 
    #df = pd.DataFrame(df).head()
    #print(df)
 #   df['month'] = pd.DatetimeIndex(df['Start Time']).year
    # TO DO: display the most common month
    print("The most common month is : ", df['month'].value_counts().idxmax())
  
    # TO DO: display the most common day of week
    #df['day'] = pd.to_datetime(df['Start Time']).dt.dt.weekday_name 
    print("The most common day of the week is : ", df['day'].value_counts().idxmax())
    
    # TO DO: display the most common start hour
    df['start_hour'] = pd.to_datetime(df['Start Time']).dt.hour 
    print("The most common start hour is : ", df['start_hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is : ", df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print("The most commonly used end station is : ", df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    df['combo_station']=df['Start Station'] +" to " + df['End Station']
    print("The most frequent combination of start and end station are : ", df['combo_station'].value_counts().idxmax())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    #Convert to hours
    total_hour=int(df['Trip Duration'].sum(skipna='true') / 60 /60)
    # TO DO: display total travel time
    print("Total travel time (hour) : ", total_hour)

    # TO DO: display mean travel time
    mean_travel_time = int(df['Trip Duration'].mean(skipna='true')/ 60)
    print("Mean Travel Time (in Minutes): ", mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    #data=df['User Type'].value_counts()
    user_type = pd.DataFrame(df['User Type'].value_counts())
    # TO DO: Display counts of user types
    print("Counts of user types : \n", user_type)

    # TO DO: Display counts of gender
    try:
        gender=pd.DataFrame(df['Gender'].value_counts())
        print("Counts of gender : \n", gender)
    except KeyError as e:
        print("Gender information is not avaiable in", city.title())
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("Earliest Year of Birth is : \n",int(df['Birth Year'].min()))
        print("Recent Year of Birth is : \n",int(df['Birth Year'].max()))
        print("Common Year of Birth is : \n",int(df['Birth Year'].value_counts().idxmax()))
    except KeyError as e:
        print("Birth Year information is not available in", city.title())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        print("You have provided \nCity : {}\nMonth : {} \nDay : {} \n".format(city,month,day).title())
        df = load_data(city, month, day)
        view_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
