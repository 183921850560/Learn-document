# -*-coding:utf-8 -*-
import requests
import json


url = 'http://114.55.6.227:8779/rescue/v1/getToken'
headers = {'Content-Type': 'application/json'}
#
#
databody={
    "AppKey": "F9JtQ0agwJTLZoE6SXmkOYI0G9LSMDjS",
    "AppSecret": "iYAxfNlHRKsHtvvzd3q5p0FiaoCk4P9n"
}
values = json.dumps(databody)
req = requests.post(url, data=values, headers=headers, cert=('C:\\Users\\chengxue\PycharmProjects\\untitled1\\client.crt',
                                                             'C:\\Users\\chengxue\PycharmProjects\\untitled1\\client.key'))
content = req.text
print(content)
print('status_code:', req.status_code)

