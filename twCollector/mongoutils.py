
import pymongo


DBPATH = "mongodb://localhost:27017/"
db_name = 'Twitter'
collection_name= 'Tweets'


class MongodbClient:
    def __init__(self):
        self.mongo_client = pymongo.MongoClient(DBPATH)
        self.db = self.mongo_client[collection_name]
        self.collection = self.db[collection_name]


class MongodbWriter(MongodbClient):
    def __init__(self, tweets_generator, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tweets_generator = tweets_generator

    def __iter__(self):
        count=0;
        for tweet in self.tweets_generator:
            self.collection.insert_one(tweet)
            count+=1
        return count;

    def saveTokenize(self,username):
        count=0;
        for tweet,pure in self.tweets_generator:
            selected_tweets = filter(lambda x: x not in ["RT","https","co","t","ve","in","e"], tweet)

            tw = {
                "username": username,
                'done': 0,
                "tweet":pure,
                'wordsoftweets': dict((t, 0) for t in list(selected_tweets)),
                }
            self.collection.insert_one(tw)
            count+=1
        return count;

class MongodbReader(MongodbClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __iter__(self):
        for doc in self.collection.find():
            yield doc
