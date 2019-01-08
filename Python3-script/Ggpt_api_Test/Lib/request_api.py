# coding=utf-8
import requests
from Lib.write_Log import MyLog
import os
import time
import traceback
from urllib3 import encode_multipart_formdata
from Lib.common import Common


class RequestsAPI:
    def __init__(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.data = {}
        # self.param = {}
        # self.json = None
        self.file = None
        self.response = None
        # self.url = ''
        self.headers = {}

    def set_file(self, file_data):
        key, file = file_data
        if file.strip() != '':
            if os.path.isfile(file):
                self.data, self.headers["Content-Type"] = self.encode_file_data(file,key)
            else:
                self.logger.error('File %s is not exists' % file)

    def encode_file_data(self, file_path,key_name):
        data = {}
        data[key_name] = (file_path.split("/")[-1], open(file_path, 'rb').read())
        data_encode = encode_multipart_formdata(data)
        return data_encode

    @Common.retry(3)
    def get_response(self, **request_param):
        if self.headers:
            request_param["headers"].update(self.headers)
        if self.data:
            request_param["data"] = self.data
        start_time = time.time()
        result = True
        # try:
        self.response = requests.request(**request_param)
        #     self.logger.info(self.response.text)
        # except Exception as ex:
        #     result = False
        #     self.response = traceback.format_exc()
        #     self.logger.error(traceback.format_exc())
        end_time = time.time()

        return result, end_time - start_time, self.response