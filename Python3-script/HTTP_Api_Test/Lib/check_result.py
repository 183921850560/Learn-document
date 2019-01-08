# coding=utf-8
import re
import time
import traceback
from Log.write_Log import MyLog


class CheckResult:
    def __init__(self, response, result):
        self.check = 0
        self.msg = ''
        self.response = response
        self.result = result
        self.r_value = []
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def parse_result(self):
        if self.result:
            check, msg = "", ""
            for key in self.result.keys():
                try:
                    check, msg = getattr(self, key)(self.result, self.response)
                except AttributeError as ex:
                    self.logger.error(traceback.format_exc())
                    return [-1, "用例中check_point：%s程序没有定义 " % key]
                if check:
                    return check, msg
            return check, msg
        else:
            return [1, "用例未定义check_point"]

    @staticmethod
    def status_code(result, response):
        if "status_code" in result.keys():
            if result["status_code"] == response.status_code:
                return [0, "返回status_code 符合预期"]
            else:
                return [1, "返回status_code与预期不一致, 预期返回%s ，实际返回：%s" %
                        (result["status_code"], response.status_code)]
        else:
            if response.status_code in range(200, 400):
                return [0, "返回status_code 正常"]
            else:
                return [1, "返回status_code：%s 异常" % response.status_code]

    def check_data(self, result, response):
        check = 1
        response_data = ''
        key = "result"
        target = response.text.lower()
        target = target.replace('null', 'None')
        target = target.replace('false', 'False')
        target = target.replace('true', 'True')
        target = eval(target)
        result = str(result).lower()
        result = eval(result)
        if key not in target.keys():
            if "data" in target.keys():
                key = "data"

        if result["check_data"].startswith('key'):  # 对比需要检查返回值里参数的内容
            f_key, f_value = re.findall(r'[^()]+', result["check_data"])[1].split(":")
            self.r_value = []
            self.get_data_by_key(f_key, target)  # 获取response中对应value
            if target[key]['totalsize'] == 0:
                return 1, "没有符合的数据返回"
            for k in self.r_value:
                if isinstance(k, str):
                    if k.find('[') >= 0:
                        k = k[1:-1]
                if k in f_value:
                    check = 0
                    response_data = '返回数据存在相应键值 %s: %s ' % (f_key, k)
            if check == 1:
                response_data = '返回数据中没有找到相应键值 %s' % f_key

        elif result["check_data"].startswith('size'):
            size = int(re.findall(r'[^()]+', result["check_data"])[1])
            # exp, size = re.findall(r'\d+|\D+', size_exp)
            if not isinstance(target[key]['data'], list):
                return 1, "返回数据data格式错误"
            list_len = len(target[key]['data'])
            total_size = target[key]['totalsize']
            if total_size <= size and list_len <= size:
                check = 0
            elif list_len == size:
                check = 0
            else:
                check = 6
            response_data = '返回数据total_size: %s, data Size：%s ,预期需返回Size：%s' % \
                            (total_size, list_len, size)

        elif result["check_data"].startswith('format'):
            format_str = re.findall(r'[^()]+', result["check_data"])[1]
            format_str = format_str.replace("y", "Y")
            data_list = target[key]["data"]
            if not isinstance(target[key]['data'], list):
                return 1, "返回数据data格式错误"
            if len(data_list):
                s_data = data_list[0]["statisticsdata"]
                if len(s_data):
                    for n in range(len(s_data)):
                        data_time = s_data[n]['statisticstime']
                        try:
                            time.strptime(data_time, format_str)
                            return 0, "返回数据时间格式正确，时间：%s" % data_time
                        except ValueError:
                            check = 1
                            response_data = "返回数据时间格式不正确，时间：%s" % data_time
                        except TypeError:
                            check = 1
                            response_data = "返回数据不正确，时间：%s" % data_time

                else:
                    check = 0
                    response_data = "返回数据statisticsData为空"

            else:
                check = 1
                response_data = "返回数据data为空"

        elif result["check_data"].startswith("offset"):
            offset, size = list(map(eval, re.findall(r'[^()]+', result["check_data"])[1].split(":")))
            if not isinstance(target[key]['data'], list):
                return 1, "返回数据data格式错误"

            list_len = len(target[key]['data'])
            total_size = target[key]['totalsize']
            check = 1
            res_size = 0
            if total_size:
                if total_size - offset < 1:
                    if list_len == 0:
                        check = 0
                elif total_size - offset in range(1, size):
                    if list_len == total_size - offset:
                        check = 0
                    res_size = total_size - offset
                elif total_size - offset >= size:
                    if list_len == size:
                        check = 0
                    res_size = size
            else:
                check = 0
            response_data = '返回数据total_size: %s, data Size：%s ,传入参数pageSize：%s,' \
                            ' start: %s, 需返回data_size: %s' \
                            % (total_size, list_len, size, offset, res_size)

        elif result["check_data"].startswith('time'):  # 根据时间范围对比数据返回是否正确
            s_time, e_time, name = re.findall(r'[^()]+', result["check_data"])[1].split(':')
            if not isinstance(target[key]['data'], list):
                return 1, "返回数据data格式错误"
            if key in target.keys() and target[key] not in ('', [], [''], {}, None, 'null'):
                if len(target[key]['data']) > 0:
                    for data in target[key]['data']:
                        if data[name] in range(int(s_time), int(e_time) + 1):
                            check = 0
                            response_data = '返回数据时间在条件时间范围内'
                        else:
                            check = 1
                            response_data = '返回数据时间不在条件时间范围内'
                            break
                else:
                    check = 1
                    response_data = '该时间范围内没有符合条件的数据返回'
            else:
                check = 10
                response_data = "返回数据异常，没有包含键值[%s],请检查Response内容" % "check_data"

        elif result["check_data"].startswith('name'):
            key_name = re.findall(r'[^()]+', result["check_data"])[1]
            if not isinstance(target[key]['data'], list):
                return 1, "返回数据data格式错误"
            if key in target.keys() and target[key] not in ('', [], [''], {}, None, 'null'):
                if len(target[key]['data']) > 0:
                    for data in target[key]['data']:
                        if key_name in data.keys():
                            check = 0
                            response_data = '返回数据包含[%s]的数据项' % key_name
                        else:
                            check = 1
                            response_data = '返回数据没有包含[%s]的数据内容' % key_name
                else:
                    check = 0
                    response_data = '没有符合条件的数据返回'
            else:
                check = 10
                response_data = "返回数据异常，没有包含键值[%s],请检查Response内容" % key

        elif result["check_data"].startswith('sort'):
            order_type, order_field = re.findall(r'[^()]+', result["check_data"])[1].split(":")
            array = []
            if not isinstance(target[key]['data'], list):
                return 1, "返回数据data格式错误"
            try:
                for l in target['result']['data']:
                    array.append(l[order_field])
            except KeyError as ex:
                check = 11
                response_data = '返回数据没有对应排序的字段%s ' % order_field
                self.logger.error(ex)
            if len(array) <= 1:
                check = 0
                response_data = '返回数据内容数量小于等于1，排序正确'
            elif len(set(array)) == 1:
                check = 12
                response_data = ['返回数据内容排序字段值相同，排序正确', "排序字段列表：%s\n" % array]
            else:
                order_res, res_type = self.is_sort(array)
                if order_res and res_type:
                    if res_type == order_type:
                        check = 12
                        response_data = ["返回数据排序符合预期，根据字段 %s ，按照%s 进行排序"
                                         % (order_field, order_type), "排序字段列表：%s\n" % array]
                    else:
                        check = 13
                        response_data = ["返回数据排序类型错误，预期：%s， 实际排序按照：%s 进行排序"
                                         % (order_type, res_type), "排序字段列表：%s\n" % array]
                else:
                    check = 14
                    response_data = ["返回数据未进行排序", '返回数据相应字段内容：%s' % array]

        elif result["check_data"].startswith('datatype'):
            data_list = target[key]['data']
            if not isinstance(target[key]['data'], list):
                return 1, "返回数据data格式错误"
            if len(data_list) < 1:
                check = 0
                response_data = "返回数据data列表为空"
                return check, response_data
            type_dict = {
                '1': 'screen_state',
                '2': 't_power',
                '3': 't_signal',
                '4': 'l_power',
                '5': 'l_signal',
                '6': 'camera_state',
                '7': 'l_plc_signal',
                '8': 't_plc_signal'
            }
            data_type = re.findall(r'[^()]+', result["check_data"])[1]
            res = ''
            if len(data_type) < 2:
                try:
                    if type_dict[data_type] in target[key]['data'].keys():
                        check = 0
                        response_data = '返回数据中包含设备类型：%s 的数据' % type_dict[data_type]
                    else:
                        check = 14
                        response_data = '返回数据中没有包含设备类型：%s 的数据' % type_dict[data_type]
                except KeyError as ex:
                    check = 8
                    response_data = "发生错误，KEY不存在，请检查用例是否正确"
                    self.logger.error(ex)
            else:
                data_type = data_type.split(",")
                for d_type in data_type:
                    try:
                        if type_dict[d_type] in data_list[0].keys():
                            check = 0
                            res = res + ' ' + type_dict[d_type]

                        else:
                            check = 15
                            response_data = '返回数据中没有包含设备类型：%s 的数据' % type_dict[d_type]
                            break

                    except KeyError as ex:
                        check = 8
                        response_data = "发生错误，KEY不存在，请检查用例是否正确"
                        self.logger.error(ex)
                        break
                response_data = '返回数据中包含设备类型：%s 的数据' % res.strip().replace(' ', ',')

        elif result["check_data"].startswith('type'):
            if not isinstance(target[key]['data'], list):
                return 1, "返回数据data格式错误"
            data_list = target[key]['data']
            if len(data_list) < 1:
                check = 1
                response_data = "返回数据data列表为空"
                return check, response_data
            types = re.findall(r'[^()]+', result["check_data"])[1].lower().split(",")
            for t in types:
                if t in data_list[0].keys():
                    check = 0
                    response_data = "返回数据正确，包含%s类型数据" % types
                else:
                    check = 1
                    response_data = "返回数据没有找到%s相应类型数据" % t
                    break

        elif result["check_data"].startswith('area'):
            areaType = int(result["check_data"].split(":")[1])
            self.r_value = []
            self.get_data_by_key("areacode", target)
            regex_dict = {
                "1": '^(\d{1,2}[0]{4})$',
                "2": '^(\d{4}[0]{2})$',
                "3": '^(\d{6})$',
                "4": '^(\d{9})$',
                "5": '^(\d{1,4})$',
                "6": '^(\d{9}-\d{4}-\d{4})$'
            }
            if not self.r_value:
                return 1, "返回数据未找到键值areaCode 的数据"
            if areaType in range(1, 7):
                for value in self.r_value:
                    if value == "None":
                        continue
                    elif re.findall(regex_dict[str(areaType)], value):
                        check = 0
                        response_data = "返回区域符合预期，areaCode：%s" % value
                    else:
                        return 1, "返回区域不符合预期，areaCode：%s" % value
            else:
                check = 1
                response_data = "用例对应areaType：%s 值不对" % areaType

        return check, response_data

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
    def is_sort(array):
        """
        检查数组是否排序
        :param array:
        :return:
        """
        result = True
        order = 'desc'
        if array == sorted(array):
            order = 'asc'
        elif array == sorted(array, reverse=True):
            order = 'desc'
        else:
            result = False
            order = None
        return result, order

    def check_code(self, result, response):
        """
        检查返回code是否正确
        :param result:
        :param response:
        :return:
        """
        check = 1
        code = str(result["check_code"])
        return_code = str(self.lower_key(response.json())["code"])
        if code == "0":
            if return_code == '0':
                check = 0
            else:
                check = 1

        elif re.findall(r'[^\d]', code):
            if re.findall(code, return_code):
                check = 0
            else:
                check = 1
        msg = "实际返回 Code: %s " % return_code
        return check, msg

    @staticmethod
    def lower_key(origin_dict):
        if not origin_dict or not isinstance(origin_dict, dict):
            return origin_dict

        return {
            key.lower(): value
            for key, value in origin_dict.items()
        }

    def set_data(self, result, response):
        target = response.json()["result"]
        if not target:
            return 1, "NO Token Get From Response Data"
        key, file_path = result["set_data"].split(":", 1)
        if key == "token":
            try:
                self.set_token(file_path, target)
            except FileNotFoundError:
                self.logger.error(traceback.format_exc())
                self.logger.info(target)
            return 0, "获取Token正确, 写入文件OK"

    @staticmethod
    def set_token(file, source_dict):
        with open(file, "r") as f:
            w_line = ""
            for line in f:
                if re.findall(r'^(token = \{)', line):
                    w_line += "token = " + str(source_dict)+"\n"
                else:
                    w_line += line

        with open(file, "w") as f:
            f.write(w_line)
