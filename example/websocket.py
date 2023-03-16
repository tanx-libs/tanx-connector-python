import sys
import os
import asyncio
import json
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.brine_wrapper.client import Client  # noqa: E402
from src.brine_wrapper.wsclient import WsClient  # noqa: E402

load_dotenv()
private_key = os.environ['PRIVATE_KEY']
eth_address = os.environ['ETH_ADDRESS']


async def main():

    # WsClient = wsclient.WsClient('public')
    # await WsClient.connect()
    # await WsClient.subscribe(['btcusdc.trades',
    #                           'btcusdc.ob-inc',
    #                           'btcusdc.kline-5m',])
    client = Client()
    login = client.complete_login(eth_address, private_key)
    wsClient = WsClient('private', login['token']['access'])
    await wsClient.connect()
    await wsClient.subscribe(['trade', 'order'])
    await wsClient.unsubscribe(['order'])

    async for message in wsClient.websocket:
        print(message)

    await wsClient.disconnect()


# async def handler(websocket):
#     async for message in websocket:
#         print(message)
#         break

asyncio.run(main())
