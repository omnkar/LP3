# ---------------------------------------------------------------
# Machine Learning Assignment – K-Means Clustering
# Dataset: sales_data_sample.csv
# ---------------------------------------------------------------

# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ---------------------------------------------------------------
# Step 1: Load Dataset
# ---------------------------------------------------------------
ds = pd.read_csv("sales_data_sample.csv", encoding='Latin-1')

print("Initial Data Sample:")
print(ds.head(), "\n")

print("Data Info:")
print(ds.info(), "\n")

# ---------------------------------------------------------------
# Step 2: Data Preprocessing
# ---------------------------------------------------------------

# Convert ORDERDATE to datetime and numeric (timestamp)
ds['ORDERDATE'] = pd.to_datetime(ds['ORDERDATE'], errors='coerce')
ds['ORDERDATE'] = ds['ORDERDATE'].view('int64')  # convert datetime to numeric (ns since epoch)

# Encode STATUS column (convert categorical to numeric codes)
status_mapping = {
    'Shipped': 1,
    'Resolved': 2,
    'Cancelled': 3,
    'On Hold': 4,
    'Disputed': 5,
    'In Process': 6
}
ds['STATUS'] = ds['STATUS'].map(status_mapping)

# Drop irrelevant/non-numeric columns
cols_to_drop = [
    'PRODUCTCODE', 'ADDRESSLINE1', 'ADDRESSLINE2', 'POSTALCODE', 'TERRITORY',
    'CITY', 'STATE', 'COUNTRY', 'CUSTOMERNAME', 'CONTACTLASTNAME',
    'CONTACTFIRSTNAME', 'DEALSIZE', 'PHONE'
]
ds = ds.drop(columns=cols_to_drop, errors='ignore')

# Convert categorical PRODUCTLINE to dummy variables
ds = pd.get_dummies(ds, columns=['PRODUCTLINE'], drop_first=True)

# ---------------------------------------------------------------
# Step 3: Handle Missing Values (if any)
# ---------------------------------------------------------------
ds = ds.dropna()
print(f"Dataset after cleaning: {ds.shape[0]} rows, {ds.shape[1]} columns\n")

# ---------------------------------------------------------------
# Step 4: Standardize the Data
# ---------------------------------------------------------------
scaler = StandardScaler()
dataset_scaled = scaler.fit_transform(ds)

# ---------------------------------------------------------------
# Step 5: Determine Optimal Number of Clusters (Elbow Method)
# ---------------------------------------------------------------
WCSS = []  # Within-Cluster Sum of Squares

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(dataset_scaled)
    WCSS.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), WCSS, marker='o')
plt.title("Elbow Method for Optimal k")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.grid(True)
plt.show()

# ---------------------------------------------------------------
# Step 6: Apply K-Means with chosen number of clusters (e.g. k=3)
# ---------------------------------------------------------------
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
labels = kmeans.fit_predict(dataset_scaled)
centroids = kmeans.cluster_centers_

# Add cluster labels back to dataset
ds['Cluster'] = labels

print("\nCluster Centers Shape:", centroids.shape)
print("Cluster Distribution:\n", ds['Cluster'].value_counts(), "\n")

# ---------------------------------------------------------------
# Step 7: Visualize Clusters (2D using PCA or top 2 features)
# ---------------------------------------------------------------
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
reduced_data = pca.fit_transform(dataset_scaled)

plt.figure(figsize=(8, 5))
sns.scatterplot(x=reduced_data[:, 0], y=reduced_data[:, 1], hue=labels, palette='tab10')
plt.title("Customer Segmentation via K-Means (PCA Reduced)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title='Cluster')
plt.show()

# ---------------------------------------------------------------
# Step 8: Save clustered dataset (optional)
# ---------------------------------------------------------------
ds.to_csv("clustered_sales_data.csv", index=False)
print("Clustered dataset saved as 'clustered_sales_data.csv'.")
