# --------------------------------------------------------------
# ML Assignment – Bank Customer Churn Prediction using ANN
# --------------------------------------------------------------

# 1️⃣ Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# --------------------------------------------------------------
# 2️⃣ Load Dataset
# --------------------------------------------------------------
# Dataset: https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling
data = pd.read_csv("Churn_Modelling.csv")

print("Dataset Sample:")
print(data.head())

# --------------------------------------------------------------
# 3️⃣ Feature and Target Separation
# --------------------------------------------------------------
# Drop unnecessary columns
X = data.drop(['RowNumber', 'CustomerId', 'Surname', 'Exited'], axis=1)
y = data['Exited']

# Encode categorical variables
le_gender = LabelEncoder()
X['Gender'] = le_gender.fit_transform(X['Gender'])  # Male=1, Female=0

# One-hot encode Geography
X = pd.get_dummies(X, columns=['Geography'], drop_first=True)

# --------------------------------------------------------------
# 4️⃣ Split Dataset into Train/Test
# --------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --------------------------------------------------------------
# 5️⃣ Normalize the Data
# --------------------------------------------------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# --------------------------------------------------------------
# 6️⃣ Build the Neural Network
# --------------------------------------------------------------
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=X_train.shape[1]))
model.add(Dropout(0.3))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))  # Binary classification

# Compile model
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# --------------------------------------------------------------
# 7️⃣ Train the Model
# --------------------------------------------------------------
history = model.fit(X_train, y_train,
                    epochs=50,
                    batch_size=32,
                    validation_split=0.2,
                    verbose=1)

# --------------------------------------------------------------
# 8️⃣ Evaluate on Test Data
# --------------------------------------------------------------
y_pred_prob = model.predict(X_test)
y_pred = (y_pred_prob > 0.5).astype(int)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy on Test Set:", round(accuracy * 100, 2), "%")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", cm)

# Classification Report
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# --------------------------------------------------------------
# 9️⃣ Visualize Confusion Matrix
# --------------------------------------------------------------
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()

# --------------------------------------------------------------
# 🔟 Optional: Plot training history
# --------------------------------------------------------------
plt.figure(figsize=(8, 4))
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy Over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
