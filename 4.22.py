# coding: utf-8
class tri():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def GetS(self):
        s = self.width*self.height/2
        return s

class sqr:
    def __init__(self, length):
        self.length = length

    def GetS(self):
        s = self.length*self.length
        return s

a = tri(1,2)
b = sqr(2)

print a.GetS()
print b.GetS()
