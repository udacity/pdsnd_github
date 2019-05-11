import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import itertools

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}
        
chi_df = pd.read_csv('chicago.csv')
wash_df = pd.read_csv('washington.csv')
ny_df = pd.read_csv('new_york_city.csv') 

values = {'User Type': 'Customer', 'Gender': 'Male' , 'Birth Year': '0000'}
user_types = {'User Type':'subscriber', 'User Type':'Customer'}
#np.random.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3])
#print("chi shape \n{}".format(chi_df.shape))
#print("chi \n{}".format(chi_df.stack().head(9)))
#chi_df['Birth Year'] = chi_df.fillna(method = 'ffill')
#chi_df['Gender'] = chi_df.fillna(method = 'ffill')

#chi_df = chi_df.fillna(value = values)
#print("chi na\n{}".format(chi_df.isna().sum()))
#print('chi dtypes\n{}'.format(chi_df.dtypes))
#print("-"*50)
#print("chi \n{}".format(chi_df.stack().head(9)))

#print("wash shape \n{}".format(wash_df.shape))
#print("wash shape after: \n{}".format(wash_df.shape))
#print("wash \n{}".format(wash_df.stack().head(9)))
#print("wash na\n{}".format(wash_df.isna().sum()))
#print("-"*50)

#print("ny shape \n{}".format(ny_df.shape))
#print("ny \n{}".format(ny_df.stack().head(9)))
#ny_df['Birth Year'] = ny_df.fillna(method = 'ffill')
#ny_df['Gender'] = ny_df.fillna(method = 'ffill')
#ny_df['User Type'] = ny_df.fillna(method = 'ffill')

#print("ny na\n{}".format(ny_df.isna().sum()))
#print(ny_df.dtypes)
#ny_df = ny_df.fillna(value = values)
#print("ny \n{}".format(ny_df.stack().head(9)))
#print("ny na\n{}".format(ny_df.isna().sum()))

df = pd.concat([chi_df, ny_df, wash_df],keys = ['chicago', 'new york city', 'washington'],
                names = ['Cities', 'Row ID'], sort = False)

df = df.dropna()
print(df.stack().head(9))
print(df.isna().sum())
print(df.loc[city]('User Type').value_counts())
print(df['Gender'].value_counts())
