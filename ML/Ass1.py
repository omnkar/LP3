# -----------------------------
# ML Assignment 1 – Uber Fare Prediction
# -----------------------------

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Ignore warnings
warnings.filterwarnings("ignore")

# -----------------------------
# Load and inspect data
# -----------------------------
data = pd.read_csv("uber.csv")

print("First 5 rows of dataset:")
print(data.head())

print("\nDataset Info:")
print(data.info())

# -----------------------------
# Preprocessing
# -----------------------------
# Convert pickup_datetime to datetime format
data['pickup_datetime'] = pd.to_datetime(data['pickup_datetime'], errors='coerce')

# Drop rows with missing values
data.dropna(inplace=True)

# -----------------------------
# Feature Engineering
# -----------------------------
# Extract useful time-based features
data['hour'] = data['pickup_datetime'].dt.hour
data['day'] = data['pickup_datetime'].dt.day
data['month'] = data['pickup_datetime'].dt.month
data['year'] = data['pickup_datetime'].dt.year

# Drop non-numeric or unneeded columns
if 'key' in data.columns:
    data.drop('key', axis=1, inplace=True)
data.drop('pickup_datetime', axis=1, inplace=True)

# -----------------------------
# Data Summary
# -----------------------------
print("\nStatistical Summary:")
print(data.describe())

# -----------------------------
# Boxplot for fare amount
# -----------------------------
plt.figure(figsize=(6, 4))
plt.boxplot(data['fare_amount'])
plt.title("Boxplot of Fare Amounts")
plt.ylabel("Fare Amount ($)")
plt.show()

# -----------------------------
# Define features and target
# -----------------------------
X = data.drop('fare_amount', axis=1)
y = data['fare_amount']

# Split data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------
# Linear Regression Model
# -----------------------------
lr_model = LinearRegression()
lr_model.fit(x_train, y_train)

# Predictions and RMSE
lr_pred = lr_model.predict(x_test)
lr_rmse = np.sqrt(mean_squared_error(y_test, lr_pred))
print("\nRMSE for Linear Regression:", lr_rmse)

# -----------------------------
# Random Forest Model
# -----------------------------
rfr_model = RandomForestRegressor(random_state=42, n_estimators=100)
rfr_model.fit(x_train, y_train)

rfr_pred = rfr_model.predict(x_test)
rfr_rmse = np.sqrt(mean_squared_error(y_test, rfr_pred))
print("RMSE for Random Forest:", rfr_rmse)

# -----------------------------
# Comparison
# -----------------------------
print("\n--------------------------------")
print("Model Performance Comparison")
print("--------------------------------")
print(f"Linear Regression RMSE : {lr_rmse:.4f}")
print(f"Random Forest RMSE     : {rfr_rmse:.4f}")
print("--------------------------------")
