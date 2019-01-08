# *_* coding:utf-8 *_*
import json
import requests
import unittest
'''
author: gxl
headline: 4.7.1 请求实时视屏授权
time：2018-05-21
'''

class getRealvideoAuthorization(unittest.TestCase):
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
        self.getRealvideoAuthorization_url = 'http://122.112.212.213:8777/api/v2/media/getRealvideoAuthorization?access_token=' + self.token_value

        #传入获取电梯基本信息的data
        self.getRealvideoAuthorization_data = {
            'registerCode':'34303446022018087568'
        }
        self.getRealvideoAuthorization_data_json = json.dumps(self.getRealvideoAuthorization_data)

        #利用post请求获取电梯的基本信息
        self.getRealvideoAuthorization_req = requests.post(headers=self.header, url=self.getRealvideoAuthorization_url, data=self.getRealvideoAuthorization_data_json)
        print('Code status:',self.getRealvideoAuthorization_req.status_code, self.getRealvideoAuthorization_req.json())

        # 验证结果
        print('.........................开始验证结果.........................')
        if self.getRealvideoAuthorization_req.status_code == 200:
            self.assertEqual(self.getRealvideoAuthorization_req.json()['code'], 0)
        else:
            self.assertEqual(self.getRealvideoAuthorization_req.status_code, 200)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()





# #定义url
# url = 'http://122.112.212.213:8777/api/v2/media/getRealvideoAuthorization?access_token=aa43d6c55d994b839b7a5a0a6989a251bb42c28b822ab31372127b22cbd38aabca9a91cb5b53a9a8'
# #添加报头
# header = {'Content-Type': 'application/json'}
# #传入对应的AppKey和AppSecret
# databody={
#     'registerCode':'201807301022000001',
#     }
# #打印出json格式的databody
# value = json.dumps(databody)
# #跳转post请求,并打印出来
# req = requests.post(url, data=value, headers=header)
# content = req.text
# print(content)
# #打印请求的状态
# print('status_code:', req.status_code)
