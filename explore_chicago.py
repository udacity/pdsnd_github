import numpy as np
import pandas as pd

df = pd.read_csv("chicago.csv")

#What are the different types of values in each column?
#print(df.dtypes)

#Are there any missing values?
#print(df.isnull().any())

#What columns are in this dataset?
print(df.columns)

#Lists all values and counts them
#print(df['Gender'].value_counts())

#Lists all unique values
#print(df['Gender'].unique())
