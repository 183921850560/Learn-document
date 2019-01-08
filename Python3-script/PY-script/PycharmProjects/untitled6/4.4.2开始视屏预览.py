# _*_ coding:UTF-8 _*_

import requests
import json, time
'''
Author:gxl
Headline:4.4.2 开始视屏预览
Time：2018-05-21
'''

#定义url
url = "http://eag-test.yun-ti.com:8100/api/v2/stream/real/start"
header = {'Content-Type': 'application/json'}
data ={
    "duSerial":"150560560",
    "channel":1,
    "streamServerIp":"119.3.36.59",
    "streamServerPort":40000,
    "streamType":1,
    "linkMode":0
}
data_value = json.dumps(data)
req = requests.post(url=url, headers=header, data=data_value)
req_value = req.text
print(req_value)
print('req status: %s' %(req.status_code))
