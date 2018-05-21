
dataframe = document_token_new.copy()
dataframe['class'] = dataframe['c_id']
dataframe.__delitem__('c_id')
dataframe.__delitem__('doc_id')
dataframe.__delitem__('token_id')

X = dataframe.iloc[:,:12].values
Y = dataframe.iloc[:,13].values


from sklearn.naive_bayes import BernoulliNB
bnb_classifier=BernoulliNB()

bnb_classifier=bnb_classifier.fit(variables_train,labels_train)