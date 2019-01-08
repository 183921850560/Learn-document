# -*-coding:utf-8 -*-
import requests
import json
import unittest

'''
Author:gxl
Headline:4.1.2 设置实时数据回调
Time：2018-12-19
'''

class RealTimeData(unittest.TestCase):
    def setUp(self):
        #定义报头
        self.header = {'Content-Type':'application/json'}

    def test_RealTimeData(self):
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
        self.RealTimeData_uri = 'http://122.112.212.213:8777/api/v1/webhook/realtimeData?access_token='
        self.RealTimeData_url = self.RealTimeData_uri + self.token_value

        #传入请求的参数
        self.RealTimeData_data = {
            "webHookUrl": "http://192.168.2.217:9000/sendRealTime",
            "token": self.token_value
        }
        #将传入的参数转换成json格式
        self.RealTimeData_value = json.dumps(self.RealTimeData_data)

        #请求给智能屏下发基本信息
        self.RealTimeData_req = requests.post(headers=self.header, url=self.RealTimeData_url, data=self.RealTimeData_value)
        print('Code status:', self.RealTimeData_req.status_code, self.RealTimeData_req.text)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()