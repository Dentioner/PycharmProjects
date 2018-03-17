# -*- coding:utf-8 -*-
a = open('citydata.txt')
b = open('citydata2.txt')
a1 = a.readlines()
b1 = b.readlines()
if a1 == b1:
    print('还行')
else:
    print('丢人')
