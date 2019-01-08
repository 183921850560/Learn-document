# -*- coding:utf-8 -*-
import requests
import time
import os
import keyword
import math
import random


a = 10
b = 20

#and 如果a为false，a and b会返回false，否则返回true
if (a and b):
    print('yes')
else:
    print('no')


#ceil是返回一个大于或者等于c的最小整数（必须调用math模块（math模块是静态对象模块））
c = 2.99
print(math.ceil(c))


########数字函数
#abs函数是取绝对值函数
print(abs(c))

#exp()函数是返回e的多少次方的，必须调用math模块
print(math.exp(c))

#floor()返回数字的下整数
print(math.floor(c))


d = [12, 25, 56, 789]

#max()函数为返回最大值
print(max(d))

#min()函数为返回最小值
print(min(d))

#round()函数是对数值四舍五入
print(round(c))

#sqrt()函数是返回数字的平方根
print(math.sqrt(c))

########随机函数
#choice()函数是从序列中任取一个随机数
print(random.choice(range(100)))

#randrange()函数是返回制定递增基数的一个随机数，基数的缺省值为1
print(random.randrange(1, 788, 2))
print(random.randrange(48889))

#random()返回随机生成的一个实数，在【0,1】范围内
print(random.random())

#shuffle()将序列的所有元素随机排列
list = [45, 56, 2, 23, 899, 52, 21]
value = random.shuffle(list)
print(list)

#uniform(x,y)函数是随机生成一个在x和y之间的实数
print(random.uniform(0, 788))


