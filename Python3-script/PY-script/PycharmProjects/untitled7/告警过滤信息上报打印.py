# -*-coding:utf-8 -*-
import requests
import time
import json


url = 'http://172.18.20.175:65535/alarm/info/trapfilter'
#添加http信息头管理器
headers = {"Content-Type": "application/json"}
databody = {
    "data": [
        {
            "errCode": 0,
            "triggerID": "aaa666",
            "triggerResult": "cleaning"
        }
]}
#传参的内容
value = json.dumps(databody)
#请求的类型
request_type = requests.put(url, data=value, headers=headers)
values=request_type.text
#打印出返回的数据
print(values)
print('status_code:', request_type.status_code)