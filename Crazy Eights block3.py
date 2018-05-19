# coding: utf-8
from cards import PokerCards
import random
deck = []
blocked = 0
up_card = ''  # up_card 实际上不是字符串，是一个实例，但是这里就随便定义一下，不让系统报错就行
active_symbol = ''
hand = []
valid_play = False
flower_database = ['♠', '♥', '♣', '♦']

for i in range(5):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)
# 以上为抽排, 定义都是暂时的，下面的代码块才是重要的
# 以下为向玩家展示手牌
print '\n现在你的手牌如下所示：'
for ShouPai in hand:
    print ShouPai.ShortName,  # 向玩家展示其拥有的手牌，并让玩家决定出哪张
print '现在场上的牌为' + up_card.ShortName  # 提醒玩家，上一张牌是什么，好让他对着出自己的牌
if up_card.number == 8:
    print '由于对方出了8，他指定的花色为' + active_symbol # 表示对方指定的花色


# 下面的出牌代码块很可能会被block4里面的代码替代

while not valid_play:
    chosen_number = raw_input('准备出哪张？1,2,3,4,5?不出而要抽牌的话，请输入0')
    chosen_number = int(chosen_number)
    if chosen_number == 0:  # 这表示抽牌的程序
        if len(deck) > 0:
            new_card = random.choice(deck)
            print '你抽了'+ new_card.ShortName
            hand.append(new_card)
            deck.remove(new_card)

        else:
            print '牌组已空'
            blocked += 1  # 这一个if块 是为了检测是否还有牌可以抽，否则就判定为一方玩家无法行动了
        # break
        # return
    else:
        chosen_number -= 1
        chosen_card = hand[chosen_number]
        if chosen_card.number == 8:
            valid_play = True
        # block5里面有一个函数会替代这个选花色的内容
            flower_choice = raw_input('请选择你想要的花色，按照顺序为♠，♥，♣，♦，输入1,2,3,4')
            flower_choice = int(flower_choice) -1
            active_symbol = flower_database[flower_choice]

            # is_eight = True


        elif chosen_card.symbol == active_symbol:

            valid_play = True
            active_symbol = chosen_card.symbol  # active_card 用来表示出的牌的花色

        elif chosen_card.number == up_card.number:
            valid_play = True

        if not valid_play:
            print '不是合法的出牌'

hand.remove(chosen_card)
up_card = chosen_card  # up_card 是明牌，展示自己出的牌来作为对方将要参考的牌
print '你出了' + up_card.ShortName

# active_symbol = chosen_card.symbol  # active_card 用来表示出的牌的花色


# 本代码块的很多地方都没有设定检测非法输入的功能
# 需要写入一些while循环来保证游戏的正常进行
# 本代码块也没有设置好，出相同点数的选项判断，5.18为止，只是完成了对“出相同花色”的规则的判断
