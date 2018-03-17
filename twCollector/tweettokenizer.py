#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk.tokenize import TweetTokenizer
from nltk.tokenize import RegexpTokenizer


class TwitterTokenizer:

    def __init__(self, doc_generator):
        self.doc_generator = doc_generator
        self.tokenizer = RegexpTokenizer(r'\w+')



    def __iter__(self):
        for doc in self.doc_generator:
            yield (self.tokenizer.tokenize(doc["text"]),doc["text"])


