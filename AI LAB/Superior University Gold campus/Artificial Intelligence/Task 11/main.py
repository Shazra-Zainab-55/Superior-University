import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
data = pd.read_csv("Superior University Gold campus\Artificial Intelligence\Task 11\gym_members_exercise_tracking.csv") 
print("Dataset Head:\n", data.head())
for column in data.columns:
    if data[column].dtype == 'object':
        label_encoder = LabelEncoder()
        data[column] = label_encoder.fit_transform(data[column])
X = data.drop(columns=['Age'])  
y = data['Age']  
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Applying SVM Classifier
svm_classifier = SVC(kernel='linear', random_state=42)
svm_classifier.fit(X_train, y_train)
y_pred = svm_classifier.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test,y_pred))