#coding: utf-8
type = raw_input('想打什么？')
blk = int(raw_input('几块？'))
line = int(raw_input('每块几行？'))
num = int(raw_input('每行几个？'))

for i in range(blk):
    for j in range(line):
        for k in range(num):
            print(type),
        print
    print#后两个print是为了让程序从新的一行开始打，否则由于第一个print用了逗号，所以符号全都会打到一行去
