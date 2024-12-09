import pandas as pd
import numpy as np
import pickle

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Data reading
df= pd.read_csv("Superior University Gold campus\Artificial Intelligence\Task 09 ,11\gym_members_exercise_tracking.csv")
print(df)
# Data Exploration
print(f"Number of Rows: {df.shape[0]} \nNumber of Columns: {df.shape[1]}")
df.count()
df.isnull().sum()
df.info()
df.describe()
df.head()
df.tail()
df.count()
for cols in df.columns:
    print(cols)
