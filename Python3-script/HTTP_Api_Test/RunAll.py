# coding=utf-8
import readConfig
from Lib.read_yml import ReadYml
from Lib.write_caselist import MakeCaseList
from Log.write_Log import MyLog
from Lib.request_api import RequestsAPI as api
from Lib.write_report import WriteReport
from Lib.parse_param_conf import ParseParam
from Lib.check_result import CheckResult
import os
import re
import webbrowser
import time
import traceback


class Run:
    def __init__(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.if_name = None
        self.url = None
        self.method = None
        self.data = None
        self.param = None
        self.report = WriteReport()
        self.r_value = []

    @staticmethod
    def prepare():
        """
        从目录 TestCase读取CaseFile文件明，并写入caseList.conf文件
        :return:
        """
        write_case = MakeCaseList()
        write_case.write_caselist()


    def get_case(self):
        """
        open file caseList.conf return caseName
        :return: yield caseName
        """
        file_list = os.listdir('./TestCase')
        for case_file in file_list:
            if os.path.isdir('./TestCase/' + case_file):
                continue
            elif not case_file.startswith('caseList'):
                continue
            else:
                try:
                    with open('./TestCase/' + case_file) as f:
                        for line in f.readlines():
                            line = "".join(line.split())  # remove \n ' '
                            if line != '' and not line.startswith('#'):
                                yield line
                except Exception as ex:
                    self.logger.error(traceback.format_exc())

    @staticmethod
    def set_session(response):
        session_id = re.findall('=(.+?);', response.headers['Set-Cookie'])[0]
        readConfig.ReadConfig().set_session('JSESSIONID', session_id)
        readConfig.ReadConfig().set_session('enable', '1')

    def run_case(self):
        total = 0
        if_total = 0
        prj_name = ''
        for interface_name in self.get_case():
            print("start test case : %s" % interface_name)
            if_total += 1
            if prj_name != interface_name.split("\\")[1]:
                prj_name = interface_name.split("\\")[1]
                self.report.set_prj_name(prj_name)
            try:
                file = '.\\TestCase\\' + interface_name + '.yml'
                if not os.path.isfile(file):
                    self.logger.error("File is Not exists: %s" % file)
                    if_total -= 1
                    print("Case File is not exists: %s" % file)
                    continue
                param_list = ["host", "port", "headers", "timeout"]
                param_dict = ParseParam().parse_param(param_list, file)

                if "host" in param_dict.keys() and "port" in param_dict.keys():
                    self.url = "http://%s:%s" % (param_dict.pop("host"), param_dict.pop("port"))
                else:
                    raise ValueError("Not found host in conf file ")

                case = ReadYml().open_yml(file_path=file)
                if 'enable' in case.keys():
                    if not case['enable']:
                        print("The case %s will not to be tested" % interface_name)
                        continue
                request_api = api()
                module_name = interface_name.split("\\")[2]
                self.if_name = module_name + "." + case['testInterFace']
                self.method = case['method']
                self.url += case['url']
                self.data = case['data']
                response = None
                run_time = None
                run_res = None

            except Exception as ex:
                self.logger.error(traceback.format_exc())
                self.report.set_un_num()
                self.report.state_html(self.if_name, 0, 5, '异常错误00000', traceback.format_exc(), "")
                continue

            for data in self.data:
                try:
                    self.param = {}
                    total += 1
                    paramType = ''
                    if 'paramType' in data.keys():
                        paramType = [data.pop('paramType')]
                    case_name = data.pop('caseName')
                    data = ParseParam().parse_variable(file, data)
                    result = data.pop('result')

                    # 判断是否需要在headers中加session ID字段，云梯接口专用
                    if 'cookie' in data.keys():
                        if data.pop('cookie') == 'jsessionid':
                            enable = readConfig.ReadConfig().get_session('enable')
                            if enable == '1':   # 判断配置文件中sessionID是否可用
                                session = readConfig.ReadConfig().get_session('JSESSIONID')
                                #header = {'cookie': 'JSESSIONID=%s' % session}
                                # request_api.set_header(header)
                                param_dict["headers"]['cookie'] = "JSESSIONID="+session
                            else:
                                self.report.set_un_num()
                                self.report.state_html(self.if_name + ': ' + case_name, 0, 10,
                                                       '配置文件config.ini 异常，sessionID未使能',
                                                       '配置文件config.ini 异常，sessionID未使能enable获取值为0')
                                break
                    # 判断参数形式

                    if 'url' in paramType:
                        self.url = self.url + "/" + data.pop('urlParam')

                    self.param = dict(data, **param_dict)
                    self.param["url"] = self.url

                    run_res, run_time, response = request_api.get_response(self.method, **self.param)
                    # self.logger.info("Start Running Test Case Name : %s" % (interface_name + ': ' + case_name))
                    # self.logger.info("Url: %s " % self.url)
                    # self.logger.info("Params : %s" % data)
                    # self.logger.info("Response Data: %s \n %s " % (response.text, "=" * 80))
                    if run_res:
                        # check, msg = self.check_result(result, response)
                        check_result = CheckResult(response, result)
                        check, msg = check_result.parse_result()
                        if check == 0:
                            self.report.set_pass_num()
                            self.report.state_html(self.if_name + ': ' + case_name, run_time, check, msg,
                                                   response.text, self.param[paramType[0]])
                        elif check == 1:
                            self.report.set_fail_num()
                            self.report.state_html(self.if_name + ': ' + case_name, run_time, check, msg,
                                                   response.text, self.param[paramType[0]])
                            self.logger.info("InterFaceName: %s ,\n error_info: %s,\n Param: %s,\n Response: %s " %
                                             (self.if_name + ': ' + case_name, msg, self.param[paramType[0]],
                                              response.text))
                        elif check in [12, 13, 14]:
                            if check == 12:
                                check = 0
                                self.report.set_pass_num()
                            else:
                                self.report.set_fail_num()
                            self.report.state_html(self.if_name + ': ' + case_name, run_time, check, msg[0],
                                                   msg[1], self.param[paramType[0]])
                        elif check == 8:
                            if 'url' in paramType and 'code' in result:
                                if result['code'] == 404:
                                    self.report.set_pass_num()
                                    self.report.state_html(self.if_name + ': ' + case_name, run_time, 1,
                                                           msg+"，url参数与预期一致", response.text, self.param[paramType[0]])
                                else:
                                    self.report.set_un_num()
                                    self.report.state_html(self.if_name + ': ' + case_name, run_time, check,
                                                           msg, "连接URL：%s" % request_api.url, self.param[paramType[0]])
                            else:
                                self.report.set_un_num()
                                self.report.state_html(self.if_name + ': ' + case_name, run_time, check, msg,
                                                       "连接URL：%s" % request_api.url, self.param[paramType[0]])
                        else:
                            self.report.set_fail_num()
                            self.report.state_html(self.if_name + ': ' + case_name, run_time, check,
                                                   msg, response.text, self.param[paramType[0]])
                    else:
                        self.report.set_un_num()
                        self.report.state_html(self.if_name + ': ' + case_name, run_time, 5, "连接异常错误22",
                                               response, self.param)
                except ModuleNotFoundError:
                    self.report.set_un_num()
                    self.report.state_html(self.if_name, 0, 5, 'Module Not Found In _global file', traceback.format_exc(), self.param)
                    self.logger.error(traceback.format_exc())

                except Exception:
                    self.report.set_un_num()
                    self.report.state_html(self.if_name, 0, 5, '异常错误111', traceback.format_exc(), self.param)
                    self.logger.error(traceback.format_exc())

            self.report.set_if_total()
            self.report.set_if_info()

        if total:
            self.report.report()
            webbrowser.open("file://"+self.report.report_path+'/Report.html')

    def get_data_by_key(self, key, data_dict):  # 根据key查找字典中对应的value值
        #value = []
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

    @staticmethod
    def tear_down():
        enable = readConfig.ReadConfig().get_session('enable')
        if enable == "1":
            readConfig.ReadConfig().set_session('enable', '0')


if __name__ == '__main__':
    run = Run()
    s = time.time()
    # run.prepare()  # write case list to file caseList.conf
    e = time.time()
    print("prepare time: %0.8f" % (e - s))
    run.run_case()
    e1 = time.time()
    print("run case time: %0.8f" % (e1 - e))
    # run.tear_down()
    e2 = time.time()
    print("teardown time: %0.8f" % (e2 - e1))
