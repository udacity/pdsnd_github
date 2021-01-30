import time
import pandas as pd

def program_scope():
    """
        This function displays the program scope
    """
    print('\n\nThis program will produce descriptive statistics on Bike Shares data')
    print('for Chicago, Washington, and New York City.')
    input('\n\nPress Enter to continue...')
    print('\nThe following five types of statistics are provided:')
    print('\n1 - Popular times of travel for each city:')
    print('\n\tmost common month')
    print('\tmost common day of week')
    print('\tmost common hour of day')
    print('\n2 - Popular stations and trip for each city:')
    print('\n\tmost common start station')
    print('\tmost common end station')
    print('\tmost common trip from start to end')
    print('\n3 - Trip duration for each city:')
    print('\ttotal travel time')
    print('\taverage travel time')
    print('\n4 - User info for each city:')
    print('\n\tcounts of each user type (Customer or Subscriber)')
    print('\tcounts of each gender (only available for NYC and Chicago)')
    print('\tmost common year of birth (only available for NYC and Chicago)')
    print('\n5 - Custom search base on city, month, day')
    input('\n\nPress Enter to continue...')

def type_of_report():
    """
        This function takes the users input on what kind of report to perform
    """

    num = {1,2,3,4,5}
    while True:
        try:
            user_type_of_report=int(input('\nWhat kind of report would you like to perform: (Type 1 - 5) '))
            if user_type_of_report in num:
                break
            else:
                raise ValueError
        except ValueError:
            print('\nThat\'s not a valid input!')
            continue
    return user_type_of_report

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    print('-'*50)
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    print('Which city would you like to see bikeshare data?')
    print('Chicago, New York City, Washington')
    print('-'*50)
    while True:
        try:
            city = input('Select a city (Chicago, New York City, or Washington) : ')
            if city.lower() in cities:
                break
            else:
                raise ValueError
        except ValueError:
            print('That\'s not a valid input!')
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    print('\nWhich month would you like to see bikeshare data? Type "All" to see every month')
    print('-'*80)
    while True:
        try:
            month = input('Enter the month for data review: ')
            if month.lower() in months:
                break
            else:
                raise ValueError
        except ValueError:
            print('That\'s not a valid input!')
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_week = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    print('\nWhich day of week would you like to see bikeshare data? Type "All" to see every day')
    print('-'*80)
    while True:
        try:
            day = input('Enter the day of week for data review: ')
            if day.lower() in day_of_week:
                break
            else:
                raise ValueError
        except ValueError:
            print('That\'s not a valid input!')
            continue

    print('-'*80)

    load_data(city, month, day)
    return

def pre_data(df, month, day):
    """
        This function prepares the dataframe.
        It converts the object time into datetime values.
        It adds two columns for month and day of the week.
        It filters the dataframe on months and day of the week.
    """
    df.fillna(0, inplace=True)
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['End Time']=pd.to_datetime(df['End Time'])
    df['Month']=df['Start Time'].dt.month_name()
    df['Day_of_week']=df['Start Time'].dt.day_name()

    if month !='all':
        df=df.query('Month==@month.title()')
    if day !='all':
        df=df.query('Day_of_week==day.title()')
    df.drop(['Month', 'Day_of_week', 'Hour of Day'], axis = 1, inplace = True)
    return df

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
    if city.lower() == 'washington':
        df = pd.read_csv('./washington.csv')
    elif city.lower() == 'new york city':
        df = pd.read_csv('./new_york_city.csv')
    elif city.lower() == 'chicago':
        df = pd.read_csv('./chicago.csv')
    else:
        print('Error with data!')

    df = pre_data(df, month, day)
    display(df, city)

def display(df, city):
    """
        This function displays the first five rows of the dataframe
        It asks the user if they would like to see the whole filter DataFrame
        It displays the whole filter dataframe
    """
    print('The following data is for the city of ' + city.capitalize() + '\n')
    print('Sample data of the five first row and headings.\n')
    print(df.head(5))
    restart = input('\nWould you like to the whole data set? Enter yes or no.\n')
    if restart.lower() == 'yes':
        print(df)

def time_stats():
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    cities = ['chicago','washington','new_york_city']
    print('Most Common Per City:\tMonth\t\tDay of Week\tHour of Day')
    print('-'*70)
    for city in cities:
        df=pd.read_csv(city+'.csv', usecols = ['Start Time'])
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['Month']=df['Start Time'].dt.month_name()
        df['Day_of_Week']=df['Start Time'].dt.day_name()
        df['Hour_of_Day']=df['Start Time'].dt.hour
        month_count = df.Month.value_counts()
        month_index = month_count.index[0]
        day_of_week = df.Day_of_Week.value_counts()
        day_of_week_index = day_of_week.index[0]
        hour_of_day = df.Hour_of_Day.value_counts()
        hour_of_day_index = hour_of_day.index[0]
        print(city.capitalize() + ' :\t\t ' + month_index + '\t\t' + day_of_week_index + '\t\t' + str(hour_of_day_index))
    print('-'*70)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)


def station_stats():
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    """TO DO: display most commonly used start station"""
    cities = ['chicago','washington','new_york_city']
    print('-'*70)
    for city in cities:
        df=pd.read_csv(city+'.csv', usecols = ['Start Station', 'End Station'])
        count_start_station = df['Start Station'].value_counts()
        count_end_station = df['End Station'].value_counts()
        count_trip = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)
        start_station = count_start_station.index[0]
        end_station = count_end_station.index[0]
        trip = count_trip.index[0]
        print('Most Common Per ' + city.capitalize())
        print('\nStart Station:\t\t' + start_station + '\t\t# of Start: ' + str(count_start_station[0]))
        print('End Station:\t\t' + end_station + '\t\t# of End: ' + str(count_end_station[0]))
        print('Trip:\t\t\t' + str(trip) + '# of Trips: ' + str(count_trip[0]) + '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)


def trip_duration_stats():
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    cities = ['chicago','washington','new_york_city']
    print('-'*70)
    for city in cities:
        df=pd.read_csv(city+'.csv', usecols = ['Trip Duration'])
        mean = df.mean()
        sum = df.sum()
        print(city.capitalize() + '\t\tAverage Trip(minutes): ' + str(int(mean[0]/60)) +'\tTotal Time(hours): ' + str(int(sum[0]/60/60)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)


def user_stats():
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    cities = ['chicago','washington','new_york_city']
    print('-'*70)
    for city in cities:
        df = pd.read_csv(city + '.csv', usecols= lambda x: x in ['User Type', 'Gender', 'Birth Year'])
        if set(['Gender', 'Birth Year']).issubset(df.columns):
            df.fillna(0, inplace=True)
            df['Birth Year']=df['Birth Year'].astype(int)
            gender_count = df['Gender'].value_counts()
            birth_count = df['Birth Year'].value_counts()

        user_type_count = df['User Type'].value_counts()
        print('\n\n' + city.capitalize() +'\n\n'+ str(user_type_count) + '\n\n' + str(gender_count) + '\n\n' + str(birth_count))
        print('-'*70)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*70)


def main():
    while True:
        program_scope()
        number = type_of_report()
        if number == 1:
            time_stats()
        elif number == 2:
            station_stats()
        elif number == 3:
            trip_duration_stats()
        elif number == 4:
            user_stats()
        elif number == 5:
            get_filters()
        else:
            Pirnt('Error Occurred - Please exit program!')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
