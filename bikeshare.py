import time
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

# Given that these are static calendar type values - defining them here
valid_city = [ 'chicago' , 'new york city' , 'washington' ]
valid_month = [ 'ALL' , 'january' , 'february' , 'march' , 'april' , 'may' ,
                'june' , 'july' , 'august' , 'september' , 'october' , 'november' , 'december' ]
valid_day = [ 'ALL' , 1 , 2 , 3 , 4 , 5 , 6 , 7 ]
cnum = [ 1 , 2 , 3 ]
dnum = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 ]
mnum = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 ]

city_df = pd.DataFrame ( [ ] )


def display_cht( df2 , cht_col , cht_title , cht_y ):
    fig , ax = plt.subplots ()
    data = df2[ cht_col ].value_counts ()
    points = data.index
    frequency = data.values
    ax.bar ( points , frequency )
    ax.set_title ( cht_title )
    ax.set_ylabel ( cht_y )
    df2[ cht_col ].value_counts ().sort_index ().plot.barh ( x='Values' , y=cht_y )
    plt.show


def output2( df2 , colid , pr_msg , pr_msg2 ):
    df2[ colid ] = df2.index
    print ( pr_msg2.format ( df2[ colid ].iloc[ 0 ] ) )
    msg2 = 'The 10 Most ' + pr_msg
    df2[ 'Amt' ].plot.barh ( x='Values' , y='Amt' , title=msg2 )
    plt.show ()


def get_selection( gnum , gval ):
    while True:
        print ( gval )
        print ( gnum )
        try:
            x = int ( input ( 'Enter a corresponding number for the options shown: ' ) )
            if x in (gnum):
                print ( 'Good Pick' )
                break
            else:
                print ( "Not a Valid number from the selection" )
        except ValueError:
            print ( 'That\'s not a valid number' )
        except KeyboardInterrupt:
            print ( '\nNo input taken' )
            break
        finally:
            print ( '\nAttempted Input\n' )
    return (x)


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print ( 'Hello! Let\'s explore some US bikeshare data!' )
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = valid_city[ get_selection ( cnum , valid_city ) - 1 ]
    city_df = pd.read_csv ( CITY_DATA[ city ] )
    city_df[ 'Start Time' ] = pd.to_datetime ( city_df[ 'Start Time' ] )
    city_df[ 'month' ] = city_df[ 'Start Time' ].dt.month
    city_df[ 'day_of_week' ] = city_df[ 'Start Time' ].dt.weekday_name
    mnumsht = np.unique ( city_df[ 'month' ] )
    mnum = [ 0 ]
    vm = [ 'ALL' ]
    for x in mnumsht:
        mnum = np.append ( mnum , int ( x ) )
        vm = np.append ( vm , datetime.date ( 1900 , int ( x ) , 1 ).strftime ( '%B' ) )
    valid_month = vm

    # TO DO: get user input for month (all, january, february, ... , june)
    month = valid_month[ get_selection ( mnum , valid_month ) ]
    print ( month )
    print ( valid_month )
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_selection ( dnum , valid_day )
    print ( city , month , day )
    print ( '-' * 40 )
    return city , month , day , city_df


def load_city( city ):
    city_df = pd.read_csv ( CITY_DATA[ city ] )
    city_df[ 'Start Time' ] = pd.to_datetime ( city_df[ 'Start Time' ] )
    city_df[ 'month' ] = city_df[ 'Start Time' ].dt.month
    return city_df


def all_mth( city_df ):
    # filter by month if applicable
    if month == 'all':
        # use the index of the months list to get the corresponding int
        months = valid_month
        month = months.index ( month ) + 1

        # filter by month to create the new dataframe
        city_df = df[ df[ 'month' ] == month ]
    return city_df


def all_day( city_df ):
    # filter by day of week if applicable
    if day == 'all':
        # filter by day of week to create the new dataframe
        city_df = city_df[ city_df[ 'day_of_week' ] == day.title () ]

    return city_df


def time_stats( city_df ):
    """Displays statistics on the most frequent times of travel."""
    print ( city_df.head () )
    print ( '\nCalculating The Most Frequent Times of Travel...\n' )
    start_time = time.time ()
    #    city_df['Start Time'] = pd.to_datetime(city_df['Start Time'])
    city_df[ 'End Time' ] = pd.to_datetime ( city_df[ 'End Time' ] )

    # TO DO: display the most common month
    city_df[ 'Month' ] = city_df[ 'Start Time' ].dt.month

    popular_mth = city_df[ 'Month' ].mode ()[ 0 ]
    print ( 'The Most Popular Month is: ' , popular_mth )
    display_cht ( city_df , 'Month' , 'Most Popular Month' , 'Usage' )

    # TO DO: display the most common day of week
    city_df[ 'DOW' ] = city_df[ 'Start Time' ].dt.dayofweek

    popular_wkdy = city_df[ 'DOW' ].mode ()[ 0 ]
    print ( 'The Most Popular Day Of Week is: ' , popular_wkdy )
    display_cht ( city_df , 'DOW' , 'Most Popular Day of Week' , 'Usage' )

    # TO DO: display the most common start hour
    city_df[ 'hour' ] = city_df[ 'Start Time' ].dt.hour

    # find the most popular hour
    popular_hour = city_df[ 'hour' ].mode ()[ 0 ]
    print ( 'The Most Popular Hour is: ' , popular_hour )
    display_cht ( city_df , 'hour' , 'Most Popular Hours' , 'Usage' )

    print ( "\nThis took %s seconds." % (time.time () - start_time) )
    print ( '-' * 40 )
    five_lines(city_df)

def station_stats( city_df ):
    """Displays statistics on the most popular stations and trip."""

    print ( '\nCalculating The Most Popular Stations and Trip...\n' )
    start_time = time.time ()

    # TO DO: display most commonly used start station
    colid , pr_msg , pr_msg2 = 'Start Station Name' , 'Popular Start Stations' , 'The Most Popular Start Station is: {}'
    df2 = city_df[ 'Start Station' ].value_counts ().to_frame ( 'Amt' )[ :10 ]
    output2 ( df2 , colid , pr_msg , pr_msg2 )

    # TO DO: display most commonly used end station
    colid , pr_msg , pr_msg2 = 'End Station Name' , 'Popular End Stations' , 'The Most Popular End Station is: {}'
    df2 = city_df[ 'End Station' ].value_counts ().to_frame ( 'Amt' )[ :10 ]
    output2 ( df2 , colid , pr_msg , pr_msg2 )

    # TO DO: display most frequent combination of start station and end station trip
    colid , pr_msg , pr_msg2 = 'Start Station Name' , 'Popular Start Stations' , 'The Most Popular Start Station is: {}'
    df2 = city_df[ 'Start Station' ].value_counts ().to_frame ( 'Amt' )[ :10 ]
    output2 ( df2 , colid , pr_msg , pr_msg2 )

    print ( "\nThis took %s seconds." % (time.time () - start_time) )
    print ( '-' * 40 )
    five_lines(city_df)

def trip_duration_stats( city_df ):
    """Displays statistics on the total and average trip duration."""

    print ( '\nCalculating Trip Duration...\n' )
    start_time = time.time ()

    # TO DO: display total travel time
    city_df[ 'travel_hours' ] = city_df[ 'End Time' ] - city_df[ 'Start Time' ]
    print ( city_df[ 'travel_hours' ].sum () )

    # TO DO: display mean travel time
    print ( city_df.loc[ : , 'travel_hours' ].mean () )

    print ( "\nThis took %s seconds." % (time.time () - start_time) )
    print ( '-' * 40 )
    five_lines(city_df)

def user_stats( city_df ):
    """Displays statistics on bikeshare users."""

    print ( '\nCalculating User Stats...\n' )
    start_time = time.time ()

    # TO DO: Display counts of user types
    # load data file into a dataframe
    # city_df = pd.read_csv(filename)

    # print value counts for each user type
    colid , pr_msg , pr_msg2 = 'User Types' , 'User Types' , 'The Most Popular User Types are: {}'
    city_df2 = city_df[ 'User Type' ].value_counts ().to_frame ( 'Amt' )[ :10 ]
    output2 ( city_df2 , colid , pr_msg , pr_msg2 )

    if 'Gender' in city_df.head ( 0 ):
        # TO DO: Display counts of gender
        colid , pr_msg , pr_msg2 = 'Gender' , 'User Types' , 'The Most Popular Genders are: {}'
        city_df3 = city_df[ 'Gender' ].value_counts ().to_frame ( 'Amt' )[ :10 ]
        output2 ( city_df3 , colid , pr_msg , pr_msg2 )

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in city_df.head ( 0 ):
        # TO DO: Display counts of gender
        colid , pr_msg , pr_msg2 = 'Birth Year' , 'User Types' , 'The Most Seen Birth Years are: {}'
        city_df4 = city_df[ 'Birth Year' ].dropna ().astype ( int )
        city_df4 = city_df4.value_counts ().to_frame ( 'Amt' )
        yrs = city_df4.index.tolist ()
        #       print(yrs)
        city_df5 = city_df4[ :5 ]
        print ( city_df4.columns )
        mxyr , minyr = max ( yrs ) , min ( yrs )
        print ( 'The Lowest Birth Year was :' , minyr , 'The highest Birth Year was' , mxyr )

    #        output2(city_df5, colid, pr_msg, pr_msg2)

    print ( "\nThis took %s seconds." % (time.time () - start_time) )
    print ( '-' * 40 )
    five_lines(city_df)

def five_lines(city_df):
    a = 0
    b = 5
    goodinput = [ 'Y' , 'y' , 'N' , 'n' ]
    while True:
        if b> len(city_df):
            a=0
            b=5
        try:
            print ( "Valid input Y, N or y, n" )
            x = ( input ( 'Do you want to see 5 lines of data?: ' ))
            if x in goodinput:
                print ( 'OK' )
                if x in ['N','n']:break
                print(city_df[a:b])
                a=b
                b=b+5
            else:
                print ( "Not a Valid entry from the selection" )
        except ValueError:
            print ( 'That\'s not a valid entry' )
        except KeyboardInterrupt:
            print ( '\nNo input taken' )
            break
        finally:
            print ( '\nAttempted Input\n' )
    return (x)


def main():
    while True:
        city , month , day , city_df = get_filters ()
        if month == 'ALL':
            all_mth ( city_df )
        if day == 'All':
            all_day ( city_df )
        time_stats ( city_df )
        station_stats ( city_df )
        trip_duration_stats ( city_df )
        user_stats ( city_df )

        restart = input ( '\nWould you like to restart? Enter yes or no.\n' )
        if restart.lower () != 'yes':
            break


if __name__ == "__main__":
    main ()
