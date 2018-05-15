# coding: utf-8
game_done = False
p_hand = '114514'
c_hand = '1919'
def init_cards():

    print 'emm...'

def player_turn():
    print '我的回合，抽牌！'

def computer_turn():
    print '所累瓦多卡纳'

# 以上几行的定义不属于书上写的主程序，只是为了不想让程序报错
init_cards()
while not game_done: # while 在 后面的值为True时开始循环
    blocked = 0 # 这个变量是衡量一方玩家是否能继续出牌，如果有一方出不了牌了，这个值就+1
    player_turn() # 这个是玩家回合的函数，未写
    if len(p_hand) == 0: # p_hand是 玩家手牌数
        game_done = True
        print
        print 'you win!'

    if not game_done:
        computer_turn() # 这个是电脑回合的函数，未写

    if len(c_hand) == 0:
        game_done = True
        print
        print 'you lose!'

    if blocked >= 2: # 双方都出不了牌了
        game_done == True
        print '平局'
