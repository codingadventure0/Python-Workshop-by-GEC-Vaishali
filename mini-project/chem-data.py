import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Chemistry.csv")
# print(df)
# print(df.head())
# print(df.tail())

x=df.head().iloc[:,1]
y=df.head().iloc[:,2]
# print(x)
# print(y)

# For checking number of zeros in column
# print(df.isnull().sum())

# plt.plot(x,y)
plt.bar(x,y)
# plt.pie(x,y)
plt.show()