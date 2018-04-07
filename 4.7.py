#coding:utf-8
# sum = 0
# for i in xrange(1,101):#xrange与range不同，前者是一个list生成器
#     #可以看看print这两个，有什么区别
#     #循环的时候，xrange性能更好
#
#     sum+=i
# print(sum)
#
# print(xrange(1,5))
# print(range(1,5))

# #method1
# l1 = xrange(1,101)
# def add(x,y):
#     return x+y
# print reduce(add,l1)

#method2
l1 = xrange(1,101)
print reduce(lambda x,y:x+y, l1)
