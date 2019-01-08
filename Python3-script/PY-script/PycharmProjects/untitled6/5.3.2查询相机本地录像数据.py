# -*-coding:utf-8 -*-
import requests
import json
'''
Author:gxl
Headline:5.3.2查询相机本地录像数据
Time：2018-05-21
'''
#触发的URL
url = 'http://eag-test.yun-ti.com:8100/api/v2/device/getlocalrecordfiles'

#添加http报头信息
header = {'Content-Type': 'application/json'}

#添加触发的body（格式为json形式）
databody = {
    "duSerial": "150562391",
    "beginTime":1542607433,
    "endTime": 1542693833
}
value = json.dumps(databody)
request_type = requests.post(url, data=value, headers=header)
values=request_type.text
print(values)
print('status_code:', request_type.status_code)