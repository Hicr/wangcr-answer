#!/usr/bin/python3
import pymysql
import flask
import json
import datetime
import uuid
from functools import wraps
from flask import make_response

server = flask.Flask(__name__)


def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun

@server.route('/answer/hello',methods=['get'])
@allow_cross_domain
def hello():
    return result_handler('success', "hello!")


# 返回结果
def result_handler(type,data):
    if(type == 'success'):
        if(data):
            # res = {'message': 'success!', 'code': 200, 'data': json.dumps(data,ensure_ascii=False)}
            res = {'message': 'success!', 'code': 200, 'data': data}
            return json.dumps(res,ensure_ascii=False)
        else:
            res = {'message': 'success!', 'code': 200}
            return json.dumps(res, ensure_ascii=False)
    else:
        if(data):
            res = {'message': 'error!', 'code': 500, 'data': json.dumps(data, ensure_ascii=False)}
            return json.dumps(res, ensure_ascii=False)
        else:
            res = {'message': 'error!', 'code': 500}
            return json.dumps(res, ensure_ascii=False)


server.run(port=29977, debug=True,host='0.0.0.0')
#
# if __name__ == '__main__':
#     print("$$$$$$$$$$$$$$$$$$$wangcr-answer USE ChartGPT$$$$$$$$$$$$$$$$$$$$$$$")
