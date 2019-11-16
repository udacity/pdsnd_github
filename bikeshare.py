import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    city=input("Would you like to see data for Chicago, New York, or Washington?\n").lower()
    #if input in any format, it converts it to lower case
    #Use a while loop to handle invalid inputs
    while(True):
        if(city in CITY_DATA):
            break
        else:
            city=input('Enter correct city: ').lower()
            

    check=input("Would you like to filter the data by month, day, both, or not at all? Type \"none\" for no time filter.\n").lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while(True):

        if check=="both":

        # TO DO: get user input for month (january, february, ... , june)
           month=input("Which month? January, February, March, April, May, or June?\n").lower()
        #Use a while loop to handle invalid inputs
           while(True):
                if(month in months):
                    break
                else:
                    month=input('Enter correct month: ').lower()
        # TO DO: get user input for day of week (monday, tuesday, ... sunday)
           day=int(float(input("Which day? Please type your response as an integer (e.g.,Monday=0...Sunday=6).\n")))
        #Use a while loop to handle invalid inputs
           while(True):
                if(0<=day<=6):
                    break
                else:
                    day=int(float(input('Enter correct day (0 to 6): ')))

           break
        elif check=="month":
            month=input("Which month? January, February, March, April, May, or June?\n").lower()
            #Use a while loop to handle invalid inputs
            while(True):
                if(month in months):
                    break
                else:
                    month=input('Enter correct month: ').lower()
            day=None #None for no day filter
            break



        elif check=="day":# TO DO: get user input for day of week (monday, tuesday, ... sunday)
            day=int(float(input("Which day? Please type your response as an integer (e.g.,Monday=0...Sunday=6).\n")))
            #Use a while loop to handle invalid inputs
            while(True):
                if(0<=day<=6):
                    break
                else:
                    day=int(float(input('Enter correct day (0 to 6): ')))
            month="all"#"all" for no month filter
            break
        elif check=="none":#no time filter
            day =None
            month="all"
            break
        else:
            check=input("Would you like to filter the data by month, day, both, or not at all? Type \"none\" for no time filter.\n").lower()


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])



     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        # extract month from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

     # filter by day of week if applicable
    if day != None :
        df['day_of_week'] = df['Start Time'].dt.dayofweek
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if(month =='all'):
        most_common_month=list(df['Start Time'].dt.month.mode())
        #if there are bimodal, trimodal, or multimodal
        if (len(most_common_month)>1):
            print('\nMost common months are:',most_common_month)
        else:
            print('\nMost common month is:',most_common_month[0])


    # TO DO: display the most common day of week
    if(day ==None):
        most_common_day=list(df['Start Time'].dt.dayofweek.mode())
        #if there are bimodal, trimodal, or multimodal
        if (len(most_common_day)>1):
            print('\nMost common days are:',most_common_day)
        else:
            print('\nMost common day is:',most_common_day[0])


    # TO DO: display the most common start hour
    count=df['Start Time'].dt.hour.value_counts()

    most_common_hour=list(df['Start Time'].dt.hour.mode())

    #if there are bimodal, trimodal, or multimodal
    if (len(most_common_hour)>1):
        print('\nMost common hours are:')
        for i in range(len(most_common_hour)):
            print('\n{} , Count:{}'.format(most_common_hour[i],count[most_common_hour[i]]))
    else:
        print('\nMost common hour is:{} , Count:{}'.format(most_common_hour[0],count[most_common_hour[0]]))




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=list(df['Start Station'].mode())

    if (len(most_common_start_station)>1):
        print('\nMost common start stations are: ',most_common_start_station)
    else:
        print('\nMost common start station is: ',most_common_start_station[0])



    # TO DO: display most commonly used end station
    most_common_end_station=list(df['End Station'].mode())

    if (len(most_common_end_station)>1):
        print('\nMost common end stations are:',most_common_end_station)
    else:
        print('\nMost common end station is:',most_common_end_station[0])


    # TO DO: display most frequent combination of start station and end station trip
    df['tripd']=df['Start Station']+" to "+df['End Station']
    most_common_trip=list(df['tripd'].mode())
    count=df['tripd'].value_counts()
    if (len(most_common_trip)>1):
        print('\nMost common trips are:')
        for i in range(len(most_common_trip)):
            print('{}, Count:{}'.format(most_common_trip[i],count[most_common_trip[i]]))
    elif(len(most_common_trip)==0):
        print("\nThere is no common trip")
    else:
        print('\nMost common trip is:{} , Count:{}\n'.format(most_common_trip[0],count[most_common_trip[0]]))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    time1=total_travel_time
    day=time1//(24*3600)
    time1%=(24*3600)
    hour=time1//3600
    time1%=3600
    minutes=time1//60
    time1%=60
    seconds=time1
    print("\nTotal travel time is {} days {} hours {} minutes {} seconds".format(day,hour,minutes,seconds))




    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    time2=mean_travel_time
    day2=time2//(24*3600)
    time2%=(24*3600)
    hour2=time2//3600
    time2%=3600
    minutes2=time2//60
    time2%=60
    seconds2=time2 #أاحذف الايام ؟
    print("\nMean travel time is {} days {} hours {} minutes {} seconds".format(day2,hour2,minutes2,seconds2))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nNumber of subscribers are {}\n\nNumber of customers are {}\n'.format(user_types['Subscriber'],user_types['Customer']))


    # TO DO: Display counts of gender
    if('Gender' in df):#The Chicago and New York City files also have Gender and Birth Year columns
        gender = df['Gender'].value_counts()
        print('\nNumber of male users are {}\n\nNumber of female users are {}\n'.format(gender['Male'],gender['Female']))



    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):#The Chicago and New York City files also have Gender and Birth Year columns
        earliest_year=df['Birth Year'].min()
        recent_year=df['Birth Year'].max()
        most_common_year=df['Birth Year'].mode()[0]
        print('\nEarliest birth year is {}\n\nRecent birth year is {}\n\nMost popular birth year is {}\n'.format(int(earliest_year),int(recent_year),int(most_common_year)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):

    #omit columns from visualization
    if('month' in df):
        df = df.drop(['month'], axis = 1)
    if('day_of_week' in df):
        df = df.drop(['day_of_week'], axis = 1)
    if('tripd' in df):
        df = df.drop(['tripd'], axis = 1)



    rowIndex = 0

    display_raw_data=input("Do you want to see the raw data?: ").lower()
    while(True):
        if(display_raw_data=='yes'):
            print(df[rowIndex: rowIndex + 5])
            rowIndex = rowIndex + 5
            display_raw_data=input("Do you want to see 5 more rows of the data? ").lower()
        elif(display_raw_data=='no'):
             break;
        else:
            display_raw_data=input("Do you want to see raw data?Please write 'yes' or 'no'. ").lower()


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('\nThank you\n')
            break




if __name__ == "__main__":
	main()
