# -*-coding:utf-8 -*-
import requests
import json
'''
Author:gxl
Headline: 获取报警数据
Time：2018-05-21
'''


url = 'http://192.168.20.4:8083/alarm-dispatcher/alarm/info/list/1/100'
headers = {'Content-Type': 'application/json'}

databody={}
values = json.dumps(databody)
req = requests.post(url, data=values, headers=headers)
content = req.text
print(content)
print('status_code:', req.status_code)