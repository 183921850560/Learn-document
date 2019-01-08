# coding=utf-8
import requests
import json
import unittest

'''
Author:gxl
Headline:4.15.1 查询电梯运行里程
Time：2018-05-21
'''

class getLiftMileage(unittest.TestCase):
    def setUp(self):
        #定义报头
        self.header = {'Content-Type':'application/json'}

    def test_getLiftMileage(self):
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
        self.getLiftMileage_uri = 'http://122.112.212.213:8777/api/v1/statistics/getLiftMileage?access_token='
        self.getLiftMileage_url = self.getLiftMileage_uri + self.token_value

        #传入请求的参数
        self.getLiftMileage_data = {
            "registerCodes": ["20180816192350147256666","33101239682018106881"]
        }
        #将传入的参数转换成json格式
        self.getLiftMileage_value = json.dumps(self.getLiftMileage_data)

        #请求给智能屏下发基本信息
        self.getLiftMileage_req = requests.post(headers=self.header, url=self.getLiftMileage_url, data=self.getLiftMileage_value)
        print('Code status:', self.getLiftMileage_req.status_code, self.getLiftMileage_req.json())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()