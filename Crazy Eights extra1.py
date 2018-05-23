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
