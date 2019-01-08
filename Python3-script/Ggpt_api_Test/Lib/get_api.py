# coding=utf-8
from Lib.read_yml import ReadYml as yml
import os
proDir = os.path.abspath(os.curdir)
api_dir = os.path.join(proDir, "API")


def get_api(module, interface_name):
    ry = yml()
    api_file=os.path.join(api_dir,module+"_api.yml")
    if os.path.isfile(api_file):
        ry.open_yml(api_file)
        return ry.get_data(interface_name)
    else:
        return False, "module name error ,can't find api yml file"
