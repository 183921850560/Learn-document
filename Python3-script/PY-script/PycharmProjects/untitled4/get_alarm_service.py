# coding=utf-8
'''
Author:gxl
Headline: 获取告警信息上报服务
Time：2018-05-21
'''

from flask import Flask, abort, jsonify, make_response, request

server = Flask(__name__)

@server.route('/alarm/info/trapfilter', methods=['PUT'])
def getdata():
    getdata = request.get_data()
    print(getdata)
    return jsonify({"Code": 0, "message": 'OK'})
if __name__ == '__main__':
    server.run(debug=True, host='172.18.20.175', port=65535)