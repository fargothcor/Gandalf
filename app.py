#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
from flask import Flask, request, json
from Gandalf.config import *
from Gandalf.messageHandler import create_answer

app = Flask(__name__)


@app.route('/', methods=['POST'])
def smart_thing():
    data = json.loads(request.data)

    if 'type' not in data.keys():
        return 'shut up'
    elif data['type'] == 'confirmation':
        return CONFIRMATION_TOKEN
    elif data['type'] == 'message_new':
        create_answer(data['object'])
        return 'ok'


@app.route('/', methods=['GET'])
def web_site():
    s = 'im fucking working'
    return s
