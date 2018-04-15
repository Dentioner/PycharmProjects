# coding:utf-8
number = raw_input('几个人？')
number = int(number)
lst = []
for i in range(number):
    add = raw_input('第%d个人的名字是?'%(i+1))
    lst.append(add)
lst.sort()
print '输入的名字是',lst

place = raw_input('想知道第几个名字？')
place = int(place)
print lst[place-1]

rep = raw_input('想换掉第几个？')
rep = int(rep)
lst[rep-1] = raw_input('换成啥？')
print lst
