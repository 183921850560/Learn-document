# -*-coding:utf-8 -*-
import json
import requests
import traceback
'''
Author:gxl
Headline:4.2.3 配置区域入侵算法输入参数
Time：2018-05-21
'''
#触发的URL
url = 'http://eag-test.yun-ti.com:8100/api/v2/area/setconfig'

#添加http报头信息
header = {'Content-Type': 'application/json'}

#添加触发的body（格式为json形式）

databody = {
    "duSerial": "150561379",
    "screenLength":500,
    "screenWidth": 800,
    "fieldDetectionRegions":[
        {
            "timeThreshold":0,
            "sensitivity":50,
            "objOccupation":0,
            "regionType":0,
            "coordinatesList":[
                {
			    "xaxis": 140,
			    "yaxis": 523
		         },
                {
			    "xaxis": 650,

			    "yaxis": 511
		         },
                {
			    "xaxis": 654,
			    "yaxis": 758
		         },
                {
			    "xaxis": 150,
			    "yaxis": 764
		         }
            ]
        }

    ]
}
value = json.dumps(databody)
request_type = requests.post(url, data=value, headers=header )
values=request_type.text
print(values)
print('status_code:', request_type.status_code)