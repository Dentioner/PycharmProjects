#coding:utf-8
#sample code
# import   urllib, time
#
#
# time_start = time.time()
# data = []
# for i in range(30):
#     print 'request movie:',i
#     id = 1764796 + i
#     url = 'https://api.douban.com/v2/movie/subject/%d'%id
#     d = urllib.urlopen(url).read()
#     data.append(d)
#     print i, time.time() - time_start
#
#
# print 'data:', len(data)

import   urllib, time,thread
data = []
time_start = time.time()
def get_content(i):
    id = 1764796 + i
    url = 'https://api.douban.com/v2/movie/subject/%d'%id
    content = urllib.urlopen(url).read()
    data.append(content)
    print i, time.time() - time_start
    print 'data:', len(data)

for i in range(30):
    print 'request movie:', i
    thread.start_new_thread(get_content,(i,) )

raw_input('press ENTER to exit...\n')
