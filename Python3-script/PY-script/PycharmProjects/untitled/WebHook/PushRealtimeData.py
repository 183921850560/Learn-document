# -*-coding:utf-8 -*-
import requests
import json
import unittest

'''
Author:gxl
Headline:4.2.2 推送实时信息
Time：2018-05-21
'''

class PushRealTime(unittest.TestCase):
    def setUp(self):
        #定义报头
        self.header = {'Content-Type':'application/json'}

    def test_PushRealTime(self):
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
        self.PushRealTime_uri = 'http://122.112.212.213:8777/api/v1/webhook/realtimeData?access_token='
        self.PushRealTime_url = self.PushRealTime_uri + self.token_value

        #传入请求的参数
        self.PushRealTime_data = {
             "registerCode": "32201234562018091443",
             "speed":26.5,
             "hasPerson": True,
             "smokeDetector": False,
             "carTemperature": 12.5,
             "carTopTemperature":26.4,
             "roomTemperature":45.2,
             "photoSensitive":12,
             "press":5,
             "wifiAp":5,
             "emergencyLighting":3,
             "packageTime":1545206690
        }
        #将传入的参数转换成json格式
        self.PushRealTime_value = json.dumps(self.PushRealTime_data)

        self.header_01 = {'Content-Type': 'application/json',
                          'x-xzl-token':self.token_value}

        #请求给智能屏下发基本信息
        self.PushRealTime_req = requests.post(headers=self.header_01, url=self.PushRealTime_url, data=self.PushRealTime_value)
        print('Code status:', self.PushRealTime_req.status_code, self.PushRealTime_req.text)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()