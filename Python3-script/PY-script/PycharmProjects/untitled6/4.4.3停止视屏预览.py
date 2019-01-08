# _*_ coding:UTF-8 _*_

import requests
import json, time
'''
Author:gxl
Headline:4.4.3 停止视屏预览
Time：2018-05-21
'''
#定义url
url = "http://eag-test.yun-ti.com:8100/api/v2/stream/real/stop"
header = {'Content-Type': 'application/json'}
data = {
    "duSerial":"150560560",
    "streamSession":"real-752641570-780274174"
}
value = json.dumps(data)
req = requests.post(url=url, headers=header, data=value)
va = req.text
print(va)
print('req status: %s' %(req.status_code))
