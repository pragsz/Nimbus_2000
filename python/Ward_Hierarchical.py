
import mysql.connector
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
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

numerical_features = df.select_dtypes(include=['float64', 'int64']).columns
preprocessor = ColumnTransformer(
    transformers=[('num', StandardScaler(), numerical_features)])



pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('cluster', AgglomerativeClustering(n_clusters=3, linkage='ward'))
])



pipeline.fit(df)


# In[7]:


cluster_labels = pipeline.named_steps['cluster'].labels_


# In[8]:


df['Cluster'] = cluster_labels


# In[9]:


print(df)


# In[10]:

plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Cluster'], y=df['temp'], c=df['Cluster'], cmap='viridis')
# plt.scatter(x=df['temp'], y=df['temperature_cluster'], c=df['Cluster'], cmap='viridis')
plt.title('Ward Hierarchical Clustering')
plt.xlabel('Cluster')
plt.ylabel('Temperature')
plt.savefig('clusters/Ward_Hierarchical.png')
fig = plt.figure()
plt.close(fig)
