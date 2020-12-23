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
    while True:
        city = input("Which city would you like to filter by? new york city, chicago or washington?\n")
        city = city.lower()  # in case user entred capital letters

        if city not in ("new york city", "chicago", "washington"):
            print("Wrong entry please try again.")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            "Which month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n")
        month = month.lower()
        # print("This is the monthhhh ====   "+ month)
        if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print("Wrong entry please try again.")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input ("Are you looking for a particular day? If so, kindly enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference.\n")
        day = day.lower()  # convert to lower case
        if day not in ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"):
            print("wrong entry please try again.")
            continue
        else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Load data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))

    # Convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())
    print('\nWould you like to see the raw data? Enter yes or no.')


    # filter by month
    if month != 'all':
        # this return the int for months and we use +1 becasue python start index 0
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # create the new dataframe filter by month
        df = df.loc[df['month'] == month,:]

    # filter by day of week
    if day != 'all':
        # create the new dataframe day of week
        df = df.loc[df['day_of_week'] == day,:]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df["month"].max()
    print("Most Common Month:", common_month)

    # display the most common day of week

    common_day = df["day_of_week"].max()
    print("Most Common day:", common_day)
    # display the most common start hour
    df['hour'] = df["Start Time"].dt.hour
    common_hour = df['hour'].max
    print("Most Common Hour:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    most_common_use_startstation = df["Start Station"].value_counts().idxmax()
    print("Most Commonly use start station:", most_common_use_startstation)
    # display most commonly used end station
    most_common_use_endtstation  = df["End Station"].value_counts().idxmax()
    print("Most Commonly used end station:",  most_common_use_endtstation)

    # display most frequent combination of start station and end station trip

    combination = df.groupby(["Start Station", "End Station"]).count()
    print('Most Commonly used combination of start station and end station trip:', combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    tot_travel_time = df["Trip Duration"].sum()
    print("Total travel time:", (tot_travel_time.astype(int))/3600, "hrs")


    # display mean travel time
    tot_mean_time = df["Trip Duration"].mean()
    print("Total travel time:", (tot_mean_time, "Sec"))
    # to ensure user selected a city  has gender and birthday data


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nUser classifications.')
    start_time = time.time()
    print('\n\tType:\n')
    df_User_Type = df['User Type'].value_counts()

    print('\t' + df_User_Type.to_string().replace('\n', '\n\t'))

    try:

        df_Gender_Type = df['Gender'].value_counts()

        print('\n\tGender:\n')

        print('\t' + df_Gender_Type.to_string().replace('\n', '\n\t'))


    except Exception:
        pass

    try:

        current_year = dt.now().year
        age = current_year - df['Birth Year'].mode()[0]
        print('\n\tMost common age:', int(age))

        age = current_year - df['Birth Year'].min()
        print('\tOldest: ' + str(int(age)))

        age = current_year - df['Birth Year'].max()
        print('\tYoungest: ' + str(int(age)))

        age = current_year - df['Birth Year'].mean()
        print('\tAverage: ' + str(int(age)))

    except Exception:
        pass


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def individual_data(df):
    # Ask user if they want to see individual trip data.
    start_data = 0
    end_data = 5
    df_length = len(df.index)

    while start_data < df_length:
        raw_data = input("\nWould you like to see individual trip data? Enter 'yes' or 'no'.\n")
        if raw_data.lower() == 'yes':

            print("\nDisplaying only 5 rows of data.\n")
            if end_data > df_length:
                end_data = df_length
            print(df.iloc[start_data:end_data])
            start_data += 5
            end_data += 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        individual_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
