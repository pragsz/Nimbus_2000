import mysql.connector
import numpy as np
import pandas as pd
from sklearn.cluster import BisectingKMeans
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
temp_data_scaled = scaler.fit_transform(temperature_data)


n_clusters = 4



bisecting_kmeans = BisectingKMeans(n_clusters=n_clusters)
labels = bisecting_kmeans.fit_predict(temp_data_scaled)



df['cluster_label'] = labels


plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['temp'], y=df['cluster_label'], c=df['cluster_label'], cmap='viridis')
plt.title('Bisecting K-Means Clustering Results')
plt.xlabel('Data Point Index')
plt.ylabel('Temperature (scaled)')
plt.savefig('clusters/Bisecting.png')
fig = plt.figure()
plt.close(fig)







