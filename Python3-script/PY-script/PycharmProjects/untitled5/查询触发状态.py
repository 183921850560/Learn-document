# -*-coding:utf-8 -*-
import requests
import time
import json
import random

#触发的URL地址
url = 'http://store-test.yun-ti.com:8245/v2/triggers?status=3&pageSize=&pageNum=2'
#添加http信息头管理器
headers = {'Content-Type': 'application/json'}

#请求的类型
request_type = requests.get(url, headers=headers )
values=request_type.text
#打印出返回的数据
print(values)
print('status_code:', request_type.status_code)