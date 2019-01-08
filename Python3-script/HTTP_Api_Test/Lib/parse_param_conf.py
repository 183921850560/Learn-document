# coding=utf-8
import ast
import os
from Log.write_Log import MyLog
import re
import importlib.machinery
import types
import readConfig


class ParseParam:
    def __init__(self):
        self.regex = re.compile(r"(\$[\w_]+)")
        self.fun_regex = re.compile(r"\$\{([\w_]+\([\$\w\.\-_ =,]*\))\}")
        self.function_regexp_compile = re.compile(r"^([\w_]+)\(([\$\w\.\-_ =,]*)\)*$")
        self.prj_path = readConfig.proDir
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()



    def parse_variable(self, start_path, target):
        if not target or not isinstance(target, dict):
            return None

        for key, value in target.items():
            if isinstance(value, str):
                param = {}
                var_matched = self.regex.findall(value)
                fun_matched = self.fun_regex.findall(value)
                if var_matched:
                    # list 格式参数 $elevatorId
                    for tar_value in var_matched:
                        name = tar_value.replace('$', '')
                        re_value = self.read_variable_conf(start_path, name)
                        value = value.strip()
                        if fun_matched:
                            for fun_arg in fun_matched:
                                if fun_arg.find(tar_value) > 0:
                                    #fun_matched[fun_matched.index(fun_arg)] = fun_arg.replace(tar_value, str(re_value))
                                    param[tar_value] = re_value
                                    continue
                            if not param:
                                value = value.replace(tar_value, str(re_value))
                                target[key] = value
                        else:
                            value = value.replace(tar_value, str(re_value))
                            target[key] = value
                if fun_matched:
                    for fun in fun_matched:
                        fun_meta = self.parse_function(fun.strip())
                        fun_name = self.read_variable_conf(start_path, fun_meta.pop("fun_name"), "function")
                        tar_str = "${%s}" % fun
                        if param:
                            arg_list = fun_meta["args"]
                            for p_key in param.keys():
                                for var in arg_list:
                                    if isinstance(var, str):
                                        if var == p_key:
                                            arg_list[arg_list.index(var)] = param[p_key]
                            fun_meta["args"] = arg_list

                        result = fun_name(*fun_meta["args"], **fun_meta["kwargs"])
                        value = value.replace(tar_str, str(result))
                        target[key] = value

            elif isinstance(value, list):
                for l in value:
                    self.parse_variable(start_path, l)
            elif isinstance(value, dict):
                self.parse_variable(start_path, value)

        return target

    def parse_function(self, fun_content):
        fun_match = self.function_regexp_compile.match(fun_content)
        function_meta = {"args": [], "kwargs": {}, 'fun_name': fun_match.group(1)}
        arg_str = fun_match.group(2).replace(" ", "")
        if arg_str == '':
            return function_meta

        arg_list = arg_str.split(',')
        for arg in arg_list:
            if '=' in arg:
                key, value = arg.split('=')
                function_meta["kwargs"][key] = self.parse_value(value)
            else:
                function_meta["args"].append(self.parse_value(arg))
        return function_meta

    def parse_param(self, param_list, interface_project_path):
        interface_project_path = "".join(interface_project_path.replace(" ", ""))
        if not param_list or interface_project_path == '':
            return None
        data_dict = {}
        for param in param_list:
            try:
                value = self.read_variable_conf(interface_project_path, param)
                data_dict[param] = self.parse_value(value)
            except ModuleNotFoundError as ex:
                self.logger.error(ex)
                continue
        return data_dict

    @staticmethod
    def parse_value(string_value):
        try:
            return ast.literal_eval(string_value)
        except ValueError:
            return string_value
        except SyntaxError:
            return string_value

    def read_variable_conf(self, start_path, item, item_type="variable"):
        """
        查找读取TestCase下对应项目目录下，variable参数配置文件
        :return:
        """
        dir_path = os.path.dirname(os.path.abspath(start_path))
        # if item_type == "function":
        #     file = os.path.join(dir_path, "user-defined.py")  # 获取函数模块

        file = os.path.join(dir_path, "_global.py")
        item = item.lower()
        if os.path.isfile(file):
            module = self.get_imported_module_from_file(file)
            module_dict = self.filter_module(module, item_type)
            module_dict = self.lower_key(module_dict)
            if item in module_dict:
                return module_dict[item]
            else:
                return self.read_variable_conf(dir_path, item, item_type)

        if dir_path == self.prj_path:
            err_msg = "%s:%s not found in recursive upward path!" % (item_type, item)
            raise ModuleNotFoundError(err_msg)

        return self.read_variable_conf(dir_path, item, item_type)

    def lower_key(self, origin_dict):
        if not origin_dict or not isinstance(origin_dict, dict):
            return origin_dict

        return {
            key.lower(): value
            for key, value in origin_dict.items()
        }

    @staticmethod
    def is_function(tup):
        name, item = tup
        return isinstance(item, types.FunctionType)

    @staticmethod
    def is_variable(tup):
        name, item = tup
        if callable(item):
            return False
        if isinstance(item, types.ModuleType):
            return False
        if name.startswith("_"):
            return False
        return True

    def get_imported_module_from_file(self, file_path):
        return importlib.machinery.SourceFileLoader('module_name', file_path).load_module()

    def filter_module(self, module, filter_type):
        filter_type = self.is_function if filter_type == "function" else self.is_variable
        module_function_dict = dict(filter(filter_type, vars(module).items()))
        return module_function_dict


