# -*-coding:utf-8 -*-
import json
import requests
'''
Author:gxl
Headline: 2.3.2.3 报警联动模板配置查询（按联动动作类型）
Time：2018-05-21
'''

#触发的URL
url = 'http://192.168.20.4:8082/linkage-config/alarm/linkage/type-config/list/t1001'

#添加http报头信息
header = {'Content-Type': 'application/json'}

#定义请求的类型为get
request_type = requests.get(url,  headers=header)
values=request_type.text
print(values)
print('status_code:', request_type.status_code)