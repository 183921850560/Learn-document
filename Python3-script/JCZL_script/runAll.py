#coding=utf-8
'''
HTMLTestRunnerv2 Statistical chart of test cases
HTMLTestReportCN 美化界面
'''
import HTMLTestRunnerv2 as HTMLTestRunner
import unittest
from common.log import MyLog
import readConfig
from common.configEmail import MyEmail
import os
import webbrowser

localReadConfig = readConfig.readConfig()

class TestAll:
    #执行所有用例前进行初始化下面的全局变量
    def __init__(self):
        global log, logger, resultPath, status
        log = MyLog.get_log()
        logger = log.get_logger()
        resultPath = log.get_report_path()
        status = localReadConfig.get_email('status')
        self.caseListFile = os.path.join(readConfig.proDir, "caselist.txt")
        self.caseFile = os.path.join(readConfig.proDir, "testCase")
        self.caseList = []
        self.email = MyEmail.get_email()

    #读取caselist.txt文件中的内容
    def set_case_list(self):
        try:
            fb = open(self.caseListFile)
            for value in fb.readlines():
                value= value.strip() #去掉首尾的空白行
                data = str(value)
                if data != '' and not data.startswith("#"):
                    self.caseList.append(data.replace("\n", ""))
        except Exception as e:
            logger.error("open caselistfile error! msg:%s" % e)
        finally:
            fb.close()

    #批量创建测试套并将单个测试套添加到suite_module列表中
    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in self.caseList:
            case_name = case.split("/")[-1]
            print("caseName: %s" % case_name)
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)
        print(suite_module)

        #在suite_module中找到单个测试套，并将测试用例的名称添加到单个测试套中
        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    # add testcase
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    #开始运行测试套
    def run(self):
        try:
            suit = self.set_case_suite()
            if suit is not None:
                logger.info("=======Test Start==========")
                #在resultPa(测试报告的html文件）路径下打开文件
                with open(resultPath, 'wb') as file:
                    runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='InterFaceTest Report',
                                                           description='Device Access Server Interface Test Project')
                    runner.run(suit)
            else:
                logger.info("No Case to Run")
        except Exception as e:
            logger.error("run function error : %s " % e)
        finally:
            webbrowser.open(resultPath)  # open result file
            logger.info("===========Test End=============")
            # reset sessionID enable:0
            if localReadConfig.get_session("isenable") == "1":
                localReadConfig.set_session('isenable', "0")


if __name__ == '__main__':
    print("********start*********")
    obj = TestAll()
    obj.run()
    print("********end*********")
