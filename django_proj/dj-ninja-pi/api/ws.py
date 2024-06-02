from channels.generic.websocket import AsyncWebsocketConsumer


class MyWS(AsyncWebsocketConsumer):
    async def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        if text_data == "abcabc123123":
            await self.send("BINGO")
        else:
            await self.send("not correct")
        await self.close()

    async def disconnect(self, close_code):
        # Called when the socket closes
        pass
