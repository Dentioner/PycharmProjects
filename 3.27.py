#coding:utf-8
import random
import math
a = random.random()#这个的括号里面不要加东西，它只能生成一个0.几的小数
list = [1,2,3,4]
b = random.shuffle(list)#这里其实只要写成random.shuffle（list）就可以了，不要“b=”
print(list)#注意这里如果print b的话，输出的是none。因为shuffle这个函数直接把list里面的东西改了，b没有意义


