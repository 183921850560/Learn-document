# -*-coding:utf-8 -*-
import requests
import json
import unittest

'''
Author:gxl
Headline:4.12.1 单位信息查询
Time：2018-05-21
'''

class getunitphone(unittest.TestCase):
    def setUp(self):
        #定义报头
        self.header = {'Content-Type':'application/json'}

    def test_phone(self):
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
        self.get_uri = 'http://122.112.212.213:8777/api/v1/estate/getUnitPhone?access_token='
        self.phone_url = self.get_uri + self.token_value

        #传入请求的参数
        self.phone_data = {
            "registerCodes": ["32201234562018091399", "31103301102010090041", "32201234562018090632"]
        }
        #将传入的参数转换成json格式
        self.phone_value = json.dumps(self.phone_data)

        #请求给智能屏下发基本信息
        self.phone_req = requests.post(headers=self.header, url=self.phone_url, data=self.phone_value)
        print('Code status:', self.phone_req.status_code, self.phone_req.json())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()