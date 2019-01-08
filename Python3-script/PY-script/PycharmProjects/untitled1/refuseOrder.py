# -*-coding:utf-8 -*-
import requests
import json


url = 'https://114.55.6.227:8779/rescue/v1/refuseOrder?access_token=a80a072808b614fa31ca53a289830b3bba52a262d37a29b29ac36b5a7aca498239ca629a6a235298'
headers = {'Content-Type': 'application/json'}
databody={
    "orderCode":"17121105001590",
    "ReasonType":"2，1",
    "remark":"张"
}

values = json.dumps(databody)
req = requests.post(url, data=values, headers=headers, cert=('C:\\Users\\chengxue\\PycharmProjects\\untitled1\\client.crt',
                                                             'C:\\Users\\chengxue\\PycharmProjects\\untitled1\\client.key'))
content = req.text
print(content)
print('status_code:', req.status_code)