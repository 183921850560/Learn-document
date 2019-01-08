# -*-coding:utf-8 -*-
import requests
import json
import unittest

'''
Author:gxl
Headline:4.10.6 根据智能屏ID获取电梯注册编码
Time：2018-05-21
'''

class getRegisterCode(unittest.TestCase):
    def setUp(self):
        #定义报头
        self.header = {'Content-Type':'application/json'}

    def test_getRegisterCode(self):
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
        self.getRegisterCode_uri = 'http://122.112.212.213:8777/api/v2/screen/getRegisterCode?access_token='
        self.getRegisterCode_url = self.getRegisterCode_uri + self.token_value

        #传入请求的参数
        self.getRegisterCode_data = {
            "screenId":"B44F96030E66"
        }
        #将传入的参数转换成json格式
        self.getRegisterCode_value = json.dumps(self.getRegisterCode_data)

        #请求给智能屏下发基本信息
        self.getLatestLiftRunning_req = requests.post(headers=self.header, url=self.getRegisterCode_url, data=self.getRegisterCode_value)
        print('Code status:', self.getLatestLiftRunning_req.status_code, self.getLatestLiftRunning_req.json())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()