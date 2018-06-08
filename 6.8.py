# coding: utf-8
import easygui
response = easygui.choicebox('What\'s your favorite waifu?', choices=['戦艦棲姫', '戦艦水鬼', '戦艦レ級'])
a = easygui.msgbox('You picked '+ response)
print response
print type(response)
print a
print type(a)
