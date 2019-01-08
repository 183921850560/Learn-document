# coding=utf-8
import re
import os
import random


headers = {
    "User-Agent": "Mozilla/5.0 ",
    "Content-Type": "application/x-www-form-urlencoded"
}

port = "9095"
timeout = 15

err_code = '^(\d+\#){4}$'

elevatorIds = ['330110004-0051-1099', '330621001-0101-2325', '330110004-0051-1098', '330621001-0101-2326', '330110004-0051-1097', '330621001-0101-2323', '330110004-0051-1096', '330621001-0101-2324', '330110004-0051-1095', '330621001-0101-2321', '330110004-0051-1094', '330621001-0101-2322', '330110004-0051-1093', '330110004-0051-1092', '330621001-0101-2320', '330110010-0090-2132', '330110110-0067-1530', '330621001-0101-2329', '330110010-0090-2133', '330110010-0090-2130', '330621001-0101-2327', '330110010-0090-2131', '330621001-0101-2328', '330110010-0090-2136']

file_path = os.path.join(os.path.abspath("./TestCase/ZBP_Service/WeiXiaoBao/"), "_global.py")
token = {'expiresIn': '', 'accessToken': 'a356e36a-220c-443b-a62a-4b9eae36110f'}


def get_token():
    return "e2b2febe-90f1-4dc4-93ce-20cabbc46fba"


def get_expire_token():
    return "www"

def get_elevatorId():
    return random.sample(elevatorIds, 1)[0]


# set_file(token)
