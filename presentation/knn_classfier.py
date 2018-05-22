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

variables_train, variables_test, labels_train, labels_test=train_test_split(
        variables, labels, test_size=.9, random_state=1)

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(variables_train,labels_train)
pred = neigh.predict(variables_test)
accuracy=sklearn.metrics.accuracy_score(labels_test, pred)
print(accuracy)


from sklearn.model_selection import KFold, cross_val_score
k_fold = KFold(n_splits=10,shuffle=True)
for train_indices, test_indices in k_fold.split(variables):
    x_train, x_test = variables[train_indices], variables[test_indices]
    y_train, y_test = labels[train_indices], labels[test_indices]
    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(x_train,y_train)
    pred = neigh.predict(x_test)
    accuracy=sklearn.metrics.accuracy_score(y_test, pred)
    print(accuracy)