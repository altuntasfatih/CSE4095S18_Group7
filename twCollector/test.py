#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from twCollector.tweetcollector import TwitterAPI

from twCollector.constant import consumer_key,consumer_secret,access_token,access_token_secret

def collectTweet(userlist):

    tw = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)


    for uname in userlist:

        user_tweet_generator = tw.get_user_tweets(uname)

        for item in user_tweet_generator:
            print(item)



def main():

    with open("userlist.txt") as f:
        content = f.readlines()
    userList=[x.strip() for x in content]
    print(userList);
    collectTweet(userList)



main()