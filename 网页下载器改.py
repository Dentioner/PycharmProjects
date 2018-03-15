#coding:utf-8
import urllib2
print('下载哪个网页？\n')
target = raw_input()
web = urllib2.urlopen('http://www.%s'%target,'w')
content = web.read()

name = raw_input('给网页起个名字\n')
f = open('%s.html'%name,'w')
f.write(content)
f.close()
print('好了')

