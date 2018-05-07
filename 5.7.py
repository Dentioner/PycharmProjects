# coding: utf-8
from random import *
coin = ['up', 'down']
head = 0
TenHead = 0
for i in range(1000000):
    if choice(coin)== 'up':
        head += 1
        if head == 10:
            TenHead += 1
    else:
        head = 0


print TenHead
