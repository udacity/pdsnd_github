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

    while True:
        city=input('Please,enter the city you want from list below\nChicago  or New York City or Washington\n').lower()
        if city in ('chicago','new york city', 'washington'):
           break
        else:
             print('We apology, City is not found')
             continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Please,enter the month you need from list below\nall , January ,February, March,April, May or June \n').lower()


        if  month in ('all','january', 'february', 'march', 'april', 'may', 'june'):
            break

        else:
            print('We apology, Month is not found')
            continue


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
           day=input('Please,enter the day of week you need from list below\nall ,Sunday, Monday , Tuesday, Wednesday , Thursday , Friday or Saturday \n').lower()
           if day in ('all','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
                break
           else :
                 print('Not found')
                 continue


    print('-'*40)
    return city,month, day

def load_data(city,month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month']=df['Start Time'] .dt.month
    df['day_of_week']=(pd.to_datetime(df['Start Time'])).dt.weekday_name

    if month != 'all' :
        list_months=['january', 'february', 'march', 'april', 'may', 'june']
        Month=list_months.index(month)+1
        df=df[df['Month'] == Month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Hour'] = df['Start Time'].dt.hour
    # TO DO: display the most common month\
    Common_month = df['Month'].mode()[0]
    print('The most common Month is', Common_month)

    # TO DO: display the most common day of week
    Common_day = df['day_of_week'].mode()[0]
    print('The most common Day is', Common_day)

    # TO DO: display the most common start hour

    common_hour = df['Hour'].mode()[0]
    print('The most common Hour is', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    count_start=df['Start Station'].value_counts()
    common_start=count_start.idxmax()
    print(' The most commonly used start station:', common_start)


    # TO DO: display most commonly used end station
    count_end = df['End Station'].value_counts()
    common_end=count_end.idxmax()
    print('The most t commonly used end station:', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station =pd.DataFrame(df.groupby(['Start Station', 'End Station']).size().nlargest(1).reset_index())
    print('The most Commonly used combination of start station and end station trip:', Combination_Station['Start Station'].iloc[0], " and ", Combination_Station['End Station'].iloc[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time_s = sum(df['Trip Duration'])
    print(' The total travel time is ', Total_Travel_Time_s/86400, "Days")

    # TO DO: display mean travel time
    Mean_Travel_Time_h = df['Trip Duration'].mean()
    print(' The mean travel time is', Mean_Travel_Time_h/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats_and_type(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users= df['User Type'].value_counts()
    #print(user_types)
    print('The user Type are\n', users)

    # TO DO: Display counts of gender
    try:
      gender = df['Gender'].value_counts()
      print('The gender Types:\n', gender)
    except KeyError:
      print("We apology, The gender Types not found")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Earliest = df['Birth Year'].min()
      print('The earliest year is ', Earliest)
    except KeyError:
      print("We apology, The earliest year not found")

    try:
      Recent = df['Birth Year'].max()
      print(' The most recent year is ', Recent)
    except KeyError:
         print("We apology, The most recent year not found")

    try:
      Common = df['Birth Year'].value_counts().idxmax()
      print('The most common year is', Common)
    except KeyError:
      print("We apology, The most common year not found")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def Row_data(df):
    view_data = input("Would you like to displays statistics on the most frequent times of travel.? Enter yes or no?")
    start_loc = 0
    while True :
      if   view_data=='yes' :
        start_loc += 5
        print(df.iloc[0:start_loc])
        view_display = input("Do you wish to continue?: ").lower()
        if  view_display=='yes':
            start_loc += 5
            print(df.iloc[0:start_loc])
        else:
            break
      else:
        break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city,month,day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats_and_type(df)
        Row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
# resources : https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
