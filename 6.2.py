# coding: utf-8
import datetime, os, pickle
first = True
if os.path.isfile('yuki.wife'):
    time_file = open('yuki.wife', 'r')
    time = pickle.load(time_file)
    print '上次打开时间为%s'%time
    time_file.close()
    first = False

exe = open('yuki.wife', 'r')
last = pickle.load(exe)
delta = datetime.datetime.now() - last
delta = delta.seconds + delta.microseconds/float(10**6)
print '你已经有%ss没打开过了'%delta
exe.close()
exe = open('yuki.wife', 'w')
pickle.dump(datetime.datetime.now(), exe)
exe.close()
if first:
    print '这是第一次记录'
