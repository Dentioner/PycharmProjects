# coding:utf-8
seq = [1, 2, 3, 4, 5, 6]
print(seq)
seq.append(7)
print(seq)
seq.extend([8, 9, 10, 'guna']) # 使用extend在列表末尾添加多个元素
print(seq)
seq.insert(2, 2.5) # insert(位置，元素)
print(seq)
seq.remove('guna')
print(seq)
seq2 = [1,1,1,1,1,1,1,2]
seq2.remove(1)
print(seq2)
del seq[10]
print(seq)
last = seq.pop(8)#pop会让seq的某个元素分离出来，括号里面没填就是默认最后一位
print(seq)
print(last)
