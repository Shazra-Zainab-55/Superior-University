import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer

train_data = pd.read_csv('Superior University Gold campus/Artificial Intelligence/Task 12/train.csv')
test_data = pd.read_csv('Superior University Gold campus/Artificial Intelligence/Task 12/test.csv')
gender_submission = pd.read_csv('Superior University Gold campus/Artificial Intelligence/Task 12/gender_submission.csv')
print("Train Data Info:")
print(train_data.info())
print("\nSummary Statistics:")
print(train_data.describe())
sns.countplot(x='Survived', data=train_data)
plt.title('Survival Counts')
plt.show()

sns.countplot(x='Survived', hue='Sex', data=train_data)
plt.title('Survival Counts by Gender')
plt.show()

sns.histplot(train_data['Age'].dropna(), kde=True, bins=30)
plt.title('Age Distribution')
plt.show()
missing_values = train_data.isnull().sum()
print("Missing Values:\n", missing_values)

X = train_data.drop(columns=['Survived', 'PassengerId', 'Name', 'Ticket', 'Cabin'])
y = train_data['Survived']
imputer = SimpleImputer(strategy='most_frequent')
X_imputed = imputer.fit_transform(X)
encoder = LabelEncoder()
X_encoded = pd.DataFrame(X_imputed, columns=X.columns)
X_encoded['Sex'] = encoder.fit_transform(X_encoded['Sex'])
X_encoded['Embarked'] = encoder.fit_transform(X_encoded['Embarked'].astype(str))

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)
X_train, X_val, y_train, y_val = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train, y_train)
y_val_pred = rf_classifier.predict(X_val)
accuracy = accuracy_score(y_val, y_val_pred)
print(f"Validation Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_val, y_val_pred))
conf_matrix = confusion_matrix(y_val, y_val_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.show()
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
grid_search = GridSearchCV(estimator=rf_classifier, param_grid=param_grid, cv=3, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)
tuned_model = grid_search.best_estimator_
print("Best Parameters:\n", grid_search.best_params_)

y_val_pred_tuned = tuned_model.predict(X_val)
tuned_accuracy = accuracy_score(y_val, y_val_pred_tuned)
print(f"Tuned Validation Accuracy: {tuned_accuracy * 100:.2f}%")
test_X = test_data.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])
test_X_imputed = imputer.transform(test_X)
test_X_encoded = pd.DataFrame(test_X_imputed, columns=test_X.columns)
test_X_encoded['Sex'] = encoder.transform(test_X_encoded['Sex'])
test_X_encoded['Embarked'] = encoder.transform(test_X_encoded['Embarked'].astype(str))
test_X_scaled = scaler.transform(test_X_encoded)

test_predictions = tuned_model.predict(test_X_scaled)
output = pd.DataFrame({'PassengerId': test_data['PassengerId'], 'Survived': test_predictions})
output.to_csv('submission.csv', index=False)
print("Predictions saved to submission.csv")
