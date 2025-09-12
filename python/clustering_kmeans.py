import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Standardisation of the dataset
scaler = StandardScaler()
scaled_features = scaler.fit_transform(dataset)

# Convert the scaled array back to a DataFrame with original column names
scaled_df = pd.DataFrame(scaled_features, columns=dataset.columns)

#  Clustering with KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(scaled_features)

#Predict clusters and add to DataFrame
dataset["clusters"] = kmeans.predict(scaled_df)

# Delete scaled_df as it is no longer needed
del scaled_df