# coding=utf-8

import unittest
import paramunittest
import readConfig
from common import log
from common import common
from common import configHttp
import hashlib
from common import configDB

#将变量提出来
SQL = 'select * from jczl_user where userCode=9999'
FILE_PATH = 'D:\\Python3--script\\DASInterfaceTest --unittest\\testFile\\resetPwd.xls'

#调用configDB中的MyDB方法来连接数据库并查出对应的数据
db = configDB.MyDB()
sql_ex = db.executeSQL(SQL)
result= db.get_one(sql_ex)
print(result)
close_db = db.closeDB()

#获取数据表中的参数
sheet = common.get_xls_sheet("resetPwd.xls", "resetPwd")
test_xls = common.get_xls_param(sheet)
test_param_name = common.get_xls_key(sheet)
localReadConfig = readConfig.readConfig()
confighttp = configHttp.configHTTP()

#使用paramunittest.parametrized对表中获取的参数进行参数化
@paramunittest.parametrized(*test_xls)

class resetPwd(unittest.TestCase):
    def setParameters(self, case_name, method, url,operatorUserId, pwd, userGuid, msg):
        self.case_name = str(case_name)
        self.method = str(method)
        self.url = str(url)
        #将newpwd转换成MD5加密encoding='UTF-8')).hexdigest()
        newPwd_hash = hashlib.md5(pwd.encode(encoding='UTF-8')).hexdigest()
        self.param = [int(operatorUserId), int(userGuid)]
        self.param.insert(1,newPwd_hash)
        self.msg = int(msg)
        self.response = None
        self.info = None

    #前置条件（打印出获取的日志和将日志开始的标志）
    def setUp(self):
        self.log = log.MyLog.get_log()
        self.logger = self.log.get_logger()
        print(self.case_name+"test will start....")

    #操作步骤（创建用户）
    def testresetPwd(self):

        #传url
        confighttp.set_url(self.url)

        #填写请求的报头（header）
        header = {
            "content-type": "application/json",
            "appCode":"XYWPT",
            "verifyCode":"fa8ea9cf-354f-420b-a095-5781c826afef"
        }
        confighttp.set_header(header)

        #将sheet中test_param_name和self.param进行组装成字典形式
        data = dict(zip(test_param_name, self.param))
        confighttp.set_data(data)

        #传请求方式（为post）
        self.response = confighttp.post()

        #检查结果
        self.checkResult()

    #检查数据的创建是否成功
    def checkResult(self):
        #将返回的信息转换成json格式并打印出来
        self.info = self.response.json()
        print(self.info)
        print("check result------")
        #如果返回的数据状态为200，则对比msg的返回码是否和code一致
        if self.response.status_code == 200:
                self.assertEqual(self.msg, self.info['code'])
        else:
            #如果返回不是200，则返回日志信息并返回状态信息和200比较
            self.logger.info(self.info)
            self.assertEqual(self.response.status_code, 200)

    #清理创建的数据
    def tearDown(self):
        print("test over")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(resetPwd("testresetPwd"))
    runner = unittest.TextTestRunner()
    runner.run(suite)





