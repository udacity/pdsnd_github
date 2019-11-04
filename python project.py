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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("\nPlease enter the city you want to filter by? new york city, chicago or washington?\n").lower()

    while (True):
        if (city == 'new york city' or city == 'chicago' or city == 'washington'):
            break
        else:
            city = input("enter one of the three cities.").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('\nWhich month - January, February, March, April, May, or June?\n'.title()).lower()



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n'.title()).lower()

    

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
    df['hour'] = df['Start Time'].dt.hour



    #filter by month if applicable 

    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        
    	# filter by month to create the new dataframe
        df = df[df['month'] == month]



    #filter by day if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""



    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()



    # TO DO: display the most common month
    print("The most common month is :", df['month'].value_counts().idxmax())

    

    # TO DO: display the most common day of week
    print("The most common day of week is :", df['day_of_week'].value_counts().idxmax())

    # TO DO: display the most common start hour
    print("The most common start hour is :", df['hour'].value_counts().idxmax())



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def station_stats(df):
    """Displays statistics on the most popular stations and trip."""



    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station :", df['Start Station'].value_counts().idxmax())


    # TO DO: display most commonly used end station
    print("The most commonly used end station :", df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip

    start_end = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}".format(start_end[0], start_end[1]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""



    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # TO DO: display total travel time
    print("Total travel time :", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Mean travel time :", df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def user_stats(df):
    """Displays statistics on bikeshare users."""



    print('\nCalculating User Stats...\n')
    start_time = time.time()



    # TO DO: Display counts of user types
    print("Counts of user types:", df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print("Counts of gender:", df['Gender'].value_counts())

    except KeyError:
      print("error")



    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        print("The most common birth year:", df['Birth Year'].idxmax())

    except KeyError:
      print("error")

    try:
        print("The most recent birth year:", df['Birth Year'].max())

    except KeyError:
      print("error")

    try:

        print("The most earliest birth year:", df['Birth Year'].min())

    except KeyError:

      print("error")



    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

    



def display_data(df):
    answer = input('\nWould you like to see 5 raw data? Enter yes or no.\n')
    start = 0
    end = 5
    if answer == 'yes':
        while end <= df.shape[0]:
            print(df.iloc[start:end])
            start += 5
            end += 5
            answer2 = input('\nWould you like to another see 5 raw data? Enter yes or no.\n')
            if answer2 != 'yes':
                break



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