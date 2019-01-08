# *_* coding:utf-8 *_*
import json, time
import requests
import unittest
'''
author:gxl
headline:4.2.2 获取电梯的基本信息
time：2018-05-21
'''

class getLiftInfo(unittest.TestCase):
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

    def test_getLiftInfo(self):
        # 传入获取电梯基本信息的url
        self.getLiftInfo_url = 'http://122.112.212.213:8777/api/v2/lift/getInfo?access_token=' + self.token_value

        #传入获取电梯基本信息的data
        self.getLiftInfo_data = {
            "registerCodes": ['31103301102014075069']
        }
        self.getLiftInfo_data_json = json.dumps(self.getLiftInfo_data)

        #利用post请求获取电梯的基本信息
        self.getLiftInfo_req = requests.post(headers=self.header, url=self.getLiftInfo_url, data=self.getLiftInfo_data_json)
        print('Code status:',self.getLiftInfo_req.status_code, self.getLiftInfo_req.json())

        # 验证结果
        print('.........................开始验证结果.........................')
        if self.getLiftInfo_req.status_code == 200:
            self.assertEqual(self.getLiftInfo_req.json()['code'], 0)
        else:
            self.assertEqual(self.getLiftInfo_req.status_code, 200)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()




