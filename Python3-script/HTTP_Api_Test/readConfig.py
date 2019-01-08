# coding=utf-8
import os
import codecs
import configparser


proDir = os.path.split(os.path.realpath(__file__))[0]
global configPath
configPath = os.path.join(proDir, 'config.ini')


class ReadConfig:
    def __init__(self):
        with open(configPath) as f:
            data = f.read()

            if data[:3] == codecs.BOM_UTF8:
                data = data[3:]
                with codecs.open(configPath, 'w') as file:
                    file.write(data)
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_server(self, value):
        return self.cf.get('Server', value)

    def get_sql(self, value):
        return self.cf.get('Mysql', value)

    def get_session(self, value):
        return self.cf.get('Session', value)

    def set_session(self, name, value):
        self.cf.set("Session", name, value)
        with open(configPath, 'w+') as f:
            self.cf.write(f)
