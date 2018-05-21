# coding: utf-8
# 已经录入

finally_done = False
game_done = False
p_win = 0
c_win = 0
ping = 0

while not finally_done:

    while not game_done:
        p_score = 0
        c_score = 0
        init_cards()# 建立一副牌，以及玩家和电脑抽牌的函数？也就是洗牌
        blocked = 0
        # if len(hand) > 0:
        player_turn()

        if len(hand) == 0:
            print '你赢了'
            game_done = True
            p_win += 1

        else:
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

        else:
            finally_done = True

    print '游戏结束，最后比分为%d:%d'%(p_win, c_win)

    # 两个布尔指标，一个用来判断是否继续游戏，一个判断每一盘是否结束
    # 表示出得分
    # 考虑平局
    # 每一盘结束打印至此的分数
    # 最终结束打印最后分数

