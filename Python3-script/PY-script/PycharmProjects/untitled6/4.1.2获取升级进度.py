# -*-coding:utf-8 -*-
import json
import requests
import traceback
'''
Author:gxl
Headline:4.1.2 获取升级进度
Time：2018-05-21
'''

#触发的URL
url = ' http://eag-test.yun-ti.com:8100/api/v2/device/upgradeprogress'

#添加http报头信息
header = {'Content-Type': 'application/json'}

#添加触发的body（格式为json形式）
databody = {
    "duSerial": "150561034",
    # "sessionID":"1",
    "version":"V5.5.0 build 180723"
}
value = json.dumps(databody)
request_type = requests.post(url, data=value, headers=header)
values=request_type.text
print(values)
print('status_code:', request_type.status_code)