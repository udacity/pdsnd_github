import time
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

#dictionary where csv files can be accessed
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # used while loops to verify inputs.  The outer loop verifies all the user inputs are correct.  The 3 inner loops verifiy the city,
    # month, and day are valid inputs
    while True:                        #outer while loop
        while True:
            city = input("Which cities information do you want [Chicago, Washington, New York]: ")
            if city.lower() == ("new york"):
                city = "new york city"
            if city.lower() in CITY_DATA:
                break
            else:
                print("invalid input, please enter a valid city")
        
    # TO DO: get user input for month (all, january, february, ... , june),
    # use while loop to catch invalid inputs, use months list to compare user input with
    
        months = ['all', 'january', 'february', 'march', 'april', 'may' , 'june']
        while True:
            month = input("Which month do you want data from [all , or any from January to June]: ")

            if month.lower() in months:
                break
            else:
                print("invalid input, please enter a valid month")
            
     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
     # use while loop to catch invalid inputs, use days of week list to compare user input with.
        days_of_week = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        while True:
            day = input("Which day of the week do you want data from [all, or any day monday through sunday]: ")
    
            if day.lower() in days_of_week:
                break
            else:
                print("invalid input, please enter a valid day")

        user_input = input("\nIs your input correct:\n city:{},\n month:{},\n day:{}?\n Enter yes or no: ".format(city, month, day))       
        if user_input.lower() == 'yes':
            break
        elif user_input.lower() == 'y':
            break
        else:
            print("please enter city, month, day again")

    
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
    # read csv file for user city using city input
    #df = pd.read_csv(CITY_DATA[city.lower()]) 
    chi_df = pd.read_csv('chicago.csv')
    wash_df = pd.read_csv('washington.csv')
    ny_df = pd.read_csv('new_york_city.csv') 
    
    print("processing city data:\n")
    
    print("-"*40)
    

    df = pd.concat([chi_df, ny_df, wash_df],keys = ['chicago', 'new york city', 'washington'],
                names = ['Cities', 'Row ID'],sort = False)
    
    #df = df.dropna()
    
  # convert year_start into a format that can be accessed to pull day, month and year
    df['year_start'] = pd.DatetimeIndex(df['Start Time']).year
    
    #extract month and day of week from Start Time to create new columns
    #use to_datetime to extract month and day names from start time column
    
    df['months'] = pd.to_datetime(df['Start Time']).dt.month_name()

    df['days'] = pd.to_datetime(df['Start Time']).dt.day_name()
    
    #determine if the user input is all or is a specific month or day, then copy to dataframe
    if month.lower() != 'all':
        df_month = df[df['months'].str.contains(month.title())] 
        df = df_month.copy()
    
    if day.lower() != 'all':
        df_day = df[df['days'].str.contains(day.title())]
        df = df_day.copy()
        
    if city.lower() == 'new york':
        city = ' new york city'
        
    df = df.loc[city]
    
    if city == 'washington':
        gender_value = {0: 'male', 1: 'female'}
        random_value = np.random.randint(2)
        #df['Gender'].fillna(value = lambda x: gender_value(random_value), inplace = True)
        df['Gender'].fillna(value = chi_df['Gender'].value_counts().index[random_value], inplace = True)
        #df['Gender'].fillna(value = chi_df['Gender'].value_counts().index[random_value], inplace = True)
        df['Birth Year'].fillna(value = ny_df['Birth Year'].value_counts().index[random_value], inplace = True )
           
    print("Looking at first rows of {}:\n {}".format(city, df.stack().head(9)))  #print the first few rows of the dataframe 
    print("df missing data:\n{}".format(df.isna().sum()))                                                                  #from user choice ofcity
    print("\ndf shape {}\n df column names:\n{}".format(df.shape, df.columns))   #show shape of dataframe to get idea of size of data
    
    while True:
        proceed = input("\nto continue enter yes\n")
        if proceed.lower() == 'yes':
            break
        elif proceed.lower() == 'y':
            break
    
    return df   
    print('-'*40)
    
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #show data by months
    month_counts = df.groupby('months')['months'].count()
    print("months:\n{}".format(month_counts))
    
       # TO DO: display the most common month
    #common_month = df['months'].mode()
    print("\nThe most popular month is {}\n".format(df['months'].mode()))
    
    #show data by days
    day_count = df.groupby('days')['days'].count()
    print("days:\n{}".format(day_count))
    
    # TO DO: display the most common day of week
    common_day = df['days'].mode()
    print("\nThe most popular day is {}\n".format(common_day))
    
    # TO DO: display the most common start hour
    common_hour = pd.to_datetime(df['Start Time']).dt.time.mode() 
    print("The most common hour to start is \n{}".format(common_hour))
    
    common_month_day = df.groupby(['months', 'days']).size().nlargest(1)
    print("\nThe most frequent month and day to ride is \n{}".format(common_month_day))
    
    proceed = input("\nto continue enter")
    if proceed.lower() == 'yes':
        return
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    station_counts = df.groupby('Start Station')['Start Station'].count()
    print("\nStart Station counts:\n{}".format(station_counts.sort_values().tail(5)))
    
     # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()
    print("\nThe most common starting point is \n{}".format(common_start_station))

    # TO DO: display most commonly used end station
    end_station_counts = df.groupby('End Station')['End Station'].count()
    print("\nEnd Station counts:\n{}".format(end_station_counts.sort_values().tail(5)))
    
    common_end_station = df['End Station'].mode()
    print("\nThe most common stopping point is \n{}".format(common_end_station))

       # TO DO: display most frequent combination of start station and end station trip
    common_start_stop = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("\nThe most common start and stop stations are \n{}".format(common_start_stop))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    proceed = input("\nto continue enter")
    if proceed.lower() == 'yes':
        return 

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    travel_counts = df.groupby('Gender')['Trip Duration'].mean()
    print("The average trip duration by\n{}".format(travel_counts))
        
     # TO DO: display total travel time
    total_travel = df['Trip Duration'].mode()
    print("Longest travel time:\n{}\n".format(total_travel))
    
    # TO DO: display mean travel time
    travel_mean = df['Trip Duration'].mean()
    print("The average travel time is {} minutes".format(travel_mean/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    proceed = input("\nto continue enter")
    if proceed.lower() == 'yes':
        return 
    elif proceed.lower() == 'y':
        return 

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print("Count of user types: \n{}".format(user_type_count))
    
    user_by_gender = df.groupby('Gender')['User Type'].count()
    print("user gender {}\n".format(user_by_gender))
    
    
        # TO DO: Display counts of gender
        #gender_fill = df['Gender'].fillna(method = 'ffill')   
    gender_counts = df['Gender'].fillna(method = 'ffill').value_counts()
    print("Gender counts \n{}".format(gender_counts))
    
    df['age'] = df['year_start'] - df['Birth Year'].fillna(method = 'ffill')
    
    gender_age = df.groupby('Gender')['age'].mean()
    print("Gender by average age \n{}".format(gender_age))
    
    df['age 50'] = df['age'] > 50
    df['Trip > 5'] = df['Trip Duration'] > 300
    print("Trip duration over 5 minutes by person over 50\n{}\n".format(df..cut(groupby('age 50')['Trip > 5'].value_counts())))
    age_range = df.groupby('Gender')['age']
    print("Age ranges\n{}".format(age_range.describe()))
    # TO DO: Display earliest, most recent, and most common year of birth
    
    birth_year_earliest = df['Birth Year'].min()
    print("The earliest birth year is {}".format(birth_year_earliest))

    birth_year_recent = df['Birth Year'].max()
    print("The most recent birth year is {}".format(birth_year_recent))

    birth_year_common = df.groupby(['Birth Year']).size().nlargest(1)
    print("The most common year {}".format(birth_year_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
      
    proceed = input("\nto continue enter")
    if proceed.lower() == 'yes':
        return 
    
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
