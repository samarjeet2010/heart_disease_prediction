import pandas as pd
import numpy as np

# Step 1: Load Data
data = pd.read_csv("heart.csv")

print("Data Loaded Successfully")
print(data.head())

# Step 2: Check Missing Values
print(data.isnull().sum())

# Step 3: Split Data
X = data.drop("target", axis=1)
y = data["target"]

# Step 4: Train-Test Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Train Model
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("Model Trained Successfully")

# Step 6: Prediction
y_pred = model.predict(X_test)

# Step 7: Accuracy
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 8: Save Model
import joblib

joblib.dump(model, "heart_model.pkl")
print("Model Saved Successfully")