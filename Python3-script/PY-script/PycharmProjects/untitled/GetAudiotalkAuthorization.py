# _*_ coding:UTF-8 _*_

'''
Author:gxl
Headline:4.9.1请求对讲授权
Time：2018-05-21
'''

import json
import requests
import unittest

class getAudiotalkAuthorization(unittest.TestCase):
    def setUp(self):
        # 添加报头
        self.header = {'Content-Type': 'application/json'}

    #获取token值
    def test_GetCodesList(self):
        # 定义获取token的url
        self.Token_url = 'http://122.112.212.213:8777/api/v1/getToken'

        # 传入对应的AppKey和AppSecret
        self.token_data = {
            'AppKey': 'soKAM14J7hXQpEVbnBOdYzqUySR9kju5',
            'AppSecret': '3Zd0O6ExyC9mhJUHg4WsDvGSNATBfkKV'
        }
        self.token_json = json.dumps(self.token_data)

        #请求并打印token值
        self.Token_req = requests.post(url=self.Token_url, headers=self.header, data=self.token_json)

        #将取出来的json值转换成字典形式
        self.dic_data = json.loads(self.Token_req.text)

        #获取token变量
        self.token_value = self.dic_data['data']['accessToken']
        # print(self.token_value)

        #定义获取对讲授权的url
        self.uri = 'http://122.112.212.213:8777/api/v1/media/getAudiotalkAuthorization?access_token='
        self.Talk_Url = self.uri + self.token_value

        # 传入对应的data值
        self.Talk_data = {
            "registerCode":"32201234562018090460",
            "channel":0,
            "authType":"appkey"
        }
        self.Talk_value = json.dumps(self.Talk_data)

        #请求获取对讲授权
        talk_req = requests.post(url=self.Talk_Url, headers=self.header, data=self.Talk_value)
        print('Code status:', talk_req.status_code, talk_req.text)

    def tearDown(self):
        pass


