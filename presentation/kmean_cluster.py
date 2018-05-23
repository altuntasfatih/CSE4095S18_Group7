from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

kmeans = KMeans(n_clusters=10, random_state=0).fit(variables)
y_kmeans = kmeans.predict(variables)

plt.scatter(variables[:, 0], variables[:, 1], c=y_kmeans, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=100, alpha=0.5);

y_classes = []


for index in range(1,11):
    temp = []
    for i in range(0,len(labels)):
        if (labels[i]) == index:
            temp.append(y_kmeans[i])
            
    y_classes.append(temp)


cluster_df= pd.DataFrame(y_classes[1])

dic_array = []
for i in range(0,10):
    dic = {}
    for item in y_classes[i]:
        if (int(item) not in dic):
            dic[item]=1
        else:
             dic[item]= dic[item]+1
    dic_array.append(dic)         
