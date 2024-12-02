
import pandas as pd
import numpy as py
# Data reading
df= pd.read_csv("Superior University Gold campus\Artificial Intelligence\Task 09\gym_members_exercise_tracking.csv")
print(df)
# Data Exploration
print(f"Number of Rows: {df.shape[0]} \nNumber of Columns: {df.shape[1]}")
df.count()
df.isnull().sum()

df.info()

df.describe()

df.head()

df.tail()
df.nunique()
# Data preprocessing
