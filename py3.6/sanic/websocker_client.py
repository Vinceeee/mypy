#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import websockets

async def send_data(url,data):
    """
    :parm url url wanted to connect (str)
    :parm data data wanted to send out
    """
    
    async with websockets.connect(url) as socket:
        await socket.send(data)
        data = await socket.recv()
        print(data)


if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(
            send_data("ws://localhost:12345","hello")
            )
        
