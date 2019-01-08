# -*-coding:utf-8 -*-
import requests
import json
'''
Author:gxl
Headline: 创建报警配置
Time：2018-05-21
'''


url = 'http://192.168.20.4:8085/alarm-config/alarm/filter/config/create'
headers = {'Content-Type': 'application/json'}
databody={
  "alarmType": "222",
  "filterType": "TIMEOUT_FILTER",
  "target": "A-B-C-D-000025689174275878",
  "config": "{“blackList”:true}",
  "updateId": "555544sd"
}
values = json.dumps(databody)
req = requests.post(url, data=values, headers=headers)
content = req.text
print(content)
print('status_code:', req.status_code)