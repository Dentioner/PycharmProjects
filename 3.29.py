#coding : utf-8
import  random
a = 0
try:
    for i in range(5):
        b = random.choice(range(5))
        print('b=%f')%b
        a+= i/b
        print a
    print('Congratulations!')
except:
    print('Trash')
