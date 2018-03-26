#coding:utf-8
import  re
#a = raw_input('请输入114.514')
#m= re.findall('\d+\.\d+',a)
#if m :
   # print(m)
#else:
   # print('guna')
i=0
a = ['(021)88776543',  '010-55667890','02584453362','0571 66345673','0743 4727051','1551','(02188776543']
for ai in a:

    m = re.findall('[()\d]{2,5}[\s\w-]{1}\d{7,8}',a[i])
    print(m)

    i+=1

