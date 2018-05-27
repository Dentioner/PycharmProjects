# coding :utf-8
def get_new_symbol_for_computer():
    global c_hand, ready_card, up_card, active_symbol
    flower_statistic = [0, 0, 0, 0]
    #                    ['♠', '♥', '♣', '♦']
    flower_database = ['♠', '♥', '♣', '♦']

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

    up_card = ready_card
    active_symbol = flower_database[best_flower]
    c_hand.remove(card)
    print '电脑打出了'+ up_card.ShortName
    print '电脑选择了花色'+ active_symbol

def computer_turn():
    # import random
    global c_hand, active_symbol, up_card, deck, blocked, ready_card, c_blocked
    option = []
    # flower_database = ['♠', '♥', '♣', '♦']

    for card in c_hand:
        print card.ShortName
        # print 'test===c-hand=' + str(len(c_hand))
        if card.number =='8':
            print 'number is 8!'
        if card.number == '8' and str(len(c_hand)) != 1:
            ready_card = card
            print '进入选色函数了'
            get_new_symbol_for_computer()
            # print '在函数之后'

            # flower_statistic = [0, 0, 0, 0]
            #
            # #                    ['♠', '♥', '♣', '♦']
            # for card in c_hand:
            #     if card.symbol == '♠':
            #         flower_statistic[0] += 1
            #     elif card.symbol == '♥':
            #         flower_statistic[1] += 1
            #     elif card.symbol == '♣':
            #         flower_statistic[2] += 1
            #     elif card.symbol == '♦':
            #         flower_statistic[3] += 1
            #     # 统计四种花色在手牌中的个数
            #
            # best_flower = 0
            # if flower_statistic[1] > flower_statistic[0]:
            #     best_flower = 1
            #
            # elif flower_statistic[2] > flower_statistic[0]:
            #     best_flower = 2
            #
            # elif flower_statistic[3] > flower_statistic[0]:
            #     best_flower = 3
            #
            # active_symbol = flower_database[best_flower]
            # up_card = card
            # c_hand.remove(card)
            # print '电脑打出了'+ up_card.ShortName
            # print '电脑选择了花色'+ active_symbol
            return

        else:
            if card.symbol == active_symbol:
             option.append(card)

            elif card.number == up_card.number:
             option.append(card)

        # else:
        #     for card in c_hand:
        #         if card.symbol == active_symbol:
        #             option.append(card)
        #
        #         elif card.number == up_card.number:
        #             option.append(card)
# 把能出的牌放进option里面

    if len(option) > 0:
        before_up_card = option[0]
        # print 'mark1'
        for i in range(1, len(option)):
            if option[i].value > before_up_card.value:
                before_up_card = option[i]
                # print 'mark2,type%d'%i
            # print 'mark3'
        up_card = before_up_card
        # print 'mark4'
        active_symbol = up_card.symbol
        print '电脑出了' + up_card.ShortName

        # print 'mark5'
        c_hand.remove(up_card)
        print '电脑手中还有%d张牌' % len(c_hand)
        return
        # print 'mark6'
    elif len(deck) > 0:
        new_card = random.choice(deck)
        c_hand.append(new_card)
        deck.remove(new_card)
        print '电脑摸了一张牌'
        print '电脑手中还有%d张牌' % len(c_hand)
        return

    else:
        # blocked += 1
        c_blocked = True
        print '电脑动不了了'
        print '电脑手中还有%d张牌' % len(c_hand)
        return

    print '电脑手中还有%d张牌' % len(c_hand)
