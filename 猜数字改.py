#coding:utf-8
f = open('game.txt')
score = f.read().split()
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
#以上是读取游戏数据
if game_times > 0:
    avg_times = float(total_times)/game_times
else:
    avg_times = 0
f.close()

#猜数字部分
print('★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
print('★你已经玩了%d次了★最少%d次猜出答案★平均猜了%.5f次★')%(game_times,min_times,avg_times)
print('★★★★★★★★★★★★★★★★★★★★★★★★★★★★')
print('猜猜看数字是啥？')

from random import randint
answer = randint(1,5)
you = input()
times = 1 #本回合游戏次数

while answer != you:
    print('ん？')
    print('不对')

    if answer > you:
        print('太小了')
    else:
        print('太大了')
    times+=1
    you = input()

#记录数据部分




if min_times == 0:
    min_times = times

if game_times == 0 or times < min_times:
    print('惊了，新记录%d次还行')%times
    min_times = times

total_times += times
game_times +=1


print('还行')
print('★★★★★★★★★★★★★')
print('★★本次用的次数为%d次★★' ) % times
print('★已累计在你游上玩了%d次★' ) % game_times
print('★★★★★★★★★★★★★')
f=open('game.txt','w')
data = '%d %d %d'%(game_times,min_times,total_times)
f.write(data)
f.close()
