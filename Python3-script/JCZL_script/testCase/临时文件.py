# coding=utf-8

import unittest
import paramunittest
import readConfig
from common import log
from common import common
from common import configHttp
import hashlib
from common import configDB
import sys, os,xlrd, xlwt
from xlutils.copy import copy
import time

#将变量提出来
SQL = 'select * from jczl_user where userCode=9999'
FILE_PATH = 'D:\\Python3--script\\DASInterfaceTest --unittest\\testFile\\resetPwd.xls'

#调用configDB中的MyDB方法来连接数据库并查出对应的数据
db = configDB.MyDB()
sql_ex = db.executeSQL(SQL)
result= db.get_one(sql_ex)
close_db = db.closeDB()

#截取获得数据库的数据表中userguid和operatorUserId的值
exe_value = result[0]
print('userguid and operatorUserId value is: %s' %(exe_value))

#定义需要写进数据表中的pwd的值
exe_value02= 'g' + str(time.time())
print('Pwd value is: %s' %(exe_value02))

#打开需要修改的文件路径，然后将mysql数据库中获取到的参数写进对应的表格中
file_path  = os.path.abspath(FILE_PATH)
print('file path is: %s' %(file_path))

#打开文件
open_file = xlrd.open_workbook(file_path, formatting_info=True)

#复制一份文件，在的复制的文件中写入数据
co_file = copy(open_file)
first_sheet = co_file.get_sheet(0)
value01 = first_sheet.write(1, 3, exe_value)
value02 = first_sheet.write(1, 5, exe_value)
value03 = first_sheet.write(1, 4, exe_value02)
value04 = first_sheet.write(2, 4, exe_value02)
value05 = first_sheet.write(2, 5, exe_value)

#保存写入的值
co_file.save(file_path)
