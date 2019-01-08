# -*- coding:utf-8 -*-

import logging
import time
import threading
import sys
sys.path.insert(0, '/Python3-script/JCZL_script') #进入和readConfig的同级目录
import readConfig
import os


class Log:
    def __init__(self):
        global logPath, resultPath, proDir

        #导入文件的路径
        proDir = readConfig.proDir
        # print(proDir)

        #加入resultPath路径
        resultPath = os.path.join(proDir, "result")
        # print(resultPath)

        #如果不存在resultPath，则创建一个resultPath
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)

        #以当前的本地时间来写日志然后加入到resultPath下
        logPath = os.path.join(resultPath, time.strftime('%Y%m%d%H%M%S', time.localtime()))

        #如果logPath不存在，则创建一个logPath
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        self.logger = logging.getLogger()

        #打印日志的级别为info级别
        self.logger.setLevel(logging.INFO)

        #打印日志输出到logPath目录下的output.log文件中
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))


        #打印日志的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        #增加打印日志的目录
        self.logger.addHandler(handler)

    #返回self.logger信息
    def get_logger(self):
        return self.logger

    #日志开始行区分
    def build_start_line(self, case_no):
        self.logger.info("--------" + case_no + " START--------")

    #日志的结束行区分
    def build_end_line(self, case_no):
        self.logger.info("--------" + case_no + " END--------")

    #日志中的信息是以case_name加上信息
    def build_case_line(self, case_name, msg):
        self.logger.info(case_name + " - msg:" + msg)

    #获取测试报告的路径并加入testReport.html文件路径
    def get_report_path(self):
        report_path = os.path.join(logPath, "testReport.html")
        return report_path

    #获取结果的路径
    def get_result_path(self):
        return logPath

    #将测试结果写进测试报告中
    def write_result(self, result):
        result_path = os.path.join(logPath, "report.txt")
        fb = open(result_path, "wb")
        try:
            fb.write(result)
        except FileNotFoundError as ex:
            self.logger.error(str(ex))

#创建自己的log
class MyLog:
    log = None
    #定义个进程锁
    mutex = threading.Lock()

    def __init__(self):
        pass

    #使用静态类方法（不需要实例化，直接类名.方法名()来调用）
    @staticmethod
    def get_log():
        if MyLog.log is None:
            #在进程中获取锁
            MyLog.mutex.acquire()
            MyLog.log = Log()
            #获取日志后释放锁
            MyLog.mutex.release()
        #返回日志
        return MyLog.log

if __name__ == "__main__":
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.debug("test debug")
    logger.info("test info")
