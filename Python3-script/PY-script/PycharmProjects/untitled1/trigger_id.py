# -*-coding:utf-8 -*-
import requests
import time
import json
import random
'''
author:gongxiaolong
headline:触发trigger
time：2018-05-21
'''

url = 'http://172.18.20.244:8201/v1/trigger'
headers = {'Content-Type': 'application/json'}
params ={
     "triggerID":800,
    "triggerStoreType": 1,
    "triggerType": 2,
    "triggerPri": 2,
    "triggerTime": 1515374255,
    "beforeTime": 120,
    "afterTime": 20,
    #"vedioFileName": "20170321/0_0_20170321135311_20170321135339_1.h264",
    "cameraID": "780246568",
    "cameraChan": 1,
    "cameraType": 1
}
triggerID = 300000
cameraID = 300000
num = int(input("input test num:"))
n = 1

beginTime = int(time.time())

while (n <= num):
    params["triggerID"]= str(triggerID)
    params["triggerTime"] = int(time.time())
    params["cameraID"] = str(cameraID)
    if (n%200 == 0):
        params["cameraID"] = "172.18.20.88:21"
        params["cameraType"] = 1
    else:
        params["cameraType"] = 3
    values = json.dumps(params)
    req = requests.put(url, data=values, headers=headers)
    #content = req.text
    if(req.status_code == 200):
        print('%s triggerID:%s cameraID:%s  status_code:%s' % (n, triggerID, params["cameraID"], req.status_code))
    else:
        print(req.text)
    triggerID += 1
    cameraID += 1
    n += 1
    sleepTime = random.randrange(1, 9) / 10
    time.sleep(sleepTime)
endTime = int(time.time())

print("Running Time: %s" % (endTime-beginTime))