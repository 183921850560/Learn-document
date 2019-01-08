# coding=utf-8
import hmac
import hashlib
import base64
import datetime
import requests
import time

#获取当前时间作为triggerID
triggerID = str(time.time())
print(triggerID)

#定义全局变量
path1 = "/v2/triggers/"
url = 'http://store-test.yun-ti.com:8245/'
method = "PUT"
sk = "36REuGSACkX1qkyhQXvsKIqfcjVgDjCDiq36Bbgk"
ak = "TFVINCVAHHJMNPIVJTEF"

#获取triggerID
path = path1 + triggerID
print(path)


#获取当前的日期为date
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
date = datetime.datetime.utcnow().strftime(GMT_FORMAT)
print(date)

#获得所需的stringToSign
stringToSign = "%s\n\n\n%s\n%s" % (method, date, path)
stringToSign = stringToSign.encode(encoding='utf_8')
print(stringToSign)

#根据base64算法算出stringSign_value的值
sk_str = sk.encode(encoding='utf_8')
stringSign = hmac.new(sk_str, stringToSign,  digestmod=hashlib.sha1).digest()
#stringSign2= stringSign.encode(encoding='utf_8')
stringSign_value = base64.b64encode(stringSign)
print(stringSign_value)

#获取报头Authorization的value值
value = 'AWS ' + ak + ':' + stringSign_value.decode()
print(value)

#定义报头
headers = {
    'Content-Type1': 'application/json',
    'Date': date,
    'Content-Type':'text/plain',
    'Authorization': value
}

#获取所需的body
body = {
    "triggerStoreType": 1,
    "triggerType": 2,
    "triggerPri": 0,
    "triggerTime": 1514791525 ,
    "beforeTime": 80,
    "afterTime": 20,
    "cameraID": "780246606",
    #"videoFileName":"20171123/0_0_20171123065658_20171123070138_1.h264",
    "cameraChan": 1,
    "cameraType": 1
}

#定义请求的类型
req = requests.put(url+path, json=body, headers=headers)
content = req.text

#打印相应的值
print(content)
print('status_code:', req.status_code)
