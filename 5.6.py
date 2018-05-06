# coding: utf-8
import random
# totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(1000):
#     dice_total = random.randint(2, 12)
#     totals[dice_total] += 1
#
# for i in range(2, 13):
#     print 'total', i, 'came up', totals[i], 'times'
# 以上是11面骰子

totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1000):
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    dice_total = die_1 + die_2
    totals[dice_total] += 1


for i in range(2, 13):
    print 'total', i, 'came up', totals[i], 'times'
# 以上是2个6面骰子
