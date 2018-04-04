#coding:utf-8
'''def func(a,b,c):
    return a+b+c
print func(1,2,3)'''

"""func = lambda a,b,c: a+b+c#格式：lambda 参数 ：表达式

print(func(1,2,3))
"""

def fn(x):
    return lambda y:x+y#返回值不是一个数值，而是一个lambda函数
a = fn(2)#相当于 a= lambda y : 2+y
print(a(3))
