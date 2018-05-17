# coding: utf-8
import random
from cards import PokerCards

deck = []
for flower in range(1, 5):
    for num in range(1, 15):
        deck.append(PokerCards(flower, num))

hand = []
for i in range(5):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)

print
# for c in hand:
#     print c.ShortName, '=', c.LongName, 'value:', c.value
for c in hand:
    print c.symbol
