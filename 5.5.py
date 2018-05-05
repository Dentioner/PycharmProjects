# coding: utf-8
import random
import time

b = 0
c = 1
a = [1, 2, 3, 4, 5, 6]
i = 0
start = time.time()
while b !=c:
    b = random.choice(a)
    c = random.randint(1, 7)

    i +=1
    print 'round %d'%i

end = time.time()
print 'finish'
cost = end - start
print 'you took %.f seconds to finish it.'%cost
print(start, end)

# a = time.time()
# print a
# time.sleep(2)
# b = time.time()
# print b
# print b-a
