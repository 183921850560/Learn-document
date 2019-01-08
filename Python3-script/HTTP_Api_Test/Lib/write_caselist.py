# coding=utf-8
from Log.write_Log import MyLog
import readConfig
import os
import re

proDir = readConfig.proDir
global casepath
casepath = os.path.join(proDir, 'TestCase\\')


class MakeCaseList:
    def __init__(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.prj_name = ''
        if os.path.exists(os.path.join(casepath, 'caseList.conf')):
            os.remove(os.path.join(casepath, 'caseList.conf'))

    def write_caselist(self, file_path=casepath):
        file_list = os.listdir(file_path)
        # caseList = casepath
        file_list.sort(key=str.lower)
        prj_name = os.path.split(file_path)[1]
        for f_name in file_list:
            if f_name[-3:] == "tmp" or f_name[-4:] == 'conf' or f_name.startswith(('tmp',  '.') or f_name.endswith("_")):
                continue
            elif os.path.isdir(os.path.join(file_path, f_name)):
                # self.prj_name = self.prj_name + '/' + f_name
                self.write_caselist(file_path=os.path.join(file_path, f_name))
            else:
                if f_name.lower()[-3:] != 'yml' or len(re.findall(r'tmp', f_name)) > 0:
                    continue
                with open(casepath+'caseList.conf', 'a+') as f:
                    path = os.path.abspath(file_path).split('\\TestCase')
                    if len(path) > 1:
                        f.write(path[1] + '\\'+f_name.strip()[:-4]+'\n')
                    else:
                        f.write(f_name.strip()[:-4])



if __name__ == "__main__":
    a = MakeCaseList()
    a.write_caselist(file_path=casepath)