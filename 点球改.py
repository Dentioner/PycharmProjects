#coding=utf-8
from random import choice
player = 0
pc = 0
direction = ['left'   , 'center' , 'right']
i=1
while i < 6 :
    print('第%d回合，你先攻')%(i)
    print('猜猜看?')
    print(direction)
    you= raw_input()
    com=choice(direction)
    print('你选择了%s，对面选择了%s')%(you,com)
    if you != com:
        print('还行')
        player+=1
    else:
        print('丢人')

    print('比分：%d(你)-%d(对面)\n')%(player,pc)
    i+=1
    print('第%d回合，你防守')%(i)
    print('猜猜看?')
    print(direction)
    you= raw_input()
    com=choice(direction)
    print('你选择了%s，对面选择了%s')%(you,com)
    if you!= com:
        print('丢人')
        pc+=1
    else:
        print('还行')
    print('比分：%d(你)-%d(对面)\n')%(player,pc)
    i+=1
print('完了')
