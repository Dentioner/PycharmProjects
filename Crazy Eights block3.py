# coding: utf-8
from cards import PokerCards
import random
deck = []
up_card = ''  # up_card 实际上不是字符串，是一个实例，但是这里就随便定义一下，不让系统报错就行
active_symbol = ''
hand = []
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
chosen_number = raw_input('准备出哪张？1,2,3,4,5?不出而要抽牌的话，请输入0')
chosen_number = int(chosen_number)
if chosen_number == 0:  # 这表示抽牌的程序
    new_card = random.choice(deck)
    hand.append(new_card)
    deck.remove(new_card)
else:
    chosen_number -= 1
    chosen_card = hand[chosen_number]
    hand.remove(chosen_card)
    up_card = chosen_card  # up_card 是明牌，展示自己出的牌来作为对方将要参考的牌
    print '你出了' + up_card.ShortName

    active_symbol = chosen_card.symbol  # active_card 用来表示出的牌的花色
# 这里没有设计 考虑出8的情况，8可以自己选择花色
