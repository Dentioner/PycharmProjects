# coding: utf-8
a = raw_input()
a = bool(a)
while not a:
    print a, type(a)
    a = raw_input()
    a = bool(a)
print 'end'

