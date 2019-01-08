# coding = utf-8
import yaml
from Log.write_Log import MyLog
import traceback


class ReadYml:
    def __init__(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.yml_dict = {}

    def open_yml(self, file_path):
        try:
            with open(file_path, encoding='UTF-8') as f:
                self.yml_dict = yaml.load(f)
                return self.yml_dict
        except FileNotFoundError as e:
            self.logger.error(traceback.format_exc())
            return False

    def get_data(self, data):
        return self.yml_dict[data]
