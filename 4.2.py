#coding:utf-8
def func(*seq):


    sum = 0
    for i in seq:
        sum+=i
    print(sum)

func(1,2,3)
'''
这里*是可以接受任意数量的参数
后面的func调用的时候，我想输入多少个数字相加都行'''
