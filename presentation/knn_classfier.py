from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(variables,labels)

pred = neigh.predict(variables)
accuracy=sklearn.metrics.accuracy_score(labels, pred)
print(accuracy)

from sklearn.metrics import f1_score
knn_f1_score = f1_score(labels, pred, average='macro')
print(knn_f1_score)