#coding:utf-8
import time
ans = raw_input('Are you ready?')
if ans == 'yes':
    startnum = raw_input('How many seconds do you need?')
    startnum = int(startnum)
    start = time.time()
    print('buffering...')
    for i in range(startnum,-1,-1):

        time.sleep(1)
        print(i)


    print('counting finished')
else:
    print('rua')
end = time.time()
cost = end-start
print('This program took about %f seconds to count down')%cost
