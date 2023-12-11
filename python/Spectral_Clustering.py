import mysql.connector
import pandas as pd
from sklearn.cluster import SpectralClustering
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



spectral = SpectralClustering(n_clusters=3, random_state=42)  
df['temperature_cluster'] = spectral.fit_predict(temperature_data_scaled)


plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['temp'], y=df['temperature_cluster'], c=df['temperature_cluster'], cmap='viridis')
# plt.scatter(df['DT'], df['Temperature'], c=df['temperature_cluster'], cmap='viridis')
plt.xlabel('Temperature')
plt.ylabel('Cluster')
plt.title('Spectral Clustering of Temperature')
plt.savefig('clusters/Spectral_Clustering.png')
fig = plt.figure()
plt.close(fig)


