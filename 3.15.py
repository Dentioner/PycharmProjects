# -*- coding:utf-8 -*-
import urllib2
import json
from  city import city
print('注意：只能直接复制city.py里面的乱码来查询城市')
cityname = raw_input('哪个城市？\n')

citycode = city.get(cityname)
if citycode:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' %citycode)
    content = urllib2.urlopen(url).read()
    print(content)
else:
    print('buzai,cnm')


