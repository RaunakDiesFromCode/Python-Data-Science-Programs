import numpy as np 
from sklearn import datasets 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score 
# Load the Iris dataset 
iris = datasets.load_iris() 
X = iris.data  # Features 
Y = iris.target  # Target classes 
# Split the dataset into training and test sets (70% train, 30% test) 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42) 
# Create a Random Forest model 
model = RandomForestClassifier(n_estimators=100, random_state=42) 
# Fit the model to the training data 
model.fit(X_train, Y_train) 
# Make predictions on the test set 
Y_pred = model.predict(X_test) 
# Calculate accuracy 
accuracy = accuracy_score(Y_test, Y_pred) 
print(f'Accuracy: {accuracy * 100:.2f}%') 