#coding=utf-8
import os
import random
import string
from urllib3 import encode_multipart_formdata


advert = {
    "host": "http://10.10.0.244",
    "port": "10080",
    "timeout": 5,
    "headers": {"content-type": 'application/json; charset=UTF-8',
                "User-Agent": "Mozilla/5.0 ",
                "token": "123456789"
                }
}

contentName = "测试at_"+ "".join(random.sample(string.ascii_letters + string.digits, 8)) # 随机生成广告内容名称
file_path = os.path.abspath("./TestCase/AdPlatform_tmp/dsp/_global.py")  # 当前文件的绝对路径
material_path = "/Users/zhengqiang/123.jpg"

content_guid = ['1181', '1215', '1214', '1209', '1208', '1207', '1206', '1198', '1197', '1194', '1192', '1191', '1190', '1183', '1182', '1216']

content_contentName = ['测试at_vi8NYMqZ', '测试at_lTBpwXaM', '测试at_KB3LUzAG', '测试at_kyx0wi1p', '测试at_tI03TxEC', '测试at_Th4QRCL9', '测试at_DZ5oNs8V', '测试at_LHip9DyO', '测试at_f4VzulKg', '测试at_dUtqxO7P'] 


def get_content(num, data_type="list"):
    tmp = ""
    guids_list = random.sample(content_guid, num)
    if data_type == "str":
        tmp = ",".join(guids_list)
    elif data_type == "list" :
        tmp = guids_list
    elif num == 1 and data_type == "int":
        tmp = int(guids_list[0])
    return tmp

def get_contentName():
    return  random.sample(content_contentName,1)[0]

