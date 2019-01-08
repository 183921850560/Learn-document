# -*-coding:utf-8 -*-
import json
import requests
'''
Author:gxl
Headline: 2.3.3.4按报警联动动作查询（按单位类型）
Time：2018-05-21
'''

#触发的URL
url = 'http://192.168.20.4:8082/linkage-config/alarm/linkage/config/list/2424'

#添加http报头信息
header = {'Content-Type': 'application/json'}

#添加请求的类型
request_type = requests.get(url, headers=header)
values=request_type.text
print(values)
print('status_code:', request_type.status_code)