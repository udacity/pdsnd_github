import pandas as pd
import matplotlib.pyplot as plt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

user = input("which city:")
if user.lower() == 'all':
    chi_df = pd.read_csv('chicago.csv')
    wash_df = pd.read_csv('washington.csv')
    ny_df = pd.read_csv('new_york_city.csv') 
    multi_df = pd.concat([chi_df, wash_df, ny_df], sort = False)
    
df = pd.MultiIndex.from_frame(multi_df)
                        
                   
print(df)
