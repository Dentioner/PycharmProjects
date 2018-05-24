# coding: utf-8
#这游戏就是UNO
import random
import time
deck = []
hand = []
c_hand = []
finally_done = False
game_done = False
p_win = 0
c_win = 0
ping = 0
cishu = 0

def init_cards():
    global deck, hand, c_hand, up_card, active_symbol
    from cards import PokerCards

    # 为牌组重新赋值，由于8最大
    deck = []
    for flower in range(1, 5):
        for num in range(1, 15):
            new_card = PokerCards(flower, num)
            if new_card.number == 8:
                new_card.value =50
            deck.append(new_card)

    for i in range(5):
        card = random.choice(deck)
        hand.append(card)
        deck.remove(card)

    for i in range(5):
        card = random.choice(deck)
        c_hand.append(card)
        deck.remove(card)

    up_card = random.choice(deck)
    active_symbol = up_card.symbol
    deck.remove(up_card)

def get_new_symbol():
    global active_symbol
    got_symbol = False
    flower_database = ['♠', '♥', '♣', '♦']

    while not got_symbol:
        choice = raw_input('请选择你想要的花色，按照顺序为♠，♥，♣，♦，输入1,2,3,4')
        try:
            if 1 <= int(choice) <= 4:
                choice = int(choice) - 1
                active_symbol = flower_database[choice]
                got_symbol = True

            else:
                print '输入不合法，请重试'

        except:
             print '输入不合法，请重试'

    print '玩家选择了' + active_symbol + '作为最新的花色'

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
    c_hand.remove(up_card)
    print '电脑打出了'+ up_card.ShortName
    print '电脑选择了花色'+ active_symbol


def player_turn():
    # import random
    global hand, up_card, active_symbol, deck, blocked, flower_choice, flower_database
    valid_play = False
    # is_eight = False

    print '\n现在你的手牌如下所示：'
    for ShouPai in hand:
        print ShouPai.ShortName,  # 向玩家展示其拥有的手牌，并让玩家决定出哪张
    print '现在场上的牌为' + up_card.ShortName  # 提醒玩家，上一张牌是什么，好让他对着出自己的牌
    # print 'test===='+ active_symbol
    # print 'test===='+ up_card.number
    if up_card.number == '8':
        if cishu > 1:
            print '由于场上的牌为8，指定的花色为' + active_symbol # 表示对方指定的花色


    # 下面的出牌代码块很可能会被block4里面的代码替代

    while not valid_play:
        try:
            chosen_number = raw_input('准备出哪张？1,2,3,...?不出而要抽牌的话，请输入0')
            chosen_number = int(chosen_number)
            if chosen_number == 0:  # 这表示抽牌的程序
                if len(deck) > 0:
                    new_card = random.choice(deck)
                    print '你抽了'+ new_card.ShortName
                    hand.append(new_card)
                    deck.remove(new_card)

                else:
                    print '牌组已空'
                    blocked += 1  # 这一个if块 是为了检测是否还有牌可以抽，否则就判定为一方玩家无法行动了
                # break
                return

            else:
                chosen_number -= 1
                chosen_card = hand[chosen_number]

                # if chosen_card.number == '8':
                #
                #     get_new_symbol()

                #     valid_play = True
                # # block5里面有一个函数会替代这个选花色的内容
                #     flower_choice = raw_input('请选择你想要的花色，按照顺序为♠，♥，♣，♦，输入1,2,3,4')
                #     flower_choice = int(flower_choice) -1
                #     active_symbol = flower_database[flower_choice]
                #
                #     # is_eight = True


                if chosen_card.symbol == active_symbol:

                    valid_play = True
                    active_symbol = chosen_card.symbol  # active_card 用来表示出的牌的花色

                elif chosen_card.number == up_card.number:
                    valid_play = True

                if not valid_play:
                    print '不是合法的出牌'
            if chosen_card.number== '8' and valid_play :

                get_new_symbol()

                print 'test==='+ active_symbol
        except:
            print '不是合法的出牌'


    hand.remove(chosen_card)
    up_card = chosen_card  # up_card 是明牌，展示自己出的牌来作为对方将要参考的牌
    if up_card.number != '8':
        active_symbol = up_card.symbol
    print '你出了' + up_card.ShortName


def computer_turn():
    import random
    global c_hand, active_symbol, up_card, deck, block, ready_card
    option = []
    # flower_database = ['♠', '♥', '♣', '♦']

    for card in c_hand:
        if card.number == '8':
            ready_card = card
            print 'test==='
            get_new_symbol_for_computer()


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
            for card in c_hand:
                if card.symbol == active_symbol:
                    option.append(card)

                elif card.number == up_card.number:
                    option.append(card)
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
                print '电脑出了'+ up_card.ShortName

                # print 'mark5'
                c_hand.remove(up_card)
                print '电脑手中还有%d张牌'%len(c_hand)
                return
                # print 'mark6'
            elif len(deck) > 0:
                new_card = random.choice(deck)
                c_hand.append(new_card)
                print '电脑摸了一张牌'
                print '电脑手中还有%d张牌'%len(c_hand)
                return

            else:
                block += 1
                print '电脑动不了了'
                print '电脑手中还有%d张牌'%len(c_hand)

    print '电脑手中还有%d张牌'%len(c_hand)

print '★★★★★★★★★★★'
print '★Crazy Eights ver1.0★'
print '★★★★★★★★★★★'

while not finally_done:
    print '============================================================================================================================='
    init_cards()# 建立一副牌，以及玩家和电脑抽牌的函数？也就是洗牌
    game_done = False
    while not game_done:
        p_score = 0
        c_score = 0
        cishu += 1
        blocked = 0
        # if len(hand) > 0:
        player_turn()

        if len(hand) == 0:
            print '你赢了'
            game_done = True
            p_win += 1

        else:
            time.sleep(2)
            print '====='+ active_symbol
            computer_turn()


            if len(c_hand) == 0:
                print '你输了'
                game_done = True
                c_win += 1

            elif blocked == 2:
                print '破游戏玩不下去了'
                ping += 1
                game_done = True

    print '双方得分如下'
    for card in hand:
        c_score += card.value

    for card in c_hand:
        p_score += card.value

    print '玩家得分为%d'%p_score
    print '电脑得分为%d'%c_score

    print '至此双方比分为%d:%d'%(p_win, c_win)

    a = raw_input('\n还要来吗？（Y/N）')

    if a.lower() == 'y':
        finally_done = False
        hand = []
        c_hand = []

    else:
        finally_done = True

print '游戏结束，最后比分为%d:%d'%(p_win, c_win)

    # 两个布尔指标，一个用来判断是否继续游戏，一个判断每一盘是否结束
    # 表示出得分
    # 考虑平局
    # 每一盘结束打印至此的分数
    # 最终结束打印最后分数




# 做一个出8的if
# 选择花色的规则是统计手牌里面花色最多的那个花色
# 如果能选花色，选完就return
# 如果出的不是8，就先统计哪些牌能出，把他们装到option里面
# 在option中找出价值最大的那张卡
# 否则抽牌或block加1

# 5.21 bug：
# 1. 选择出牌的时候，之间按enter键，会报错   (ok)
# 2. 选择出牌的时候，如果选择的数字超过手牌数，会报错 (ok)
# 3. 玩家回合结束的时候，upcard没有改变
# 4. 第二轮的时候，出不了同花色的牌，其实是当前upcard显示错误了
# 5. 抽完牌，回合没结束 （ok）
# 6. 出8的时候没出现选花色的模块

# 5.22bug:
# 电脑方的问题比较多。重写电脑方的函数。先判断手牌里面是否有8，如果有，执行一个单独的出8的程序，在extra1里面，还没写的
# 如果没有8，再执行下面的步骤
# 电脑的问题就是，在玩家出8之后，选了花色，但是电脑仍按照出的8的花色来出，而不是新制定的花色

# 5.23bug
# 1. 如果一开场的牌为8，就不要再说“指定的花色”了。 ok
# 2. 电脑绝杀牌为8，就不要让它再选花色了
# 3. 似乎电脑没有执行选花色的函数，注意一下
# 4. 玩家在改花色的时候电脑还能按照原花色出牌  ok



