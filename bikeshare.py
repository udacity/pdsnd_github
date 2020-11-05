import time
import pandas as pd
import numpy as np

#Refactoring code1 : Dataset from csv 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#To get username 
name = input("please input your name here!: ")

#To state your Github (if there is any)

Github = input("please input your Github user-id if you have one!: ")


def get_filters():
    # Define global 2 variables in order to avoid unboundlocalerror!
    month = "march"
    day = "sunday"
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print("\nHello! {} 'Let\'s explore some US bikeshare data!".upper().format(name))
    # TO  ask user input for city (chicago, new york city, washington). 
    while True:
      city = input("\nWhich city would you like to explore the data?  Chicago or New York City or Washington?: ").lower()
      if city.lower() not in ( 'chicago','new york city', 'washington'):
        print("Sorry,You might type wrong city spelling or no attempt city's data.Please try again.")
        continue
      else:
        print("You are going to explore {} city, let's go!".format(city).lower())
        break

   # TO ask user to filter day,month,both,or none until they type correct filter! 
   # Loop the filter as long as user get correct word 
    while True:
        filter_choice = input("\nDo you wish to filter by month,day,both,or none?: ").lower()
        if filter_choice not in ('both','month','day','none'):
            print("Sorry,please type the given filter! which are month,day,both,or none")
            continue
   # If user get correct filter there will be 4 conditions which are 'both'/'month'/'day'/'none'
        else :
   # Condition 1 is both
            if filter_choice == 'both':
                while True:
                    month = input("\nWhich month? (e.g. january, february, march, april, may, june, all): ").lower()
                    if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
                        print("Sorry, I didn't catch that. Try again.")
                        continue
                    else: 
                        while True:
                            day = input("\nWhich day (e.g. sunday, monday, tuesday, wednesday, thursday, friday, saturday, all)?: ").lower()
                            if day.lower() not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
                                print("Sorry, I didn't catch that. Try again.")
                                continue
                            else:
                                break
                        break
    # Condition 2 is month                    
            elif filter_choice == 'month':
                while True:
                    month = input("\nWhich month? (e.g. january, february, march, april, may, june, all: ").lower()
                    if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
                        print("Sorry, I didn't catch that. Try again.")
                        continue
                    else:
                        break
    # Condition 3 is day              
            elif filter_choice == 'day':
                while True:
                    day = input("\nWhich day (e.g. sunday, monday, tuesday, wednesday, thursday, friday, saturday, all)?: ").lower()
                    if day.lower() not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
                        print("Sorry, I didn't catch that. Try again.")
                        continue
    # Condition 4 is none
                    else:
                        day
                        break
                
            elif filter_choice == 'none' : 
                    break  
            break
    print('-'*40)
    return city,month,day
    # load data from city,month,day
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

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)


    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)


    # TO DO: display most commonly used end station

    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)


    # TO DO: display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")


    # TO DO: display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def disp_raw_data(df):
    '''
    Displays statistic data 5 roll as commend from mentor!
    So I need to create these fucntion
    Input:
        the df with all the bikeshare data
    '''
    df = df.drop(['month', 'day_of_month'], axis = 1)
    
def main():
    row_index = 0
    
    while True:
        city,month,day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        raw_data = input("\Would you like to see statistic raw data? please type 'yes or 'no': ").lower()
        while True:
            if raw_data == 'no':
                break
            if raw_data == 'yes':
                print(df[row_index: row_index + 5])
                row_index = row_index + 5
                break
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

#Refactoring code2 : Call all function
if __name__ == "__main__":
	main()

