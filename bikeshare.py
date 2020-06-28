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
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    cities = ['new york city', 'chicago', 'washington']
    isCityOk = 'N'
    try:
        while isCityOk == 'N':
            city = str.lower(input("Would you like to see data for Chicago, New York City, or Washington? "))
            if  city in cities:
                isCityOk = 'Y'
            else:
                isCityOk == 'N'

    except ValueError:
        print('That\'s not a valid input')
    except KeyboardInterrupt:
        print('Keyboard interrupt input')

##Filter
    month = 'all'
    day   = 'all'
    isInputOk = 'N'
    try:
        while isInputOk == 'N':
            filter = str.lower(input("Would you like to filter the data by month, day, both, or none? "))
            if (filter == 'month' or filter == 'day' or filter == 'none' or filter == 'both'):
                isInputOk = 'Y'
            else:
                isInputOk = 'N'

    except ValueError:
        print('That\'s not a valid input')
    except KeyboardInterrupt:
        print('Keyboard interrupt input')

    # TO DO: get user input for month (all, january, february, ... , june)
        ##MonthFilter
    months1 = ['january', 'february', 'march', 'april', 'may', 'june']
    months1 = set(months1)
    isMonthOk = 'N'

    try:
        if (filter == 'month' or filter == 'both'):
            while isMonthOk == 'N':
                month = str.lower(input("Enter month:january or february or march or april or may or june: "))
                if month in months1:
                    isMonthOk = 'Y'
                else:
                    isMonthOk = 'N'

    except ValueError:
        print('That\'s not a valid input')
    except KeyboardInterrupt:
        print('Keyboard interrupt input')


    #get user input for day of week (all, monday, tuesday, ... sunday)

    isDayOk = 'N'
    dofwk = 'all'
    day_ofWeek = ['monday', 'tuesday', 'wednesday' , 'thursday', 'friday','saturday','sunday','All']
    day_ofWeek = set(day_ofWeek)


    try:
        if (filter == 'day' or filter == 'both'):
            while isDayOk == 'N':
                dofwk =  str.lower(input("Enter Day of the Week, monday tuesday etc or all: "))

                if dofwk in day_ofWeek:
                    isDayOk = 'Y'
                    day = dofwk
                else:
                    isDayOk = 'N'
                break
    except ValueError:
        print('That\'s not a valid input')
    except KeyboardInterrupt:
        print('Keyboard interrupt input')


    print(city)
    print(month)
    print(day)
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
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

    filename = CITY_DATA[city]
    df = pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['year'] = df['Start Time'].dt.year
    df['day_of_week'] = df['Start Time'].dt.weekday

# filter by month if applicable
    month2='all'
    if month != 'all':

        try:
            # use the index of the months list to get the corresponding int
                months = ['january', 'february', 'march', 'april', 'may', 'june']
                #month = months.index(month) + 1

                monthnum = get_month_num(month)
                # filter by month to create the new dataframe
                df = df[df['month'] == monthnum]

        except KeyError as e:
            print("Invalid Key in Months {} ".format(e))



    if day != 'all':
        try:
            # filter by day of week to create the new dataframe
            # filter by day of week if applicable
            # The day of the week with Monday=0, Sunday=6.
            weekday_num = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
            daynum = weekday_num.index(day)

            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == daynum]


        except KeyError as e:
            print("Invalid Key in days {} ".format(e))
    print('\nFilter used are: City: {} Month: {} Day: {}'.format(city,month,day))
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    popular_month = df['month'].mode()[0]

    count2 = df['month'].value_counts()

    montitle = get_month_title(popular_month)
    print('\npopular_month = ', montitle[0]  ,'count :',  count2[popular_month])


    #  display the most common day of week

    popular_day_of_week = df['day_of_week'].mode()[0]

    count1 = df['day_of_week'].value_counts()

    dowtitle  = get_dow_title(popular_day_of_week)
    print('\npopular__day_of_week = ', dowtitle[0], 'count:',  count1[popular_day_of_week])


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    count = df['hour'].value_counts()
    print('\npopular_hour:', popular_hour , ' count :', count[popular_hour])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()

    # display most commonly used start station
    popular_start_station  = df['Start Station'].mode()[0]

    #display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] +' ' + df['End Station']
    popular_frequent_trip = df['Trip'].mode()[0]

    # new question display trip combination of start station and end station trip in recent year
    print("\n Count of latest 10 trips By Year:\n")
    print(df.groupby(["Trip","year"])["Start Station"].count().tail(10))


    count = df['Start Station'].value_counts()
    print('\npopular_start_station: ', popular_start_station , " count :",count[popular_start_station])
    count = df['End Station'].value_counts()
    print('\npopular_end_station: ' , popular_end_station, " count :" ,count[popular_end_station])
    count = df['Trip'].value_counts()
    print('\npopular_frequent_trip: ', popular_frequent_trip, " count :" ,count[popular_frequent_trip])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    tripduration = df['Trip Duration'].sum()
    size = df['Trip Duration'].size
    print('\nTrip Duration: ' , tripduration , 'count: ', size )

    #display mean travel time
    meantraveltime = df['Trip Duration'].mean()
    print('\nAverage Travel Time: ' , meantraveltime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type= df['User Type'].mode()[0]
    count = df['User Type'].value_counts()
    print('\nPopular User Type: ' , user_type)
    print('\ncount of User Type:\n', count)

    # Display counts of gender
    #check if column exists in the city df.
    result = df.columns
    if 'Gender' in result:
        df['Gender'].fillna('Missing')
        count = df['Gender'].value_counts()
        print('\nGender Type & count:\n', count)
        print("\n Count of User types By Gender:\n")
        print(df.groupby(["Gender","User Type"])["Birth Year"].count())
    else:
        print('\n City data csv is missing column Gender')

    #  Display earliest, most recent, and most common year of birth
    if  'Birth Year' in result:
        df['Birth Year'].fillna(0)
        popular_birth_year= df['Birth Year'].mode()[0]
        count = df['Birth Year'].value_counts()
        print('\nMost Common Birth Year: ', int(popular_birth_year))
        print('\nEarliest Birth Year: ', int(df['Birth Year'].min()))
        print('\nMost Recent Birth Year: ', int(df['Birth Year'].max()))

      # new questions: aggregates by birth year and user type
        print("\n Count of latest 10 User types By Birth Year:\n")
        print(df.groupby(["Birth Year","User Type"])["Gender"].count().tail(10))

        print("\n Count 10 largest User types By Birth Year:\n")
        print(df.groupby(["Birth Year","User Type"])["Gender"].count().nlargest(10))

        print("\n Count 10 smallest User types By Birth Year:\n")
        print(df.groupby(["Birth Year","User Type"])["Gender"].count().nsmallest(10))


    else:
        print('\nCity data csv is missing column Birth Year')

    print("\n This took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_rawdata(df):
    """Displays rawadata if users requests."""

    showraw = str.lower(input('\nDo you want to see raw data in file? Enter yes/no: '))
    if (showraw == 'yes'):
       print('\nRaw Data\n:' , df.head(10))


    # get month number if name is given
def get_month_num(monthtitle):

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    monthnum = months.index(monthtitle) + 1

    return [monthnum]

    # get month name if month number is given
def get_month_title(monthnum):

    months = ['January', 'February', 'March', 'April', 'May', 'June']
    monthtitle = months[monthnum-1]

    return [monthtitle]

    # get weekday name if weekday number is given
def get_dow_title(downum):

    weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    dowtitle = weekday[downum]

    return [dowtitle]

    # get weekday number if weekday name is given
def get_dow_num(dowtitle):

    weekday = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    downum = weekday.index(dowtitle) + 1

    return [downum]


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_rawdata(df)

        restart = input('\nWould you like to restart? Enter yes or no: ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
