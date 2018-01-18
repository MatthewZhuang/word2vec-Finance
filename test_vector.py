#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
 @description:

 @Time       : 18/1/5 上午1:10
 @Author     : guomianzhuang
"""
import logging
import os
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
# inp = "/Users/Matthew/Documents/workspace/NER-Master-zhuang/word2vec/wiki.zh.model"
# outp = "/Users/Matthew/Documents/workspace/NER-Master-zhuang/word2vec/wiki.zh.vec"
inp = "/Users/Matthew/Documents/workspace/NER-Master-zhuang/word2vec/finance.model"
outp = "/Users/Matthew/Documents/workspace/NER-Master-zhuang/word2vec/finance.vec"


def save_vector():
    model = Word2Vec.load(inp)
    model.wv.save_word2vec_format(outp, binary=False)


def test_model():
    model = Word2Vec.load(inp)
    rs = model.most_similar(u"人工智能")
    for e in rs:
        print(e[0], e[1])


if __name__ == '__main__':
    test_model()
    # save_vector()
