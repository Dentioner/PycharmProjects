# coding: utf-8
import datetime
import time
quote = 'Life is a journey. What we should care about is not where it\'s headed but what we see and how we feel.'
quote2 = '这是一个考验，来自过去的考验，人的成长，就是战胜自己不成熟的过去。'
print '弱智手速测试ver.1.0'
print '准备...'
time.sleep(3)
print '开始'
print quote2
start = datetime.datetime.now()
you = raw_input('>')
end = datetime.datetime.now()
final = end - start
final_time = final.seconds + final.microseconds/float(10**6)
wps = float(len(you))/final_time
print '总耗时：%f秒'%final_time
print '速度：%f个/秒'%wps

if you == quote2:
    print 'perfect'
else:
    print 'not so bad'
