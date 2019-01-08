#coding: utf-8
import requests
import time

#获取当前时间作为triggerID
triggerID = str(time.time())
print(triggerID)

#身体质量指数计算
weight = float(input('kk:'))
high = float(input('ii:'))
result = weight/(high ** 2)
print(result)



