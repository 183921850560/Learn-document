# _*_ coding:UTF-8 _*_

'''
Author:gxl
Headline:4.2.1获取电梯注册码列表
Time：2018-05-21
'''

import json
import requests
import unittest

class LiftList(unittest.TestCase):
    def setUp(self):
        # 添加报头
        self.header = {'Content-Type': 'application/json'}

    #获取token值
    def test_GetCodesList(self):
        # 定义获取token的url
        self.url = 'http://122.112.212.213:8777/api/v1/getToken'

        # 传入对应的AppKey和AppSecret
        self.data = {
            'AppKey': 'soKAM14J7hXQpEVbnBOdYzqUySR9kju5',
            'AppSecret': '3Zd0O6ExyC9mhJUHg4WsDvGSNATBfkKV'
        }
        self.value = json.dumps(self.data)

        #请求并打印token值
        self.req = requests.post(url=self.url, headers=self.header, data=self.value)

        #将取出来的json值转换成字典形式
        self.dic_data = json.loads(self.req.text)

        #获取token变量
        self.token_value = self.dic_data['data']['accessToken']

        #定义获取电梯注册码的url
        self.uri= 'http://122.112.212.213:8777/api/v1/info/getLiftRegCodes?access_token='
        self.Codes_ListUrl =  self.uri + self.token_value

        # 传入对应的AppKey和AppSecret
        self.data = {}
        self.value = json.dumps(self.data)

        #请求获取电梯的注册码列表
        List_req = requests.post(url=self.Codes_ListUrl, headers=self.header, data=self.value)
        print('Code status:', List_req.status_code, List_req.text)

    def tearDown(self):
        pass


