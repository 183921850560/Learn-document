# -*-coding:utf-8 -*-
import requests
import json


url = 'http://192.168.20.4:8085/alarm-config/alarm/filter/config/7'
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