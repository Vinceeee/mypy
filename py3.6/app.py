#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic.response import json,text

app = Sanic()

@app.route("/")
async def test(request):
    return json({'hello': 'world'})

@app.route("/home")
async def test2(request):
    return text("HI,你好")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=12345)
