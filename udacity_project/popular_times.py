import pandas as pd

filename = 'chicago.csv'

# load data file into a dataframe
df = pd.read_csv(filename)
#print(df.columns)

# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract hour from the Start Time column to create an hour column
df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
#print(df['hour'].head())
# find the most common hour (from 0 to 23)
popular_hour = df['hour'].mode()[0]

    
print('Most Frequent Start Hour:', popular_hour)
