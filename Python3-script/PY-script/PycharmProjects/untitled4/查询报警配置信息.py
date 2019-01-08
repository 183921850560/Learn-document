# -*-coding:utf-8 -*-
import requests
'''
Author:gxl
Headline: 查询报警配置信息
Time：2018-05-21
'''

url = 'http://192.168.20.4:8085/alarm-config/alarm/filter/config/list?alarmType=3000037&filterType=BLACKLIST_FILTER&target=555-225-22-dd666'
headers = {'Content-Type': 'application/json'}

req = requests.get(url,  headers=headers)
content = req.text
print(content)
print('status_code:', req.status_code)