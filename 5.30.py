# coding: utf-8
import datetime
a = datetime.datetime(2018, 5, 30, 15, 51, 55)
print a
print a.ctime()
print a.date()
print a.year
print a.day
print a.time()

b = a.date()
c = a.time()
d = datetime.datetime.combine(b, c)
print d
