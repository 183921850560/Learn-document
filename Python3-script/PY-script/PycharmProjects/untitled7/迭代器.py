# -*- coding:utf-8 -*-
import requests
import os
import math
import random
import keyword
import sys

list = [1, 2, 3, 4, 5, 6]
it = iter(list)
print(next(it))

aa = [4, 5, 6, 7, 8, 9]
rr = iter(aa)
for i in rr:
    print(i)


list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
