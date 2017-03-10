# encoding=utf-8
'''
Created on 2017-03-10
@author: user
'''
import gensim
import os
'''
# 函数功能：读取文本，解决中文乱码问题
'''
def Read_data(path):

    sentences = []
    fid = open(path, 'r')

    for line in fid:
        line = line.strip().split()      # 以空格分开
        sentences.append(line)

    return sentences


'''
# 函数功能：读取文本，解决中文乱码问题，以及避免一次性引入所有的数据到内存造成内存爆满
'''
class MySentences(object):
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        for line in open(self.filename,'r'):
            yield line.strip().split()
sentences = MySentences('D:/语料库/筛选/30000_del_duplicateedSentence_30characterLengthofSentence.txt'.decode("utf8").encode("gbk"))
model = gensim.models.Word2Vec(sentences, min_count=0)
model.save('w2vmodel')