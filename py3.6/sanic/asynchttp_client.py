#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio


class AsyHttpProtocal(asyncio.Protocol):
    """
    inherit from asyncio.Protocol -> asyncio.BaseProtocol
    """

    def __init__(self, loop):
        self.transport = None
        self.loop = loop
        self._eof = False
        self._waiter = None

    def connection_made(self, transport):
        #       request = 'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'
        #       transport.write(request.encode())
        self.transport = transport

    def connection_lost(self, exc):
        # no need to implement
        pass

    def data_received(self, data, encoding="utf8"):
        """Called when some data is received.

        The argument is a bytes object.
        """
        #       print(data.decode())
        rs = data
        if encoding:
            rs = data.decode(encoding)
        print(rs)

    def _wakeup(self):
        if self._waiter:
            self._waiter.set_result(None)
            self._waiter = None

    def eof_received(self):
        """Called when the other end calls write_eof() or equivalent.
        If this returns a false value (including None), the transport
        will close itself.  If it returns a true value, closing the
        transport is up to the protocol.
        """
        self._eof = True
        self._wakeup()

    async def wait_for_data(self):
        assert not self._eof
        assert not self._waiter

        self._eof = True
        self._waiter = self.loop.create_future()
        await self._waiter


class AsyHttpSession:
    """description"""

    def __init__(self, loop, host, port):
        self.host = host
        self.port = port
        self.loop = loop

    async def get(self, url):
        transport, protocol = await self._loop.create_connection(
            lambda: AsyHttpProtocal(loop), self.host, self.port)
        request = 'GET {} HTTP/1.1\r\nHost: {}\r\n\r\n'.format(url, self.host)
        transport.write(request.encode())

        await protocol.wait_for_data()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    coro = loop.create_connection(lambda: AsyHttpProtocal(loop), 'localhost',
                                  12345)
    loop.run_until_complete(coro)
    #   loop.run_forever()
#   loop.close()
