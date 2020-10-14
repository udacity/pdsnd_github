import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_day():       # Asks the user for a day and returns the specified day
    day = input('\nWhich day? Please type a day M, Tu, W, Th, F, Sa, Su. \n')
    while day.lower().strip() not in ['m', 'tu', 'w', 'th', 'f', 'sa', 'su']:
        day = input('\nPlease type a day as a choice from M, Tu, W, Th, F, Sa, Su. \n')
    return day.lower().strip()
    
def get_month(): # Asks the user to choose the month between Jan to Jun
    month = input('\nChoose month! January, February, March, April, May, or June? Please type the full month name.\n')
    
    #Validate, if not found correct retry
    while month.strip().lower() not in ['january', 'february', 'march', 'april', 'may', 'june']:
        month = input('\nPlease choose between January, February, March, April, May, or June? Please type the full month name.\n')

    return month.strip().lower()

def get_duration():
    '''
    the code below asks the user to choose between month and day of month,
    day of the week or no filters
    '''
    month = dom = day = 'none'
    duration = input('\nChose your filter options: \n -- Month: By month  \n -- DoM: Day of the month \n -- Day: By day of the week \n -- No: No filter at all \n')
    duration = duration.lower()

    if duration == "month":
        print('\n The data is now being filtered by the month...\n')
        return 'month'

    elif duration == "dom":
        print('\n The data is now being filtered by the day of the month...\n')
        return 'day_of_month'

    elif duration == "day":
        print('\n The data is now being filtered by the day of the week...\n')
        return 'day_of_week'

    elif duration == "no":
        print('\n No duration filter is being applied to the data\n')
        return 'none'
    
    input('\n Given input is invalid, do you want to try again...\n')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    print('Enter the city you want to analyze the data for:')
    print('1: For Chicago')
    print('2: New York')
    print('3: Washington')
    print(' ')
    city = input('Please choose the city: ')
    city = city.lower()
    while True:     # for handling the unexpected input by user
        if city == '1' or city == 'chicago':
            print("\nCity : Chicago\n")
            city = 'chicago'
            break;
        if city == '2' or city == 'new york':
            print("\nCity : New York\n")
            city = 'new york city'
            break;
        elif city == '3' or city == 'washington':
            print("\nCity : Washington\n")
            city = 'washington'
            break;
        else:
            # retry
            print('\nPlease enter 1, 2 or 3 or the names of cities\n')
            city = input('Please choose the city: ')
            city = city.lower()
            break;
    
    month = day = 'all'
    
    duration = get_duration()
    # Get user input for month (all, january, february, ... , june)
    if duration == 'month':
        month = get_month()
    
    if duration == 'day_of_month':
        month = get_month()
        day = get_day()

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    if duration == 'day_of_week':
        day = get_day()

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
    print('\nLoading the data... .. .. ..\n')
    df = pd.read_csv(CITY_DATA[city])

    #extracting from Start Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    df["day_of_month"] = df["Start Time"].dt.day

    #Filter by Month
    if month == 'month':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    #Filter by day of week
    if day == 'day_of_week':
        days = ['Monday', 'Tuesday', 
        'Wednesday', 'Thursday', 
        'Friday', 'Saturday', 'Sunday']
        for d in days:
            if week_day.capitalize() in d:
                day_of_week = d
        df = df[df['day_of_week'] == day_of_week]

    #Filter by day of month
    if day == "day_of_month":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = md[0]
        month = months.index(month) + 1
        df = df[df['month'] == month]
        day = md[1]
        df = df[df['day_of_month'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    print('\n ******** Most Common Riding Time ********* ')
    # Display the most common month
    print('\n Month: ')
    m = df.month.mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = months[m - 1].capitalize()
    print(common_month)

    # Display the most common day of week
    print('\n Day of week: ')
    common_dow = df['day_of_week'].value_counts().reset_index()['index'][0]
    print(common_dow)
    
    # Display the most common start hour
    print('\n Start hour: ')
    df['hour'] = df['Start Time'].dt.hour
    common_start_hr = df.hour.mode()[0]
    print(common_start_hr)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    print('\nStart station: ' )
    start_station = df['Start Station'].value_counts().reset_index()['index'][0]
    print(start_station)
    
    #return start_station, end_station

    # Display most commonly used end station
    print('\nEnd station: ')
    end_station = df['End Station'].value_counts().reset_index()['index'][0]
    print(end_station)
    
    # Display most frequent combination of start station and end station trip
    print('\nUsed frequent combination of start station and end station trip: ' )
    result = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(result)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']
    total_ride_time = np.sum(df['Travel Time'])
    print('\n Total trip duration:' + str(total_ride_time))
    
    # Display mean travel time
    mean_ride_time = np.mean(df['Travel Time'])
    print('\n Mean trip duration:' + str(mean_ride_time).split()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        print('\n Counts of user types: ')
        print(df['User Type'].value_counts())
    except:
        print('\n Counts of user types: data not found.')

    # Display counts of gender
    try:
        print('\n Gender count: ')
        print(df['Gender'].value_counts())
    except:
        print('\n No gender data found.')

    # Display earliest, most recent, and most common year of birth
    try:
        print('\n Earliest birth year: ')
        print(str(np.min(df['Birth Year'])))
        print('\n Latest birth year: ')
        print(str(np.max(df['Birth Year'])))
        print('\n Most Frequent birth year: ')
        print(str(df['Birth Year'].mode()[0]))
    except:
        print('No available birth date data for this duration.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def filtered_data(df): # Display raw data from data file
    """Displays filtered data."""
    
    row_index = 0
    show_data = input("\n Display Filtered Data? Answer 'y' or 'n' \n").lower()
    while True:
        if show_data == 'n':
            return
        if show_data == 'y':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5
        show_data = input("\n Show next 5 rows? Answer 'yes' or 'no' \n").lower()
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # Display filtered data
        filtered_data(df)

        # Statistics on data
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter y or n.\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
    main()
