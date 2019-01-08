# _*_coding:utf-8 _*_

import json
import requests
'''
Author:gxl
Headline:5.3.1 获取在线设备列表
Time：2018-05-21
'''
#请求的url
url = 'http://eag-test.yun-ti.com:8100/api/v2/device/onlinelist'
#请求的报头
header = {'Content-Type': 'application/json'}
#请求的databody
data= {}
data_value = json.dumps(data)
req = requests.post(url=url, headers=header, data=data_value)
req_value = req.text
print(req_value)
print('req status: %s' %(req.status_code))
