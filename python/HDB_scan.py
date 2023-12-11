import mysql.connector
import pandas as pd
import numpy as np
import hdbscan
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  db="clustering"
)
mycursor = mydb.cursor()
mycursor.execute("select temp from iot_temp")
arr=[]

for x in mycursor:
    arr.append(x[0])
print(arr)
df = pd.DataFrame({'temp': arr})
print(df)

temperature_data = df[['temp']]
scaler = StandardScaler()
temperature_data_scaled = scaler.fit_transform(temperature_data)

# temperature_data = df.select_dtypes(include=['float64', 'int64']).columns

# Standardize the data
# scaler = StandardScaler()
# temperature_data_scaled = scaler.fit_transform(temperature_data)
# Create an HDBSCAN model
hdbscan_model = hdbscan.HDBSCAN(min_cluster_size=5, min_samples=3)

# Fit the model to the data
df['temperature_cluster'] = hdbscan_model.fit_predict(temperature_data_scaled)


# Add the cluster labels to the original dataframe
# df['cluster'] = cluster

# Visualize the clusters (you can modify this based on your requirements)
plt.figure(figsize=(10, 6))
plt.scatter(x=df['temp'], y=df['temperature_cluster'], c=df['temperature_cluster'], cmap='viridis', s=50)
plt.title('HDBSCAN Clustering')
plt.xlabel('Temperature')
plt.ylabel('Cluster')
plt.savefig('clusters/HDB.png')
fig = plt.figure()
plt.close(fig)
