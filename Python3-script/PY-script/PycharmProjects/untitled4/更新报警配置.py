# -*-coding:utf-8 -*-
import requests
import json
'''
Author:gxl
Headline: 更新报警配置
Time：2018-05-21
'''

url = 'http://192.168.20.4:8085/alarm-config/alarm/filter/config/update/7'
headers = {'Content-Type': 'application/json'}
databody={
  "config": "{'level':3}",
  "target": "bssbfbf-525523-4522889999",
  "updateId": "456"
}
values = json.dumps(databody)
req = requests.put(url, data=values, headers=headers)
content = req.text
print(content)
print('status_code:', req.status_code)