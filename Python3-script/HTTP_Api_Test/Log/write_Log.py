# coding = utf-8
import time
import threading
import os
import readConfig
import logging


class Log:
    def __init__(self):
        global proDir, reportPath
        proDir = readConfig.proDir
        reportPath = os.path.join(proDir, 'Report')
        if not os.path.exists(reportPath):
            os.mkdir(reportPath)
        self.logPath = os.path.join(reportPath, time.strftime('%Y%m%d', time.localtime()))  # 修改日志文件夹目录名称
        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)  # defined log level

        # defined handler
        handler = logging.FileHandler(os.path.join(self.logPath, time.strftime('%Y%m%d', time.localtime())+'.log'), 'w')
        # defined formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger

    def get_log_path(self):
        return self.logPath


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log


if __name__ == "__main__":
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.debug('test debug dddd')
    logger.info('test info ddd')
    logger.error('sserror   ')
    logger.warning('warn')
