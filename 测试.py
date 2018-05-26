# coding: utf-8
from cards import PokerCards

deck = []
for flower in range(1, 5):
    for num in range(1, 14):
        new_card = PokerCards(flower, num)

        deck.append(new_card)

for card in deck:
    print card.ShortName
