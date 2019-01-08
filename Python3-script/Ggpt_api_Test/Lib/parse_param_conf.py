# coding=utf-8
import ast
import os
from Lib.write_Log import MyLog
import re
import importlib.machinery
import types


class ParseParam:
    def __init__(self):
        self.regex = re.compile(r"(\$[\w_]+)")
        self.fun_regex = re.compile(r"\$\{([\w_]+\([\$\w\.\-_ =,]*\))\}")
        self.function_regexp_compile = re.compile(r"^([\w_]+)\(([\$\w\.\-_ =,]*)\)*$")
        self.prj_path = os.path.abspath(os.curdir)
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def parse_variable(self, start_path, target):
        target_str = str(target)
        param = {}
        var_matched = self.regex.findall(target_str)
        fun_matched = self.fun_regex.findall(target_str)
        value = target_str.strip()
        if var_matched:
            # list 格式参数 $elevatorId
            var_matched = list(set(var_matched)) # 去重
            for tar_value in var_matched:
                name = tar_value.replace('$', '')
                re_value = self.read_variable_conf(start_path, name)

                if isinstance(re_value,int):
                    value = self.replace(eval(value),re_value,tar_value) #
                else:
                    value = value.replace(tar_value, str(re_value))
                if fun_matched:
                    fun_matched = self.fun_regex.findall(value)
        if fun_matched:
            fun_matched = list(set(fun_matched)) # 去重
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
                try:
                    result = fun_name(*fun_meta["args"], **fun_meta["kwargs"])
                    if isinstance(result,int):
                        value = self.replace(eval(value),result,tar_str)
                    else:
                        value = value.replace(tar_str, str(result))

                except TypeError as e:
                    self.logger.error(e)
                    continue
        return eval(value)

    def replace(self,target, dist, original):
        if isinstance(dist,int):
            for k, v in target.items():
                if isinstance(v, dict):
                    self.replace(v,dist,original)
                elif str(v).find(original) == 0:
                    target[k] = dist
                elif str(v).find(original) > 0:
                    target[k] = v.replace(original,str(dist))
        else:
            tmp = str(target).replace(original,dist)
            return tmp
        return str(target)
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
            err_msg = "%s : {%s} not found in recursive upward path!" % (item_type, item)
            raise ModuleNotFoundError(err_msg)

        return self.read_variable_conf(dir_path, item, item_type)

    @staticmethod
    def lower_key(origin_dict):
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
