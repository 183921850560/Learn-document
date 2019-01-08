# coding=utf-8

from flask import Flask, abort, jsonify, make_response, request

server = Flask(__name__)

@server.route('/alarm/info/trapfilter', methods=['PUT'])
def getdata():
    getdata = request.get_data()
    print(getdata)
    return jsonify({"Code": 0, "message": 'OK'})


if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=65535)