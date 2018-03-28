#coding: utf-8
import time
start = time.time()
print('start at: %f')%start
for i in range(0,10):
    print(i)
    time.sleep(i)
end = time.time()
print('end at: %f')%end
print('total cost: %f')%(end-start)

