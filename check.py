import pandas as pd
import numpy as np
chicago_data = pd.read_csv('chicago.csv')
NY_data = pd.read_csv('new_york_city.csv')
Washington_data = pd.read_csv('washington.csv')

#lets see this see only the first 5 rows:
print()
print('The first 5 rows include:\n', Washington_data.head())

print()
print('The first 5 rows include:\n', NY_data.head())

#lets see which columns have 'NaN' values in this file
print()
print('Washington NaN-valuesinclude:\n',Washington_data.isnull().any())

print()
print('NY NaN-valuesinclude:\n',NY_data.isnull().any())

print()
print('Chicago NaN-valuesinclude:\n',chicago_data.isnull().any())

#lets add the new columns in the washington data
#lets create the Gender, and Birth Year columns in washington 
