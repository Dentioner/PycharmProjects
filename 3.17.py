# -*- coding:utf-8 -*-
import urllib2
url1 = 'http://m.weather.com.cn/data3/city.xml'
content1 = urllib2.urlopen(url1).read() #读取url1的内容
provinces = content1.split(',')#把url1内容用逗号分隔成不同的元素，构成province
result = 'city= {\n' #def a new dictionary


url = 'http://m.weather.com.cn/data3/city%s.xml'

book = open('citydata2.txt','w')

for p in provinces:
    p_code = p.split('|')[0]   #把province里面的每一个元素用|分隔
    url2 = url%p_code #注意url字符串里面有个%s，这里便将%s替换为了p_code的内容，即province里面的内容
    content2 = urllib2.urlopen(url2).read()#新得到的content2
    cities = content2.split(',')#将content2用逗号分开


    for c in cities[:3]:
        c_code = c.split('|')[0]
        url3 = url% c_code#同上面的p_code
        content3 = urllib2.urlopen(url3).read()
        districts = content3.split(',')


        for d in districts:
            d_pair = d.split('|')
            d_code = d_pair[0]
            name = d_pair[1]
            url4 = url % d_code
            content4 = urllib2.urlopen(url4).read()
            code = content4.split('|')[1]

            line = "    '%s': '%s',\n"%(name,code)

            result += line
            final = name + ':' + code

            book.writelines(final)


book.close()
print('好了')
