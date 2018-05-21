# coding: utf-8
# 已经录入

def computer_turn():
    import random
    global c_hand, active_symbol, up_card, deck, block
    option = []
    flower_database = ['♠', '♥', '♣', '♦']

    for card in c_hand:
        if card.number == 8:
            flower_statistic = [0, 0, 0, 0]

            #                    ['♠', '♥', '♣', '♦']
            for card in c_hand:
                if card.symbol == '♠':
                    flower_statistic[0] += 1
                elif card.symbol == '♥':
                    flower_statistic[1] += 1
                elif card.symbol == '♣':
                    flower_statistic[2] += 1
                elif card.symbol == '♦':
                    flower_statistic[3] += 1
                # 统计四种花色在手牌中的个数

            best_flower = 0
            if flower_statistic[1] > flower_statistic[0]:
                best_flower = 1

            elif flower_statistic[2] > flower_statistic[0]:
                best_flower = 2

            elif flower_statistic[3] > flower_statistic[0]:
                best_flower = 3

            active_symbol = flower_database[best_flower]
            up_card = card
            c_hand.remove(card)
            print '电脑打出了'+ up_card.ShortName
            print '电脑选择了花色'+ active_symbol
            return
# 以上是对应出8的情况
        elif card.symbol == active_symbol:
            option.append(card)

        elif card.number == up_card.number:
            option.append(card)
# 把能出的牌放进option里面

    if len(option) > 0:
        before_up_card = option[0]
        for i in range(1, len(option)+1):
            if option[i].value > before_up_card.value:
                    before_up_card = option[i]

        up_card = before_up_card
        c_hand.remove(up_card)
        print '电脑出了'+ up_card.ShortName

    elif len(deck) > 0:
        new_card = random.choice(deck)
        c_hand.append(new_card)
        print '电脑摸了一张牌'

    else:
        block += 1
        print '电脑动不了了'

    print '电脑手中还有%d张牌'%len(c_hand)





# 做一个出8的if
# 选择花色的规则是统计手牌里面花色最多的那个花色
# 如果能选花色，选完就return
# 如果出的不是8，就先统计哪些牌能出，把他们装到option里面
# 在option中找出价值最大的那张卡
# 否则抽牌或block加1
