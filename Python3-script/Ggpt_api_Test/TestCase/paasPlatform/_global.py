# coding=utf-8
import os
import base64
import random
import string
import re


paas_env = {
    "host": "http://122.112.251.59",
    "port": "20090",
    "timeout": 5,
    "headers": {
        "content-type": 'application/json; charset=UTF-8',
        "User-Agent": "Mozilla/5.0 ",
        "x-xzl-appkey":  "appkey12"
    }
}
headers = {}
account = "test_" + "".join(random.sample(string.ascii_letters + string.digits, 10))

def paasPlatform():
    if "headers" in paas_env.keys() and headers :
        paas_env["headers"].update(headers)
    return paas_env

file_path = os.path.abspath("./TestCase/paasPlatform/_global.py")

account_Id = 9130

account_Account = "test_40010a01101" 
