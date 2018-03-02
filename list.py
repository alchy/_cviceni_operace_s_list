# -*- coding: utf-8 -*-

# save and load list with pickle
import pickle
my_list = ['a', 'b', 'c', 'd']

# save list
filehandler = open('saved_list.pickle', 'wb')
pickle.dump(my_list, filehandler)

# load list
filehandler = open('saved_list.pickle', 'rb')
my_list = pickle.load(filehandler)
print(my_list)

# get item's index 
index = my_list.index('c')
print(index)

# sort list
my_list = ['c', 'b', 'a']
my_list.sort()
print(my_list)

# remove from list
my_list.remove('c')
print(my_list)

# append to list
my_list.append('d')
print(my_list)

