import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
mon_def = { # numeric reference to month.  
        1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December'
    }

hour_def = { # numeric reference to time of day.
      0: 'Midnight',
      1: '1:00 am',
      2: '2:00 am',
      3: '3:00 am',
      4: '4:00 am',
      5: '5:00 am',
      6: '6:00 am',
      7: '7:00 am',
      8: '8:00 am',
      9: '9:00 am',
      10: '10:00 am',
      11: '11:00 am',
      12: 'Noon',
      13: '1:00 pm',
      14: '2:00 pm',
      15: '3:00 pm',
      16: '4:00 pm',
      17: '5:00 pm',
      18: '6:00 pm',
      19: '7:00 pm',
      20: '8:00 pm',
      21: '9:00 pm',
      22: '10:00 pm',
      23: '11:00 pm'
    }
day_ref = {  #  numeric reference to days
        0:'Monday',
        1:'Tuesday',
        2:'Wednesday',
        3:'Thursday',
        4:'Friday',
        5:'Saturday',
        6:'Sunday'
    }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #1 TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # City Selection as follows
    city_choice = {
      1 : 'Chicago', 
      2 : 'New York City', 
      3 : 'Washington'
    }
    print()
    print('Please select a number for the following data you would')
    print('like to see US bikeshare data for:')
    print()
    print('1: Chicago')
    print('2: New York City')
    print('3: Washington')
    print()
    print('Please select your city:')
    user_choice = input()

    s=1 # variable to break while loop.
    while s==1:
      while user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice == 1:  # Chicago
          user_choice = city_choice[user_choice]
          city = user_choice.lower()
          s=2
          break
        elif user_choice == 2:  # New York City
          user_choice = city_choice[user_choice]
          city = user_choice.lower()
          s=2
          break
        elif user_choice == 3: # Washington
          user_choice = city_choice[user_choice]
          city = user_choice.lower()
          s=2
          break
        else:  # Lets user try again if a number other than 123 is selected.
          print('You selected:',user_choice)
          print('This is an invalid selection.')
          print('Select from below:')
          print()
          print('1: Chicago')
          print('2: New York City')
          print('3: Washington')
          print()
          print('Please select your city:')
          user_choice = input()
      else: # Lets user try again if a string is entered.
        print()
        print('Instead of ',user_choice,', try typing the number associated with your choice.')
        print()
        print('1: Chicago')
        print('2: New York City')
        print('3: Washington')
        print()
        print('Please select your city:')
        user_choice = input()

      print('Processing data for',user_choice, '.......')

    #2 TO DO: get user input for month (all, january, february, ... , june)

    #  Month Selection

    print()
    print('Please select the month for your data.')
    print("Choose 1-12 or type "'all'" for all months:")
    user_choice = input()  # user inputs month
    print()
    

    if user_choice.isdigit():  # process for user input, determines if digits or letters were input.
      user_choice = int(user_choice) #converts digit to integer.
      if user_choice >=1 and user_choice <=12: # range of valid input.
        month = user_choice         # month is defined.
        user_choice = mon_def [user_choice]  #converts integer into month using month_def line 8.

      else:  # returns 'all' if user select number that is not 1-12
        user_choice = 'All Months'
        month = 'all'
    else:  # assumes user has typed all.
        user_choice = 'All Months'
        month = 'all'
    print('You have selected:',user_choice) # confirms users input.

    #3 TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Day Selection.
   
    print()
    print('Please select the day for your data.') # Instructions to Gather user input
    print("Choose 1-7 with Monday starting at 1, or type "'all'" for all days:")
    user_choice = input()
    print()
    # Checks to see if user input digit.
    if user_choice.isdigit(): 
        # Converts date type to integer.
      user_choice = int(user_choice)  
       # returns day based on choice of 1-7
      if user_choice >=1 and user_choice <=7: 
        day = user_choice -1
        user_choice = day_ref[day]
      else:  #if number chosen is not 1-7, all days is assumed
        user_choice = 'All Days'
        day = 'all'
    else:  # Assumes the user typed all.
        user_choice = "All Days"
        day = 'all'
    print('You have selected:',user_choice) # Confirms user selection as day.
    print('Press enter to continue')
    input()

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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday

    # filter by month if applicable
    m = df['month']
    mm = month
    if month != 'all':
        if(m==mm).any()==True:  #If df contains the month user inputs.
            df = df[df['month'] == month]
        else:  #If month is not available, user is prompted to change the month or get data for all months.
            
            print ('Sorry, No trips were logged in '+ city + ' for the month of '+ mon_def [month]+'.')
            print()
            print('Would you like to try again? y/n   ')
            restart = input ()
            if restart.lower() == 'y':
                print()
                print('~'*40)
                if __name__ == "__main__":
                    main()  
            else:
                print()
                print('Ok, then we will show results for all months.')
                input('Press Enter to Continue....')
                month = 0
 
    
    # filter by day of week if applicable
    if day != 'all':
       
        df = df[df['day'] == day]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month

    
    # find the most popular month
    common_month = df['month'].mode()[0]
    

    print('Most Common Month:', mon_def[common_month])


    # TO DO: display the most common day of week

    # find the most popular month
    common_day = df['day'].mode()[0]

    print('Most Common Day:', day_ref[common_day])


    # TO DO: display the most common start hour
    
    # extract day from the Start Time column to create an day column
    df['hour'] = df['Start Time'].dt.hour
    
    # find the most popular hour
    common_hour = df['hour'].mode()[0]
    common_hour = int(common_hour)

    print('Most Popular Hour:', hour_def[common_hour])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
      # find the most popular month
    df['ss'] = df['Start Station']
    common_ss = df['ss'].mode()[0]

    print('Most Common Start Station:', common_ss)
    print()


    # TO DO: display most commonly used end station
    # find the most popular month
    df['es'] = df['End Station']
    common_es = df['es'].mode()[0]

    print('Most Common End Station:', common_es)
    print()


    # TO DO: display most frequent combination of start station and end station trip
    # find the most popular month
    df['cs'] = 'From: '+df['Start Station'] + ' To: ' +df['End Station']
    common_cs = df['cs'].mode()[0]

    print('Most Common Commute:')
    print(common_cs)
    print()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['tt'] = df['Trip Duration']
    total_tt = df['tt'].sum()
    # total time to integer
    total_tt = int(total_tt)
    # Convert total time to minutes using floor div
    minutes_tt = total_tt // 60
    # Remainder remains seconds using modulo.
    seconds_tt = total_tt % 60
    # seconds to string
    seconds_tt = str(seconds_tt)
    # Converts minutes to hours using floor div.
    hours_tt = minutes_tt // 60
    # converts hours to days using floor div.
    days_tt = hours_tt // 24
    # remaining hours placed using modulo.
    hours_tt = hours_tt % 24
    # days to string
    days_tt = str(days_tt)
    # hours to string
    hours_tt = str(hours_tt)
    # Remaining minutes placed using modulo.
    minutes_tt = minutes_tt % 60
    # minutes to string.
    minutes_tt = str(minutes_tt)
    # User friendly output
    total_tt = (days_tt + ' days, ' + hours_tt + ' hours, ' + minutes_tt + ' minutes, ' + seconds_tt + ' seconds.')

    print('The total travel time for this period is:')
    print()
    print(total_tt)
    print()



    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    df['cut'] = df['User Type']
    cut = df['cut'].value_counts()
    print('The Count of User Types...')
    print()
    print(cut)
    print()
    print()
    

    
    # TO DO: Display counts of gender
  
    
    if 'Gender' in list(df):
        df['cog'] = df['Gender']
        cog = df['cog'].value_counts()
        print('The Counts of Gender...')
        print()
        print(cog)
    else:
        print()
        print()
        print('The Counts of Gender are not available for this City.......')
        print()
      
    # TO DO: Display earliest, most recent, and most common year of birth
   
    # get current year as variable now.
    now = pd.Timestamp(1)
    now = now.today()
    now = now.year
    if 'Birth Year' in list(df):
        
        
        df['yob'] = df['Birth Year']
        # Finds earliest year
        earliest = df['yob'].min() 
        earliest = int(earliest)
        #  Finds most recent year.
        most_recent = df['yob'].max()  
        most_recent = int(most_recent)
        # Finds the most common year.
        most_common_year = df['yob'].mode()[0]  
        most_common_year = int(most_common_year)
        
        print()
        print()
        print('User\'s approximate age:')
        print()
        print('Oldest: ',now - earliest)
        print ()
        print('Youngest: ', now - most_recent)
        print ()
        print('Most Common: ', now - most_common_year)
        print()
        print('* User age is approximate because user submits his/her year of birth.  The user does not submit their actual birthday.')
    # Column for data used is not be included in the washington.csv file    
    else:
        print()
        print()
        print('The user\'s age is not available for this city..........')
        print()
        print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def raw_data(df):
    """ Display Raw Data 5 rows at a time """
    
    
    print()
    print('Would you like to look at the raw data for your city?')
    print('y/n')
    yes_no = input()
    five_at_a_time = df
    # Remove all columns not originally in the data.  Washington.csv will not generate a cog or yob column, if statment to 
    # get rid of error when tryint to delete a column that does not exsist.
    del five_at_a_time['ss']
    if 'cog' in list(five_at_a_time):
        del five_at_a_time['cog']
    del five_at_a_time['cut']
    del five_at_a_time['tt']
    del five_at_a_time['cs']
    if 'yob' in list(five_at_a_time):
        del five_at_a_time['yob']
    del five_at_a_time['es']
    del five_at_a_time['month']
    del five_at_a_time['day']
    del five_at_a_time['hour']
    
    while yes_no.lower() == 'y':
        # outputs five lines
        print(five_at_a_time.head()) 
        # removes five lines from the top of df, then loops if the user chooses y.
        five_at_a_time = five_at_a_time.tail(-5) 
        
        print('Continue?  y/n:')
        yes_no= input()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('Would you like to restart?   y/n :  ')
        
        if restart.lower() != 'y':
            break



if __name__ == "__main__":
	main()
    