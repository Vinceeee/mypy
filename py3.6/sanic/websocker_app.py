#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic.response import json, text


app = Sanic()

@app.websocket("/put")
async def put(request,ws):
    while True:
        data = await ws.recv()
        await ws.send(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=12345)
