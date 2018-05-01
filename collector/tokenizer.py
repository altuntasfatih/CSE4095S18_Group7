#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from nltk.tokenize import TweetTokenizer
from nltk.tokenize import RegexpTokenizer


class WordTokenizer:

    def __init__(self, doc_generator,type):
        self.doc_generator = doc_generator
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.type=type;
            #0 is pure string
            #1 is tweet

    def __iter__(self):
        if self.type==1:
            for doc in self.doc_generator:
                yield (self.tokenizer.tokenize(doc["text"]),doc["text"])
        else:
                yield(self.tokenizer.tokenize(self.doc_generator),self.doc_generator)
