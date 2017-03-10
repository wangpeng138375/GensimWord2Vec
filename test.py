# encoding=utf-8
'''
Created on 2017-03-10
@author: user
'''
import gensim
import os
from gensim.models import word2vec
model = word2vec.Word2Vec.load('w2vmodel')


result = model.most_similar(positive=['中'], topn = 50)

for item in result:
    print('   "' + item[0] + '"  相似度: ' + str(item[1]))