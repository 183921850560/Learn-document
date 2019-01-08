# coding=utf-8
import readConfig
import requests
from Log.write_Log import MyLog
import os
import time
import traceback


class RequestsAPI:
    def __init__(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.data = {}
        self.param = {}
        self.json = None
        self.file = None
        self.response = None
        self.url = ''

    def set_url(self, url, url_param='', param_type='data'):
        # self.url = 'http://%s:%s' % (self.host, self.port)
        if url.startswith('/'):
            self.url = self.url + url
        else:
            self.url = self.url + '/' + url
        if param_type.lower() == 'url':
            self.url = self.url + '/' + url_param

    def set_data(self, data):
        self.data = data

    def set_json(self, data):
        self.json = data

    def set_param(self, param):
        self.param = param

    def set_file(self, file):
        if file.strip() != '':
            file_path = os.path.join(readConfig.proDir, file)
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    self.file = {'file': f}
            else:
                self.logger.error('File %s is not exists' % file_path)

    def get_response(self, method, **request_param):

        result = True
        start_time = time.time()
        try:
            self.response = requests.request(method=method,  **request_param)
        except Exception as ex:
            result = False
            self.response = traceback.format_exc()
            self.logger.error(traceback.format_exc())
        finally:
            end_time = time.time()

        return result, end_time - start_time, self.response


if __name__ == '__main__':
    api = RequestsAPI()
    api.set_file('config.ini')