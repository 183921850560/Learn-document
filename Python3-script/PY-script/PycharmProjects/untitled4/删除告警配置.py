# -*-coding:utf-8 -*-
import requests
import json
'''
Author:gxl
Headline: 删除告警配置
Time：2018-05-21
'''


url = 'http://192.168.20.4:8085/alarm-config/alarm/filter/config/6'
headers = {'Content-Type': 'application/json'}
'''
databody={
  "config": "{'level':3}",
  "target": "A-B-C-D-001,A-B-C-D-002",
  "updateId": "2"
}
'''
#values = json.dumps(databody)
req = requests.delete(url,  headers=headers)
content = req.text
print(content)
print('status_code:', req.status_code)