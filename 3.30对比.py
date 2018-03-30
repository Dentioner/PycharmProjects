#coding : utf-8
f =open('compare.txt','w')
data = ['guna',114.514, True]
i = 0
while i <=2:

    f.writelines(str(data[i])+'\n')
    i+=1
f.close()
print('done')

g= open('compare.txt')
data2 = g.read()
print(data2)
