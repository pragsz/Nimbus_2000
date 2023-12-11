import mysql.connector
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
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




agglomerative = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
df['temperature_cluster'] = agglomerative.fit_predict(temperature_data_scaled)


plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['temp'], y=df['temperature_cluster'], c=df['temperature_cluster'], cmap='viridis')
plt.xlabel('Temperature')
plt.title('Hierarchical Clustering of Temperature')
plt.savefig('clusters/Hierarchical_clustering.png')
fig = plt.figure()
plt.close(fig)





# In[ ]:




