# coding=utf-8
import unittest
import paramunittest
import readConfig
from common import log
from common import common
from common import configHttp

#将变量提取出来
sheet = common.get_xls_sheet("userLogin.xls", "userLogin")
test_xls = common.get_xls_param(sheet)
test_param_name = common.get_xls_key(sheet)
localReadConfig = readConfig.readConfig()
confighttp = configHttp.configHTTP()

#使用paramunittest.parametrized对表中获取的参数进行参数化
@paramunittest.parametrized(*test_xls)
class userLogin(unittest.TestCase):
    def setParameters(self, case_name, method, url, userCode, userPwsd, msg):
        self.case_name = str(case_name)
        self.method = str(method)
        self.url = str(url)
        self.param = [str(userCode), str(userPwsd)]
        self.msg = int(msg)
        self.response = None
        self.info = None

    #前置准备（记录日志）
    def setUp(self):
        self.log = log.MyLog.get_log()
        self.logger = self.log.get_logger()
        print(self.case_name+"test will start....")

    #操作步骤（用户登陆）
    def testuserLogin(self):

        #获取请求的URL
        confighttp.set_url(self.url)

        #传入对应的报头信息（header）
        header = {
            "content-type": "application/json",
            "appCode":"TLW",
            "verifyCode":"06b97038-e6e0-4bd0-a875-fd0fb25560e8"
        }
        confighttp.set_header(header)

        #将sheet中test_param_name和self.param字段进行组装成字典形式
        data = dict(zip(test_param_name, self.param))
        confighttp.set_data(data)

        #传入请求方法
        self.response = confighttp.post()

        #结果检查
        self.checkResult()

    #检查结果（登陆的结果）
    def checkResult(self):
        self.info = self.response.json()
        print(self.info)
        print("check result------")
        if self.response.status_code == 200:
                self.assertEqual(self.msg, self.info['code'])
        else:
            self.logger.info(self.info)
            self.assertEqual(self.response.status_code, 200)

    #清理数据和环境
    def tearDown(self):
        print("test over")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(userLogin("testuserLogin"))
    runner = unittest.TextTestRunner()
    runner.run(suite)





