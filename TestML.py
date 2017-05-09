# -*- coding: utf-8 -*-
'''
Created on 2017年3月6日

@author: didi
'''
import unittest
from nltk.probability import ConditionalFreqDist
from nltk.tokenize import word_tokenize
import pickle as pk

import pickle
import itertools
import sklearn
import os
from random import shuffle

from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist
from nltk.classify.scikitlearn import SklearnClassifier

from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer 

def _testFreqCondition():
    s="中国"
    #print(s.decode('utf-8').encode('utf-8'))
    sent = "the the the dog dog some other words that we do not care about"
    cfdist = ConditionalFreqDist()
    for word in word_tokenize(sent):
        #print word
        condition = len(word)
        #print condition
        cfdist[condition][word] += 1
        
    print cfdist.conditions()
    for its in cfdist.items():
        print its
        
    cfdist = ConditionalFreqDist((len(word), word) for word in word_tokenize(sent))  
    print cfdist
    #print cfdist[2]
    print cfdist[3].freq('the')
    
def _testReadFile():
    f=open('/Users/didi/Documents/t.txt','r')
    cty=[]
    for fl in f:
        print fl    
    for cy in cty:
        print cy
    pkl_file = file('/Users/didi/Documents/t.txt','wb')
    
    f.close()
def _testEmotion():
    pos_review = pickle.load(open('/E/data/pos_review.pkl','r'))
    neg_review = pickle.load(open('/E/data/neg_review.pkl','r'))
    
    #第二步，使积极文本的数量和消极文本的数量一样。
    shuffle(pos_review) #把积极文本的排列随机化
    size = int(len(pos_review)/2 - 500)
    pos = pos_review[:size]
    neg = neg_review
    print "正样本数量：",len(pos)
    print "负样本数量：",len(neg)
    
    vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频  
    transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值  
    tfidf=transformer.fit_transform(vectorizer.fit_transform(neg+pos))
    print tfidf
    word=vectorizer.get_feature_names()#获取词袋模型中的所有词语 
    print len(word)
    for w in word:
        #print w
        pass
    weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重  
    print weight 
    for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重  
        print "-------这里输出第",i,"类文本的词语tf-idf权重------"  
        for j in range(len(word)):  
            if weight[i][j]>0.2:
                print word[j],weight[i][j]
                
def _testDict():
    words=["acb","bcd","efg"]
    tp=("我是","B")
    #print len(tp[0]),len(tp[1])
    dt={}
    for word in words:
        dt[word]=True
        #return dict([(word,True)])
    #return dt,len(tp[0]),len(tp[1])
    return dict([(word,True) for word in words ]),dt

class Tool():
    name="www"
    @staticmethod
    def getName(self):
        print "test....."    
    def setName(self):
        print "set"
    
if __name__ == '__main__':
    #_testClass()
    #_testFreqCondition()
    #_testReadFile()
    #_testEmotion()
    #print _testDict()
    tool=Tool()
    tool.getName("sss")

    tool.setName()