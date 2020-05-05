import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    
#     set values don't have to false
    have_city = have_filter = have_month = have_day = False
#     set values to empty string
    city = filter_type = month = day = ''
    
#     get city name
    while have_city == False:
        city = input('Would you like to see data for \'Chicago\', \'New York City\', or \'Washington\'? \n').lower()
        if city in CITY_DATA.keys():
            have_city = True
        else:
            print('Choose one of the given cities.')
#         try:
#             city = input('Would you like to see data for \'Chicago\', \'New York\', or \'Washington\'? \n').lower()
#             file = open(CITY_DATA[city])
#             have_city = True
#         except:
#             print('try again')
            
    
    
#     get filter type
    filter_types = ['month','day','both','none']
    while have_filter == False:
        filter_type = input('How would you like to filter the data? Enter \'month\', \'day\', \'both\', or \'none\' \n').lower()
        if filter_type in filter_types:
            have_filter = True
        else:
            print('try again')
            
            
    month = 'all'
    day = 'all'
    
    months = ['january','february','march','april','may','june']
    if filter_type == 'month' or filter_type == 'both':
        while have_month == False:
            month = input('Which month - \'January\', \'February\', \'March\', \'April\', \'May\', or \'June\'? \n').lower()
            if month in months:
                have_month = True
            else:
                print('Choose among the given options.')
            
    
    days = range(0,7)
    weekDays = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday',' Friday', 'Saturday']
    if filter_type == 'day' or filter_type == 'both':
        while have_day == False:
            day_num = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? Enter number 0 to 6. eg. 0 = Sunday \n')
            try:
                if int(day_num) in days:
                    day = weekDays[int(day_num)-1]
                    have_day = True
                else:
                    print('Choose from 0 to 6.')
            except:
                print('Choose from 0 to 6.')
                

        
    print('-'*40)
    return city, month, day
    # TO DO: get user input for month (all, january, february, ... , june)
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)



def load_data(city, month, day):
    city = city
    month = month
    day = day

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
    popular_start_month = df['month'].mode()[0]
    print('Most Popular Start month:', popular_start_month)

    # TO DO: display the most common day of week
    popular_d_of_week = df['day_of_week'].mode()[0]
    print('Most Popular Day of week:', popular_d_of_week)

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['start_hour'].mode()[0]
    print('Most Popular Start Hour:', popular_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().nlargest(1)
    print('The most popular start station: '+ str(start_station.index[0]))
    print('Count: '+ start_station.to_string(index = False,header=False))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().nlargest(1)
    print('The most popular  start station: '+ str(start_station.index[0]))
    print('Count: '+ end_station.to_string(index = False,header=False))
    # TO DO: display most frequent combination of start station and end station trip
    combi = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    popular_trip = str(combi.index[0])
    popular_trip_count = combi.to_string(index = False,header=False)
    print('The most frequent combination of start station and end station trip: '+ popular_trip)
    print('Count: '+ popular_trip_count)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print('Total trip duration: '+ str(total_duration))

    # TO DO: display mean travel time
    avg_duration = df['Trip Duration'].mean() 
    print('The average duration: '+ str(avg_duration))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

# or type_count = df['User Type'].value_counts().to_numpy()
    start_time = time.time()
    type_count = df['User Type'].value_counts().values 
    # get indeces
    keys = df['User Type'].value_counts().index

# print both
    # TO DO: Display counts of user types
    for (k,v) in zip(keys,type_count):
        print(str(k),': ',str(v))
        
        
    # TO DO: Display counts of gender
    # get values
    gender_info = df['Gender'].value_counts()
    gender_count = gender_info.values 
    # get indeces
    genders = gender_info.index

    for (k,v) in zip(genders,gender_count):
        print(str(k),': ',str(v))

    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_cData():
    mistakesCount = 0
    while mistakesCount < 3:
        cData = input('Would you like to see the raw data? Enter \'Yes\' or \'No\.').lower()
        if cData =='yes':
            return True
        elif cData == 'no':
            return False
        else:
            print('Unrecognizable input.')
            mistakesCount+=1
    return False


def get_cData_again():
    mistakesCount = 0
    while mistakesCount < 3:
        cDataagain = input('Would you like to see more data? Enter \'Yes\' or \'No\.').lower()
        if cDataagain =='yes':
            return True
        elif cDataagain == 'no':
            return False
        else:
            print('Unrecognizable input.')
            mistakesCount+=1
    return False
    
def show_raw_data(df):
    cData = get_cData()
    row_start = 0
    row_end = 5
    row_total = df.shape[0]+1
    
    if cData == False:
        pass
    else:
        while cData == True:
            if row_end<= row_total:
                print('row start: ' + str(row_start) + '  row end: ' + str(row_end))
                print(df[row_start:row_end]) 
                row_start += 5
                row_end += 5
            else:
                print('row start: ' + str(row_start) + '  row end: ' + str(row_end))
                print(df[row_start:row_total]) 
                row_start = 0
                row_end = 5
            cData = get_cData_again()
# 
# 

def main():
    while True:
        
        city, month, day = get_filters()
        df = load_data(city, month, day)


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'washington':
            user_stats(df)
        
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
