#coding:utf-8
a= raw_input()
try:
    f = file(a)
    print('file successfully opened')
    print('here are the words:\n')
    b=f.read()
    print(b)
    f.close()
except:
    print('file failed to be opened')
    print('this file may not exist')
print('Done')
