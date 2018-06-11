# coding: utf-8
import random
import easygui
truth = random.choice(range(10))
easygui.msgbox('猜数字gui版——ver1.0', ok_button='继续')
you = 0
times = 0
while you != truth and times < 10:
    you = easygui.integerbox('你觉得数字是0~9中的哪个？')
    if not you:
        # easygui.msgbox('here')
        # print type(you)
        break
    if you < truth:
        easygui.msgbox('小了点')
    elif you > truth:
        easygui.msgbox('大了点')
    elif you == truth:
        easygui.msgbox('还行')
    times += 1

if you == truth:
    easygui.msgbox('过了')
else:
    easygui.msgbox('丢人')
