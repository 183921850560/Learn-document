# -*-coding:utf-8 -*-
import requests
import json
import unittest

'''
Author:gxl
Headline:4.10.3 救援信息下发
Time：2018-05-21
'''

class RescueInfo(unittest.TestCase):
    def setUp(self):
        #定义报头
        self.header = {'Content-Type':'application/json'}

    def test_RescueInfo(self):
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
        self.Res_uri = 'http://122.112.212.213:8777/api/v1/screen/forwardRescueInfo?access_token='
        self.RescueInfo_url = self.Res_uri + self.token_value

        #传入请求的参数
        self.RescueInfo_data = {
            "registerCode": "31101122332018091007",  # ""32201234562018091888",  # 31101122332018091007
            "content": {
                "rescuer": "周三",
                "phoneNum": "18888888889",
                "latitude": 31.183111,
                "longitude": 121.184011,
                "status": 5,
                "statusDesc": "1"
            }

        }
        #将传入的参数转换成json格式
        self.RescueInfo_value = json.dumps(self.RescueInfo_data)

        #请求给智能屏下发基本信息
        self.RescueInfo_req = requests.post(headers=self.header, url=self.RescueInfo_url, data=self.RescueInfo_value)
        print('Code status:', self.RescueInfo_req.status_code, self.RescueInfo_req.json())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()