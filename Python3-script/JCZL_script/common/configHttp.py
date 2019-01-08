# -*- coding:utf-8 -*-

import json
import requests
import sys
sys.path.insert(0, '/Python3-script/JCZL_script')
import readConfig
from common.log import *
localReadConfig = readConfig.readConfig()


class configHTTP:
    # 初始化执行设置host, port, timeout为全局变量（后续可以修改）
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_http("url")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.cookies = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0

    #获取URL
    def set_url(self, url):
        self.url = host + ":" + port + url

    #获取header（信息报头）
    def set_header(self, headers):
        self.headers = headers

    #获取需要传递的参数
    def set_params(self, params):
        self.params = params

    #获取请求的data
    def set_data(self, data):
        self.data = json.dumps(data)


    #获取cookie
    def set_cookies(self, cookies):
        self.cookies = cookies

    #获取文件（打开文件）
    def set_files(self, files):
        if files != '':
            file_path = readConfig.proDir + files
            self.files = {'file': open(file_path, 'rb')}
        if files == '' or files is None:
            self.state = 1

    #获取get的请求
    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, cookies=self.cookies, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out")
            return None

    #获取post请求方法
    def post(self):
        """
        defined post method with json
        :return:
        """
        try:
            self.logger.info("set url:"+self.url)
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,
                                     cookies=self.cookies, timeout=float(timeout))
            # response.raise_for_status()
            self.logger.info("data:%s response status: %d  header:%s files: %s timeout:%s"
                             % (self.data, response.status_code, self.headers, self.files, timeout))
            self.logger.info("Response data: %s " % response.json())
            self.logger.info("="*160)
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    #获取put请求方法
    def put(self):
        try:
            response = requests.put(self.url, data=self.data, headers=self.headers, cookies=self.cookies, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")

    #获取delete请求
    def delete(self):
        try:
            response = requests.delete(self.url, data=self.data, headers=self.headers, cookies=self.cookies, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error('Time out!')

    #post方法请求的异常处理（对于文件）
    def postWithFile(self):
        """
        defined post method with file
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    #对post返回值为none的处理
    def postWithNone(self):
        """
        defined post normal method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None


if __name__ == "__main__":
    print("ConfigHTTP")