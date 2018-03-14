#coding: utf-8
def hello(name = 'world'):
    print('hello '+name)

a = raw_input()
hello(a)#这个函数有参数a，正常工作
hello()#意思是，我这个函数没有参数，那么就会自动使用我在def里面设置的默认值
hello('jojo')#与第一个不同的是，这个函数直接把参数塞在括号里面了
