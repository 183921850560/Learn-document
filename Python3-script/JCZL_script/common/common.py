# -*-coding:utf-8-*-

import os
from xlrd import open_workbook
from xml.etree import ElementTree as ET
import sys
sys.path.insert(0, '/Python3-script/JCZL_script')
import readConfig
from common.log import MyLog
from common.configHttp import configHTTP
localConfigHttp = configHTTP()
log = MyLog.get_log()
logger = log.get_logger()

#返回sessionID的日志信息
def show_return_msg(response):
    url = response.url
    msg = response.text
    jsessionID = response.cookies["JSESSIONID"]
    logger.info("\nResponse Info:\n\t\tUrl:%s\n\t\tMsg:%s\n\t\tjsessionID:%s" % (url, msg, jsessionID))


# 获取数据表并将表名称打印出来
def get_xls_sheet(xls_name, sheet_name):
    xlsPath = os.path.join(readConfig.proDir, "testFile", xls_name)
    file = open_workbook(xlsPath)
    sheet = file.sheet_by_name(sheet_name)
    return sheet


# 在数据表中获取表中的数据并生成列表形式
def get_xls_param(sheet):
    cls = []
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != 'Case_Name':
            cls.append(sheet.row_values(i))
    return cls


# 在数据表中获取第一行的数据并把列的名称读出来写进key列表中
def get_xls_key(sheet):
    key = []

    if len(sheet.row_values(0)) > 3:

        for index in range(len(sheet.row_values(0))):
            if index < 3:
                continue
            elif sheet.row_values(0)[index] == 'msg':
                break
            else:
                key.append(sheet.row_values(0)[index])
                index += 1
    return key


#获取testfile目录下的sql.xml文件中的参数并返回到database字典中
database = {}
def get_xml():

    if len(database) == 0:
        sql_path = os.path.join(readConfig.proDir, "testFile", "sql.xml")
        tree = ET.parse(sql_path)
        for db in tree.findall("database"):
            db_name = db.get("name")
            table = {}
            for tb in db.getchildren():
                table_name = tb.get("name")
                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get("id")
                    sql[sql_id] = data.text.strip()
                table[table_name] = sql
            database[db_name] = table

#从database{}字典中获取数据库名称和表的名称
def get_xml_dict(database_name, table_name):
    get_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict

#获取数据库的名称、表的名称、sql的语句并返回
def get_sql(database_name, table_name, sql_id):
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    return sql

