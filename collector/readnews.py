#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collector.tokenizer import WordTokenizer
from collector.mongoutils import *
from collector.constant import ROOTPATH


import time
import os

directory={"root":ROOTPATH+"/news/",
           "dirs":{},
           }
def walkDirectory():
    for root, dirs, files in os.walk(ROOTPATH + "/news/"):

        if root == ROOTPATH + "/news/":
            for item in dirs:
                directory[item] = 'item'
        if len(files) != 0:
            directory['dirs'][root.split('/')[-1]]=files
def readFiles(dirs='dunya'):
    for file in directory['dirs'][dirs]:
        print(directory['root']+dirs+file)
        news=''
        with open(directory['root']+dirs+"/"+file, 'r') as myfile:
            news = myfile.read()
        tokenized_news_generator = WordTokenizer(news,0)
        mdb_writer = MongodbWriter(tokenized_news_generator)
        _count = mdb_writer.saveTokenizeNews(dirs);


def main():
    walkDirectory()
    readFiles()




main()



