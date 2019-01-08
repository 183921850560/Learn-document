# -*-coding:utf-8 -*-
import requests
import json
import unittest

'''
Author:gxl
Headline:4.2.1 推送报警信息
Time：2018-05-21
'''

class AlarmData(unittest.TestCase):
    def setUp(self):
        #定义报头
        self.header = {'Content-Type':'application/json'}

    def test_AlarmData(self):
        #获取需要的token值
        self.token_url = 'http://122.112.212.213:8777/api/v1/getToken'

        # 传入对应的AppKey和AppSecret
        self.app_data = {
            'AppKey': 'soKAM14J7hXQpEVbnBOdYzqUySR9kju5',
            'AppSecret': '3Zd0O6ExyC9mhJUHg4WsDvGSNATBfkKV'
        }

        # 打印出json格式的data
        self.token_va = json.dumps(self.app_data)

        #请求获取token值
        self.token_req = requests.post(url=self.token_url, headers=self.header, data=self.token_va)

        #获取token的值并打印出来
        self.token_value = self.token_req.json()['data']['accessToken']

        #传入给智能屏下发信息的uri
        self.Alarm_uri = 'http://122.112.212.213:8777/api/v1/webhook/alarmData?access_token='
        self.AlarmData_url = self.Alarm_uri + self.token_value

        #传入请求的参数
        self.Alarm_data = {
             "alarmCode": "31b509b6-7eb1-4f18-bd70-5a7fadf2821c",
             "registerCode": "32201234562018091443",
             "alarmType": 1000001,
             "alarmStatus": 1,
             "alarmTime":1544584580,
             "hasPerson":True,
             "alarmAttr":1,
             "standardType":"9000001",
             "ytStatus":"50"
        }
        #将传入的参数转换成json格式
        self.AlarmData_value = json.dumps(self.Alarm_data)

        self.header_01 = {'Content-Type': 'application/json',
                          'x-xzl-token':self.token_value}

        #请求给智能屏下发基本信息
        self.AlarmData_req = requests.post(headers=self.header_01, url=self.AlarmData_url, data=self.AlarmData_value)
        print('Code status:', self.AlarmData_req.status_code, self.AlarmData_req.text)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()