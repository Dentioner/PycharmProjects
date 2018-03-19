#coding: utf-8
class guna:
    pass #pass表示一个空的代码块

class Myclass:
    name = 'ywwuyi'
    def hello(self):
        print('guna,%s')%self.name

mc = Myclass()
print(mc)
print(mc.name)
mc.hello()
mc.name = 'wuyikoei'

print(mc.name)
#a =mc.hello()
#print(a)
#mc.hello()
mc.hello()
