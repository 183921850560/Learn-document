# *_* coding:utf-8 *_*
import paramiko
import os
'''
Author:gxl
Headline:循环登陆
Time：2018-05-21
'''
'''
author:gxl
headline:login cycle
time：2018-10-25
'''

def content_linux(hostname, username, password):
    ssh = paramiko.SSHClient()

    #取消安全认证
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    #连接linux
    ssh.connect(hostname=hostname, username=username, password=password)

    #执行linux命令
    stdin, stdout, stderr=ssh.exec_command('ls -l')
    data = os.system('sh ./taa.sh')
    print(data)

    #读取执行结果并返回
    result = stdout.read()
    return result

if __name__ == '__main__':
    # count = 0
    # while True:
    ten = content_linux(hostname='172.16.16.111', username='root', password='g18392185056')
    print(ten)
        # count += 1
        # if count > 3:
        #     break










