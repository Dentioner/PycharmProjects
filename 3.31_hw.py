#coding:utf-8
'''list=[]
s = '2'
for i in range(1,101):
    if i%2==0 and i%3==0 and i%5==0:
        list.append(i)

print(list)
num = 0

while num<len(list)-1:
    s= s+';'+str(list[num+1])
    num+=1
print(s)'''

print(';'.join([str(i) for i in range(1,101) if i%2==0 and i%3==0 and i%5==0]))

