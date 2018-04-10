#coding:utf-8
a= raw_input('多大的乘法表？')
a= int(a)
#原版乘法表
# for i in range(1,10):
#     mult = a*i
#     print('%dx%d=%d')%(a,i,mult)

#while版乘法表
# i=0
# while i < 9:
#     i+=1
#     mult = a*i
#     print('%dx%d=%d')%(a,i,mult)

for i in range(1,a+1):
    for j in range(1, i+1):
        mult = i*j
        print('%dx%d=%d')%(i,j,mult),
    print('\n')
