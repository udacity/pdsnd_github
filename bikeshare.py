import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #  get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city=input('Enter your city:').lower()
    while city not in ['chicago','new york','washington']:
          city=input('sorry not in the range please pick from these three cities chicago ,new york or washington :').lower()
    
    if city.lower() == "new york":
        city+= " city"
      
    #  get user input for month (all, january, february, ... , june)
    month=input('Enter the month to filter by between January to June or not and make sure that the first letter in the upper case :')
    while month not in ['January', 'February', 'March', 'April', 'May', 'June','all']:
          month=input('Enter the month to filter by between January to June or not and make sure that the first letter in the upper case :')


    #  get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Enter the day to filter by between Monday to Sunday or not:').lower()
    while day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
          day=input('Enter the day to filter by between Monday to Sunday or not:').lower()
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
   
    
    if month != 'all':
   
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1      
        df = df[df['month'] == month]
    if day != 'all':
         df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #  display the most common month
    
    print("The most common MONTH is: {}".format(str(df['month'].mode()[0])))
    
    #  display the most common day of week
    
    print('The most common DAY is: {}  '.format(str(df['day_of_week'].mode()[0])))
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common HOUR is: {} '.format(str(df['hour'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #  display most commonly used start station
    print("The most common START STATION is:  {}".format(str(df['Start Station'].mode()[0])))
    #  display most commonly used end station
    EndStation= df['End Station'].mode()[0]
    print("The most common END STATION is:  ",EndStation )
    #  display most frequent combination of start station and end station trip
    df['spe']=df['Start Station']+'  '+df['End Station']
    FrequentCombination=df['spe'].mode()[0]
    print('the most FREQUENT COMBITION of start station and end station is: ', FrequentCombination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #  display total travel time
    
    print('The TOTAL Travel Time is: {} '.format(str(df['Trip Duration'].sum())))
     
    #  display mean travel time
   
    print('The MEAN Travel Time is: {} '.format(str(df['Trip Duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #  Display counts of user types
    u_type=df['User Type'].value_counts()
    print('the count of USER TYPES:  ',u_type)

    #  Display counts of gender
    try:
       print('the count of GENDER:  {}'.format(df['Gender'].value_counts()))
    except KeyError:
       print('we can not count the gender ')
    

    #  Display earliest, most recent, and most common year of birth
    try:
      print('the EARLIEST yaer is : {}'.format(int(df['Birth Year'].min())))
      print('the RECENT yaer is : {}'.format(int(df['Birth Year'].max())))
      print('the most COMMON yaer is : {}'.format(int(df['Birth Year'].mode()[0])))
    except KeyError:
     print('we can not get the year of brith in washington city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
# define a display_data function
def display_data(df): 
   counter_a=0
   counter_b=5
   dis_q=input(" do you want to see raw data?Enter yes or no ").lower()
   while dis_q =='yes':
     if dis_q =='yes': 
        counter_a+=5
        counter_b+=5
        print(df.iloc[counter_a:counter_b])
        dis_q=input(" do you want to see raw data?Enter yes or no ").lower()
        
                       
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
     main()
