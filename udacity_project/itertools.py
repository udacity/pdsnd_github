import itertools
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

chi_df = pd.read_csv('chicago.csv')
name = pd.Series([city])
chi_df.set_index([name])
wash_df = pd.read_csv('washington.csv')
ny_df = pd.read_csv('new_york_city.csv') 
multi_df = pd.concat([chi_df, wash_df, ny_df],
                keys = ['chicago', 'new york city', 'washington'],
                names = ['Cities', 'Row ID'], sort = False)

print(multi_df.loc['washington'].head())
print(multi_df.loc['new york city'].head())
print(multi_df.loc['chicago'].head())

print(multi_df.loc['chicago'].groupby('Gender').apply(lambda subf: subf['Birth Year'][subf['Trip Duration'].idxmax()]))


print(chi_df.head())

