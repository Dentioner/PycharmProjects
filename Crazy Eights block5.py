# coding: utf-8
# 已经录入

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

get_new_symbol()
