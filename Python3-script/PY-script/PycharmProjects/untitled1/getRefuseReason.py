# -*-coding:utf-8 -*-
import requests
import json


url = 'https://114.55.6.227:8779/rescue/v1/getRefuseReason?access_token=a802c5dd5814f51231ca53a289830b3bba52a262d37a29b29ac36b5a7aca498239ca629a6a235298'
headers = {'Content-Type': 'application/json'}

#values = json.dumps(databody)
req = requests.post(url, headers=headers, cert=('C:\\Users\\chengxue\\PycharmProjects\\untitled1\\client.crt',
                                                             'C:\\Users\\chengxue\\PycharmProjects\\untitled1\\client.key'))
content = req.text
print(content)
print('status_code:', req.status_code)