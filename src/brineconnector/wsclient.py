import asyncio
import websockets
from typing import Optional
from .exception import AuthenticationException
import json
import socket


class WsClient:
    def __init__(self, type: str = 'public', jwt: Optional[str] = None,
                 base_url: Optional[str] = "wss://api-testnet.brine.fi"):
        self.websocket = None
        if type == 'public':
            self.connection = f"{base_url}/public"
        else:
            if not jwt:
                raise AuthenticationException(
                    'JWT token must be provided for private connections')
            self.connection = f"{base_url}/private?auth_header={jwt}"

    async def connect(self):
        self.websocket = await websockets.connect(self.connection)

    async def disconnect(self):
        if self.websocket is not None:
            try:
                await self.websocket.close()
            except socket.gaierror:
                print("Socket gaia error, let's disconnect anyway...")
            except websockets.ConnectionClosedError:
                print("WebSockets connection closed error, let's disconnect anyway...")
            except websockets.ConnectionClosedOK:
                print("WebSockets connection closed ok, let's disconnect anyway...")
            except ConnectionResetError:
                print("Connection reset error, let's disconnect anyway...")
            del self.websocket

    async def _send(self, data: dict) -> None:
        while not self.websocket:
            await asyncio.sleep(0.1)
        try:
            await self.websocket.send(json.dumps(data))
        except socket.gaierror:
            print("Socket gaia error, message not sent...")
        except websockets.ConnectionClosedError:
            print("WebSockets connection closed error, message not sent...")
        except websockets.ConnectionClosedOK:
            print("WebSockets connection closed ok, message not sent...")
        except ConnectionResetError:
            print("Connection reset error, message not sent...")

    async def subscribe(self, streams: "list[str]"):
        data = {
            "event": "subscribe",
            "streams": streams
        }
        await self._send(data)

    async def unsubscribe(self, streams: "list[str]"):
        data = {
            "event": "unsubscribe",
            "streams": streams
        }
        await self._send(data)
