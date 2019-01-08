# -*-coding:utf-8 -*-
import json
import requests
'''
Author:gxl
Headline: 2.3.2.2 报警联动模板配置修改
Time：2018-05-21
'''

#触发的URL
url = 'http://192.168.20.4:8082/linkage-config/alarm/linkage/type-config/update'

#添加http报头信息
header = {'Content-Type': 'application/json'}

#添加触发的body（格式为json形式）
databody = {
    "id":"2",
    "config":"您好！ 位于“{ccliftName}”电梯检测到有{warnName}，请及时查看，谢谢!",
    "updaterId":"16"
}
value = json.dumps(databody)
request_type = requests.put(url, data=value, headers=header)
values=request_type.text
print(values)
print('status_code:', request_type.status_code)