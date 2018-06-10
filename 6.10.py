# coding: utf-8
import easygui
# choice = easygui.enterbox('who is your waifu?', default='戦艦棲姫')
# msg = easygui.msgbox('your wife is '+ choice)
choice = easygui.integerbox('Type in a number < 99')
msg = easygui.msgbox('you entered '+ str(choice))
