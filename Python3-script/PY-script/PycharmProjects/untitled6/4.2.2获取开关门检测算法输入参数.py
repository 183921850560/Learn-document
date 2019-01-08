# -*-coding:utf-8 -*-
import json
import requests
import traceback
'''
Author:gxl
Headline:4.2.2 获取开关门检测算法输入参数
Time：2018-05-21
'''

#触发的URL
url = 'http://eag-test.yun-ti.com:8100/api/v2/door/getconfig'

#添加http报头信息
header = {'Content-Type': 'application/json'}

#添加触发的body（格式为json形式）
databody = {
	"duSerial":"139615688",
    # "sensitivityIndexList":[1]

}
value = json.dumps(databody)
request_type = requests.post(url, data=value, headers=header )
values=request_type.text
print(values)
print('status_code:', request_type.status_code)