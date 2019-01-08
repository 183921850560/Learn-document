# coding=utf-8

from flask import Flask, abort, jsonify, make_response, request
from xml.etree import ElementTree as ET

app = Flask(__name__)


@app.route('/hello')
def index():
    return 'hello world!'


code_list = [{
    "id": 1,
    "des": 'Hello'
    },
    {
        "id": 2,
        "des": 'Hi'
    }
]


@app.route('/1.0/getDetail/<int:code_id>', methods=["GET"])
def getDetail(code_id):
    code = list(filter(lambda l: l['id'] == code_id, code_list))
    if len(code) == 0:
        abort(404)
    return jsonify({"Code": 0, "message": 'OK', 'code_list': code[0]})


@app.route('/1.0/getId', methods=['GET'])
def getID():
    res = {}
    for a in code_list:
        print("id %s" % a['id'])
        res = a

    return jsonify(res)


@app.route('/1.0/save', methods=['POST'])
def save():
    root = ET.fromstring(request.data.decode())
    print(root.tag)

    return jsonify({'msg': 'OK'})


@app.route('/1.0/add', methods=['POST'])
def add():
    get_id = {'id': request.get_json().get('id'), 'des': request.get_json().get('des')}
    print(get_id)
    result = {
        "Code": 0,
        "Message": "OK",
        "Data": [get_id]
              }
    for l in code_list:
        if l["id"] == get_id["id"]:
            result["Code"] = 1
            result["Message"] = "ID exists"
            result["Data"] = ['']
    return jsonify(result)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
