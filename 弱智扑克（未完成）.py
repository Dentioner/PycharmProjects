# coding: utf-8
class PokerCards:
    def __init__(self, flower, num):
        self.flower = flower
        self.num = num

# flower 是花色1,2,3,4，num是点数, value 是对应的分值
# symbol 是♠这些东西
# number是 A J K Q这些

        if self.num == 1:
            self.number = 'A'
            self.value = 1

        elif self.num == 11:
            self.number = 'J'
            self.value = 10

        elif self.num == 12:
            self.number = 'Q'
            self.value = 10

        elif self.num == 13:
                    self.number = 'K'
                    self.value = 10

        elif 2 <= self.num <= 10:
                    self.number = str(self.num)
                    self.value = self.num

        else:
            print 'error'
