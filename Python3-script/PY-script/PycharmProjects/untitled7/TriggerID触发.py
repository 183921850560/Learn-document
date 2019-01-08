# -*-coding:utf-8 -*-
import requests
import time
import json
import random
import base64
import hashlib

url = 'http://192.168.1.210:8203/v2/triggers/aaa780'
#添加http信息头管理器
headers = {"Content-Type": "application/json"}
databody = {
    "triggerStoreType": 1,
    "triggerType": 1,
    "triggerPri": 1,
    "triggerTime": 1525662469,
    "beforeTime": 90,
    "afterTime": 0,
    #"vedioFileName": "20171113/0_0_20171113064131_20171113064611_1.h264",
    "cameraID": "139615699",
    "cameraChan": 1,
    "cameraType": 1
}
#传参的内容
value = json.dumps(databody)
#请求的类型
request_type = requests.put(url, data=value, headers=headers)
values=request_type.text
#打印出返回的数据
print(values)
print('status_code:', request_type.status_code  )