# Bike share data analysis
# Calculate the statistics of bike share data, such as most important hours and stations
# Author: Lu Chen

import pandas as pd

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:  # continue loop until the condition is met and breaks the loop
        city=input('which city would you like to explore? chicago, or new york, or washington\n')
        if city.upper() not in ('CHICAGO','NEW YORK','WASHINGTON'):
            print('please specify a city in: chicago, new york, or washington')
        else:
            break


    # get user input for month (all, january, february, ... , june)
    while True:
        month=input('which month would you like to explore?\n')
        if month.lower() not in ('all','january','febrary','march','april','may','june'):
            print('not a valid month')
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('which day of week would you like to explore?\n')
        if day.lower() not in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
            print('not a valid day of week', day.lower(), day)
            continue
        else:
            break


    print('-'*40)
    return(city, month, day)

[city, month, day] = get_filters()

# ------------------------------------load specified data------------
CITY_DATA={'chicago','chicago.csv',
'new york city','new_york_city.csv',
'washington','washington.csv'}

def load_data(city,month,day):
    #load data into a DataFrame
    df=pd.read_csv(CITY_DATA[city])

    #convert start time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])

    # extract month and day from the start time column to create a new column
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month !='all':
        months=['january','february','march','april','may','june']
        month=months.index(month)+1

        #fidaylter by month:
        df=df[df['month']==month]

    if day !='all':
        df=df[df['day_of_week']==day.title()]

    return df

df=load_data(city,month,day)
print(df.head())

# ---------------------------get the most popular time, station,--------------------------------
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['hour']=df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('most popular_hour is: ',popular_hour)

    # display the most common day of week

    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

time_stats(df)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]

    # display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]


    # display most frequent combination of start station and end station trip

    print('the most popular start station is: ',popular_start_station)
    print('the most popular end station is: ',popular_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

station_stats(df)
