import time
import pandas as pd
import numpy as np
from IPython.display import display


# the dictionaries used for user inputs
CITY_DATA = { 'Chicago': 'chicago.csv', 'New York City': 'new_york_city.csv', 'Washington': 'washington.csv' }

Days_of_Week =  {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6, 'All':'All'}

Months_of_year = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,'All':'All'}



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
    chosen_city = ''
    while chosen_city not in CITY_DATA.keys():
        chosen_city = input("Please enter a valid city name of the following:\n"+ str(list(CITY_DATA.keys()))).title().strip()
    city = chosen_city

    # TO DO: get user input for month (all, january, february, ... , june)
    chosen_month = ''
    while chosen_month not in Months_of_year.keys():
        chosen_month = input("Please enter a valid month from the following:\n"+ str(list(Months_of_year.keys()))).title().strip()
    month = chosen_month

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    chosen_day = ''
    while chosen_day not in Days_of_Week.keys():
        chosen_day = input("Please enter a valid day of week from the following:\n"+ str(list(Days_of_Week.keys()))).title().strip()
    day = chosen_day
    
    print('-'*40)
    #choices summary
    print('The statistics will be calculated based on these filters:\n' + 'City:', city, '-' ,'Month:', month,'-' , 'Day of week:', day)
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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] =   pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] =  df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        # filter by month to create the new dataframe
         df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df  = df[df['day_of_week']==day]
    
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = df['month'].mode()[0]
    month_count= df['month'].astype('str').value_counts()[0]
    for key, val in Months_of_year.items():
        if month == val:
            month = key
            break
    print('The most common month is:', month,'- count:', month_count)


    # TO DO: display the most common day of week
    dow_count = df['day_of_week'].value_counts()
    print('The most common day of week is:', dow_count.index[0], '- count:', dow_count[0])


    # TO DO: display the most common start hour
    hour_count = df['Start Time'].dt.hour.astype('str').value_counts()
    print('The most common start hour is:', hour_count.index[0],'- count:',hour_count[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_st_count= df['Start Station'].value_counts()
    print('The most common Start Station is:', start_st_count.index[0],'- count:', start_st_count[0])

    # TO DO: display most commonly used end station
    end_st_count= df['End Station'].value_counts()
    print('The most common End Station is:', end_st_count.index[0],'- count:', end_st_count[0])

    # TO DO: display most frequent combination of start station and end station trip
    tempdf = pd.DataFrame()
    tempdf['comb'] = df['Start Station']  + ' : ' + df['End Station']
    comb_count = tempdf['comb'].value_counts()
    print('The most common Start & End Station combination is:', comb_count.index[0],'- count:', comb_count[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print('The total of all trip duraitons is:', total, 'seconds')


    # TO DO: display mean travel time
    avg = df['Trip Duration'].mean()
    print('The average of all trip duraitons is:', avg, 'seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('The number of users for each category:\n')
    print(user_type_count,'\n')


    # TO DO: Display counts of gender
    for col in df.columns:
        if col == 'Gender':
            gen_df = df['Gender'][df['Gender'].notnull()]
            gender_count =gen_df.value_counts()
            print('The count of gender category:\n')
            print(gender_count,'\n')
            break


    # TO DO: Display earliest, most recent, and most common year of birth
    for col in df.columns:
        if col == 'Birth Year':
            db_df= df['Birth Year'][df['Birth Year'].notnull()]
            earliest = db_df.min()
            recent = db_df.max()
            year_count = db_df.astype('str').value_counts()
            print("The Birth year statistics:\n")
            print('The earliest year is:', int(earliest))
            print('The most recent year is:', int(recent))
            print('The most common year is:',year_count.index[0],'- count:', year_count[0])
            break
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def data_chunks(dataset, chunk_size=5):
    """This functions shows the raw data based on user request until the user ends the display or the reaches its end"""
    # cheking the dataframe before applying any operations
    if type(dataset) == pd.core.frame.DataFrame and len(dataset) > 1:
        # this is initial user input
        userinput= input("do you want to see raw data? please enter 'y' or 'yes'\n")
        x=chunk_size #the number of data rows that we want to show
        w = 0 # the counter for shown data in order to stop when we reach the end of the data
        # the while loop shows the data as long as the answer is yes and the counter showed a number of rows equal or less than the number of rows in the dataset
        while (userinput.lower().strip() == 'yes' or  userinput.lower().strip() == 'y'):
            #this loop cuts the data into chunks to display them for the user as long as we did not reach the end of our data and the user still wants to see more chunks
            for i in range(0,len(dataset),x):
                try:
                    display(dataset.iloc[i:i+x])
                except:
                    print(dataset.iloc[i:i+x])
                w += i+x
                userinput= input("do you want to see more raw data?\n")
                if (userinput.lower().strip() == 'yes' or  userinput.lower().strip() == 'y'):
                    if w < len(dataset):
                        continue
                else:
                    print("you have reached an end point.")
                    break
            else:
                print("You have reached an end point.")
                break
    else:
        raise ValueError("invalid dataframe")
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(CITY_DATA[city], Months_of_year[month],day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_chunks(df)
     
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()




