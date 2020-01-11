#coding=utf-8
from random import choice
score=[0,0]
direction=['left','right','center']
def ball():
    print('你的回合')
    print('选哪一边')
    print('left,right,or center?')
    #you = raw_input()
    you = input()

    com = choice(direction)
    print('你选择了%s')%you
    print('对方选择了%s')%com
    if you != com:
        print('还行')
        score[0]+=1
    else:
        print('丢人')
    print('现在比分\n %d:%d\n')%(score[0],score[1])
    print('对方回合')
    print('选哪一边')
    print('left,right,or center?')
    #you = raw_input()
    you = input()
    com = choice(direction)
    print('你选择了%s')%you
    print('对方选择了%s')%com
    if you != com:
        print('丢人')
        score[1]+=1
    else:
        print('还行')
    print('现在比分\n %d:%d\n')%(score[0],score[1])

for i in range(3):
    print('第%d回合')%(i+1)
    ball()
while (score[0]==score[1]):
    print('加时赛还行')
    i+=1
    print('第%d回合')%(i+1)
    ball()

if score[0] < score[1]:
    print('真鸡儿丢人，退群吧')
else:
    print('代打guna')

print('吃凉吧唧光速下播')


