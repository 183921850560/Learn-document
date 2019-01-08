# -*-coding:utf-8 -*-
import requests
import json
'''
Author:gxl
Headline: 删除报警配置
Time：2018-05-21
'''


url = 'http://192.168.20.4:8083/alarm-dispatcher/alarm/info/aa_5558888/1'
headers = {'Content-Type': 'application/json'}
'''
databody={
  "config": "{'level':3}",
  "target": "A-B-C-D-001,A-B-C-D-002",
  "updateId": "2"
}
'''
#values = json.dumps(databody)
req = requests.put(url,  headers=headers)
content = req.text
print(content)
print('status_code:', req.status_code)