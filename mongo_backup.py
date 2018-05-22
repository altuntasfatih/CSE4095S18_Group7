from pymongo import MongoClient
import pandas as pd
import json

db_name = 'data-science-database'
collection_name= 'Tweets'

mongo_uri = "mongodb://fotercim:212427123a1@ds121349.mlab.com:21349/data-science-database"
conn = MongoClient(mongo_uri)
db = conn[db_name]
collection = db[collection_name]
cursor = collection.find({'done' : 1})

df =  pd.DataFrame(list(cursor))
df = df.drop(['_id','done','tweetID'],axis=1)

conn = MongoClient('localhost', 27017)
db = conn.data_science_v2_backup
collection = db.tweets

for index, row in df.iterrows():
    dic = row.to_json()
    dic = json.loads(dic)
    collection.insert_one(dic)
