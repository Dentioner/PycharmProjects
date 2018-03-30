#coding: utf-8
import cPickle#c语言版的pickle，比pickle更快，下面会混用这两个包

import pickle
a =1551
b = 'guna'
c = True
f= file('data_kai.txt','w')
cPickle.dump(a,f,True)#使用参数True会使得dump函数将此字符串以二进制的形式存储
pickle.dump(b,f)
pickle.dump(c,f)

f.close()
print('done')

g= file('data_kai.txt')#注意 在之前的教程里面这里用的是open函数，可以参见3.30对比.py
x= cPickle.load(g)
y= cPickle.load(g)
print('test......')#在这个中间打断，下次的pickleload还是会接着进行
z = pickle.load(g)#这个会依次读取下一行，如果只写一遍pickle.load，那么只会输出1551，如果写了四遍pickle.load，那么会报错，因为文件本来只有三行

print(x,y,z)


g.close()
