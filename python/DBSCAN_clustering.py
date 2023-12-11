import mysql.connector
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
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


dbscan = DBSCAN(eps=0.5, min_samples=5)  # You can adjust parameters as needed
df['temperature_cluster'] = dbscan.fit_predict(temperature_data_scaled)

num_clusters = len(set(df['temperature_cluster'])) - (1 if -1 in df['temperature_cluster'] else 0)
print(f"Number of clusters: {num_clusters}")

plt.figure(figsize=(10, 6))
plt.scatter( x=df['temp'],y=df['temperature_cluster'], c=df['temperature_cluster'], cmap='viridis')
plt.ylabel('Cluster')
plt.xlabel('Temperature')
plt.title('DBSCAN Clustering of Temperature')
plt.savefig('clusters/DBSCAN.png')
fig = plt.figure()
plt.close(fig)





