import pandas as ps
import time
import numpy as ny

city_data={'new york':'new_york.csv','washington':'washington.csv','chicago':'chicago.csv'}

def get_city():
    '''
    request city from user and returns the city name supplied
    Args:
        none
    returns:
        (str) city
    '''
    print('welcome, you can view bikeshare data now!\n')
    city=''
    while city.lower not in ['washington','chicago','new york']:
        city=input('choose a city data to view, washington,new york or chicago?\n' )
        if city.lower()=='new york':
            return 'new york'
        elif city.lower()=='washington':
            return 'washington'
        elif city.lower()=='chicago':
            return 'chicago'
        else:
            print('wrong input, enter right city name now\n')
    return city
def get_filter():
    """
    user to input filter - month or day.
    Args:
        none.
    returns:
        (str)filter - month or day
    """
    filter=""
    while filter.lower() not in ['day','month','none']:
        filter=input('filter option- day or month or none. type \'none\' for none\n')
        if filter.lower() not in ['day','month','none']:
            print('wrong input. try again\n')
    return filter
def get_month():
    """
    prompt user for month under review
    Args:
        none.
    Returns:
        (tuple) Upper and lower point of month
    """
    month=""
    month_dic={'january':1, 'february':2, 'march':3, 'april':4,'may':5, 'jube':6}
    while month.lower() not in month_dic.keys():
        month= input('\n month data of interest - January, February, March, April, May, or June?\n')
        if month.lower() not in month_dic.keys():
            print('wrong input. try again\n')
    month=month_dic[month.lower()]
    return month
def get_day():
    '''prompt user for day and return the day supplied.
    Args:
        none
    Returns:
        (tuple) Lower limit, upper limit of date on the bikeshare data.
    '''
    day=""
    day_dic={'mon':'Monday', 'tue':'Tuesday', 'wed':'Wednesday','thu':'Thursday','fri':'Friday','sat':'Saturday','sun':'Sunday'}
    while day.lower() not in day_dic.keys():
        day=input('day to view - mon, tue, wed, thu, fri, sat, sun\n')
        if day.lower() not in day_dic.keys():
            print('wrong input. try again\n')
    day=day_dic[day.lower()]
    return day
def get_month(df):
    """
    shows popular month in the bikeshare database
    Args:
        bikeshare dataframe.
    Returns:
        None.
    """
    print('\n determine the most popular month.')
    start_time=time.time()
    months=['January', 'February','March', 'April','May','June']
    value=int(df['start Time']).dt.month.mode())
    g_month=months[value-1]
    print('\n Most popular month is {}'.format(g_month))
    print("\n it require %s seconds." %(time.time()-start_time))
    print('-'*40)

def get_day(df):
    """
    Display the most popular day for bikeshare dataframe
    Args:
        bikeshare dataframe.
    Returns:
        None.
    """
    print('\n determines the most popular day...')
    start_time=time.time()

    day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday']
    value=int(df['start Time'].dt.dayofweek.mode())
    m_day=day[value]
    print('\n most popular day is {}'.format(m_day))
    print("\n it requires %s seconds.")%(time.time()-start_time))
    print('-'*40)

def get_hour(df):
    """
    determine most popular popular_hour
    Args:
        bikeshare dataframe.
    Returns:
        None.
    """
    print('\n determine most popular hour...')
    start_time=time.time()

    value=int(df['start_time'].dt.hour.mode())
    print('\n most popular hour for start time in 24-hour format is {}'.format(value))
    print("\n it takes %s seconds." % (time.time()-start_time))
    print('-'*40)

def popular_station(df):
    """
    most visited station to start and end trip
    Args:
        bikeshare dataframe.
    Returns:
        None.
    """
    print('\n determine common station for begining and end trip...')
    start_time=time.time()
    start=df['start station'].mode().to_string(index=False)
    end=df['end station'].mode().to_string(index=False)
    print('\n the most visited start station is {}'.format(start))
    print('\n the most visited end station is {}'.format(end))
    print("\n it takes %s seconds." %(time.time()-start-time))
    print('-'*40)

def popular_combine_station(df):
    """
    show most combine trip start and end popular
    Args:
        bikeshare dataframe.
    Returns:
        None.
    """
    print('\n find the most combine trip start and end station...')
    start_time=time.time()

    df['trip']=df['Start Station'].str.cat(df['End Station'], sep=' to ')
    value= df['trip'].mode().to string(index=False)
    print('\n most combine trip start and end station is {}'.format(value))
    print("\n it require %s seconds." % (time.time()-start_time))
    print('_'*40)

 def count_gender(df):
    """
    Display counts of gender
    Args:
        bikeshare dataframe.
    Returns:
        None.
    """
    print('\nCalculating The Total Count of Genders...\n')
    start_time = time.time()
    male = (df['Gender'] == 'Male').sum()
    female = (df['Gender'] == 'Female').sum()
    print('\nThe  male is {} and female is {}'.format(male, female))
    print("\nit took %s seconds." % (time.time() - start_time))
    print('-'*40)

def count_user(df):
    """
    shows number of user types
    Args:
        bikeshare dataframe.
    Returns:
        None.
    """
    print('\nCalculating The Total Count of User Types...\n')
    start_time = time.time()

    sub = (df['User Type'] == 'Subscriber').sum()
    cust = (df['User Type'] == 'Customer').sum()
    print('\nThe number of subscriber is {} and Customer is {}'.format(sub, cust))
    us = df['User Type'].value_counts()
    print(us)

def time_travel(df):
    """
    Displays the total and mean trip time
    Args:
        bikeshare dataframe.
    Returns:
        None.
    """
    print('\nCalculating The Total and Mean Travel Time...\n')
    start_time = time.time()

    total_time = df['Trip Duration'].sum()
    mins, sec = divmod(total_time, 60)
    hour, mins = divmod(mins, 60)
    print('The total trip time is {} hours {} minutes and {} seconds'.format(hour, mins, sec))

    mean_time = round(df['Trip Duration'].mean())
    mins, sec = divmod(mean_time, 60)
    #if mins > 60:
    hour, mins = divmod(mins, 60)
    print('The mean trip time is {} hours {} minutes and {} seconds'.format(hour, mins, sec))
    #else:
        #print('The mean trip time is {} hours {} minute and {} seconds'.format(hour, mins, sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def count_age(df):
    """
    Display most common year of birth
    Args:
        bikeshare dataframe.
    Returns:
        None.
    """
    print('\nCalculating The Youngest, Most oldest, and Most Common Year of Birth...\n')
    start_time = time.time()

    dob_oldest = int(df['Birth Year'].min())
    dob_youngest = int(df['Birth Year'].max())
    dob_common = int(df['Birth Year'].mode())
    print('\nThe most earliest year of birth is {}'.format(dob_oldest))
    print('\nThe most recent year of birth is {}'.format(dob_youngest))
    print('\nThe most common year of birth is {}'.format(dob_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_data(df):
    """
    Display individual trip data
    Args:
        bikeshare dataframe.
    Returns:
        None.
    """
    start = 0
    end = 5
    select = ''
    while select.lower() not in ['yes', 'no']:
        select = input('Do you want to view indiviual trip data? Type \'Yes\' or \'No\'\n')
        if select.lower() not in ['yes', 'no']:
            print('Maybe you made a typo. Please try again\n')
        elif select.lower() == "yes":
            print(df.iloc[start:end])
            # Write a while loop
            while True:
                sec_select = input('\nDo you want to view more trip data? Type \'Yes\' or \'No\'\n')
                if sec_select.lower() not in ['yes', 'no']:
                    print('Maybe you made a typo. Please try again\n')
                elif sec_select.lower() == "yes":
                    start += 5
                    end += 5
                    print(df.iloc[start:end])
                elif sec_select == "no":
                    return
        elif select.lower() == "no":
            return
    return

def main():
    while True:
        # Read city name (Either New York, Chicago or Washington)
        city = get_city()
        print('getting requested data from {} for you...'.format(city))

        # Read csv file for the city selected
        df = pd.read_csv(CITY_DATA[city], parse_dates = ['Start Time', 'End Time'])

        df['Start Time'] = pd.to_datetime(df['Start Time'])
        # Read month and day
        filters = get_filter()
        #if filter == 'none':
            #df = df
        if filters == 'month':
            month = get_month()
            df['month'] = df['Start Time'].dt.month
            df = df[df['month'] == month]
        elif filters == 'day':
            day = get_day()
            df['day'] = df['Start Time'].dt.weekday_name
            df = df[df['day'] == day]

        # Most common month
        if filters == 'none':
            get_month(df)

        # Most common day
        if filters == 'none' or filters == 'month':
            get_day(df)

        # Most common hour
        get_hour(df)

        # Most commonly used start and end station
        get_station(df)

        # Displays the most frequent combination of start station and end station
        popular_combine_station(df)

        # Displays the total and mean teavel time
        time_travel(df)

        # Displays the count of each user type
        count_user(df)

        if city == 'chicago' or city == 'new york':
            # Displays the count of gender
            count_gender(df)

            # Display earliest, most recent, and most common year of birth
            count_age(df)

        if city == 'washington':
            print('\nNo gender and birth year data available')


        # Display data info
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
