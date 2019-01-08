# -*-coding:utf-8 -*-
import requests
import json

url = 'http://192.168.4.72:9098/zbp-service/1.0.0/search/alarm/history'

headers = {'Content-Type': 'application/x-www-form-urlencoded'}
params = {
    "start": 0,
    "pageSize": 1,
    "queryJson": '''{"elevatorIds": null ,"areaType": null,"areaCode": null,"alarmType": "1",
      "subAlarmType": null,"alarmLevel": null,"typeCode": null ,
      "collectStartTime": null ,"collectEndTime": null,
      "handleStatusCode": null}'''
}


req = requests.get(url, data=params, headers=headers)
content = req.json()

print(content)
print('status_code:', req.status_code)
