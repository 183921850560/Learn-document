# coding=utf-8
import hmac
import hashlib
import base64
import datetime
import requests

#定义全局变量/v2/triggers/{trigger_id}/status
url = 'http://172.18.20.244:8201'
path = "/v2/triggers/66613/status"
method = "GET"
sk = "36REuGSACkX1qkyhQXvsKIqfcjVgDjCDiq36Bbgk"
ak = "TFVINCVAHHJMNPIVJTEF"

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
'''
#获取所需的body
body = {
    "triggerStoreType": 1,
    "triggerType": 2,
    "triggerPri": 2,
    "triggerTime": 1515487286,
    "beforeTime": 120,
    "afterTime": 20,
    "cameraID": "780246606",
    "cameraChan": 1,
    "cameraType": 1
}
'''
#定义请求的类型
req = requests.get(url+path,  headers=headers)
content = req.text

#打印相应的值
print(content)
print('status_code:', req.status_code)
