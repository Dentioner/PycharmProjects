#coding:utf-8

#method 1
'''l1=[1,2,3,4,5,6]
l2=[]
for i in l1:
    l2.append(i*2)
print(l2)
'''

#method 2
# l1 = [1,2,3,4,5,6]
# l2 = [i*2 for i in l1]
# print(l2)



#method 3
# l1= [1,2,3,4,5,6]
# def func(x):
#     return x*2
# l2 = map(func, l1)
# print(l2)
# l3=(1,2,3,4,5,6)
# l4 = map(lambda x:x*2, l3)
# print(l4)
# print(type(l1),type(l2),type(l3),type(l4))
# lsum = map(lambda x,y:x+y, l1,l3)
# print(lsum)
# print(type(lsum))

l1 = [1,2,3,4,5,6]
l2 = [1,3,5,7,9,11]
l3 = map(None, l1)
print(l3)
l4 = map(None, l1, l2)
print(l4)
print(type(l4))
print(type(l4[1]))
print(type(l4[1][1]))
