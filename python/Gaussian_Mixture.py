import mysql.connector
import pandas as pd
import numpy as np
from sklearn.mixture import GaussianMixture
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


gmm = GaussianMixture(n_components=3, covariance_type='full', random_state=42)  # You can adjust the number of components
df['temperature_cluster'] = gmm.fit_predict(temperature_data_scaled)

plt.figure(figsize=(10, 6))
plt.scatter( x=df['temp'], y=df['temperature_cluster'], c=df['temperature_cluster'], cmap='viridis')
plt.xlabel('Clusters')
plt.ylabel('Temperature')
plt.title('Gaussian Mixture Clustering of Temperature')
plt.savefig('clusters/Gaussian.png')
fig = plt.figure()
plt.close(fig)




