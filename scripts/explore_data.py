import pandas as pd

df = pd.read_csv("../data/taxi_trip.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())