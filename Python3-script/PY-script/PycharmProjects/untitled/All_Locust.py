# coding=utf-8
from locust import *
import json, requests

'''
Author: gxl
Headline: all open platform performance
Time：2018/12/29
'''

global value,header,token_value
value=json.dumps({"AppKey": "soKAM14J7hXQpEVbnBOdYzqUySR9kju5","AppSecret": "3Zd0O6ExyC9mhJUHg4WsDvGSNATBfkKV"})
header = {'Content-Type': 'application/json'}
token_value = requests.post(url='http://122.112.212.213:8777/api/v1/getToken', headers=header, data=value).json()['data']['accessToken']

class Open_platform(TaskSet):
    #4.1.1获取token接口
    @task(weight=1)
    def get_token(self):
        response = self.client.post(name='get_token', url='/api/v1/getToken', data=value, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')


    #4.2.1获取电梯注册码列表
    @task(weight=1)
    def getLiftRegCodes(self):
        url = '/api/v1/info/getLiftRegCodes?access_token=' + token_value
        response = self.client.post(name='getLiftRegCodes', url=url, json='', catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')


    #4.2.2获取电梯基本信息
    @task(weight=1)
    def GetLiftInfo(self):
        url = '/api/v2/lift/getInfo?access_token=' + token_value
        data = {"registerCodes": ['31103301102014075069']}
        response = self.client.post(name='GetLiftInfo', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')

    #4.3.1获取接口能力集
    @task(weight=1)
    def getApiList(self):
        url = '/api/v1/global/getApiList?access_token=' + token_value
        data = {'limit':10}
        response = self.client.post(name='getApiList', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')


    #4.4.1获取电梯历史告警
    @task(weight=1)
    def getLiftHisAlarm(self):
        url = '/api/v1/alarm/getLiftHisAlarm?access_token=' + token_value
        data = {
            "registerCodes": ["33010800300070173000"],
            "PageSize": 5,
            "PageIndex": 1,
            "beginTime": 1542612107,
            "endTime": 1545722507
        }
        response = self.client.post(name='getLiftHisAlarm', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')

    #4.5.1获取电梯当前状态
    @task(weight=1)
    def getLiftStatus(self):
        url = '/api/v1/status/getLiftStatus?access_token=' + token_value
        data = {'registerCode':'32201234562018090898'}
        response = self.client.post(name='getLiftStatus', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')


    #4.6.1获取电梯环境监测数据
    @task(weight=1)
    def getLiftPointData(self):
        url = '/api/v1/point/getLiftPointData?access_token=' + token_value
        data = {'registerCode':'32201234562018090898'}
        response = self.client.post(name='getLiftPointData', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')


    #4.7.1请求实时视频授权
    @task(weight=1)
    def getRealvideoAuthorization(self):
        url = '/api/v2/media/getRealvideoAuthorization?access_token=' + token_value
        data = {'registerCode':'32201234562018090898'}
        response = self.client.post(name='getRealvideoAuthorization', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')


    #4.8.1查询历史视频信息
    @task(weight=1)
    def getLocalRecordFiles(self):
        url = '/api/v1/media/getLocalRecordFiles?access_token=' + token_value
        data = {
            "registerCodes":['34303446022018087568'],
            "beginTime": 1545538332,
            "endTime": 1545619891
        }
        response = self.client.post(name='getLocalRecordFiles', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')

    #4.8.2请求历史视频授权
    @task(weight=1)
    def getRecordvideoAuthorization(self):
        url = '/api/v1/media/getRecordvideoAuthorization?access_token=' + token_value
        data = {
            "registerCode":'31103301102013090157',
            "beginTime": 1545883932,
            "endTime": 1545984970,
            "channel": 0,
            "authType": "token"
        }
        response = self.client.post(name='getRecordvideoAuthorization', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')


    #4.8.3请求历史告警视频授权
    @task(weight=1)
    def getAlarmvideoAuthorization(self):
        url = '/api/v1/media/getAlarmvideoAuthorization?access_token=' + token_value
        data = {
            "alarmCode":'176b1015-3692-48bc-9b29-0df66ad54b68',
            "authType": "token"
        }
        response = self.client.post(name='getAlarmvideoAuthorization', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')

    #4.9.1请求对讲授权
    @task(weight=1)
    def getAudiotalkAuthorization(self):
        url = '/api/v1/media/getAudiotalkAuthorization?access_token=' + token_value
        data = {
            "registerCode":"32201234562018090460",
            "channel":0,
            "authType":"appkey"
        }
        response = self.client.post(name='getAudiotalkAuthorization', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')

    #4.10.1基本信息下发
    @task(weight=1)
    def BaseInfo(self):
        url = '/api/v1/screen/forwardBaseInfo?access_token=' + token_value
        data = {
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
        response = self.client.post(name='BaseInfo', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')


    #4.10.2评分信息下发
    @task(weight=1)
    def Score(self):
        url = '/api/v1/screen/forwardScore?access_token=' + token_value
        data = {
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
        response = self.client.post(name='Score', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')

    #4.10.3救援信息下发
    @task(weight=1)
    def forwardRescueInfo(self):
        url = '/api/v1/screen/forwardRescueInfo?access_token=' + token_value
        data = {
            "registerCode": "32201234562018091888",  # ""32201234562018091888",  # 31101122332018091007
            "content": {
                "rescuer": "周三",
                "phoneNum": "18888888889",
                "latitude": 31.183111,
                "longitude": 121.184011,
                "status": 5,
                "statusDesc": "1"
            }

        }
        response = self.client.post(name='forwardRescueInfo', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')


    #4.10.4获取维保屏幕状态
    @task(weight=1)
    def Status(self):
        url = '/api/v1/screen/status?access_token=' + token_value
        data = {
            "requestId": "11132131231221",
            "url": "http://192.168.2.217:9000/sendInfo",
            "message": [
               {
                   "registerCode": "32201234562018091888"
               },
               {
                   "registerCode": "31101122332018091007"
               }
            ]
        }
        response = self.client.post(name='Status', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')


    #4.10.6根据智能屏ID获取电梯注册编码
    @task(weight=1)
    def getRegisterCode(self):
        url = '/api/v2/screen/getRegisterCode?access_token=' + token_value
        data = {
            "screenId":"B44F96030E66"
        }
        response = self.client.post(name='getRegisterCode', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')

    #4.11.1设备配置接口
    @task(weight=1)
    def Device_config(self):
        url = '/api/v1/device/config?access_token=' + token_value
        data = {
            "requestId": "11132131231221",
            "url": "http://192.168.2.217:9000/sendInfo",
            "message": [
                {
                    "registerCode": "201807681",
                    "commandCode": "1000001"
                }
            ]
        }
        response = self.client.post(name='Device_config', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')

    #4.12.1单位信息查询
    @task(weight=1)
    def getunitphone(self):
        url = '/api/v1/estate/getUnitPhone?access_token=' + token_value
        data = {
            "registerCodes": ["32201234562018091399", "31103301102010090041", "32201234562018090632"]
        }
        response = self.client.post(name='getunitphone', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')

    #4.13.1请求获取异常电梯设备列表
    @task(weight=1)
    def getAbnormal(self):
        url = '/api/v1/ops/getAbnormalDevList?access_token=' + token_value
        data = {
            "subDevType": "all"
        }
        response = self.client.post(name='getAbnormal', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')


    #4.14.1 96333电梯状态保存
    @task(weight=1)
    def Liftstatus(self):
        url = '/api/v1/lift/saveCheckStatus?access_token=' + token_value
        data = {
            "registerCodes": ["32201234562018091346", "32201234562018011025"],
            "verifyTime": "2018-12-11 09:00:00",
            "verifyResult": "2"
        }
        response = self.client.post(name='Liftstatus', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')

    #4.14.2 96333电梯状态查询
    @task(weight=1)
    def getCheckStatus(self):
        url = '/api/v1/lift/getCheckStatus?access_token=' + token_value
        data = {
            "registerCodes": ["32201234562018091346", "32201234562018011025", "33101239682018106881"]
        }
        response = self.client.post(name='getCheckStatus', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')

    #4.15.5查询近期电梯厅门开关次数
    @task(weight=1)
    def getlatestdoorswitchtime(self):
        url = '/api/v1/statistics/getLatestLiftDoorSwitchTimes?access_token=' + token_value
        data = {
            "registerCodes":["31103305022015100005"],
            "beginTime":1545717594,
            "endTime":1545890394
        }
        response = self.client.post(name='getlatestdoorswitchtime', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')

    #4.15.6查询近期电梯运行次数
    @task(weight=1)
    def getlatestliftrunningtime(self):
        url = '/api/v1/statistics/getLatestLiftRunningTimes?access_token=' + token_value
        data = {
            "registerCodes": ["31103305022015100005"],
            "beginTime": 1546063692,
            "endTime": 1546063872
        }
        response = self.client.post(name='getlatestliftrunningtime', url=url, json=data, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failture('error')


class run(HttpLocust):
    task_set = Open_platform
    host = 'http://122.112.212.213:8777'
    max_wait = 10000
    min_wait = 2000










