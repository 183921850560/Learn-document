#coding=utf-8
import time
from Lib.write_Log import MyLog
import traceback
from functools import wraps


class Common(object):

    def __init__(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    @classmethod
    def retry(cls, times=3):
        def wrap(method):
            @wraps(method)
            def fun(*args, **kwargs):
                start_num = 0
                msg = ""
                start_time = time.time()
                while start_num < times:
                    start_num += 1
                    try:
                        result = method(*args, **kwargs)
                        return result
                    except Exception:
                        print("Start execution function %s retry times: %s" %(method.__name__ ,start_num))
                        msg = traceback.format_exc()
                        time.sleep(1)
                        continue
                return False, time.time()-start_time, msg
            return fun
        return wrap

    @staticmethod
    def parse_response(response):
        tmp = {}
        try:
            tmp["result"] = response.json()
        except TypeError:
            tmp["result"] = response.text
        tmp["status_code"] = response.status_code

        return tmp

    def parse_content_dict(self, key, response_data):
        if not isinstance(response_data, dict) and "result" not in response_data.keys():
            return False, "response data type error or No valid data is included."

    @staticmethod
    def update_requests(data, original):
        """
        :param data: 更新数据
        :param original: 原始数据dict
        :return: 更新后的dict
        """
        if not isinstance(data, dict):
            return False, "input data type error"
        return original.update(data)

