# -*-coding:utf-8 -*-
import requests
import json
import unittest

'''
Author:gxl
Headline:4.13.1 请求获取异常电梯设备列表
Time：2018-05-21
'''

class getAbnormal(unittest.TestCase):
    def setUp(self):
        #定义报头
        self.header = {'Content-Type':'application/json'}

    def test_getAbnormal(self):
        #获取需要的token值
        self.token_url = 'http://122.112.212.213:8777/api/v1/getToken'

        # 传入对应的AppKey和AppSecret
        self.app_data = {
            'AppKey': 'nMqbGHTSJNwqgzIRTAx56vHrqUxrhQBY',
            'AppSecret': '5NR1nrbvjlbJuqymCuMjVUoGjSKa5iqS'
        }

        # 打印出json格式的data
        self.token_va = json.dumps(self.app_data)

        #请求获取token值
        self.token_req = requests.post(url=self.token_url, headers=self.header, data=self.token_va)

        #获取token的值并打印出来
        self.token_value = self.token_req.json()['data']['accessToken']

        #传入给智能屏下发信息的uri
        self.normal_uri = 'http://122.112.212.213:8777/api/v1/ops/getAbnormalDevList?access_token='
        self.normal_url = self.normal_uri + self.token_value

        #传入请求的参数
        self.normal_data = {
            "subDevType": "all"
        }
        #将传入的参数转换成json格式
        self.normal_value = json.dumps(self.normal_data)

        #请求给智能屏下发基本信息
        self.normal_req = requests.post(headers=self.header, url=self.normal_url, data=self.normal_value)
        print('Code status:', self.normal_req.status_code, self.normal_req.json())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()