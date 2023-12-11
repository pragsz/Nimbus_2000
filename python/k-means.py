import mysql.connector
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
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

k = 3  
kmeans = KMeans(n_clusters=k)
kmeans.fit(df)
df['cluster'] = kmeans.labels_
print(df)

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='temp', y='cluster', palette='viridis', hue='cluster', legend=False)
plt.title('K-means Clustering')
plt.xlabel('Temperature')
plt.ylabel('Cluster')
plt.savefig('clusters/kmeans.png')
fig = plt.figure()
plt.close(fig)