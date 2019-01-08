# -*-coding:utf-8 -*-
import requests
import json
'''
Author:gxl
Headline: 获取报警详情
Time：2018-05-21
'''


url = 'http://192.168.20.4:8083/alarm-dispatcher/alarm/info/07dcc86b-f2a5-4ea4-bb21-a5c0422209ed'
headers = {'Content-Type': 'application/json'}
'''
databody={
  "config": "{'level':3}",
  "target": "A-B-C-D-001,A-B-C-D-002",
  "updateId": "2"
}
'''
#values = json.dumps(databody)
req = requests.get(url,  headers=headers)
content = req.text
print(content)
print('status_code:', req.status_code)