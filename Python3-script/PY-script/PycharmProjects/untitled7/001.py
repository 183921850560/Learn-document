# _*_ coding:UTF-8 _*_
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
# if __name__ == '__main__':
#     app.run()

sum = 0
count = 0
while count <= 100:
    sum = count + sum
    count += 1
print(sum)