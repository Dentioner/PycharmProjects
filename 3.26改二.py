#coding:utf-8
import  re
#a = raw_input('请输入114.514')
#m= re.findall('\d+\.\d+',a)
#if m :
   # print(m)
#else:
   # print('guna')
i=0
a = ['(021)88776543',  '010-55667890','02584453362','0571 66345673','(02188776543','11451419191551801']
for ai in a:
#首先，（有特殊含义，为了找到（，在前面加上\；？表示这个（是可有可无的；0\d{2,3}表示区号；[) -]?表示在这之后可能跟的是')',' ','-',或者什么都没跟
   # m = re.findall('\(?0\d{2,3}[) -]?\d{7,8}',a[i])
    m =re.findall('\(0\d{2,3}\)\d{7,8}|0\d{2,3}[ -]?\d{7,8}|\d+',a[i])
# m = re.findall('[()\d]{2,5}[\s\w-]{1}\d{7,8}',a[i])
    print(m)

    i+=1
