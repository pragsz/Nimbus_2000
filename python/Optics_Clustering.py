import mysql.connector
import pandas as pd
from sklearn.cluster import OPTICS
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



optics = OPTICS(min_samples=5, xi=0.05, min_cluster_size=0.05)
df['temperature_cluster'] = optics.fit_predict(temperature_data_scaled)


plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['temp'], y=df['temperature_cluster'], c=df['temperature_cluster'], cmap='viridis')
# plt.scatter(df['DT'], df['Temperature'], c=df['temperature_cluster'], cmap='viridis')
plt.xlabel('Cluster')
plt.ylabel('Temperature')
plt.title('OPTICS Clustering of Temperature')
plt.savefig('clusters/Optics_Clustering.png')
fig = plt.figure()
plt.close(fig)






