#coding:utf-8
import  random
list1=[random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]
list2=[i/2 for i in list1 if i%2==0]
'''for i in list1:
    if i%2==0:
        list2.append(i)'''
print(list1)
print(list2)
print('rua')
