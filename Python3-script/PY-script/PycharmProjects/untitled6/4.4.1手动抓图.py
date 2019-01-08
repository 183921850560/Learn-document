# _*_coding:utf-8 _*_

import json
import requests
'''
Author:gxl
Headline:4.4.1 手动抓图
Time：2018-05-21
'''

#请求的url
url = 'http://eag-test.yun-ti.com:8100/api/v2/picture/snap/manual'
#请求的报头
header = {'Content-Type': 'application/json'}
#请求的databody
data= {
    "duSerial":"139615688",
    "channel":1,
    "snapType":0,
    "frequency":2
}
data_value = json.dumps(data)
req = requests.post(url=url, headers=header, data=data_value)
req_value = req.text
print(req_value)
print('req status: %s' %(req.status_code))

