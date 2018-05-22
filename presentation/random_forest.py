from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
import pandas as pd
from time import time
import nltk
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
import sklearn.metrics
from pandas import DataFrame,Series
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
rf_classifier=RandomForestClassifier(n_estimators=10)

t0=time()
rf_classifier=rf_classifier.fit(variables,labels)

training_time_container['random_forest']=time()-t0
print("Training Time: %fs"%training_time_container['random_forest'])

t0=time()
rf_predictions=rf_classifier.predict(variables)
prediction_time_container['random_forest']=time()-t0
print("Prediction Time: %fs"%prediction_time_container['random_forest'])

accuracy_container['random_forest']=sklearn.metrics.accuracy_score(labels, rf_predictions)
print ("Accuracy Score of Random Forests Classifier: ")
print(accuracy_container['random_forest'])


from sklearn.metrics import f1_score
random_forest_f1_score = f1_score(labels, rf_predictions, average='macro')
print("Random Forest F1 Score:",random_forest_f1_score)

from sklearn.metrics import precision_score
random_forest_precision_score = precision_score(labels, rf_predictions, average='macro')
print("Random Forest Precision Score:",random_forest_precision_score)

from sklearn.metrics import recall_score
random_forest_recall_score = recall_score(labels, rf_predictions, average='macro')
print("Random Forest Recall Score:",random_forest_recall_score)
