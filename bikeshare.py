import time
import pandas as pd
import numpy as np
from bullet import Bullet
from bullet import colors

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Code to get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
def get_city():
    """
    Asks user to specify a city using colorful keyboard input selection 

    Returns:
        (str) city - name of the city to analyze
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print()

    cli = Bullet(
            prompt = "\nPlease choose a City Please ?: ",
            choices = ["chicago", "new york city", "washington"], 
            indent = 0,
            align = 5, 
            margin = 2,
            bullet = "★",
            bullet_color=colors.bright(colors.foreground["cyan"]),
            word_color=colors.bright(colors.foreground["yellow"]),
            word_on_switch=colors.bright(colors.foreground["yellow"]),
            background_color=colors.background["black"],
            background_on_switch=colors.background["black"],
            pad_right = 5
        )

    city = cli.launch()
    print()
    print("Looks like you would like to know more about: \n", city.title())
    print('-'*50)
    return city

#Code to get user input for month (all, january, february, ... , june)
def get_month():
    """
    Asks user to specify a month using colorful keyboard input selections and a star 

    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
    """

    cli = Bullet(
            prompt = "\n Choose a month of interest Please ?: ",
            choices = ['all', 'january', 'february', 'march', 'april', 'may', 'june'], 
            indent = 0,
            align = 5, 
            margin = 2,
            bullet = "★",
            bullet_color=colors.bright(colors.foreground["cyan"]),
            word_color=colors.bright(colors.foreground["yellow"]),
            word_on_switch=colors.bright(colors.foreground["yellow"]),
            background_color=colors.background["black"],
            background_on_switch=colors.background["black"],
            pad_right = 5
        )

    month = cli.launch()
    print()
    print("Looks like you would like to get information for the month of: \n", month.title())
    print('-'*50)
    return month

#Code to get user input for day of week (all, monday, tuesday, ... sunday)
def get_day():
    """
    Asks user to specify a day using colorful keyboard input selections and a star 

    Returns:
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    cli = Bullet(
            prompt = "\n Choose a day of interest Please ?: ",
            choices = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], 
            indent = 0,
            align = 5, 
            margin = 2,
            bullet = "★",
            bullet_color=colors.bright(colors.foreground["cyan"]),
            word_color=colors.bright(colors.foreground["yellow"]),
            word_on_switch=colors.bright(colors.foreground["yellow"]),
            background_color=colors.background["black"],
            background_on_switch=colors.background["black"],
            pad_right = 5
        )

    day = cli.launch()
    print()
    print("Looks like you would like to get information for : \n", day.title())
    print('-'*60)
    return day


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
# I will load data file into a dataframe
    
    df = pd.read_csv(CITY_DATA[city])

    #lets remove all 'NaN' values in all columns in this data.
    df = df.fillna(method = 'backfill', axis = 0)

    # I will convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # I will extract month and day of week from Start Time to create new columns
    df['month'] = df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['day_of_week'] = df['Start Time'].dt.weekday_name


    # I am now going to filter by month if applicable
    if month != 'all':
        #I am now going to use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        #I am now going to filter by month to create the new dataframe
        df = df[df['month'] == month]


    # I am now going to filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print()

    # I will need to first extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour


    #Code to display the most common month
    common_month = df['month'].mode()[0]
    
    print('Most trips happen in the {}st/th month'.format(common_month))
    print()

    #Code to display the most common day of week
    common_DOW = df['day_of_week'].mode()[0]
    
    print('Most trips happen on {} in the week'.format(common_DOW))
    print()

    #Code to display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    
    print('Most trips happen at - {}:00 Hours:'.format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Code to display most commonly used start station
    c_s_stn = df['Start Station'].mode()[0]
    
    print('It appears that {} is the most commonly used start station'.format(c_s_stn))
    print()

    #Code to display most commonly used end station
    c_e_stn = df['End Station'].mode()[0]
    
    print('Looks like {} is the most commonly used end station.'.format(c_e_stn))
    print()

    #Code to display most frequent combination of start station and end station trip
    freq_comb = c_e_stn + ''+ c_s_stn

    print('Wow the most frequent combination of start station and end station trip is:', print(freq_comb))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # Since we are dealing with decimals values we shall set the precision to 3 decimal places
    pd.set_option('precision', 3)
    

    #Code to display total travel time 
    sum_ttt = df['Trip Duration'].sum()
    
    print('The total travel time is {} Hours, or {} Minutes, or {} seconds'.format(sum_ttt/3600,sum_ttt/60,sum_ttt))
    print()

    #Code to display mean travel time
    mean_ttt = df['Trip Duration'].mean()
    
    print('The Average travel time is {} Hours, or {} Minutes, or {} seconds'.format(mean_ttt/3600,mean_ttt/60,mean_ttt))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def user_stats(df,city):
    """Displays statistics on the gender and user types including count, number of
    entries, and prompts the user to input 'yes' if they need to see more data and 
    ends the program incase they are not interested any more."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    #Code to display counts of user types
    user_types = df['User Type'].value_counts()

    print('The total number of user types include: \n', user_types)
    print()
    
    #Code to display number of entries for user types

    print('There are {} of number of entries for user types'.format(len(df['User Type'])))
    print()

    #User stats for Gender and Birth Year are only available for New York and Chicago (used 'check.py' to find this) so
    #I will create an If statement to handle this
    capitals_c = ('chicago','new york city')

    if (city in capitals_c):
        #Code to display counts of Gender
        user_gender = df['Gender'].value_counts()
        
        print('The total values by user gender include: \n', user_gender)
        print()
        
        #Code to display number of entries for Gender
        print('There are {} of number of entries for Gender'.format(len(df['Gender'])))
        print()

        #Code to display earliest, most recent, and most common year of birth
        c_BY = df['Birth Year'].mode()[0]

        print('{} is the most common year of birth.'.format(int(c_BY)))
        print()

        recent_BY = df['Birth Year'].min()
        print('{} seems to be the earliest year of birth.'.format(int(recent_BY)))
        print()

        max_BY = df['Birth Year'].max()
        print('{} seems to be the most recent year of birth.'.format(int(max_BY)))
        print()

        #Code to display number of entries for year of birth
        print('There are {} of number of entries for year of birth'.format(len(df['Birth Year'])))
        print()
    else:
        print("\nGender and Birth Year data are not available for the selected city")
    print("\nThis took %s seconds." % (time.time() - start_time))  
    print('-'*60)

def more_stats(df,city):
    """Displays statistics on trips including the gender and user types including count, number of
    entries, and prompts the user to input 'yes' if they need to see more data and 
    ends the program incase they are not interested any more."""
     
    print('\nGathering additional raw data for trip User Stats...\n')
    start_time = time.time()
     
    count = 1
    index = 0
    nrows = 5
    while True:

        user_input = input('\n Would you like to see raw data on cities...dont worry only 5 lines will display at a time? Enter yes or no.\n')
        
        while user_input.lower() not in ("yes","no"):
            print('You have entered an invalid input..')
            user_input = input('\n To see data please...Enter Yes/No.\n')
            break

        if user_input == 'yes':
            
            #Code to display raw data without NaN values, set na_filter as 'False'
            df = pd.read_csv(CITY_DATA[city],na_filter=False)
            print(df.iloc[index*nrows:nrows*count])
            print("\nThis took %s seconds." % (time.time() - start_time))
           #If user wants to see additional 5 lines of raw data 
            count+=1
            index+=1
            

        elif user_input == 'no':
            print('-THE END-'*7)
            break
          
def main():
    while True:
        city = get_city()
        month = get_month()
        day = get_day()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        more_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() not in ("yes","no"):
            print('You have entered an invalid input..')
            restart = input('\n For program to restart please...Enter Yes/No.\n')
        elif restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()



