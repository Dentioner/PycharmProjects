# coding: utf-8
class GameObject():
    def __init__(self, name):
        self.name = name

    def PickUp(self):
        pass
    # pass的作用是跳过这一块代码

class Coin(GameObject): #这么写表示，coin类是GameObject的子类
    def __init__(self, value):
        GameObject.__init__(self)
        self.value = value

    def Spend(self, buyer, seller):
        pass


print 'OJBK'
