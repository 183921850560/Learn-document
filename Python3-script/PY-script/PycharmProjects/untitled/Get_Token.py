# *_* coding:utf-8 *_*

'''
Author:gxl
Headline:4.1.1获取token值
Time：2018-05-21
'''

import json
import requests
import unittest

class AccessToken(unittest.TestCase):
    def setUp(self):
        # 定义url
        self.url = 'http://122.112.212.213:8777/api/v1/getToken'

        # 添加报头
        self.header = {'Content-Type': 'application/json'}

        # 传入对应的AppKey和AppSecret
        self.data = {
            'AppKey': 'soKAM14J7hXQpEVbnBOdYzqUySR9kju5',
            'AppSecret': '3Zd0O6ExyC9mhJUHg4WsDvGSNATBfkKV'
        }

        # 打印出json格式的data
        self.value = json.dumps(self.data)

    def test_AccessToken(self):
        # 跳转post请求,并打印出来
        self.req = requests.post(url=self.url, data=self.value, headers=self.header)
        print('Code status:', self.req.status_code, self.req.text)
        dic_Reqvalue = json.loads(self.req.text)
        token_value = dic_Reqvalue['data']['accessToken']
        print('accessToken:', token_value)
        return token_value

    def tearDown(self):
        pass


