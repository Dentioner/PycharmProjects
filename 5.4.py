# coding: utf-8
import pickle
# my_list = ['a', 1551, 'guna', 3.1415926, True]
# pickle_file = open('my_pickle_list.dxl', 'w')
# pickle.dump(my_list, pickle_file)

pickle_file = open('my_pickle_list.dxl', 'r')
reco = pickle.load(pickle_file)
pickle_file.close()
print reco

