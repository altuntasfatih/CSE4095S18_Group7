import pandas as pd
from pymongo import MongoClient
import openpyxl

db_name = 'data-science-database'
collection_name= 'Tweets'

def normalize(class_name):
    if(class_name == 'YAS'):
        return 1
    if(class_name == 'ILETISIM'):
        return 2
    if(class_name == 'TARIH'):
        return 3
    if(class_name == 'ID'):
        return 4
    if(class_name == 'ADDRESS'):
        return 5
    if(class_name == 'MESLEK'):
        return 6
    if(class_name == 'FIRMA'):
        return 7
    if(class_name == 'MEKAN'):
        return 8
    if(class_name == 'OLAY'):
        return 9
    if(class_name == 'ISIM'):
        return 10
    if(class_name == 'TRASH'):
        return 11


def read_mongo():
    mongo_uri = "mongodb://fotercim:212427123a1@ds121349.mlab.com:21349/data-science-database"
    conn = MongoClient(mongo_uri)
    db = conn[db_name]
    collection = db[collection_name]
    cursor = collection.find({'done' : 1})
    df =  pd.DataFrame(list(cursor))
    return df.drop(['_id','done','tweetID'],axis=1)

df=read_mongo()


documents=df['tweet']
document_token_pure=df['wordsoftweets']

column_names= ['doc_id','token_id','token_text','c_id']
document_token = pd.DataFrame(columns=column_names)

for index_outher, row in document_token_pure.iteritems():
    for index_ineer, (key, value) in enumerate(row.items()):
        document_token=document_token.append({'doc_id': index_outher+1,
                               'token_id':index_ineer+1,
                               'token_text':key,
                               'c_id': normalize(value),
                               },ignore_index=True)



writer = pd.ExcelWriter('document.xlsx')
documents.to_excel(writer)
writer.save()

writer = pd.ExcelWriter('document_token.xlsx')
document_token.to_excel(writer)
writer.save()