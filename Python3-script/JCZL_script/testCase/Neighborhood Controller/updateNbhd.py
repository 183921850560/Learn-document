# coding=utf-8

import unittest
import paramunittest
import readConfig
from common import log
from common import common
from common import configHttp
from common import configDB

#将需要用到的常量提取出来
sheet = common.get_xls_sheet("updateNbhd.xls", "updateNbhd")
test_xls = common.get_xls_param(sheet)
test_param_name = common.get_xls_key(sheet)
localReadConfig = readConfig.readConfig()
confighttp = configHttp.configHTTP()

#使用paramunittest.parametrized对表中获取的参数进行参数化
@paramunittest.parametrized(*test_xls)

class updateNbhd(unittest.TestCase):
    def setParameters(self, case_name, method, url,guid,nbhdName,msg):
        self.case_name = str(case_name)
        self.method = str(method),
        self.url = str(url)
        self.guid_se = str(int(guid))
        self.nbhdName = str(nbhdName)
        self.param = [int(guid),str(nbhdName)]
        self.msg = int(msg)
        self.response = None
        self.info = None

    #前置条件（打印出获取的日志和将日志开始的标志）
    def setUp(self):
        self.log = log.MyLog.get_log()
        self.logger = self.log.get_logger()
        print(self.case_name+"test will start....")

    #操作步骤（创建用户）
    def testupdateNbhd(self):

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

        #连接数据库
        db = configDB.MyDB()

        #如果能取到self.user_co（为userCode），则删除该条数据成功
        execute_sql = db.executeSQL('select * from jczl_neighborhood where guid=' + self.guid_se )
        #返回一条数据并打印出来
        result = db.get_one(execute_sql)

        #关闭数据库
        db.closeDB()

        #校验修改的小区名称
        if list(result)[1] == self.nbhdName:
            print('para modify success')
        else:
            print('para modify error')

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(updateNbhd("testupdateNbhd"))
    runner = unittest.TextTestRunner()
    runner.run(suite)





