import pandas as pd
import numpy as np 
import pickle

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

df = pd.read_csv("Superior University Gold campus\Artificial Intelligence\Task 10\Dataset.csv")
# df = pd.read_json("data.json")
# pd.set_option("display.max_rows", None, "display.max_columns", None)
print(f"Number of Rows: {df.shape[0]} \nNumber of Columns: {df.shape[1]}")
df.head(2)
df.tail(2)
df.describe()
df.info()
print("-- Attributes in Data --")
for cols in df.columns:
    print(cols)
    print("-- Number of instances in Data --")
print(df.count())
df['city'].unique()
df.nunique()
print("-- Number of Null Values in Data --")
print(df.isnull().sum())
df = df.drop('date', axis=1)
df.head(2)
df.info()
df['street'].mode()[0]
# df['street'] = df['street'].fillna(df['street'].mode()[0])
def fillNaObjMode(cols):
    for i in cols:
        df[i] = df[i].fillna(df[i].mode()[0])

columns = ['street','city','statezip','country']
fillNaObjMode(columns)
def fillNaIntMode(cols):
    for i in cols:
        df[i] = df[i].fillna(df[i].mode()[0])

columns = ['bedrooms','bathrooms','floors','waterfront','view','yr_built']
fillNaIntMode(columns)
def fillNaFloat(cols):
    for i in cols:
        df[i] = df[i].fillna(df[i].mean())

columns = ['price','sqft_living','sqft_lot','sqft_above','sqft_basement']
fillNaFloat(columns)
df.info()
# df['price'] = df['price'].astype('int64')

def convertFloatintoInt(cols):
    for i in cols:
        df[i] = df[i].astype('int64')

columns = ['bedrooms','bathrooms','floors','waterfront','view','yr_built','price','sqft_living','sqft_lot','sqft_above','sqft_basement']
convertFloatintoInt(columns)
df.info()
df['street'].nunique()
df['country'].nunique()
df['city'].nunique()
df['statezip'].nunique()
df = df.drop('street',axis=1)
df = df.drop('country',axis=1)
df.info()
def dataEncoder(cols):
    for i in cols:
        dataLabelEncoder = LabelEncoder()
        df[i] = dataLabelEncoder.fit_transform(df[i])

columns = ['city','statezip']
dataEncoder(columns)
df.info()
df.head(2)
df.to_csv(r'encoded-data.csv', index = False, header = True)
# X, y
# train_x, train_y, test_x, test_y
# train, test
trainData, testData = train_test_split(df, test_size=0.2, shuffle=False)
trainData.shape
testData.shape
# testData.iloc()[:, 1:]

train_x = trainData.iloc()[:, 2:]
test_x  = testData.iloc()[:, 2:]

train_y = trainData.iloc()[:, 2]
test_y  = testData.iloc()[:, 2]
train_x.head(2)
train_y.head(2)
test_x.head(2)
test_y.head(2)
model_svc = SVC(C=1, gamma='scale', kernel='rbf', random_state=0)  # Modified parameters
model_svc.fit(train_x, np.ravel(train_y))

print(model_svc)
# Saving Trained Model
pickle.dump(model_svc, open('model_svc.pkl', 'wb'))
# Load saved Model
model_svc = pickle.load(open('model_svc.pkl', 'rb'))
model_predictions = model_svc.predict(test_x)
model_accuracy_score = accuracy_score(test_y, model_predictions)

print("-- Model Accuracy Score: ", end='')
print(round(model_accuracy_score,3))
testdata_predict = testData.copy(deep=True)
pd.options.mode.chained_assignment = None

testdata_predict['Prediction'] = model_predictions
model_accuracy_score = accuracy_score(testdata_predict['price'], testdata_predict['Prediction'])
