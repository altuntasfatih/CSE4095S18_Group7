#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from twCollector.tweetcollector import TwitterAPI
from twCollector.tweettokenizer import TwitterTokenizer
from twCollector.mongoutils import *
import time, os



#consumer_key = os.environ['CONSUMER_KEY']
#consumer_secret = os.environ['CONSUMER_SECRET_KEY']
#access_token = os.environ['ACCESS_TOKEN']
#access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
consumer_key = 'GF7CSQPUIVtNYfjcCFDaO81aN'
consumer_secret = 'uYzrrOqo3vX3P3zcRO4KPzLl6C7pNSO7kdkbBhUT0Rz32OrsfQ'
access_token = '165432951-aQH41KBBuDfqpRQQfh6S0ocRbO7UpXn9f5Ri6CUk'
access_token_secret = 'yFsvWY1dkY25BwWfB5RZMKE7V9b9fmOTEvjTsCcLUeeDO'

def collectTweet(userlist):

    tw = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
    start_time = time.time();
    endTime=time.time();
    total=0
    for uname in userlist:

        user_tweet_generator = tw.get_user_tweets(uname)
        tokenized_tweet_generator = TwitterTokenizer(user_tweet_generator)

        mdb_writer = MongodbWriter(tokenized_tweet_generator)
        _count=mdb_writer.saveTokenize(uname);

        print("{} 's {} numbers tweets added in seconds {}".format(uname,_count,int(time.time()-endTime)))
        endTime = time.time();
        total=total+int(_count)


    print("{} users , {} tweets , in  {} seconds".format(len(userlist),total,int(time.time()-start_time)))

def main():

    with open("userlist.txt") as f:
        content = f.readlines()
    userList=[x.strip() for x in content]
    print(userList);
    collectTweet(userList)



main()