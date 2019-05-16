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
 
        city = input('Which city would you like to analyse the  data for?(chicago, new york city, washington): ')
        city = city.lower()
        if city in ('chicago', 'new york city', 'washington'):
            print('thank you')  
            break
        else:
            print('please enter a valid city')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
    
        month = input('Would you like to filter the data for a particular month between january to june or all of it?')
        month = month.lower()   
        if month in ('all', 'january', 'february','march', 'april', 'may' , 'june'):
            print('thank you')
            break
        else:
            print('please enter a valid month')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day of the week would you like to apply the filter for or all the days?')  
        day = day.lower()
        if day in ('all', 'monday', 'tuesday','wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('thank you')
            break
        else:
            print('please enter a valid day of the week')
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
    df['day'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
   
    if day != 'all':
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = months[common_month-1]
    print('Most popular month: {}'.format(month))
    # TO DO: display the most common day of week
    common_day =  df['day'].mode()[0]
    print('Most common day of the week: {}'.format(common_day))
    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most common hour of the day: {}'.format(common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_sstation = df['Start Station'].mode()[0]
    print('most commonly used start station: {}'.format(common_sstation))
    # TO DO: display most commonly used end station
    common_estation = df['End Station'].mode()[0]
    print('most commonly used end staton: {}'.format(common_estation))

    # TO DO: display most frequent combination of start station and end station trip
    
    frequent_combination =df.groupby(['Start Station', 'End Station'])
    print('most frequent combination of stations: {}'.format(frequent_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('total travel time: {}'.format(total_time)) 
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('average time travelled: {}'.format(mean_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('count of user_types:\n{}'.format(user_types))
    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('counts of each gender:\n {}'.format(gender_count)) 
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print('oldest people to ride the bicycle are born in {}'.format(earliest_year))
        recent_year = df['Birth Year'].max()
        print('youngest people to ride the bicycle are born in {}'.format(recent_year))
        common_year =  df['Birth Year'].mode()[0]                  
        print('most of the citizens riding the bicycle are born  in {}'.format(common_year))
    except KeyError as e:
        print('No data related to gender and year of birth')   
    finally:    
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        i = 0
        while True:
            print(df.head(5+i).tail())
            Next = input('\nWould you like to view the next five? Enter yes or no.\n')
            i += 5
            if Next.lower() != 'yes':
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
