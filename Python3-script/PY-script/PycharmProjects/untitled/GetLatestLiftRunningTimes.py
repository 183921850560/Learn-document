# -*-coding:utf-8 -*-
import requests
import json
import unittest

'''
Author:gxl
Headline:4.15.6 查询近期电梯运行次数
Time：2018-05-21
'''

class getlatestliftrunningtime(unittest.TestCase):
    def setUp(self):
        #定义报头
        self.header = {'Content-Type':'application/json'}

    def test_getLatestLiftRunning(self):
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
        self.getLatestLiftRunning_uri = 'http://122.112.212.213:8777/api/v1/statistics/getLatestLiftRunningTimes?access_token='
        self.getLatestLiftRunning_url = self.getLatestLiftRunning_uri + self.token_value

        #传入请求的参数
        self.getLatestLiftRunning_data = {
            "registerCodes":["31103305022015100005"],
            "beginTime": 1546063692,
            "endTime": 1546063872
        }
        #将传入的参数转换成json格式
        self.getLatestLiftRunning_value = json.dumps(self.getLatestLiftRunning_data)

        #请求给智能屏下发基本信息
        self.getLatestLiftRunning_req = requests.post(headers=self.header, url=self.getLatestLiftRunning_url, data=self.getLatestLiftRunning_value)
        print('Code status:', self.getLatestLiftRunning_req.status_code, self.getLatestLiftRunning_req.json())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()