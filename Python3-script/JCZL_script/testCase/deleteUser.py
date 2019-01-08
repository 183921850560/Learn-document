# coding=utf-8

import unittest
import paramunittest
import readConfig
from common import log
from common import common
from common import configHttp
from common import configDB

#将变量提取出来
sheet = common.get_xls_sheet("deleteUser.xls", "deleteUser")
test_xls = common.get_xls_param(sheet)
test_param_name = common.get_xls_key(sheet)
localReadConfig = readConfig.readConfig()
confighttp = configHttp.configHTTP()

#使用paramunittest.parametrized对表中获取的参数进行参数化
@paramunittest.parametrized(*test_xls)

class deleteUser(unittest.TestCase):
    def setParameters(self, case_name, method, url,guid, operatorUserId, msg):
        self.case_name = str(case_name)
        self.method = str(method)
        self.url = str(url)
        self.guid_user = str(int(guid))
        self.param = [int(guid), int(operatorUserId)]
        self.msg = int(msg)
        self.response = None
        self.info = None

    #前置条件（打印出获取的日志和将日志开始的标志）
    def setUp(self):
        self.log = log.MyLog.get_log()
        self.logger = self.log.get_logger()
        print(self.case_name+"test will start....")

        #先查询数据库中是否存在要删除的数据（连接数据库）
        db = configDB.MyDB()
        print('mysql connect success')

        # 将需要删除的数据查询出来
        execute_sql = db.executeSQL('select * from jczl_user where guid=' + self.guid_user)
        # 返回一条数据并打印出来
        result = db.get_one(execute_sql)
        print(result)

    #操作步骤（创建用户）
    def testdeleteUser(self):

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
        print(data)

        #传请求方式（为delete）
        self.response = confighttp.delete()

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
    suite.addTest(deleteUser("testdeleteUser"))
    runner = unittest.TextTestRunner()
    runner.run(suite)





