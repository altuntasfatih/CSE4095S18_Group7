import pandas as pd
from pymongo import MongoClient
import openpyxl

db_name = 'data-science-database'
collection_name= 'Tweets'
url=["mongodb://fotercim:212427123a1@ds121349.mlab.com:21349/data-science-database","mongodb://localhost:27017/data-science-database"]

def normalize(class_name):
    if(class_name.upper() == 'YAS' or class_name.upper() == 'AGE'):
        return 1
    if(class_name.upper() == 'ILETISIM' or class_name.upper() == 'CONTACT'):
        return 2
    if(class_name.upper() == 'TARIH' or class_name.upper() == 'DATE'):
        return 3
    if(class_name.upper() == 'ID' or class_name.upper() == 'ID'):
        return 4
    if(class_name.upper() == 'ADDRESS' or class_name.upper() == 'ADDRESS'):
        return 5
    if(class_name.upper() == 'MESLEK' or class_name.upper() == 'JOB'):
        return 6
    if(class_name.upper() == 'FIRMA' or class_name.upper() == 'COMPANY'):
        return 7
    if(class_name.upper() == 'MEKAN' or class_name.upper() == 'PLACE'):
        return 8
    if(class_name.upper() == 'OLAY' or class_name.upper() == 'EVENT/ACTIVITY'):
        return 9
    if(class_name.upper() == 'ISIM' or class_name.upper() == 'NAME'):
        return 10
    if(class_name.upper() == 'TRASH'):
        return 11



def read_mongo(flag=0):
    
    mongo_uri = url[flag]
    conn = MongoClient(mongo_uri)
    db = conn[db_name]
    collection = db[collection_name]
    cursor = collection.find({'done' : 1})
    df =  pd.DataFrame(list(cursor))
    return df.drop(['_id','done','tweetID'],axis=1)


df=read_mongo(0)
df1=read_mongo(1)
df=df.append(df1)

documents=df['tweet']
document_token_pure=df['wordsoftweets']

column_names= ['doc_id','token_id','token_text','c_id']
document_token = pd.DataFrame(columns=column_names)

for index_outher, row in document_token_pure.iteritems():
    for index_ineer, (key, value) in enumerate(row.items()):
        document_token=document_token.append({'doc_id': index_outher+1,
                               'token_id':index_ineer+1,
                               'token_text':key,
                               'c_id': normalize(str(value)),
                               },ignore_index=True)
counter = 272
for index, row in document_token.iterrows():
    if index > 3541:
        new_id = counter + int(row['doc_id'])
        document_token.at[index,'doc_id'] = new_id

    
writer = pd.ExcelWriter('presentation/CSE4062_Group7_raw_dataset.xlsx')
documents.to_excel(writer)
writer.save()

writer = pd.ExcelWriter('document_token.xlsx')
document_token.to_excel(writer)
writer.save()