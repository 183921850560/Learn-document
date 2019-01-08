# coding=utf-8
import unittest
import paramunittest
import readConfig
from common import log
from common import common
from common import configHttp
from datetime import datetime
import xlrd
import hashlib
from common import configDB

#将对应的变量提取出来
sheet = common.get_xls_sheet("saveUser.xls", "saveUser")
test_xls = common.get_xls_param(sheet)
test_param_name = common.get_xls_key(sheet)
localReadConfig = readConfig.readConfig()
confighttp = configHttp.configHTTP()

#使用paramunittest.parametrized对表中获取的参数进行参数化
@paramunittest.parametrized(*test_xls)
class saveUser(unittest.TestCase):
    def setParameters(self, case_name, method, url, guid, address,unitGuid, mobilephone, telephone, userName, userPwsd,userCode,
                      roleGuids,operatorUserId, remark, expireDate, userGroupGuid,loginSmsVarify, sessionTimeOut,msg):
        self.case_name = str(case_name)
        self.method = str(method)
        self.url = str(url)
        # 用MD5算法来加密userPwsd
        userCode_hash = hashlib.md5(userPwsd.encode(encoding='UTF-8')).hexdigest()
        # 将expireDate转换成当前的时间
        expireDate_time = xlrd.xldate_as_datetime(expireDate,0)
        self.user_co = str(int(userCode))
        self.param = [int(guid),str(address), int(unitGuid), str(int(mobilephone)), str(telephone),str(userName), str(int(userCode)),
                      eval(roleGuids), int(operatorUserId),str(remark), datetime.strftime(expireDate_time, '%Y-%m-%d'),
                      int(userGroupGuid), int(loginSmsVarify), int(sessionTimeOut),int(msg)]
        ##将加密过的userPwsd添加到self.param列表中
        self.param.insert(6,userCode_hash)
        print(self.param)
        self.msg = int(msg)
        self.response = None
        self.info = None

    # 前置条件（打印出获取的日志和将日志开始的标志）
    def setUp(self):
        self.log = log.MyLog.get_log()
        self.logger = self.log.get_logger()
        print(self.case_name+"test will start....")

    # 操作步骤（创建用户）
    def testsaveUser(self):

        #获取请求的url
        confighttp.set_url(self.url)

        #传入对应的报头（header）
        header = {
            "content-type": "application/json",
            "appCode":"XYWPT",
            "verifyCode":"fa8ea9cf-354f-420b-a095-5781c826afef"
        }

        #获取请求的报头
        confighttp.set_header(header)

        #将sheet中test_param_name和self.para对应起来，并传成字典形式
        data = dict(zip(test_param_name, self.param))
        #获取对应的databody
        confighttp.set_data(data)

        #获取请求的方法
        self.response = confighttp.post()

        #检查结果
        self.checkResult()

    #检查结果
    def checkResult(self):
        self.info = self.response.json()
        print(self.info)
        print('hhhhhhhhhhhhhhhhhhhhhhhh')
        print("check result------")
        if self.response.status_code == 200:
                self.assertEqual(self.msg, self.info['code'])

                # 连接数据库
                db = configDB.MyDB()
                print('mysql connect success')

                # 如果能取到self.user_co（为userCode），则查询该条数据成功
                execute_sql = db.executeSQL('select * from jczl_user where userCode=' + self.user_co)
                # 返回一条数据并打印出来
                result = db.get_one(execute_sql)
                print(result)
        else:
            self.logger.info(self.info)
            self.assertEqual(self.response.status_code, 200)


    #清理环境数据
    def tearDown(self):
        print("test over")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(saveUser("testsaveUser"))
    runner = unittest.TextTestRunner()
    runner.run(suite)






