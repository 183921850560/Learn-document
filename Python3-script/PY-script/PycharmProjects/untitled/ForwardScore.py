# -*-coding:utf-8 -*-
import requests
import json
import unittest

'''
Author:gxl
Headline:4.10.2评分消息下发
Time：2018-05-21
'''

class Score(unittest.TestCase):
    def setUp(self):
        #定义报头
        self.header = {'Content-Type':'application/json'}

    def test_Score(self):
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
        self.sco_uri = 'http://122.112.212.213:8777/api/v1/screen/forwardScore?access_token='
        self.score_url = self.sco_uri + self.token_value

        #传入请求的参数
        self.Score_data = {
            "requestId": "11132131231221",
            "url": "http://192.168.2.217:9000/sendInfo1",

            "message": [

           {
            "registerCode": "32201234562018091888",
            "content": {
                "score": 88,
                "level": 6,
                "scoreDesc": "干嘛呢呢扭扭捏捏袅袅娜娜哪各国国歌古古怪怪哪哪密密麻麻密密",
                "protectDay": 888888888,
                "protectStartDate": "2018-02-01",
                "dataSwTime": 5,
                "runningDatas": [
                    {
                        "date": "2018-09-01",
                        "runningTimes": 50,
                        "runningDistance": 3010
                    },
                    {
                        "date": "2018-09-02",
                        "runningTimes": 90,
                        "runningDistance": 6010
                    },
                    {
                        "date": "2018-09-03",
                        "runningTimes": 26,
                        "runningDistance": 1010
                    },
                    {
                        "date": "2018-09-04",
                        "runningTimes": 10,
                        "runningDistance": 2001
                    },
                    {
                        "date": "2018-09-05",
                        "runningTimes": 1120,
                        "runningDistance": 5010
                    },
                    {
                        "date": "2018-09-06",
                        "runningTimes": 700,
                        "runningDistance": 500
                    },
                    {
                        "date": "2018-09-07",
                        "runningTimes": 190,
                        "runningDistance": 10
                    }
                ]
            }
        },
        {
            "registerCode": "31101122332018091007",
            "content": {
                "score": 8,
                "level": 6,
                "scoreDesc": "你好干嘛呢呢扭扭捏捏袅袅娜娜哪",
                "protectDay": 999999999,
                "protectStartDate": "2018-02-01",
                "dataSwTime": 5,
                "runningDatas": [
                    {
                        "date": "2018-09-01",
                        "runningTimes": 50,
                        "runningDistance": 3020
                    },
                    {
                        "date": "2018-09-02",
                        "runningTimes": 20,
                        "runningDistance": 6100
                    },
                    {
                        "date": "2018-09-03",
                        "runningTimes": 80,
                        "runningDistance": 1010
                    },
                    {
                        "date": "2018-09-04",
                        "runningTimes": 80,
                        "runningDistance": 2600
                    },
                    {
                        "date": "2018-09-05",
                        "runningTimes": 50,
                        "runningDistance": 5000
                    },
                    {
                        "date": "2018-09-06",
                        "runningTimes": 70,
                        "runningDistance": 510
                    },
                    {
                        "date": "2018-09-07",
                        "runningTimes": 1190,
                        "runningDistance": 110
                    },
                    {
                        "date": "2018-09-08",
                        "runningTimes": 90,
                        "runningDistance": 10
                    }
                ]
            }
        }

    ]
}
        #将传入的参数转换成json格式
        self.Score_value = json.dumps(self.Score_data)

        #请求给智能屏下发基本信息
        self.Score_req = requests.post(headers=self.header, url=self.score_url, data=self.Score_value)
        print('Code status:', self.Score_req.status_code, self.Score_req.json())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()