import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

user_input = input("Which cities information do you want? Enter: Chicago, Washington, New York: ")
try:
    if user_input.lower() == ('new york'):
        filename = ('new york city')
    else:
        filename = (user_input).lower()   
except KeyError:
    print("Sorry you did not enter a valid city")
                
df = pd.read_csv(CITY_DATA[filename])
    
df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
df['month'] = pd.to_datetime(df['Start Time']).dt.month_name()
df['day of week'] = pd.to_datetime(df['Start Time']).dt.day_name()


print(df.head())