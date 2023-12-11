import mysql.connector
import pandas as pd
import numpy as np
from sklearn.cluster import Birch
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




birch = Birch(threshold=0.5, n_clusters=3)  
df['temperature_cluster'] = birch.fit_predict(temperature_data_scaled)

print(df)



# scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['temp'], y=df['temperature_cluster'], c=df['temperature_cluster'], cmap='viridis')
plt.title('Birch Clustering')
plt.xlabel('Temperature')
plt.ylabel('Cluster')
plt.savefig('clusters/birch.png')
fig = plt.figure()
plt.close(fig)

# Box
# plt.figure(figsize=(10, 6))
# plt.subplot(1, 2, 2)
# sns.boxplot(x='temperature_cluster', y='temp', data=df)
# plt.xlabel('Cluster')
# plt.ylabel('Temperature')
# plt.title('Box Plot for Each Cluster')
# plt.savefig('clusters/birch.png')
# fig = plt.figure()
# plt.close(fig)


#Heatmap
# clustered_data = pd.DataFrame({'Temperature': temperature_data.squeeze(), 'Cluster': df['temperature_cluster']})
# plt.subplot(1, 2, 2)
# sns.heatmap(clustered_data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
# plt.title('Heatmap of Temperature and Cluster')
# plt.savefig('clusters/birch.png')
# fig = plt.figure()
# plt.close(fig)




#bar
# cluster_counts = df['temperature_cluster'].value_counts()
# plt.bar(cluster_counts.index, cluster_counts.values, color='skyblue')
# plt.xlabel('Cluster')
# plt.ylabel('Count')
# plt.title('Cluster Count for Birch Clustering')
