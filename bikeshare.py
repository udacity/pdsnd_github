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

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #To repeat input request until user enters a valid city
    while True:
        print('Which city would like to analyze?\n')
        print('\t---------------------------------\n\t 1. Chicago \n\t 2. New York City \n\t 3. Washington')
        print('\t---------------------------------')
        city = input("Enter Ciy Name: ").lower()

        if city in CITY_DATA:
            break
        else:
            True

    # get user to choose whether they want to filter by day, month or no filter

    while True:
        answer = input('Would you like to filter your data(yes/y or no/n): ').lower()
        if answer == 'yes' or answer == 'y':
            while True:
                filter_data = input("Would you like to filter by month or day?: ")
                if filter_data == 'month':
                    print('\nMonths run from january to june')
                    print('_______________________________\n')
                    while True:
                        month = input('Enter Month(eg. january ):  ').lower()
                        if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june':
                            day = 'all'
                            break
                    else:
                        True
                    break


                elif filter_data == 'day':
                    while True:
                        day = input('Enter Day (eg. Monday ): ').title()
                        if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day  == 'Friday' or day == 'Saturday' or day == 'Sunday':
                            month = 'all'
                            break
                    else:
                        True
                    break

                else:
                    True
            break

        elif answer == 'no' or answer == 'n':
            print('\nPerforming Statistical Analysis without filter..........................')
            month = 'all'
            day   = 'all'
            break
        else:
            #if invalid input is entered repeat the loop
            True

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    #Ask user to view overview of the city data from top or bottom
    print("---------------------------------------------------------------------------")
    print("Display 5 top and bottom lines of raw data:?")

    while True:
        answer = input("Enter Yes/Y or No/N or Skip/S: ").lower()
        if answer == 'yes' or answer == 'y':

            while True:
                answer_2 = input("Include Raw Data statistics (Yes/No): ").lower()
                if answer_2 == 'yes' or answer_2 == 'y':
                    print('\t_____Top 5 Overview of Raw Data of ' + city.title()+ '_______ ')
                    print(df.head(5))
                    print('\t_____Bottom 5 Overview of Raw Data of ' + city.title() + '______')
                    print(df.tail(5))
                    print('\t_____Raw Data Statistics of'+ city.title() +'_____')
                    print(df.describe())

                    break

                elif answer_2 == 'no' or answer_2 == 'n':
                    print('\t_____Top 5 Overview of Raw Data of ' + city.title()+ '_______ ')
                    print(df.head(5))
                    print('\t_____Bottom 5 Overview of Raw Data of ' + city.title() + '______')
                    print(df.tail(5))

                    break

                else:
                    print('Please Enter a valid answer yes/y or no/n')
                    True
            break

        elif answer == 'skip' or answer == 'no' or answer == 's' or answer == 'n':

            while True:
                describe_answer = input('Display Statistics of Raw Data(yes//y or no/n)?: ').lower()
                if describe_answer == 'yes' or describe_answer == 'y':
                    print('\t_____Raw Data Statistics of ' + city.title() + '_____')
                    print(df.describe())
                    break
                elif describe_answer == 'no' or describe_answer == 'n':
                    break

            else:
                print('Please Enter yes/y or no/n')
                True

            break
    else:
        Print('Please Enter yes/y or no/n')
        True




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

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    most_common_month = df['month'].mode()[0]
    print('Most Common Month: ', most_common_month)



    # display the most common day of week

    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common day: ',most_common_day)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('Most Common Hour: ', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):


    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Common Start Station: ', df['Start Station'].mode()[0])


    # display most commonly used end station
    print('Common End Station: ', df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    frequent_travel_combination = df['Start Station'].mode()[0] and df['End Station'].mode()[0]
    print('Frequent Start & End Station: ', frequent_travel_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: {} minutes'.format(total_travel_time))



    # display mean travel time
    print('Mean Travel Time: {} minutes'. format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('Number of Users: ',count_user_type)


    # Display counts of gender
    while True:
        try:
            print('Gender Count: ',df['Gender'].value_counts())
            break
        except KeyError:
            print('Gender: NaN')
            break

    # Display earliest, most recent, and most common year of birth
    if str('Birth Year') in df:
        print('Earliest Birth Year: ', df['Birth Year'].min())
        print('Recent Birth Year:t', df['Birth Year'].max())
        print('Most Common Birth Year: ', df['Birth Year'].mode()[0])


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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
