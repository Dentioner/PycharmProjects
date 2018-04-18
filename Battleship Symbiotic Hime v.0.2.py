# coding: utf-8
import random


class DysonWife:
    name = 'Battleship Symbiotic Hime'
    attack_voice = 'ナンドデモ…シズメテ…アゲル…'
    def voice(self):
        print('ナンドデモ…シズメテ…アゲル…')

    def __init__(self):
        self.hp = 400
        self.atk = random.randint(180, 227)
        self.defend = 160
        self.torpedo = 0
        self.miss = 30
        self.air = 80
        self.aircraft = 0
        self.antisub = 0
        self.speed = 'low'
        self.search = 70
        self.range = 'long'
        self.luck = 40
        self.item = ['16inch三连装炮', '16inch三连装炮', '12.5inch连装副炮', '水上雷达Mark.II']


print 'version 0.2'
mywife = DysonWife()

# Here are the v.0.1 code
# mywife.hp = 400
# mywife.atk = random.randint(180, 227)
# mywife.defend = 160
# mywife.torpedo = 0
# mywife.miss = 30
# mywife.air = 80
# mywife.aircraft = 0
# mywife.antisub = 0
# mywife.speed = 'low'
# mywife.search = 70
# mywife.range = 'long'
# mywife.luck = 40
# mywife.item = ['16inch三连装炮', '16inch三连装炮', '12.5inch连装副炮', '水上雷达Mark.II']
n = mywife.name
v = mywife.attack_voice

mission = raw_input('What do you want to do?\nHearing her voice?')
if mission == 'yes':
    mywife.voice()
    txt = []
    txt.append([n, v])
    a = open('hime.txt', 'w')
    for i in txt:
        a.writelines(i)
    a.close()
else:
    print('guna')
