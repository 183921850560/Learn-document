# -*-coding:utf-8 -*-
import json
import requests
import traceback
'''
Author:gxl
Headline: 2.3.2.1 报警联动模板配置新增
Time：2018-05-21
'''

#触发的URL
url = 'http://192.168.20.4:8082/linkage-config/alarm/linkage/type-config/create'

#添加http报头信息
header = {'Content-Type': 'application/json'}

#添加触发的body（格式为json形式）
databody = {
    "typeCode": "t1001",
    "config":"哈哈哈， 位于“{liftName}”电梯有{warnName}，谢谢！",
    "updaterId": "16"
}
value = json.dumps(databody)
request_type = requests.post(url, data=value, headers=header )
values=request_type.text
print(values)
print('status_code:', request_type.status_code)