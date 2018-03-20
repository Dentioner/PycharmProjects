#coding:utf-8
a= 'heaven'
b = 'hell'
c = True and a or b
print(c)
d = False and a or b
print(d)
#在 'bool' and a or b中
# 当bool为真时，输出为a；否则为b
e = int(raw_input())
print e>0 and '+' or '-'
f = ''
g = True and f or b
h = (True and [f] or [b])[0]
print(g)
print(h)
