# coding: utf-8
from cards import PokerCards
import random
deck = []

hand  = []
for i in range(5):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)
# 以上为抽排
#以下为出牌
print '现在你的手牌如下所示：'
print hand #向玩家展示其拥有的手牌，并让玩家决定出哪张
chosen_number = raw_input('准备出哪张？1,2,3,4,5?不出而要抽牌的话，请输入0')
chosen_number = int(chosen_number)
if chosen_number == 0:# 这表示抽牌的程序
    new_card = random.choice(deck)
    hand.append(new_card)
    deck.remove(new_card)
else:
    chosen_number -= 1
    chosen_card = hand[chosen_number]
    hand.remove(chosen_card)
    up_card = chosen_card.ShortName # upcard 是明牌，展示自己出的牌
    print '你出了'+ up_card

