import urllib
import urllib.request
import jieba
import jieba.posseg as pseg


jieba.load_userdict("./ai_dic.txt")
words = pseg.cut("1960年男子20公里冠军")

for word, flag in words:
    print('%s %s' % (word, flag))



