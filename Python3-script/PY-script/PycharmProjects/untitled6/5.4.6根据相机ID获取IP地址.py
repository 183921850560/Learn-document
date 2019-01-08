# _*_ coding:UTF-8 _*_

import requests
import json, time
'''
Author:gxl
Headline:5.4.6 根据相机ID获取IP地址
Time：2018-05-21
'''
#定义url
url = "http://eag-test.yun-ti.com:8100/api/v2/device/getaddr"
header = {'Content-Type': 'application/json'}
data = {
    "duSerial":"139615688"
}
value = json.dumps(data)
req = requests.post(url=url, headers=header, data=value)
va = req.text
print(va)
print('req status: %s' %(req.status_code))
