import random
from cards import PokerCards

deck = []

for flower in range(1, 5):
    for num in range(1, 14):
        deck.append(PokerCards(flower, num))

hand = []

for cards in range(5):
    i = random.choice(deck)
    hand.append(i)
    deck.remove(i)


for ThisIsCard in hand:
    print ThisIsCard.ShortName
    print ThisIsCard
