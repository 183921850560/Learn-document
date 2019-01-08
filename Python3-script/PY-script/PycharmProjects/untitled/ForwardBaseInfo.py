# -*-coding:utf-8 -*-
import requests
import json
import unittest

'''
Author:gxl
Headline:4.10.1给智能屏下发基本信息
Time：2018-05-21
'''

class BaseInfo(unittest.TestCase):
    def setUp(self):
        #定义报头
        self.header = {'Content-Type':'application/json'}

    def test_BaseInfo(self):
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
        self.Info_uri = 'http://122.112.212.213:8777/api/v1/screen/forwardBaseInfo?access_token='
        self.BaseInfo_url = self.Info_uri + self.token_value

        #传入请求的参数
        self.BaseInfo_data = {
            "requestId": "11132131231221",
            "url": "http://192.168.2.217:9000/sendInfo",
            "message": [
                {
                    "registerCode": "32201234562018091888",
                    "content": {
                        "isWxbView": 1,
                        "isWxbEnable": 1,
                        "wxbPhoneNum": "138484848484",
                        "tips": "ths 可以返回一个合法的以JSON表示的结果出",
                        "ssid": "QQQwifi",
                        "password": "QQQQQQQQ",
                        "qrcodeSwTime": 5,
                        "qrcodeList": [
                            {
                                "qrcode": "testestets",
                                "desc": "estestets"
                            },
                            {
                                "qrcode": "本意是没有找到任何请求的数据",
                                "desc": "忐忑鹅鹅鹅饿飞飞飞"
                            }
                        ]
                    }

                },
                {
                    "registerCode": "31101122332018091007",
                    "content": {
                        "isWxbView": 1,
                        "isWxbEnable": 1,
                        "wxbPhoneNum": "40040040004000",
                        "tips": "th cecessdfsfdfsdfsdfsdfssdddddddddddddddd",
                        "ssid": "QQQwifi",
                        "password": "QQQQQQQQ",
                        "qrcodeSwTime": 5,
                        "qrcodeList": [
                            {
                                "qrcode": "xxxxx",
                                "desc": "xxxxx"
                            },
                            {
                                "qrcode": "WWWWWWW",
                                "desc": "GOGOGOGOGOGOGOGOGOGOGOO!!!!!!!!!"
                            }
                        ]
                    }

                }

            ]

        }
        #将传入的参数转换成json格式
        self.BaseInfo_value = json.dumps(self.BaseInfo_data)

        #请求给智能屏下发基本信息
        self.BaseInfo_req = requests.post(headers=self.header, url=self.BaseInfo_url, data=self.BaseInfo_value)
        print('Code status:', self.BaseInfo_req.status_code, self.BaseInfo_req.json())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()