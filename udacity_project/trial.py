import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv',
              'all' : 'all'}
while True:
    city = input("Which cities information do you want [All, Chicago, Washington, New York City]: ")
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

if city.lower() == 'all':
    chi_df = pd.read_csv('chicago.csv')
    wash_df = pd.read_csv('washington.csv')
    ny_df = pd.read_csv('new_york_city.csv') 
    df = pd.concat([chi_df, wash_df, ny_df], keys = ['chicago', 'new york city', 'washington'], sort = False)
else:          
    df = pd.read_csv(CITY_DATA[city.lower()])
    
df['Start Time'] = pd.to_datetime(df['Start Time'])

#extract month and day of week from Start Time to create new columns
df['months'] = pd.to_datetime(df['Start Time']).dt.month_name()

df['days'] = pd.to_datetime(df['Start Time']).dt.day_name()

if month.lower() != 'all':
    df_month = df[df['months'].str.contains(month.title())] 
    df = df_month.copy()
if day.lower() != 'all':
    df_day = df[df['days'].str.contains(day.title())]
    df = df_day.copy()
 
print(df.head())
print(df.columns)
#df.groupby(['Trip Duration', 'Gender']).size().nlargest().plot()
#plt.show()
    # TO DO: display the most common month
common_month = df['months'].mode()


    # TO DO: display the most common day of week
common_day = df['days'].mode()

    # TO DO: display the most common start hour
    
common_hour = pd.to_datetime(df['Start Time']).dt.time.mode()   

 # TO DO: display most commonly used start station
common_start_station = df['Start Station'].mode()
print("The most common starting point is {}".format(common_start_station))

    # TO DO: display most commonly used end station
common_end_station = df['End Station'].mode()
print("The most common stopping point is {}".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
common_start_stop = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
print("The most common starting and stopping stations are \n {}".format(common_start_stop))

df.groupby(['Start Station', 'End Station']).size().nlargest().plot()
plt.show()
 # TO DO: display total travel time
total_travel = df['Trip Duration'].sum()
print("Total travel time {} seconds".format(total_travel))

    # TO DO: display mean travel time
travel_mean = df['Trip Duration'].mean()
print("The average travel time is {} minutes".format(travel_mean/60))

 # TO DO: Display counts of user types
user_type_count = df['User Type'].value_counts()
print("Count of user types: \n{}".format(user_type_count))
    # TO DO: Display counts of gender
gender = np.array(df['Gender'])  
print(gender)
gender_counts = df['Gender'].fillna(method = 'ffill').value_counts()
print("Gender counts \n{}".format(gender_counts))

    # TO DO: Display earliest, most recent, and most common year of birth
birth_year_earliest = df['Birth Year'].min()
print("The earliest birth year is {}".format(birth_year_earliest))

birth_year_recent = df['Birth Year'].max()
print("The most recent birth year is {}".format(birth_year_recent))

birth_year_common = df.groupby(['Birth Year']).size().nlargest(1)
print("The most common year {}".format(birth_year_common))
