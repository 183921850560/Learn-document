# coding=utf-8
import re
import time
import traceback
from Lib.write_Log import MyLog
from Lib import comparators


class CheckResult:
    def __init__(self, response, validate):
        self.check = 0
        self.msg = ''
        self.response = response
        self.validate = validate
        self.r_value = []
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def verify_result(self):
        response = self.parse_response()
        verify_result = None
        verify_msg = ""
        for check_point in self.validate:
            for comp, verify in check_point.items():
                result = None
                uniform_comparators = comparators.get_uniform_comparator(comp)
                check_content, expect = verify
                dict_keys = check_content.split(".")

                if "status_code" in dict_keys:
                    result = response["status_code"]

                elif uniform_comparators == "set_data":
                    self.set_data(verify,response["body"])
                    continue
                elif uniform_comparators == "set_headers":
                    self.get_data_by_key(check_content.split(".")[-1], response["body"])
                    var_value = self.r_value.copy()
                    self.r_value.clear()
                    self.set_header(var_value[0],expect,response["headers"])
                    continue
                else:
                    if self.check_keys(dict_keys) == "dict":
                        tmp = response["body"]
                        try:
                            for key in dict_keys[1:]:
                                tmp = tmp[key]
                            result = tmp
                        except KeyError :
                            verify_result = 1
                            verify_msg += "Can't find key_value in response body"
                            return verify_result, verify_msg
                    elif self.check_keys(dict_keys) == "list":
                        self.get_data_by_key(dict_keys[-1],response["body"])
                        result = self.r_value.copy()
                        self.r_value.clear()
                try:
                    if not getattr(comparators, uniform_comparators)(result, expect):
                        verify_result = 0
                        verify_msg += " %s: %s  %s ;"%(check_content, uniform_comparators,expect)
                except AssertionError as e:
                    verify_result = 1
                    verify_msg += " %s:  %s ;" % (check_content,str(e))
                    return verify_result, verify_msg
        return verify_result,verify_msg

    def check_keys(self,key_list):
        for key in key_list:
            if key.endswith("[]"):
                return "list"
            else:
                continue
        return "dict"
    def parse_response(self):
        """
        parse the response into dictionary, like
        response={
        "status_code": 200,
        "headers": headers,
        "body": body content
        }
        :return:  response dict
        """
        response = {}
        response["status_code"] = self.response.status_code
        response["headers"] = self.response.headers
        try:
            response["body"] = self.response.json()
        except ValueError:
            response["body"] = self.response.text
        return response


    def get_data_by_key(self, key, data_dict):  # 根据key查找字典中对应的value值
        # value = []
        if isinstance(data_dict, list):
            for ll in data_dict:
                self.get_data_by_key(key, ll)
        elif key in data_dict.keys():
            self.r_value.append(str(data_dict[key]))
        else:
            for i in data_dict.keys():
                if isinstance(data_dict[i], dict):  # value值为dict类型
                    if key in data_dict[i].keys():
                        self.r_value.append(str(data_dict[i][key]))

                    else:
                        self.get_data_by_key(key, data_dict[i])
                elif isinstance(data_dict[i], (list, tuple)):  # value 值为list tuple类型
                    for l in data_dict[i]:
                        if isinstance(l, dict):
                            if key in l.keys():
                                self.r_value.append(str(l[key]))


    @staticmethod
    def lower_key(origin_dict):
        if not origin_dict or not isinstance(origin_dict, dict):
            return origin_dict

        return {
            key.lower(): value
            for key, value in origin_dict.items()
        }

    def set_header(self, var_value,file_path,headers):
        value = ""
        try:
            value = headers[var_value]
        except KeyError as e:
            self.logger.error(e)
        tmp_dict = {var_value:value}
        self.write_to_file(file_path,"headers",tmp_dict)

    def set_data(self,verify, value):
        result = None
        keys, file_path = verify
        keys_list = keys.split(".")
        if self.check_keys(keys_list) == "dict":
            tmp = value.copy()
            try:
                for key in keys_list[1:]:
                    tmp = tmp[key]
                result = tmp
            except KeyError as e:
                return False, str(e)
        else:
            self.get_data_by_key(keys_list[-1], value)
            result = self.r_value
        self.write_to_file(file_path,"%s_%s"%(keys_list[0],keys_list[-1]),result)

    def write_to_file(self, file_path, key, value):
        status = False
        regex = r'^(%s = )' % key
        with open(file_path, "r") as f:
            w_line = ""
            for line in f:
                if re.findall(regex, line):
                    status = True
                    if isinstance(value, str):
                        w_line += "%s = \"%s\" \n"%(key,str(value))
                    else:
                        w_line += "%s = %s \n" % (key, value)
                else:
                    w_line += line
            if not status:
                if isinstance(value, str):
                    w_line += "\n%s = \"%s\" \n" % (key, str(value))
                else:
                    w_line += "\n%s = %s \n" % (key, value)

        with open(file_path, "w") as f:
            f.write(w_line)
        time.sleep(4)
