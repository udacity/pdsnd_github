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
    month='all'
    day='all'
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Would you like to see data for Chicago, New York or Washington\n')
            if city.lower() not in ['chicago','washington','new york']:
                print('Looks like you entered something incorrect! Please check again.')
                continue
            else:
                break
        except ValueError:
            print('Looks like you entered something incorrect! Please check again.')
        except KeyboardInterrupt:
            print('Oops! You pressed some on command your keyboard')
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            time_filter = input('Would you like to filter the data by month, day or not at all? Type none for no time filter\n')
            if(time_filter.lower() == 'month'):
                print('We will make sure to filter the data by month\n\n')
                while True:
                    month = input('Which month? January, February, March, April, May or June? Please enter the whole name of the month\n')
                    if month.lower() not in ['january','february','march','april','may','june']:
                        print('Looks like you entered something incorrect! Please check again.')
                        continue
                    else:
                        break
                break
            elif(time_filter.lower() == 'day'):
                print('We will make sure to filter the data by day\n\n')
                while True:
                    day = input('Which day?\n')
                    if day.lower() not in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']:
                        print('Looks like you entered something incorrect! Please check again.')
                        continue
                    else:
                        break
                break
            elif(time_filter.lower() == 'none'):
                month='all'
                day='all'
                break
            else:
                print('Please enter a valid option for filtering the data')
                continue


        except ValueError:
            print('Looks like you entered something incorrect! Please check again.')
        except KeyboardInterrupt:
            print('Oops! You pressed some command on your keyboard')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)



    print('-'*40)
    return city.lower(), month.lower(), day


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
    print('Which is the most common month of travel?')
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

   #extract month from the Start Time column to create a month column
    df['month'] =df['Start Time'].dt.month

# find the most popular month
    popular_month = df['month'].mode()[0]

    print('Most Frequent Month:', popular_month)

    # TO DO: display the most common day of week
    print('Which is the most common day of travel?')
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

   #extract day from the Start Time column to create a weekday column
    df['day_of_week'] =df['Start Time'].dt.weekday_name

# find the most popular day
    popular_day = df['day_of_week'].mode()[0]

    print('Most Frequent Day:', popular_day)

    # TO DO: display the most common start hour
    print('Which is the most common hour of travel?')
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

   #extract hour from the Start Time column to create an hour column
    df['hour'] =df['Start Time'].dt.hour

# find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Frequent Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Which is the most common start station?')
    popular_station = df['Start Station'].mode()[0]
    print(popular_station)
    # TO DO: display most commonly used end station
    print('Which is the most common end station?')
    popular_station = df['End Station'].mode()[0]
    print(popular_station)

    # TO DO: display most frequent combination of start station and end station trip
    print('Which is the most frequent combination of start station and end station trip')
    df['start_end'] = df['Start Station'].astype(str) + "and" + df['End Station'].astype(str)
    popular_combo = df['start_end'].mode()[0]
    print(popular_combo)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('What is the total travel time?')
    total_time = df['Trip Duration'].sum()
    print(total_time)


    # TO DO: display mean travel time
    print('What is the average travel time?')
    avg_time = df['Trip Duration'].mean()
    print(avg_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city,df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('What are the counts of each user type?')
    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    print('What are the counts of each gender?')
    if(city.lower()=='washington'):
        print('No data available for this city')
    else:
        gender_count = df['Gender'].value_counts()
        print(gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    print('Which is the most earliest, most recent and most common year of birth?')
    if(city.lower()=='washington'):
        print('No data available for this city')
    else:
        earliest_year = int(df['Birth Year'].min())
        common_year = int(df['Birth Year'].mode()[0])
        recent_year = int(df['Birth Year'].max())
        print('Earliest Year: ',earliest_year)
        print('Most Recent Year: ',recent_year)
        print('Most common Year: ',common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    try:
        while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(city,df)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                user_input = input('Would you like to see the raw data ? Enter yes or no.\n')

                while user_input.lower() == 'yes':
                    city_name = input('Would you like to see data for Chicago, New York or Washington\n')
                    if city_name.lower() in ['chicago','new york','washington']:
                        rawdata = pd.read_csv(CITY_DATA[city_name])
                        n=5
                        print(rawdata[0:n])
                        while True:
                            more_data = input('Would you like to continue and see the next 5 rows? Enter yes or no\n')
                            if more_data == 'yes':
                                print(rawdata[n:n+5])
                                n=n+5
                                continue

                            else:
                                user_input = 'no'
                                break

                    else:
                        print('Enter a valid city name')
                        continue


                else:
                    print('Okay, time to say bye bye!')
                    break

    except KeyboardInterrupt:
        print('Oops! You pressed some command on your keyboard')




if __name__ == "__main__":
	main()
