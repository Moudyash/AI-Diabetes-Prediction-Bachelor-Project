import pickle

import h5py as h5py
import pandas as pd
import numpy as np
from numpy import e
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from lazypredict.Supervised import LazyClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, adjusted_rand_score, normalized_mutual_info_score

# Load the dataset
data = pd.read_csv(r"E:\programming\python\pythonProject6\dataset.csv")

def checkZeroValue(df, x):
    if (df[x] == 0).any():
        num_zeros = (df[x] == 0).sum()
        print(x, 'column contains', num_zeros, 'zero values')
    else:
        print(x, 'column does not contain zero values')

# Check zero value counts
for col in data.columns:
    checkZeroValue(data, col)
    print('------------------------')

# Replace zero values with mean or median for specific columns
data['Glucose'] = data['Glucose'].replace(0, int(data['Glucose'].mean()))
data['BloodPressure'] = data['BloodPressure'].replace(0, int(data['BloodPressure'].mean()))
data['SkinThickness'] = data['SkinThickness'].replace(0, int(data['SkinThickness'].mean()))
data['Insulin'] = data['Insulin'].replace(0, int(data['Insulin'].mean()))
data['BMI'] = data['BMI'].replace(0, data['BMI'].mean())

# Split the data into features (X) and target (y)
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Classification - KNeighbors
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
classifier = KNeighborsClassifier(n_neighbors=24)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print("KNeighbors Accuracy Score:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Classification - DecisionTree
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print("DecisionTree Accuracy Score:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
# Classification - GaussianNB
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
gnb = GaussianNB().fit(X_train, y_train)
y_pred = gnb.predict(X_test)
print("GaussianNB Accuracy Score:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
def btnOnclick(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,DiabetesPedigreeFunction,BMI,Age):
    # Classification - DecisionTree
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,DiabetesPedigreeFunction,BMI,Age]])
    print("DecisionTree Accuracy Score:", accuracy_score(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
def saveModel(fileName, model):
    # Save the model to an HDF5 file
    try:
        with h5py.File(fileName, 'w') as h5file:
            for key, value in model.items():
                h5file.create_dataset(key, data=value)
        print("Model saved successfully as HDF5.")
    except Exception as e:
        print("Error while saving the model:", str(e))
saveModel(r"E:\programming\python\pythonProject6\model.h5", classifier)
