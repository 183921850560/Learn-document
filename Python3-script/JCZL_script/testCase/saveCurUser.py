# coding=utf-8

import unittest
import paramunittest
import readConfig
from common import log
from common import common
from common import configHttp
from datetime import datetime
import xlrd
from common import configDB
import hashlib

#将对应的变量提出来
sheet = common.get_xls_sheet("saveCurUser.xls", "saveCurUser")
test_xls = common.get_xls_param(sheet)
test_param_name = common.get_xls_key(sheet)
localReadConfig = readConfig.readConfig()
confighttp = configHttp.configHTTP()

#使用paramunittest.parametrized对表中获取的参数进行参数化
@paramunittest.parametrized(*test_xls)

class saveCurUser(unittest.TestCase):
    def setParameters(self, case_name, method, url, guid, address, mobilephone, telephone, userName, userCode,
                      operatorUserId, remark, expireDate,loginSmsVarify, sessionTimeOut,msg):
        self.case_name = str(case_name)
        self.method = str(method)
        self.url = str(url)
        #将expireDate转换成当前的时间
        expireDate_time = xlrd.xldate_as_datetime(expireDate,0)
        self.user_co = str(int(userCode))
        self.param = [int(guid), str(address), str(int(mobilephone)), str(telephone), str(userName), str(int(userCode)),int(operatorUserId),
                      str(remark), datetime.strftime(expireDate_time, '%Y-%m-%d'), int(loginSmsVarify), int(sessionTimeOut),int(msg)]
        print(self.param)
        self.msg = int(msg)
        self.response = None
        self.info = None

    #前置条件（打印出获取的日志和将日志开始的标志）
    def setUp(self):
        self.log = log.MyLog.get_log()
        self.logger = self.log.get_logger()
        print(self.case_name+"test will start....")

    #操作步骤（创建用户）
    def testsaveCurUser(self):

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
        ff = confighttp.set_data(data)
        print(ff)

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

                #连接数据库
                db = configDB.MyDB()
                print('mysql connect success')

                #如果能取到self.user_co（为userCode），则查询该条数据成功返回
                execute_sql = db.executeSQL('select * from jczl_user where userCode=' + self.user_co )
                #返回一条数据并打印出来
                result = db.get_one(execute_sql)
                print(result)
        else:
            #如果返回不是200，则返回日志信息并返回状态信息和200比较
            self.logger.info(self.info)
            self.assertEqual(self.response.status_code, 200)

    #清理创建的数据
    def tearDown(self):
        print("test over")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(saveCurUser("testsaveCurUser"))
    runner = unittest.TextTestRunner()
    runner.run(suite)





