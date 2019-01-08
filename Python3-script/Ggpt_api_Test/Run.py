# coding=utf-8
from Lib import get_api as getapi
from Lib.read_yml import ReadYml
from Lib.write_caselist import MakeCaseList
from Lib.write_Log import MyLog
from Lib.request_api import RequestsAPI
from Lib.write_report import WriteReport
from Lib.parse_param_conf import ParseParam
from Lib.check_result import CheckResult
import os
import re
import webbrowser
import time
import traceback


class Run(object):
    def __init__(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.report = WriteReport()
        self.url = ""
        self.api = None
        self.environment = ""

    @staticmethod
    def prepare():
        """
        从目录 TestCase读取CaseFile文件名，并写入caseList.conf文件
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

    def run_case(self, tag=None):
        """
        执行用例
        :param tag: 需要执行的用例tag，如smoke等
        :return:
        """
        total = 0

        prj_name = ''
        if tag:
            pass
        for suite_path in self.get_case():
            suite_enable = 0   # 标定该suite 是否执行的状态
            print("start test suite : %s" % suite_path)
            if prj_name != suite_path.split("/")[1]:
                prj_name = suite_path.split("/")[1]
                self.environment = prj_name
                self.report.set_prj_name(prj_name)
            try:
                file = './TestCase' + suite_path + '.yml'
                if not os.path.isfile(file):
                    self.logger.error("The File Does Not exists: %s" % file)
                    # suite_total -= 1
                    print("The File does not exists: %s" % file)
                    continue
                param_dict = self.get_environment(self.environment, file)  # # 获取对应测试环境参数

                if "host" in param_dict.keys() and "port" in param_dict.keys():
                    self.url = "%s:%s/" % (param_dict.pop("host"), param_dict.pop("port"))
                else:
                    raise ValueError("Not found host in conf file ")
                suite = ReadYml().open_yml(file_path=file)
                case_list = suite["testCase"]
                suite_name = suite["suiteName"]
                for case in case_list:
                    for title in case.keys():
                        self.api = RequestsAPI()
                        tearDown_enable = False
                        if title.find("case") >= 0:
                            case_tmp = case[title]
                            total += 1
                            setup_status = True
                            setup_data = {}
                            run_time = 0
                            tearDown_list = []

                            # 根据tag 判断是否需要执行
                            try:
                                ex_tag = case_tmp.pop("tag")
                            except KeyError:
                                ex_tag = ""
                            if tag:
                                if ex_tag != tag:
                                    total -= 1
                                    print("testCase %s not running" % case_tmp["testCaseName"])
                                    continue


                            if "setup" in case_tmp.keys():
                                setup_list = case_tmp.pop("setup")
                                if setup_list:
                                    setup_status, suite_enable, setup_data, run_time = self.case_setup(setup_list, file)
                            if "tearDown" in case_tmp.keys():
                                tearDown_list = case_tmp.pop("tearDown")
                                if tearDown_list:
                                    tearDown_enable = True

                            try:
                                case_tmp = ParseParam().parse_variable(file, case_tmp)  # 解析case中参数
                            except ModuleNotFoundError as e:
                                suite_enable = 1
                                self.report.set_un_num()
                                self.report.state_html(suite_name + ":" + case_tmp["testCaseName"],
                                                       0, 11, "用例定义module未定义", str(e), "")
                                self.logger.error(str(e))
                                continue
                            if suite_enable == 2:  # 判断需要更新环境变量或headers等内容
                                param_dict = self.get_environment(self.environment, file)  # # 获取对应测试环境参数

                                if "host" in param_dict.keys() and "port" in param_dict.keys():
                                    self.url = "%s:%s" % (param_dict.pop("host"), param_dict.pop("port"))
                                else:
                                    raise ValueError("Not found host in conf file ")

                            # 判断setup 步骤是否运行正常
                            if not setup_status:
                                self.report.set_un_num()
                                self.report.state_html(suite_name + ": " +case_tmp["testCaseName"] , run_time, 11,
                                                       "setup: %s步骤失败，用例没有运行，"% setup_data["name"]
                                                       + setup_data["msg"],
                                                       setup_data["response"], setup_data["param"])
                                continue

                            suite_enable = 1


                            param_dict.update(case_tmp)

                            run_status, (validate, ac_param, testcase, run_res, run_time, response) = \
                                self.do_case(suite_path, param_dict, suite_name)
                            if not run_status:  # 判断是否执行该用例，未执行直接继续不进行下面的操作
                                total -= 1
                                continue
                            if run_res:
                                check_result = CheckResult(response, validate)
                                check, msg = check_result.verify_result()
                                if check == 0:
                                    if tearDown_enable:  # 判断是否需要执行tearDown
                                        tearDown_status, suite_enable, setup_data, run_time = \
                                            self.case_setup(tearDown_list, file)
                                        if not tearDown_status:
                                            self.report.set_fail_num()
                                            self.report.state_html(suite_name + ": Setup_" + case_tmp["testCaseName"],
                                                                   run_time, 11,
                                                                   "setup:%s 步骤失败，用例没有运行，" % setup_data["name"] +
                                                                   setup_data["msg"], setup_data["response"],
                                                                   setup_data["param"])
                                            continue
                                        else:
                                            self.report.set_pass_num()

                                    else:
                                        self.report.set_pass_num()
                                else:
                                    self.report.set_fail_num()
                                self.report.state_html(suite_name + ":" + testcase, run_time,
                                                       check, msg, response.text, ac_param)
                            else:
                                self.report.set_un_num()
                                self.report.state_html(suite_name + ":" + testcase, run_time,
                                                       10, "服务器连接异常", response, ac_param)

                        elif title.startswith("step"):
                            pass  # do run Multiple interface

                if suite_enable:
                    self.report.set_if_total()
                    self.report.set_if_info()
            except Exception as ex:
                print(traceback.format_exc())
                # suite_total -= 1
                self.logger.error(traceback.format_exc())
                continue

        if total:
            self.report.report()
            # open report.html in default browser
            webbrowser.open("file://" + self.report.report_path + '/Report.html')
        else:
            print("this is no case to be running")

    @staticmethod
    def step_return_data(name,msg,param,response):
        return_data = {}
        return_data["name"] = name
        return_data["msg"] = msg
        return_data["param"] = param
        return_data["response"] = response
        return return_data

    def case_setup(self, case, file):
        """
        setup\tearDown 步骤
        :param case:  case list
        :param file: file path
        :return:
        """
        setup_status, setup_data, suite_enable, run_time = True, {}, 0, 0

        for setup_tmp in case:
            if "operation" in setup_tmp.keys():

                name = setup_tmp["name"]
                op = setup_tmp["operation"]
                try:
                    op_fun = ParseParam().read_variable_conf(file, op, item_type="function")
                    op_fun()
                    suite_enable = 2
                except Exception as e:
                    setup_data = self.step_return_data(name,"Operation 操作执行异常","operation: %s" % op, traceback.format_exc())
                    return False, suite_enable, setup_data, 0

            elif "api" in setup_tmp.keys():
                summary,module_name,api_name = None, None,None

                try:
                    module_name,api_name = setup_tmp.pop("api")
                    api = getapi.get_api(module_name,api_name)
                    summary = api.pop("summary")
                except KeyError:
                    setup_data = self.step_return_data(summary, " 获取api接口数据异常", module_name+":"+api_name, traceback.format_exc())
                    return False, suite_enable, setup_data, 0
                try:
                    setup_tmp = ParseParam().parse_variable(file, setup_tmp)
                    env_name = self.environment
                    if "environment" in setup_tmp.keys():
                        env_name = setup_tmp.pop("environment")

                    env_fun = ParseParam().read_variable_conf(file, env_name, item_type="function")
                    param_dict = env_fun()
                    uri = "%s:%s/" % (param_dict.pop("host"), param_dict.pop("port"))
                except (KeyError,ModuleNotFoundError) as e:
                    self.logger.error(traceback.format_exc())
                    setup_data = self.step_return_data(summary, " 获取接口系统环境数据异常", module_name + ":" + api_name,
                                                       traceback.format_exc())
                    return False, suite_enable, setup_data, 0
                validate = None
                setup_name = ""
                setup_tmp["url"] = uri + api.pop("path")
                param_dict.update(api)
                tmp = param_dict.copy()
                tmp.update(setup_tmp)
                try:
                    setup_name = tmp.pop("name")
                    validate = tmp.pop("validate")
                except KeyError:
                    pass
                run_res, run_time, response = self.api.get_response(**tmp)
                self.logger.info(response.text)
                suite_enable = 1
                if run_res:
                    check_result = CheckResult(response, validate)
                    check, msg = check_result.verify_result()
                    if check:
                        setup_status = False
                        setup_data = self.step_return_data(setup_name,msg,tmp,response.text)

                        return setup_status, suite_enable, setup_data, run_time
                    continue
                else:
                    setup_status = False
                    setup_data = self.step_return_data(setup_name," 获取response异常", setup_tmp, response)

                    return setup_status, suite_enable, setup_data, run_time

        return setup_status, suite_enable, setup_data, run_time

    @staticmethod
    def update_param(original, update):
        """
        实现更新字典两级
        :param original:  原始字典
        :param update:
        :return:
        """
        tmp = original.copy()
        for key, item in original.items():
            if isinstance(item, dict):
                if key in update.keys():
                    tmp[key].update(update.pop(key))
        tmp.update(update)
        return tmp

    def do_case(self, suite_name, case_dict, interface_name):
        """
        run case_dict
        :param suite_name: caseList.conf file
        :param case_dict: dict type testCase
        :param interface_name:
        :return:
        """
        # run_res, run_time, response = None, None, None
        prj_name, module, suite = None, None, None
        path_list = suite_name.split('/')[1:]
        if len(path_list) == 3:
            prj_name, module, suite = path_list
        elif len(path_list) == 2:
            prj_name, suite = path_list
            module = prj_name
        else:
            prj_name, module = path_list[:2]
            suite = path_list[-1]
        api_dict = getapi.get_api(module, interface_name)
        if isinstance(api_dict, tuple):
            return False, (None, None, None, None, 0, api_dict[1])
        summary = api_dict.pop("summary")
        # path = api_dict.pop("path")
        # url = self.url + path
        data = api_dict.copy()
        case_name = case_dict.pop("testCaseName")

        data = self.update_param(data, case_dict)
        data["url"] = self.url + data.pop("path")
        validate = data.pop("validate")
        if "data" in data.keys():
            data_tmp = data.pop("data")
            if "file" in data_tmp:
                file_data = data_tmp.pop("file")
                self.api.set_file(file_data)
        run_res, run_time, response = self.api.get_response(**data)
        return True, (validate, data, case_name, run_res, run_time, response)

    @staticmethod
    def get_environment(env_name, file_path):
        env_fun = ParseParam().read_variable_conf(file_path, env_name, item_type="function")
        env_param = env_fun()
        return env_param


if __name__ == "__main__":
    run = Run()
    # run.prepare() # caseList file prepare
    run.run_case()
