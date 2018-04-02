#coding:utf-8
def func(args):
    sum = 0
    for i in range(len(args)):
        sum+=args[i]
    print(sum)
INPUT=''
seq=[]
while INPUT!= 'ok':
    a=raw_input('add what?')
    seq.append(int(a))
    INPUT=raw_input('ok?')
func(seq)

