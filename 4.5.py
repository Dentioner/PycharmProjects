#coding:utf-8

'''def func():
    global x
    print 'X in the beginning of func(x): ', x
    x=2
    print 'X in the end if func(x): ', x
#不用global的情况：

#def func(x)这里如果不用global，就要在括号里面先定义x
  #  print '...', x
    #x=2
  #  print '...', x

x = 50
func()
print 'X after calling func(x): ', x'''

def func():
    print 'X in the beginning is', x
    #x=2
    print 'X in the end is',x

x=50
func()
print 'X after calling is',x
y=2
func()
print(y)
