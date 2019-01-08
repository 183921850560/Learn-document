# coding=utf-8
import hmac
import hashlib
import base64
import datetime
import requests

#定义全局变量/v2/triggers/{trigger_id}/status
url = 'http://store-test.yun-ti.com:8245/'
path = "/v2/triggers/66626"
method = "PATCH"
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

#获取所需的body
body = {
    "triggerPri": 12
}

#增加get请求的url参数
#value1 = {
#"storeID":"eb539f6a-8d69-4dc2-bdb7-50a0b45200f9"
#}

#定义请求的类型
req = requests.patch(url+path, json=body, headers=headers)#params=value1,
content = req.text

#打印相应的值
print(content)
print('status_code:', req.status_code)
