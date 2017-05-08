#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
from nltk.probability import FreqDist,ConditionalFreqDist
from nltk.tokenize import word_tokenize

import json

movie_sim_mat={}
movie=movie_sim_mat
movie={"kk",0}
#movie.setdefault("k",0)

print("movie_sim_mat:",movie_sim_mat)

data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}
print(data['name'])

json_str = json.dumps(data)
 
#排序 
word_scores = {}
word_scores['w']=1
word_scores['c']=2
word_scores['l']=3
print word_scores
best_vals = sorted(word_scores.iteritems(), key=lambda (w, s): s, reverse=True)[:3]
#print 'best_vals:',best_vals
best_words = set([w for w, s in best_vals])
#print 'best_words:',best_words


#词频统计 
sent = "the the the dog dog some dog other words that we do not care about"
word_fd = FreqDist() #可统计所有词的词频
cond_word_fd = ConditionalFreqDist()
for word in word_tokenize(sent):
    condition = len(word)
    word_fd.inc(word)
    cond_word_fd[condition].inc(word)
    #print word,word_fd,cond_word_fd
    #print cond_word_fd['pos']
for word,cn in word_fd.iteritems():
    #print cfword,cn 
    print word,cn
for ws in word_fd.iteritems():
    #print cfword,cn 
    print ws    
print word_fd['dog'],cond_word_fd[3].N()
print cond_word_fd[3].freq('dog')

s=u"中国"
token = "，。！？：；"
print token
uu = open('d:/unicode.txt','w')
for t in token.decode('utf-8'):
    print t
    #uu.write(t.encode('utf-8'))
uu.write(token)
uu.close()
