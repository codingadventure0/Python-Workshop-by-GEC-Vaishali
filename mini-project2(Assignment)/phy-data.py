
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Physics.csv")

# 1. Highest attendance student in first five rows
# x=df.head().iloc[:,1]
# y=df.head().iloc[:,3]
# plt.bar(x,y)
# plt.show()

# 2. Highest attendance student in Last five rows
# x=df.tail().iloc[:,1]
# y=df.tail().iloc[:,3]
# plt.bar(x,y)
# plt.show()

# 3. Student having highest attendance between 10-20 rows. 
# x=df.iloc[10:20,1]
# y=df.iloc[10:20,3]
# plt.bar(x,y)
# plt.show()

# 4. Student having highest attendance overall. 
x=df.iloc[:,1]
y=df.iloc[:,3]
plt.bar(x,y)
plt.show()