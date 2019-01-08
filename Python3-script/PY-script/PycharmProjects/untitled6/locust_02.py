# coding=utf-8
from locust import *

class MyTest(TaskSet):
    @task(weight=1)
    def upgrade(self):
        param ={
            "duSerial": "139615688",
            "protocol":1,
            "serverIp": "172.16.16.68",
            "serverPort":21,
            "fileUrl":"digicap180723.dav",
            "account":"ftpxiao",
            "password":"g18392185056",
            "version":"V5.5.0 build 180723"
        }
        response = self.client.post(name='upgrade', url='/api/v2/device/upgrade', json=param, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failure('error')


    @task(weight=1)
    def upgrade_process(self):
        param = {
            "duSerial": "139615688",
            "version":"V5.5.0 build 180830"
}
        response = self.client.post(name='upgrade_process', url='/api/v2/device/upgradeprogress', json=param, catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failure('error')

    @task(weight=1)
    def setconfig(self):
        param = {
	        "duSerial":"139615688",
	        "sensitivityParamList":[
		       {
			       "sensitivityIndex":0,
			       "sensitivityValue":100
		       },
		       {
			       "sensitivityIndex":1,
			       "sensitivityValue":100
		       },
		       {
			       "sensitivityIndex":2,
			       "sensitivityValue":100
		       },
		       {
			       "sensitivityIndex":3,
			       "sensitivityValue":100
		       },
		       {
			       "sensitivityIndex":4,
			       "sensitivityValue":100
		       },
		       {
			       "sensitivityIndex":5,
			       "sensitivityValue":100
		       },
		       {
			       "sensitivityIndex":6,
			       "sensitivityValue":100
		       }
	]
}
        response = self.client.post(name='setconfig', url='/api/v2/door/setconfig', json=param,
                                    catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failure('error')

    @task(weight=1)
    def getconfig(self):
        param = {
            "duSerial": "139615688"
        }
        response = self.client.post(name='getconfig', url='/api/v2/door/getconfig', json=param,
                                    catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failure('error')

    @task(weight=1)
    def setconfig_02(self):
        param = {
    "duSerial": "150561379",
    "screenLength":500,
    "screenWidth": 800,
    "fieldDetectionRegions":[
        {
            "timeThreshold":0,
            "sensitivity":50,
            "objOccupation":0,
            "regionType":0,
            "coordinatesList":[
                {
			    "xaxis": 140,
			    "yaxis": 523
		         },
                {
			    "xaxis": 650,

			    "yaxis": 511
		         },
                {
			    "xaxis": 654,
			    "yaxis": 758
		         },
                {
			    "xaxis": 150,
			    "yaxis": 764
		         }
            ]
        }

    ]
}
        response = self.client.post(name='setconfig_02', url='/api/v2/area/setconfig', json=param,
                                    catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failure('error')

    @task(weight=1)
    def getlocalrecordfiles(self):
        param = {
            "duSerial": "139615688"
        }
        response = self.client.post(name='getlocalrecordfiles', url='/api/v2/device/getlocalrecordfiles', json=param,
                                    catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failure('error')

    @task(weight=1)
    def getconfig_03(self):
        param = {
            "duSerial": "139615688"
        }
        response = self.client.post(name='getconfig_03', url='/api/v2/area/getconfig', json=param,
                                    catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failure('error')

    @task(weight=1)
    def onlinelist(self):
        param = {}
        response = self.client.post(name='onlinelist', url='/api/v2/device/onlinelist', json=param,
                                    catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failure('error')

    @task(weight=1)
    def getaddr(self):
        param = {
            "duSerial": "139615688"
        }
        response = self.client.post(name='getaddr', url='/api/v2/device/getaddr', json=param,
                                    catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failure('error')

    @task(weight=1)
    def sdp(self):
        param = {
            "duSerial": "139615688"
        }
        response = self.client.post(name='sdp', url='/api/v2/stream/real/sdp', json=param,
                                    catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failure('error')

    @task(weight=1)
    def heartbeat(self):
        param = {
            "duSerial": "139615688"
        }
        response = self.client.post(name='heartbeat', url='/api/v2/stream/heartbeat', json=param,
                                    catch_response=True)
        if response.status_code == 200:
            response.success()
            print(response.json())
        else:
            response.failure('error')


class Run(HttpLocust):
    task_set = MyTest
    host = 'http://eag-test.yun-ti.com:8100'
    max_wait = 10000
    min_wait = 2000
