#!/usr/bin/python3

# requests 模块安装 pip install requests

import requests
import json


def get():
    headers = {
        'Content-Type': 'application/json',
        'HC-ACCESS-TOKEN': 'czo1OToiZTE0ZWFFWmZpSkNrd3Y5enNYTFRoLzJ6K0paUnZuT0ViR2dvTS9XLzNjSG5LZk9jL0wvY3YzR01XNHMiOw=='
    }

    url = 'http://test-hantalk-app.hanmaker.com/api/office/chat-group-list'

    res = requests.get(url, None, headers=headers)
    data = json.loads(res.text)
    print(data['data'], res.status_code)


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
    res = requests.post(url, json.dumps(data), headers=headers)
    data = json.loads(res.text)
    print(data)


# post()
get()
