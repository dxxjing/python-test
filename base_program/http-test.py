#!/usr/bin/python3

from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import urlencode
import json

# python自带的太难用 使用requests 模块 见 http_request.py

# http get请求

def get():
    headers = {
        'Content-Type': 'application/json',
        'HC-ACCESS-TOKEN': 'czo1OToiZTE0ZWFFWmZpSkNrd3Y5enNYTFRoLzJ6K0paUnZuT0ViR2dvTS9XLzNjSG5LZk9jL0wvY3YzR01XNHMiOw=='
    }

    url = 'http://test-hantalk-app.hanmaker.com/api/office/chat-group-list'

    with urlopen(Request(url, None, headers)) as res:
        res = res.read().decode()

    res = json.loads(res)
    print(res)


# get()


def post():
    headers = {
        'Content-Type': 'application/json',
        'HC-ACCESS-TOKEN': 'czo1OToiZTE0ZWFFWmZpSkNrd3Y5enNYTFRoLzJ6K0paUnZuT0ViR2dvTS9XLzNjSG5LZk9jL0wvY3YzR01XNHMiOw=='
    }

    url = 'http://test-hantalk-app.hanmaker.com/api/office/doc/create'

    data = {
        'title': 'python create',
        'content': 'python3 create',
        'type': 1,
        'version': '1.0'
    }
    
    # 这里不知道怎么回事 数据无法发送过去

    data = urlencode(data)  # 将字典类型的请求数据转变为url编码
    data = data.encode('ascii')  # 将url编码类型的请求数据转变为bytes类型
    req_data = Request(url, data, headers)  # 将url和请求数据处理为一个Request对象，供urlopen调用

    with urlopen(req_data) as res:
        res = res.read().decode()

    res = json.loads(res)
    print(res)


post()
