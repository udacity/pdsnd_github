import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
filename = 'chicago.csv','new_york_city.csv','washington.csv'
print('Hello! Let/s explore some US bikeshare data!\n')
while True:
    try:
        city = input ('What City would you like to analyze Bikeshare data for? Enter city\n')
        city = city.lower()
        if city in CITY_DATA[city]:
            print ("\n{} if true,if not restart now \n".format(city))
            break
    except (ValueError,KeyError):
        print("Please pick city on list")



month = ('january','february','march','april','may','june')
list2 = ('january','february','march','april','may','june')
answer_month = input('What month would you like to analyze Bikeshare data for? Enter month\n')
while answer_month.lower() not in list2:
          if answer_month.lower() == 'january':
           month = ['january']
          elif answer_month.lower() == 'february':
           month = ['february']
          elif answer_month.lower() == 'march':
           month = ['march']
          elif answer_month.lower() == 'april':
           month = ['april']
          elif answer_month.lower() == 'may':
           month = ['may']
          elif answer_month.lower() == 'june':
           month = ['june']
          elif answer_month.lower() == 'july':
           month = ['july']
          else: input('\nYou have entered an invalid response. Would you like to restart? Enter yes or no.\n')
          break

days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
list3 = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
answer_day = input('What day of the week would you like to analyze Bikeshare data for? Enter day\n')
while answer_day.lower() not in list3:
          if answer_day.lower() == 'monday':
           day = ['monday']
          elif answer_day.lower() == 'tuesday':
           day = ['tuesday']
          elif answer_day.lower() == 'wednesday':
           month = ['wednesday']
          elif answer_day.lower() == 'thursday':
           day = ['thursday']
          elif answer_day.lower() == 'friday':
           day = ['friday']
          elif answer_day.lower() == 'Saturday':
           day = ['saturday']
          elif answer_day.lower() == 'sunday':
           day = ['sunday']
          else: input('\nYou have entered an invalid response. Would you like to restart? Enter yes or no.\n')
          break

usertype = ('customer','subscriber')
list4 = ('customer', 'subscriber')
answer_usertype = input('What user type would you like to analyze Bikeshare data for? Enter user type\n')
while answer_usertype.lower() not in list4:
           if answer_usertype.lower() == 'customer':
            usertype = ['customer']
           elif answer_usertype.lower() == 'subscriber':
            usertype = ['subscriber']
           else: input('\nYou have entered an invalid response. Would you like to restart? Enter yes or no.\n')
# load data file into a dataframe
if answer_city == 'chicago':

 df = pd.read_csv('chicago.csv')

elif answer_city == 'new york city':

 df = pd.read_csv('new_york_city.csv')

elif answer_city == 'washington':

 df = pd.read_csv('washington.csv')


df['Start Time'] = pd.to_datetime(df['Start Time'])
# extract hour from the Start Time
df['hour'] = df['Start Time'].dt.hour
# most popular hour
popular_hour = df['hour'].mode()[0]
print('You have chosen to view the following Bikesahre data, you wanted to see', answer_usertype, 'data in', answer_city, 'for the month of', answer_month, 'specifically for', answer_day)
print()
print('For', answer_city, 'Most Popular Start Hour:', popular_hour)

print('the following is all six months of data for the city you selected above. we will show total users and trips by point of origin, in descending order.\n')
 # print counts for each user type
user_types = df['User Type'].value_counts()

print(user_types)
start = df['Start Station'].value_counts()
print()
print('Below are the Bikeshare stations in', answer_city, 'trips totaling\n')
print(start)
