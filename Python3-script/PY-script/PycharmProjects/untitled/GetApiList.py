# *_* coding:utf-8 *_*

import json
import requests
import unittest

'''
author: gxl
headline: 4.3.1 获取接口能力集
time：2018/12/24
'''

class getApiList(unittest.TestCase):
    #获取token值
    def setUp(self):
        #定义传入的报头信息
        self.header = {'Content-Type':'application/json'}

        # 定义获取token的url
        self.token_url = 'http://122.112.212.213:8777/api/v1/getToken'

        # 定义获取token的appkey和AppSecret
        self.token_data = {
            'AppKey': 'soKAM14J7hXQpEVbnBOdYzqUySR9kju5',
            'AppSecret': '3Zd0O6ExyC9mhJUHg4WsDvGSNATBfkKV'
        }
        # 将传入的data值换成json格式
        self.token_data_json = json.dumps(self.token_data)

        # 利用post请求触发并返回token值
        self.token_req = requests.post(headers=self.header, url=self.token_url, data=self.token_data_json)
        self.token_value = self.token_req.json()['data']['accessToken']

    def test_getApiList(self):
        # 传入获取电梯基本信息的url
        self.getApiList_url = 'http://122.112.212.213:8777/api/v1/global/getApiList?access_token=' + self.token_value

        #传入获取电梯基本信息的data
        self.getApiList_data = {
            'limit':10
        }
        self.getApiList_data_json = json.dumps(self.getApiList_data)

        #利用post请求获取电梯的基本信息
        self.getApiList_req = requests.post(headers=self.header, url=self.getApiList_url, data=self.getApiList_data_json)
        print('Code status:',self.getApiList_req.status_code, self.getApiList_req.json())

        # 验证结果
        print('.........................开始验证结果.........................')
        if self.getApiList_req.status_code == 200:
            self.assertEqual(self.getApiList_req.json()['code'], 0)
        else:
            self.assertEqual(self.getApiList_req.status_code, 200)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()



