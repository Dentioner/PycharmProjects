#coding:utf-8
#关于多玩家的思路：
#首先要新建一个空的字典，然后让玩家自己输入名字
#字典的格式为名字：成绩
#注意新玩家

print('目前只支持英文名')

f = open('multigame.txt')
everyone = f.readlines()#读取每个人的信息，分成一行一行


cast = {}#create a new dictionary
print('zaima?')
name = raw_input('你是哪个？')

for someone in everyone: #everyone的每一行，叫做someone
    s = someone.split() #someone 是含有 ‘姓名：成绩’ 的，用split将各个成绩以及姓名切分
    cast[s[0]] = s[1:] #这是字典的格式，字典名[索引名] = 索引对应的数据。s[0]是姓名，s1以后的就是成绩了

score = cast.get(name) #字典的get函数，查找输入的name对应的数据，name就是用raw input定义的

if score is None:#没找到就新建一个数据
    print('都8102年了还有新玩家？')
    score = [0,0,0]



#score = f.read().split() 这行数据就不要了，因为这个score获取数据的来源不同
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
print('=============================================用户“%s”============================================')%name
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

cast[name] = [str(game_times), str(min_times), str(total_times)]#更新cast里面的讯息
result = ''
for n in cast:
    someone = n + ' '+ ' '.join(cast[n])+'\n'
    #join函数的用法：比如','.join(‘abc’),函数会把字符串abc中的每个成员用‘，’分开，输出为‘a,b,c'
    result += someone


f=open('multigame.txt','w')
#data = '%d %d %d'%(game_times,min_times,total_times)
f.write(result)
f.close()
