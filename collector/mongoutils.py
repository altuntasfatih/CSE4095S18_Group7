#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymongo
from random import randint
from collector.constant import DBPATH,db_name,collection_name

class MongodbClient:

    def __init__(self):
        print(DBPATH)
        self.mongo_client = pymongo.MongoClient(DBPATH, connectTimeoutMS=30000,
                                                        socketTimeoutMS=None,
                                                        socketKeepAlive=True,
                                                        connect=False)
        self.db = self.mongo_client[db_name]
        self.collection = self.db[collection_name]

        self.currentTweetID = None


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
            selected_tweets = filter(lambda x: x not in ["RT","https","co","t","ve","in","e"], tweet) #todo Caneeer şunu regex yapda aksin buralar

            tw = {
                "tweetID" : username + "-" + str(count),
                "username": username,
                'done': 0,
                "tweet":pure,
                'wordsoftweets': dict((t, 0) for t in list(selected_tweets)),
                }
            self.collection.insert_one(tw)
            count+=1
        return count;

    def saveTokenizeNews(self, field):
        count = 0;
        for newsWord, pure in self.tweets_generator:
            selected_tweets = filter(lambda x: x not in ["RT", "https", "co", "t", "ve", "in", "e"],
                                     newsWord)  # todo Caneeer şunu regex yapda aksin buralar

            tw = {
                "tweetID": field + "-" + str(count),
                "username": field,
                'done': 0,
                "tweet": pure,
                'wordsoftweets': dict((t, 0) for t in list(selected_tweets)),
            }
            self.collection.insert_one(tw)
            count += 1
        return count;

class MongodbReader(MongodbClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __iter__(self):
        for doc in self.collection.find():
            yield doc

    def getOneItem(self,filter={"done":0}):
        r=self.collection.count(filter)
        temp=self.collection.find(filter).limit(1).skip(randint(0,r-1))
        temp=temp.next()
        self.currentTweetID=temp["tweetID"]
        return  temp

    def getPreviousItem(self):
        previousTweetID = self.findPreviousTweetID(self.currentTweetID)
        self.currentTweetID = previousTweetID       # swap "currentTweetID" by "previousTweetID"
        filter = {"tweetID": previousTweetID}
        return self.collection.find_one(filter=filter)

    def findPreviousTweetID(self, currentTweetID):  # @ufukgurbuz44-8
        tweetID = currentTweetID.split("-")
        _id = int(tweetID[1])
        if(_id != 0):
            _id = _id - 1

        previousTweetID = tweetID[0] + "-" + str(_id)
        return previousTweetID

    def updateOneItem(self,id,_labeed):

        result = self.collection.update(
            {"_id": id},
            {
                '$set': {
                    'done': 1,
                    'wordsoftweets':_labeed
                }
            }
        )
        return result
