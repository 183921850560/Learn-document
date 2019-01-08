# -*-coding:utf-8 -*-
import pymysql
import sys
sys.path.insert(0, '/Python3-script/JCZL_script')#导入文件的路径
import readConfig
from common.log import MyLog
localReadConfig = readConfig.readConfig()

#创建数据库相关的类
class MyDB:
    #整个类中需要用到的全局变量（类的属性）
    global host, username, password, port, database, config
    #获取对数据库操作的配置信息
    host = localReadConfig.get_mysql("host")
    username = localReadConfig.get_mysql("user")
    password = localReadConfig.get_mysql("passwd")
    port = localReadConfig.get_mysql("port")
    database = localReadConfig.get_mysql("database")
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database
    }

    #调用类之前进行初始化
    def __init__(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None

    #创建连接数据库的方法
    def connectDB(self):
        try:
            # 连接数据库
            self.db = pymysql.connect(**config)
            # 使用 cursor() 方法创建一个游标对象 cursor
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")

        except ConnectionError as ex:
            self.logger.error(str(ex))

    # 创建一个执行sql语句的方法
    def executeSQL(self, sql):
        self.connectDB()
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 执行提交数据库
            self.db.commit()
        except Exception as e:
            # 返回错误的信息
            self.db.rollback()
        #返回操作的游标
        return self.cursor

    #获取游标中的所有数据
    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    #获取游标中的单条数据
    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    #关闭数据库
    def closeDB(self):
        self.db.close()
        print("Database closed!\n")

