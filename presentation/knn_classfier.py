from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(variables,labels)

pred = neigh.predict(variables)
accuracy=sklearn.metrics.accuracy_score(labels, pred)
print(accuracy)

from sklearn.metrics import f1_score
knn_f1_score = f1_score(labels, pred, average='macro')
print(knn_f1_score)

from sklearn.metrics import precision_score
knn_precision_score = precision_score(labels, pred, average='macro')
print(knn_precision_score)

from sklearn.metrics import recall_score
knn_recall_score = recall_score(labels, pred, average='macro')
print(knn_recall_score)

'''
#AUC

import numpy as np
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
fpr, tpr, thresholds = roc_curve(labels, pred, pos_label=2)
knn_auc = auc(fpr,tpr)
print(knn_auc)
'''