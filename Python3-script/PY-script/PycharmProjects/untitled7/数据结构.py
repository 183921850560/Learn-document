# -*- coding:utf-8 -*-
import requests
import os
import math
import random
import keyword
import sys


#append（参数）函数的应用
list_name = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
aa = list_name.append(888)
print(list_name)

#extend（列表）函数的应用
list_name1 = [11, 22, 33, 44, 55, 66, 77]
bb = list_name.extend(list_name1)
print(list_name)

#insert(索引位置， 值)函数的应用
cc = list_name.insert(0,521)
print(list_name)

#remove(值)函数的应用
list_name2 = [10, 20, 30, 40, 50, 60, 70, 80]
ee = list_name2.remove(30)
print(list_name2)

#pop()函数的应用
ff = list_name2.pop()
print(list_name2)

#pop([])函数的应用
gg = list_name2.pop(2)
print(list_name2)

#clear()函数的应用
list_name3 = [11, 22, 33, 44, 55, 66, 77,88, 99]
hh = list_name3.clear()
print(list_name3)

#count(值)函数的应用
list_name4 = [0, 2, 23, 24, 22, 26]
ii = list_name4.count(22)
print(ii)

#index(值)函数的应用
jj = list_name4.index(26)
print(jj)

#sort()函数的应用
kk = list_name4.sort()
print(list_name4)

#reverse()函数的应用
ll = list_name4.reverse()
print(list_name4)

#copy()函数的应用
mm = list_name4.copy()
print(list_name4)



