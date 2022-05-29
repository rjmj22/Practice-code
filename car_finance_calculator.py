import pandas as pd

df = pd.read_csv('D:\\code\data.csv')

df = df.dropna()

print(df)