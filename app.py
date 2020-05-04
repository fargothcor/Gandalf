#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
from flask import Flask, request, json
from config import *
from messageHandler import createAnswer

app = Flask(__name__)


@app.route('/', methods=['POST'])
def smartThing(): 
    data = json.loads(request.data)

    if 'type' not in data.keys():
        return 'shut up'
    elif data['type'] == 'confirmation':
        return CONFIRMATION_TOKEN
    elif data['type'] == 'message_new':
        createAnswer(data['object'], TOKEN)
        return 'ok'


@app.route('/', methods=['GET'])
def webSite():
    s = 'im fucking working'
    return s
