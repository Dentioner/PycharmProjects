# coding: utf-8
file = open('poi.mp3', 'rb')
a = file.readlines()
a = str(a)

create = open('newpoi.mp3', 'w')
create.writelines(a)

file.close()
create.close()

