# coding: utf-8
#这游戏就是UNO
from cards import PokerCards

# 为牌组重新赋值，由于8最大
deck = []
for flower in range(1, 5):
    for num in range(1, 15):
        new_card = PokerCards(flower, num)
        if new_card.number == 8:
            new_card.value =50
        deck.append(new_card)

