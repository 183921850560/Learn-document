# coding:utf-8
import json
import requests
import traceback
'''
Author:gxl
Headline:4.1.1 设备升级
Time：2018-05-21
'''

#触发的URL
url = 'http://172.16.11.67:8100/api/v2/device/upgrade'

#添加http报头信息
header = {'Content-Type': 'application/json'}

#添加触发的body（格式为json形式）
databody = {
    "duSerial": "139615573",
    "protocol":1,
    "serverIp": "172.16.16.68",
    "serverPort":21,
    "fileUrl":"digicap180830.dav",
    "account":"ftpxiao",
    "password":"g18392185056",
    "version":"V5.5.0 build 180830"
}
value = json.dumps(databody)
request_type = requests.post(url, data=value, headers=header)
values=request_type.text
print(values)
print('status_code:', request_type.status_code)