# -*- coding:utf-8 -*-
import urllib2
import json
from  city import city
print('注意：只能直接复制city.py里面的乱码来查询城市')
name = raw_input('哪个城市？\n')

code = city.get(name)
if code:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' %code)
    content = urllib2.urlopen(url).read()
    print(content)
else:
    print('buzai,cnm')
