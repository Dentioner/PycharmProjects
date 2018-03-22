#coding : utf-8
import math
print('========================unary quadratic equation calculator========================')
try:
    print('ax^2+bx+c=0')
    a = raw_input('a=')
    b= raw_input('b=')
    c= raw_input('c=')
    a= float(a)
    b=float(b)
    c=float(c)

    b2 = math.pow(b,2)
    delta = b2-4*a*c

    if delta > 0 :
        root = math.sqrt(delta)
        x1= ((-b + root)/2*a)
        x2= ((-b - root)/2*a)
        print('x1=%.f\nx2=%.f')%(x1,x2)

    elif delta == 0:
        root = math.sqrt(delta)
        x = ((-b + root)/2*a)
        print('x1=x2=%.f')%x
    else:
        print('no solution')

    print('rua')

except:
    print('cnm,guna')
