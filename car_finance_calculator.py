# Importing file data.csv
# Make sure to update the path as needed

import pandas as pd

df = pd.read_csv('D:\\code\data.csv')

df = df.dropna()

# Getting csv data to lists

superprime = df.loc[1, :].values.tolist()

prime = df.loc[3, :].values.tolist()

nonprime = df.loc[5, :].values.tolist()

subprime = df.loc[7, :].values.tolist()

deep_subprime = df.loc[9, :].values.tolist()

