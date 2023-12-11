
import mysql.connector
import pandas as pd
import numpy as np
from sklearn.cluster import AffinityPropagation
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

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

affinity_propagation_model = AffinityPropagation()
df['temperature_cluster'] = affinity_propagation_model.fit_predict(temperature_data_scaled)

min_sample= 3 
min_cluster_size = 5
cluster_counts = df['temperature_cluster'].value_counts()
valid_clusters = cluster_counts[cluster_counts >= min_cluster_size].index
df_filtered = df[df['temperature_cluster'].isin(valid_clusters)]
print(df_filtered)


plt.figure(figsize=(10, 6))
plt.scatter(x=df['temp'], y=df['temperature_cluster'], c=df['temperature_cluster'], cmap='viridis')
plt.title('Affinity Propagation Clustering')
plt.xlabel('Temperature')
plt.ylabel('Cluster')
plt.savefig('clusters/Affinity.png')
fig=plt.figure()
plt.close(fig)