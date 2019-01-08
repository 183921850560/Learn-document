# -*-coding:utf-8 -*-
import requests
import time
import json
import random

#触发的URL地址
url = 'http://172.18.20.244:8201/v2/triggers/88899922'
#添加http信息头管理器
headers = {'Content-Type': 'application/json'}
#请求的databody
databody = {
    "triggerStoreType": 1,
    "triggerType": 2,
    "triggerPri": 5,
    "videoFileName": "20170917/0_0_20170917071043_20170917071522_1.h264",
    "cameraID": "172.18.20.88:21",
    "cameraChan": 1,
    "cameraType": 2
}
#传参的内容
value = json.dumps(databody)
#请求的类型
request_type = requests.put(url, data=value, headers=headers)
values=request_type.text
#打印出返回的数据
print(values)
print('status_code:', request_type.status_code)