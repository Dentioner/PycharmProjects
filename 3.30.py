#coding : utf-8
import pickle
test_data = ['guna',114.514,True]

f = file('test.data','w')
pickle.dump(test_data,f)
f.close()
print('done')

g= file('test.data')
test_data2 = pickle.load(g)
g.close()
print(test_data2)

