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
    print('Hello! Let\'s explore some US bikeshare Data!')

    check_month = map(str, range(6))
    check_day = map(str, range(31))
    check_city = ['chicago','washington','new york city','none']
    while True :

        city = input('please choose a city (chicago, new york city, washington). make sure that you enter a string : ').lower()

        month = input('please choose month to filter by (jan=1, feb=2, mar=3,apr=4,may=5,jun=6) or None : ').lower()

        day = input('please choose day as integer or None : ').lower()

        if (month not in check_month and month != 'none') or (day not in check_day and day != 'none') or (city not in check_city) :
            print("--Oops!you have entered wrong value ,please try again --")
        else:
            break

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

    the_full_df = pd.read_csv('./{}'.format(CITY_DATA[city]))
    Time = pd.to_datetime(the_full_df['Start Time'])

    if day =="none" and month == "none" :
        df = the_full_df
    elif month == "none" :
         df = the_full_df[Time.dt.day == int(day)]
    elif day == "none" :
        df = the_full_df[Time.dt.month == int(month)]
    else :
        df = the_full_df[Time.dt.month == int(month)][Time.dt.day == int(day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    import time
    start_time = time.time()

    # display the most common month
    Time = pd.to_datetime(df['Start Time'])
    the_common_month = Time.dt.month.mode()[0]

    # display the most common day of week
    the_common_day = Time.dt.day.mode()[0]

    # display the most common start hour
    the_common_hour = Time.dt.hour.mode()[0]
    print('the most common month : {}'.format(the_common_month))
    print('the most common day : {}'.format(the_common_day))
    print('the most common hour : {}'.format(the_common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_startst = df['Start Station'].mode()[0]

    # display most commonly used end station
    most_common_endst = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    print("\n the most common start station : {}".format(most_common_startst))
    print("\n the most common end station : {}".format(most_common_endst))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tot_duration = df['Trip Duration'].sum()

    # display mean travel time
    avg_duration = df['Trip Duration'].mean()
    print("total travel duration : {}".format(tot_duration))
    print("the mean of travel duration : {}".format(avg_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if "Gender" in df:
        # Display counts of user types
        type_count = df.groupby(['User Type'])['Start Time'].count()

        # Display counts of gender
        gender_count = df.groupby(['Gender'])['Start Time'].count()

        # Display earliest, most recent, and most common year of birth
        earlist_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print("the count of eatch gender : \n {} \n ".format(type_count,gender_count))
        print("the earlist year of birth : {} \n ".format(int(earlist_birth)))
        print("the most recent year of birth : {} \n ".format(int(recent_birth)))
        print("the most common year of birth : {} \n ".format(int(common_birth)))

    else:
        type_count = df.groupby(['User Type'])['Start Time'].count()
        print("the count of eatch user type \n {}".format(type_count))
        print("this data don't have (Gender or date of birth")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """displays individual user data"""
    counter2 = 5
    while True:
        answer2 = input('if you want to see individual data choose (yes) to show 5 users or (no) to skip : ').lower()
        if answer2 == 'yes':
            i = 0
            while (i < 5):
                raw_data = df.head(counter2)
                the_user = raw_data.tail(5).iloc[i]
                print(the_user)
                print("\n\n")
                i+=1
            counter2+=5
        elif answer2 == 'no':
            break
        else:
            print("please enter (yes) or (no) ,try again")
            continue

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        counter = 0
        info_list = ['station_stats(df)', 'duration_stats(df)', 'user_stats(df)']
        info_name = ["Stations ","Trip Duration","users"]
        while counter <= 2:
            answer=input("would you like to show information about {} ?('yes' or 'skip') : ".format(info_name[counter])).lower()
            if answer == "yes" :
                exec(info_list[counter])
                counter+=1
            elif answer == "skip" :
                counter+=1
                continue
            else :
                print('please enter (yes to show data) or (skip to continue)')
                continue

        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()