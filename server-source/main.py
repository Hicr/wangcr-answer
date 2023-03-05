#!/usr/bin/python3
import pymysql
import flask
import json
import datetime
import uuid
from functools import wraps
from flask import make_response,jsonify
from flask_cors import *
# 加载 openai 依赖
import openai
# 用于读取配置文件
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()
# 设置key
openai.api_key = os.getenv("OPENAI_API_KEY")
# 初始化web
server = flask.Flask(__name__)
# 跨域
CORS(server, supports_credentials=True)

def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE,OPTIONS'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun

@server.route('/answer/hello',methods=['get'])
@allow_cross_domain
def hello():
    return result_handler('success', "hello!")

#随便聊聊
@server.route('/answer/chat/all',methods=['post'])
@allow_cross_domain
def chart_all():
    print(os.getenv("OPENAI_API_KEY"))
    # 初始化时间
    today = datetime.datetime.today()
    today_time = today.strftime("%Y-%m-%d")
    as1 = "今天是" + today_time;
    # 获取输入
    object = flask.request.json
    msg = object.get('msg')
    # 对话
    respone = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "接下来的对话都用中文回答"},
            {"role": "assistant", "content": as1},
            {"role": "user", "content": msg}
        ]
    )
    print(jsonify(respone))
    return jsonify(respone['choices'][0]['message']['content'])

# 创意生成器
@server.route('/answer/chat/originality',methods=['post'])
@allow_cross_domain
def chart_originality():
    print(os.getenv("OPENAI_API_KEY"))
    # 初始化时间
    today = datetime.datetime.today()
    today_time = today.strftime("%Y-%m-%d")
    as1 = "今天是" + today_time;
    # 获取输入
    object = flask.request.json
    msg = object.get('msg')
    # 对话
    respone = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "接下来的对话都用中文回答"},
            {"role": "system", "content": "根据人们的意愿产生数字创业点子。例如，当我说“我希望在我的小镇上有一个大型购物中心”时，你会为数字创业公司生成一个商业计划，其中包含创意名称、简短的一行、目标用户角色、要解决的用户痛点、主要价值主张、销售和营销渠道、收入流来源、成本结构、关键活动、关键资源、关键合作伙伴、想法验证步骤、估计的第一年运营成本以及要寻找的潜在业务挑战。将结果写在降价表中。"},
            {"role": "assistant", "content": as1},
            {"role": "user", "content": msg}
        ]
    )
    print(jsonify(respone))
    return jsonify(respone['choices'][0]['message']['content'])


# stackOverFlow
@server.route('/answer/chat/stack',methods=['post'])
@allow_cross_domain
def chart_stack():
    print(os.getenv("OPENAI_API_KEY"))
    # 初始化时间
    today = datetime.datetime.today()
    today_time = today.strftime("%Y-%m-%d")
    as1 = "今天是" + today_time;
    # 获取输入
    object = flask.request.json
    msg = object.get('msg')
    # 对话
    respone = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "接下来的对话都用中文回答"},
            {"role": "system", "content": "我想让你充当 stackoverflow 的帖子。我会问与编程相关的问题，你会回答应该是什么答案。我希望你只回答给定的答案，并在不够详细的时候写解释。不要写解释。当我需要用英语告诉你一些事情时，我会把文字放在大括号内{like this}。我的第一个问题是“如何将 http.Request 的主体读取到 Golang 中的字符串”"},
            {"role": "user", "content": msg}
        ]
    )
    print(jsonify(respone))
    return jsonify(respone['choices'][0]['message']['content'])

# 时间旅行
@server.route('/answer/chat/time',methods=['post'])
@allow_cross_domain
def chart_tims():
    print(os.getenv("OPENAI_API_KEY"))
    # 初始化时间
    today = datetime.datetime.today()
    today_time = today.strftime("%Y-%m-%d")
    as1 = "今天是" + today_time;
    # 获取输入
    object = flask.request.json
    msg = object.get('msg')
    # 对话
    respone = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "接下来的对话都用中文回答"},
            {"role": "system", "content": "我要你做我的时间旅行向导。我会为您提供我想参观的历史时期或未来时间，您会建议最好的事件、景点或体验的人。不要写解释，只需提供建议和任何必要的信息。我的第一个请求是“我想参观文艺复兴时期，你能推荐一些有趣的事件、景点或人物让我体验吗？”"},
            {"role": "user", "content": msg}
        ]
    )
    print(jsonify(respone))
    return jsonify(respone['choices'][0]['message']['content'])

# 作为 IT 专家
@server.route('/answer/chat/it',methods=['post'])
@allow_cross_domain
def chart_it():
    print(os.getenv("OPENAI_API_KEY"))
    # 初始化时间
    today = datetime.datetime.today()
    today_time = today.strftime("%Y-%m-%d")
    as1 = "今天是" + today_time;
    # 获取输入
    object = flask.request.json
    msg = object.get('msg')
    # 对话
    respone = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "接下来的对话都用中文回答"},
            {"role": "system", "content": "我希望你充当 IT 专家。我会向您提供有关我的技术问题所需的所有信息，而您的职责是解决我的问题。你应该使用你的计算机科学、大数据、网络基础设施和 IT 安全知识来解决我的问题。在您的回答中使用适合所有级别的人的智能、简单和易于理解的语言将很有帮助。用要点逐步解释您的解决方案很有帮助。尽量避免过多的技术细节，但在必要时使用它们。我希望您回复解决方案，而不是写任何解释。我的第一个问题是“我的笔记本电脑出现蓝屏错误”。"},
            {"role": "user", "content": msg}
        ]
    )
    print(jsonify(respone))
    return jsonify(respone['choices'][0]['message']['content'])


# 法律顾问
@server.route('/answer/chat/law',methods=['post'])
@allow_cross_domain
def chart_law():
    print(os.getenv("OPENAI_API_KEY"))
    # 初始化时间
    today = datetime.datetime.today()
    today_time = today.strftime("%Y-%m-%d")
    as1 = "今天是" + today_time;
    # 获取输入
    object = flask.request.json
    msg = object.get('msg')
    # 对话
    respone = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "接下来的对话都用中文回答"},
            {"role": "system", "content": "我想让你做我的法律顾问。我将描述一种法律情况，您将就如何处理它提供建议。你应该只回复你的建议，而不是其他。不要写解释。我的第一个请求是“我出了车祸，不知道该怎么办”。"},
            {"role": "user", "content": msg}
        ]
    )
    print(jsonify(respone))
    return jsonify(respone['choices'][0]['message']['content'])


# 厨师
@server.route('/answer/chat/cook',methods=['post'])
@allow_cross_domain
def chart_cook():
    print(os.getenv("OPENAI_API_KEY"))
    # 初始化时间
    today = datetime.datetime.today()
    today_time = today.strftime("%Y-%m-%d")
    as1 = "今天是" + today_time;
    # 获取输入
    object = flask.request.json
    msg = object.get('msg')
    # 对话
    respone = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "接下来的对话都用中文回答"},
            {"role": "system", "content": "我要你做我的私人厨师。我会告诉你我的饮食偏好和过敏，你会建议我尝试的食谱。你应该只回复你推荐的食谱，别无其他。不要写解释。我的第一个请求是“我是一名素食主义者，我正在寻找健康的晚餐点子。”"},
            {"role": "user", "content": msg}
        ]
    )
    print(jsonify(respone))
    return jsonify(respone['choices'][0]['message']['content'])

# 标题
@server.route('/answer/chat/title',methods=['post'])
@allow_cross_domain
def chart_title():
    print(os.getenv("OPENAI_API_KEY"))
    # 初始化时间
    today = datetime.datetime.today()
    today_time = today.strftime("%Y-%m-%d")
    as1 = "今天是" + today_time;
    # 获取输入
    object = flask.request.json
    msg = object.get('msg')
    # 对话
    respone = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "接下来的对话都用中文回答"},
            {"role": "system", "content": "我想让你充当一个花哨的标题生成器。我会用逗号输入关键字，你会用花哨的标题回复。"},
            {"role": "user", "content": msg}
        ]
    )
    print(jsonify(respone))
    return jsonify(respone['choices'][0]['message']['content'])

# 心理医生
@server.route('/answer/chat/psychologist',methods=['post'])
@allow_cross_domain
def chart_psychologist():
    print(os.getenv("OPENAI_API_KEY"))
    # 初始化时间
    today = datetime.datetime.today()
    today_time = today.strftime("%Y-%m-%d")
    as1 = "今天是" + today_time;
    # 获取输入
    object = flask.request.json
    msg = object.get('msg')
    # 对话
    respone = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "接下来的对话都用中文回答"},
            {"role": "system", "content": "我想让你担任心理健康顾问。我将为您提供一个寻求指导和建议的人，以管理他们的情绪、压力、焦虑和其他心理健康问题。您应该利用您的认知行为疗法、冥想技巧、正念练习和其他治疗方法的知识来制定个人可以实施的策略，以改善他们的整体健康状况。我的第一个请求是“我需要一个可以帮助我控制抑郁症状的人。”"},
            {"role": "user", "content": msg}
        ]
    )
    print(jsonify(respone))
    return jsonify(respone['choices'][0]['message']['content'])

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
