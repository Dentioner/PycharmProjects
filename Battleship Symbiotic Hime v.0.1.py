# coding: utf-8
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class dyson:
    def fire(self):
        print 'ナンドデモ…シズメテ…アゲル…'

mywife = dyson()
mywife.hp =  400
mywife.atk = random.randint(180,227)
mywife.defend = 160
mywife.torpedo = 0
mywife.miss = 30
mywife.air = 80
mywife.aircraft = 0
mywife.antisub = 0
mywife.speed = 'low'
mywife.search = 70
mywife.range = 'long'
mywife.luck = 40
mywife.item = ['16inch三连装炮', '16inch三连装炮', '12.5inch连装副炮', '水上雷达Mark.II']


mission = raw_input('What do you want to do?\nHearing her voice?')
if mission == 'yes':
    mywife.fire()
else:
    print('guna')



#mission2 =
# raw_input('So which data do you want to see?
# \nHere are the items:\n
# hp, atk, defend, torpedo, miss, air, aircraft, antisub, speed, search, range, luck, item')
# if mission2 == 'hp':
#     print
