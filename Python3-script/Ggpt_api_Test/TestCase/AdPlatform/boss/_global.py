# coding=utf-8
import os
import base64
import random
import string
import re
import time


advert_env = {
    "host": "https://test.yun-ti.com",# http://10.10.0.244" 开发
    "port": "10092",  # 10090 开发
    "timeout": 5,
    "headers": {
        "content-type": 'application/json; charset=UTF-8',
        "User-Agent": "Mozilla/5.0 "
    }
}

base_platform_env = {
    "host": "http://122.112.243.207", # 测试环境： 122.112.243.207:9999， 开发环境：http://10.10.0.244
    "port": "9999",
    "timeout": 5,
    "headers": {
        "appCode": "ADVERT",
        "verifyCode": "7f9bbc05-d26d-4f5c-abf8-8512751af72c",
        "Content-Type": "application/json; charset=UTF-8"
    }
}

file_path = os.path.abspath("./TestCase/AdPlatform/boss/_global.py")
companyName = "测试cn_" + "".join(random.sample(string.ascii_letters + string.digits, 10))
phoneNumber = "15958021797"
old_phone = "18458418558"
inviteCode = "u5uoasng"

# 自定义函数
def get_random(end):
    return float("%.1f"%random.uniform(1,end))

def adplatform():
    if "headers" in advert_env.keys() and headers :
        advert_env["headers"].update(headers)
    return advert_env

def base_platform():
    return base_platform_env

def get_companyName(num):
    return companyName * num  # 随机生成广告内容名称

def get_licenceNo():
    return "".join(random.sample(string.digits, 8))

def get_encode_str(word_type="password", word=None):
    base_str = ""
    if word_type == "sms":
        base_str = "XZL.TZX.ADV@%s" % str(sms_verifyCode)
    else:
        base_str = "XZL.TZX.ADV@%s" % str(word)
    return base64.b64encode(base_str.encode()).decode('utf-8', 'ignore')

def clear_headers():
    print("clear headers......")
    write_to_file(file_path,"headers",{})

def write_to_file(file_path, key, value):
    status = False
    regex = r'^(%s = )' % key
    with open(file_path, "r") as f:
        w_line = ""
        for line in f:
            if re.findall(regex, line):
                status = True
                if isinstance(value, str):
                    w_line += "%s = \"%s\" \n"%(key,str(value))
                else:
                    w_line += "%s = %s \n" % (key, value)
            else:
                w_line += line
        if not status:
            if isinstance(value, str):
                w_line += "%s = \"%s\" \n" % (key, str(value))
            else:
                w_line += "%s = %s \n" % (key, value)

    with open(file_path, "w") as f:
        f.write(w_line)

def do_sleep():
    print("sleep {num}s, please wait ....".format(num=5))
    time.sleep(int(5))

def do_switch():
    """
    交换password值
    :return:
    """
    old = old_password
    new = new_password
    write_to_file(file_path,"old_password", new)
    write_to_file(file_path,"new_password", old)

old_password = "zq123456" 
new_password = "zq12345678" 

# 自动写入参数
app_customerGuid = 10000122
app_customerId = 10000122
app_companyName = "测试name" 

sms_verifyCode = "357654" 
app_guid = 22272 
user_guid = "20090"

headers = {'advert-server': 'af60ba30-bf42-497d-aeca-f66f62c22ffe'}

app_inviteCode = "u5boaxzh" 

app_clienteleGuid = 10000124 
