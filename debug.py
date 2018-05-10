# coding: utf-8
class PokerCards:
    def __init__(self, suit_id, rank_id):
        self.rank_id = rank_id
        self.suit_id = suit_id

# flower 是花色1,2,3,4，num是点数, value 是对应的分值
# symbol 是♠这些东西
# number是 A J K Q这些

        if self.rank_id == 1:
            self.rank = 'A'
            self.value = 1

        elif self.rank_id == 11:
            self.rank = 'J'
            self.value = 10

        elif self.rank_id == 12:
            self.rank = 'Q'
            self.value = 10

        elif self.rank_id == 13:
                    self.rank = 'K'
                    self.value = 10

        elif 2 <= self.rank_id <= 10:
                    self.rank = str(self.rank_id)
                    self.value = self.rank_id

        else:
            self.rank = 'RankError'
            self.suit = -1

        if self.suit_id == 1:
            self.suit = 'heitao'

        elif self.suit_id == 2:
            self.suit = 'hongtao'

        elif self.suit_id == 3:
            self.suit = 'meihua'

        elif self.suit_id == 4:
            self.suit = 'fangpian'

        else:
            self.suit = 'error'

        self.ShortName = self.rank[0] + self.suit[0]

        if self.rank == '10':
            self.ShortName = self.rank + self.suit[0]

        self.LongName = self.rank + 'of' + self.suit
