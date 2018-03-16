# -*- coding:utf-8 -*-
import urllib2
import json
from  city import city
print('注意：只能直接复制city.py里面的乱码来查询城市')
cityname = raw_input('哪个城市？\n')

citycode = city.get(cityname)
if citycode:
    try:
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html' %citycode)
        content = urllib2.urlopen(url).read()
        print(content)
        data = json.loads(content)
        result = data['weatherinfo']
        str_temp = ('%s\n%s~%s')%(  #这里是：weather 多少度~多少度
        result['weather'],
        result['temp1'],
        result['temp2']
)

        print(cityname)
        print str_temp
        print type(content) #显示 content 的 类型是 str字符串
        print type(data)#显示data的 类型 是 dict 字典
    except:
        print('guna,%s查询失败')%cityname
else:
    print('%sbuzai,cnm')%cityname



