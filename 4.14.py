# coding: utf-8
letter = ['y', 'w', 'w', 'u', 'y', 'i']

# 以下两步不能写成 print(letter.sort)，要分步完成
# letter.sort()
# print(letter)

# letter.reverse()
# print(letter) 这两行和下面的两行一样
# letter.sort(reverse= True)
# print(letter)

# new = letter
# new2 = letter[:]
# letter.reverse()
# print(new)
# print(new2)
# 这是因为new只是给那个列表增加了一个名字而已，如果要复制一个列表，就要用new2的方式

# new = sorted(letter)
# print(letter)
# print(new)
# sorted 函数可以创建一个副本，使得排序不改变letter的内容

letter_standard = ('y', 'w', 'w', 'u', 'y', 'i')
# 用圆括号创建的叫做元组tuple 这个东西不能被修改
