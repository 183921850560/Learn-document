# coding=utf-8
'''
author:gongxiaolong
testname:根据摄像头ID及录像时间回放录像
createtime:2018-05-08
'''
import hmac
import hashlib
import base64
import datetime
import requests

#定义全局变量/v2/triggers/{trigger_id}/status
url = 'http://172.18.20.244:8201'
path = "/v2/video/"
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
    'Content-Type': 'text/plain',
    'Authorization': value
}

#定义请求的类型
value1 = {
    # #"storeID":"eb539f6a-8d69-4dc2-bdb7-50a0b45200f9"
    # "triggerID":1515741333.5240407,
    "cameraID":"172.18.20.88:21",#浙大摄像头填写ftp服务器地址；海康摄像头填写摄像头ID号
    "cameraChan":1,
    "startTime":"1515487166",
    "stopTime":"1515487186"
    }
req = requests.get(url+path, params=value1,  headers=headers)
content = req.text

#打印相应的值
print(content)
print('status_code:', req.status_code)
