# coding: utf-8
# 这个是抽牌部分的一个示范代码块
import random
valid_play = True
deck = []
blocked = 0
p_hand = []
print '准备干啥?'
response = raw_input('Type a card to play or \'Draw\'to take a card:')
while not valid_play :
    selected_card = None
    while selected_card == None:
        if response.lower() == 'draw':
            valid_play = True
            if len(deck) > 0:  # 抽牌

                card = random.choice(deck)# 抽牌
                p_hand.append(card)# 抽牌
                deck.remove(card)# 抽牌
                print 'you drew', card.ShortName# 抽牌

            else:# 抽牌
                print 'no card'# 抽牌
                blocked += 1# 抽牌

            return
            # 抽完牌就回到主循环
        else:
            for card in p_hand:# 出牌
                if response.upper() == card.ShortName:# 出牌
                    selected_card = card# 出牌
            if selected_card == None:# 出牌
                response = raw_input('you do not have it. Try again:')# 出牌

    if selected_card.rank == '8':
        valid_play = True
        is_eight = True
    elif selected_card.symbol == active_symbol: # 判断出牌是否合法
        valid_play = True
    elif selected_card.number == up_card.number:
        valid_play = True

    if not valid_play:
        response = raw_input('try again')
