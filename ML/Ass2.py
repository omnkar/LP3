# ---------------------------------------------
# ML Assignment – Email Spam Detection (Binary Classification)
# Using KNN and SVM
# ---------------------------------------------

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ---------------------------------------------
# Load Dataset
# ---------------------------------------------
# You can download dataset from:
# https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

# For demo, assume file is named "spam.csv"
data = pd.read_csv("spam.csv", encoding="latin-1")

# Keep only useful columns
data = data[['v1', 'v2']]
data.columns = ['label', 'message']

print("Dataset Sample:")
print(data.head(), "\n")

# ---------------------------------------------
# Encode Labels
# ---------------------------------------------
# Spam = 1, Ham (Not Spam) = 0
data['label_num'] = data['label'].map({'ham': 0, 'spam': 1})

# ---------------------------------------------
# Split Features and Target
# ---------------------------------------------
X = data['message']
y = data['label_num']

# Convert text into TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)
X_tfidf = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y, test_size=0.2, random_state=42
)

# ---------------------------------------------
# K-Nearest Neighbors (KNN)
# ---------------------------------------------
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# Evaluate KNN
knn_acc = accuracy_score(y_test, y_pred_knn)
print("KNN Accuracy:", knn_acc)
print("\nKNN Classification Report:\n", classification_report(y_test, y_pred_knn))

# ---------------------------------------------
# Support Vector Machine (SVM)
# ---------------------------------------------
svm = SVC(kernel='linear', C=1)
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)

# Evaluate SVM
svm_acc = accuracy_score(y_test, y_pred_svm)
print("SVM Accuracy:", svm_acc)
print("\nSVM Classification Report:\n", classification_report(y_test, y_pred_svm))

# ---------------------------------------------
# Confusion Matrices
# ---------------------------------------------
cm_knn = confusion_matrix(y_test, y_pred_knn)
cm_svm = confusion_matrix(y_test, y_pred_svm)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.heatmap(cm_knn, annot=True, fmt="d", cmap="Blues")
plt.title("KNN Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.subplot(1, 2, 2)
sns.heatmap(cm_svm, annot=True, fmt="d", cmap="Greens")
plt.title("SVM Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.tight_layout()
plt.show()

# ---------------------------------------------
# Compare Model Performance
# ---------------------------------------------
print("\n--------------------------------------------")
print("Model Performance Summary")
print("--------------------------------------------")
print(f"KNN Accuracy : {knn_acc*100:.2f}%")
print(f"SVM Accuracy : {svm_acc*100:.2f}%")
print("--------------------------------------------")
