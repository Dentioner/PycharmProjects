# coding: utf-8
file = open('5.1.txt', 'r')

i = 0
while i <10:
    print file.readline()
    i+=1

file.seek(1)
print file.readline()

