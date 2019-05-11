import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import itertools

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}
while True:
    while True:
        city = input("Which cities information do you want [Chicago, Washington, New York City]: ")
        if city.lower() == ("new york"):
            city = "new york city"
        if city.lower() in CITY_DATA:
            break
        else:
            print("invalid input, please enter a valid city")
        
# TO DO: get user input for month (all, january, february, ... , june)
#months = ['all', 'january', 'february', 'march', 'april', 'may' , 'june']
    months = ['all', 'january', 'february', 'march', 'april', 'may' , 'june']
    while True:
        month = input("Which month do you want data from [all , or any from January to June]: ")

        if month.lower() in months:
            break
        else:
            print("invalid input, please enter a valid month")
 # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_of_week = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Which day of the week do you want data from [all, or any day monday through sunday]: ")
    
        if day.lower() in days_of_week:
            break
        else:
            print("invalid input, please enter a valid day")
        
    user_input = input("Is city: {}, month: {}, day: {} correct? Enter yes or no: ".format(city, month, day))       
    if user_input.lower() == 'yes':
        break
    else:
        print("please enter city, month, day again")
        
chi_df = pd.read_csv('chicago.csv')
wash_df = pd.read_csv('washington.csv')
ny_df = pd.read_csv('new_york_city.csv') 
multi_df = pd.concat([chi_df, wash_df, ny_df],
                keys = ['chicago', 'new york city', 'washington'],
                names = ['Cities', 'Row ID'], sort = False)

multi_df['Start Time'] = pd.to_datetime(multi_df['Start Time'])

#extract month and day of week from Start Time to create new columns
multi_df['months'] = pd.to_datetime(multi_df['Start Time']).dt.month_name()

multi_df['days'] = pd.to_datetime(multi_df['Start Time']).dt.day_name()

if month.lower() != 'all':
    multi_df_month = multi_df[multi_df['months'].str.contains(month.title())] 
    multi_df = multi_df_month.copy()
    
if day.lower() != 'all':
    multi_df_day = multi_df[multi_df['days'].str.contains(day.title())]
    multi_df = multi_df_day.copy()

df = multi_df.loc[city]
print(df.head())
print(df.columns)
  # TO DO: display the most common month
common_month = df['months'].mode()
print(common_month)

month_count = pd.DataFrame(df.groupby(['months']).count())
plt.figure();
month_count.plot.hist()

    # TO DO: display the most common day of week
common_day = df['days'].mode()
print(common_day)


    # TO DO: display the most common start hour
    
common_hour = pd.to_datetime(df['Start Time']).dt.time.mode()   
print(common_hour)
 # TO DO: display most commonly used start station
common_start_station = df['Start Station'].mode()
print("The most common starting point is {}".format(common_start_station))


#compare = input("Would you like to compare {} to another city? [yes or no]".format(city))

