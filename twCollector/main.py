#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tweetcollector import TwitterAPI
from tweettokenizer import TwitterTokenizer
from mongoutils import *
import sys,time

# Twitter API
# You should sign in to twitter developers to get these
consumer_key = "767Q6lhPqOda7RYn9ylMi8ukn"
consumer_secret = "UgpWZwROIx6I5Es63q1y6hGdV5pEBtNMw02OjcOfYWZyf6fT5p"
access_token = "2194089737-wa5GEyuYr35j49Gdzwwgqs4elBVp3ZEAtGHub3l"
access_token_secret = "3IE4Ga4bdaDrtNcE3kJm4fBHXEuqGcBTuIEAvDMGOdDTD"



def collectTweet(userlist):

    tw = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
    start_time = time.time();
    total=0
    for uname in userlist:

        user_tweet_generator = tw.get_user_tweets(uname)
        tokenized_tweet_generator = TwitterTokenizer(user_tweet_generator)

        mdb_writer = MongodbWriter(tokenized_tweet_generator)
        _count=mdb_writer.saveTokenize(uname);

        print("{} 's {} numbers tweets added in seconds {}".format(uname,_count,time.time()-endTime))
        endTime = time.time();
        total=total+_count


    print("{} users , {} tweets , in {} seconds {} ".format(len(userlist),total,int(time.time()-start_time())))

def main():


    #if len(sys.argv) < 2:
    #    exit()

    #print(sys.argv[0])
    #print(sys.argv[1])

    with open("userlist.txt") as f:
        content = f.readlines()
    userList=[x.strip() for x in content]
    print(userList);
    collectTweet(userList)



main()