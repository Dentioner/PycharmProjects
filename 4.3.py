#coding:utf-8
def printall(**kargs):
    for k in kargs:#kargs是字典
        print k,':',kargs[k]

printall(a=1,b=2,c=3)
printall(x=4,y=5)

def func(x,y=5,*a,**b):
    print x,y,a,b

func(1)
func(1,2)
func(1,2,3)
func(1,2,3,4)
func(x=1)
func(x=1,y=1)
func(x=1,y=1,a=1)
func(x=1,y=1,a=1,b=1)
func(1,y=1)
func(1,2,3,4,a=1)
func(1,2,3,4,k=1,t=2,o=3)


