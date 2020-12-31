#!/usr/bin/python3

from urllib.request import Request
from urllib.request import urlopen
import json


def get():
    headers = {'Content-Type': 'application/json',
               'HC-ACCESS-TOKEN': 'czo1OToiZTE0ZWFFWmZpSkNrd3Y5enNYTFRoLzJ6K0paUnZuT0ViR2dvTS9XLzNjSG5LZk9jL0wvY3YzR01XNHMiOw=='}

    url = 'http://test-hantalk-app.hanmaker.com/api/office/chat-group-list'
    with urlopen(Request(url, None, headers)) as res:
        res = res.read().decode()

    res = json.loads(res)
    print(res['data'][0]['group_name'])

    #print(res)

get()
