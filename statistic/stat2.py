import pandas as pd
import numpy as np
import operator



def top10(x, n=10):
     return x.value_counts().head(n)


def top50(x, n=50):
    return x.value_counts().head(n)




class_names = pd.read_csv('class.csv')
documents = pd.read_excel('document.xlsx')
document_token = pd.read_excel('document_token.xlsx')

total_instances=document_token
total_instances= total_instances.groupby('c_id').count()['doc_id']
print(total_instances)

average=document_token
average['token_length'] = average['token_text'].map(str).apply(len)
average=average.drop(['doc_id','token_id','token_text'],axis=1)
average_length=average.groupby('c_id').mean()
std=average.groupby('c_id').std()
print(average_length)
print(std)

average=document_token
average=average.drop(['doc_id','token_id',],axis=1)
print(average)



frequent_items=average.drop(['token_length'],axis=1)
frequent_items=frequent_items.groupby('c_id')['token_text']
print(frequent_items)

print(frequent_items.apply(top10))
print(frequent_items.apply(top50))


average=document_token
average['token_length'] = average['token_text'].map(str).apply(len)
average=average.drop(['doc_id','token_id','token_text'],axis=1)

les5charcter=average[document_token['token_length'] < 5 ]
print(les5charcter.head(1))
print(les5charcter.groupby('c_id').count())