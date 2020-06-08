import time
import pandas as pd
import numpy as np
# Adding comments according to the 3rd part of assignment

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
    
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    ###         Making a list of cities i.e. ct
    ct=['chicago','new york city','washington']
    city=str(input("Enter the input city i.e. chicago, new york city or washington \n").strip().lower())
    while True:
        #Checking if the city name input is among the 3 cities i.e. from ct
        if(city in ct):
            break
        else:
        #else printing wrong output , please enter again
            print(" wrong output plse enter again  \n")
            city=input("Please enter again between chicago, new york city or washington \n")



    # TO DO: get user input for month (all, january, february, ... , june)

    ###     Making a list of months i.e. mt
    mt=['january','february','march','april','may','june','all']

    month=str(input("Enter the input month for filter i.e. january,febrary,march,april,may,june or all \n").strip().lower())
    while True:
        #checking if the month input is among the list mt
        if( month in mt):
            break
        else:
        #if it is not , telling the user to output again
            print("wrong output\n")
            month=input(" Plse enter again \n")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    ###       Making a list of all days
    da=['all', 'monday','tuesday','wednesday','thursday','friday','saturday','sunday']


    day=str(input("Enter the input day for filter i.e. monday,tuesday,wednesday,thursday,friday,saturday,sunday or all \n").strip().lower())
    while True:
    #checking if the day is correct and if it not telling the user to correct it
        if(day in da):
            break
        else:
            print("wrong output\n")
            day=input("Please enter the day again \n")
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
    #loading data into pandas dataframe
    df = pd.read_csv(CITY_DATA[city])


    ###     Converting startime to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    ###     Extracting month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        #converting the string into integer for month
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        #filtering and equating it to day_of_week
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    lo = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
        '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
    # TO DO: display the most common month
    #getting the value_counts and then extracting the no which have max value_count


    ###              Most common month is month_in_no
    month_in_no=df['month'].value_counts().idxmax()
    print("The most common month is",lo[str(month_in_no)])



    # TO DO: display the most common day of week
    #getting the value_counts and then extracting the no which have max value_count

    ###              Most common day of week is day_in
    day_in=df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is {}".format(day_in))

    
    # TO DO: display the most common start hour
    #getting the value_counts and then extracting the no which have max value_count

    ###              Most common start hour is hour_in
    hour_in=df['hour'].value_counts().idxmax()
    print("The most common day of week is {}".format(hour_in))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #getting the value_counts and then extracting the no which have max value_count
    start_station = df['Start Station'].value_counts().idxmax()
    print("most used start station is: '{}'".format(start_station))


    # TO DO: display most commonly used end station
    #getting the value_counts and then extracting the no which have max value_count
    end_station = df['End Station'].value_counts().idxmax()
    print("most used end station is: '{}'".format(end_station))

    
    # TO DO: display most frequent combination of start station and end station trip
    pair = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).reset_index(name= "counts")
    
    start = pair['Start Station'][0]
    end = pair['End Station'][0]
    print("the start station and end station for most frequent combination are {} and {}".format(start,end))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #summing to get the trip duration and then printing it
    total_time = df['Trip Duration'].sum()
    print("Total Travel Time: {}".format(total_time))
    
    # TO DO: display mean travel time
    #getting the mean to get mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Mean Travel Time: '{}' seconds ".format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    ###     Using value_counts displaying counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender

    ###     Checking if gender column exists in dataframe and then printing the value_counts() of gender types
    if "Gender" in df.columns:
        gender_types = df['Gender'].value_counts()
        print(gender_types)
    else:
        print("No column Gender exists \n")

        
    # TO DO: Display earliest, most recent, and most common year of birth

    ###     Checking if birth year column exists in dataframe and then printing the earliest most recent and common birth year
    if "Birth Year" in df.columns:    
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        common_year=df["Birth Year"].value_counts().idxmax()
        print("Earliest year of Birth is {} \n most recent year of birth is {} \n most common year of birth is {}".format(earliest,most_recent,common_year))
    else:
        print("no column Birth Year exists \n")
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        df1=df
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        ###         Found out that all the columns were not printing to have to globally set printing options. 
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

        ###         Asking the user if he/she wants to see the table
        see=str(input("Would you like to see 5 lines of the tables that you selected , Yes or No \n").strip().lower())
        if(see=="yes"):
            print(df1.head(5))
        ###         restart is yes
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        else:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()
