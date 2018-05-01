#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collector.tweetcollector import TwitterAPI
from collector.tokenizer import WordTokenizer
from collector.mongoutils import *
import time
from collector.constant import consumer_key,consumer_secret,access_token,access_token_secret

def collectTweet(userlist):

    tw = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
    print(consumer_key," ",consumer_secret," ",access_token," ",access_token_secret)
    start_time = time.time();
    endTime=time.time();
    total=0
    for uname in userlist:

        user_tweet_generator = tw.get_user_tweets(uname)
        tokenized_tweet_generator = WordTokenizer(user_tweet_generator,1)

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