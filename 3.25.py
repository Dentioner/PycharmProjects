#coding: utf-8
import re
num = []
i = 0
for a in range(0,100):
    num.append(a)

f = open('num.txt','w')
#try:
#for p in range(0,10000):
while i < 100:
    f.write(str(num[i]))
#except:
    #print('rua')
    i+=1
f.close()
print('ok')
book= open('num.txt')
out = book.read()
m = re.findall('\d+',out)
if m:
    print(m)
