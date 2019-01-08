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
import base64


sheet = common.get_xls_sheet("createUser.xls", "createUser")
test_xls = common.get_xls_param(sheet)
test_param_name = common.get_xls_key(sheet)
localReadConfig = readConfig.readConfig()
confighttp = configHttp.configHTTP()

#使用paramunittest.parametrized对表中获取的参数进行参数化,以便生成多个用例
@paramunittest.parametrized(*test_xls)

class CreateUser(unittest.TestCase):
    def setParameters(self, case_name, method, url, address,
                      unitGuid, mobilephone, telephone, userName, userCode, userPwsd, roleGuids,
                      operatorUserId, remark, expireDate, userGroupGuid,
                      loginSmsVarify, sessionTimeOut,msg):
        self.case_name = str(case_name)
        self.method = str(method)
        self.url = str(url)

        #将expireDate转换成当前的时间
        expireDate_time = xlrd.xldate_as_datetime(expireDate,0)
        self.user_co = str(int(userCode))

        #用MD5算法来加密userPwsd
        userCode_hash = hashlib.md5(userPwsd.encode(encoding='UTF-8')).hexdigest()
        # userCode_hash = base64.b64encode(userPwsd.encode()).decode("utf-8")
        self.param = [str(address), int(unitGuid), str(int(mobilephone)), str(telephone),str(userName), str(int(userCode)),
                      eval(roleGuids), int(operatorUserId),str(remark), datetime.strftime(expireDate_time, '%Y-%m-%d'),
                      int(userGroupGuid), int(loginSmsVarify), int(sessionTimeOut),int(msg)]

        #将加密过的userPwsd添加到self.param列表中
        self.param.insert(6, userCode_hash)
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
    def test_createUser(self):

        #获取url
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

        #检查结果（将返回的信息转换成json格式并打印出来）
        self.info = self.response.json()
        print(self.info)
        print("check result------")
        #如果返回的数据状态为200，则对比msg的返回码是否和code一致
        if self.response.status_code == 200:
                self.assertEqual(self.msg, self.info['code'])
                #连接数据库
                db = configDB.MyDB()
                print('mysql connect success')
                #如果能取到self.user_co（为userCode），则删除该条数据成功
                db.executeSQL('delete from jczl_user where userCode=' + self.user_co)
                #关闭数据库
                db.closeDB()
        else:
            #如果返回不是200，则返回日志信息并返回状态信息和200比较
            self.logger.info(self.info)
            self.assertEqual(self.response.status_code, 200)

    #清理创建的数据
    def tearDown(self):
        print("test over")


if __name__ == "__main__":
    #第一种执行用例的方法
    unittest.main()

    #第二种执行用例的方法
    # # 构建测试集
    # suite = unittest.TestSuite()
    # suite.addTest(CreateUser('test_createUser'))
    # # 执行测试脚本
    # runner = unittest.TextTestRunner()
    # runner.run(suite)





