#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

from sanic import Sanic
from sanic.response import json, text

UPLOAD_ROOT = "./upload"
app = Sanic()


@app.route("/")
async def test(request):
    return json({'hello': 'world'})


@app.route("/home")
async def test2(request):
    return text("HI,你好")


@app.put("/upload", stream=True)
async def upload(request):
    data = ''
    fn = '{}/file-{}'.format(UPLOAD_ROOT,int(time.time()))
    try:
        with open(fn,'wb') as f:
            while True:
                data = await request.stream.get()
                f.write(data)
                f.flush()
    except Exception as e:
        raise e
    return json({"messages": "created"}, status=201)


if __name__ == '__main__':
    if not os.path.exists(UPLOAD_ROOT):
        os.makedirs(UPLOAD_ROOT)
    app.run(host="0.0.0.0", port=12345)
