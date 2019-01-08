# -*-coding:utf-8 -*-
import requests
import time
import json
import random

url = 'http://172.18.20.244:8200/v1/triggerPri'

headers = {'Content-Type': 'application/json'}
params = {
    "triggerID": "220000080",
    "triggerPri": 0
}

triggerID = 220000003
cameraID = 44001102
num = int(input("input test num:"))
n = 1

beginTime = int(time.time())

while (n <= num):
    params["triggerID"] = str(triggerID)
    params["cameraID"] = str(cameraID)
    if (n%200 == 0):
        params["cameraID"] = "172.18.20.88:21"
        params["cameraType"] = 1
    else:
        params["cameraType"] = 3
    values = json.dumps(params)
    req = requests.post(url, data=values, headers=headers)
    #content = req.text
    if(req.status_code == 200):
        print('%s triggerID:%s cameraID:%s  status_code:%s' % (n, params["triggerID"], params["cameraID"], req.status_code))
    else:
        print(req.text)
    triggerID += 1
    cameraID += 1
    n += 1
    sleepTime = random.randrange(1, 5) / 10
    time.sleep(sleepTime)
endTime = int(time.time())

print("Running Time: %s" % (endTime-beginTime))