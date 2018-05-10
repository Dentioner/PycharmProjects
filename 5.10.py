# coding: utf-8
from debug import PokerCards
import random
deck = []
for suit_id in range(1, 5):

    for rank_id in range(1, 14):


        deck.append(PokerCards(suit_id, rank_id))


hand = []
for cards in range(5):
    a = random.choice(deck)
    hand.append(a)
    deck.remove(a)
print
for card in hand:
    print card.ShortName, '=', card.LongName

