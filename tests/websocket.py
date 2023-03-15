import sys
import os
import asyncio
import json
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.brine_wrapper import wsclient, client  # noqa: E402

load_dotenv()
private_key = os.environ['PRIVATE_KEY']
eth_address = os.environ['ETH_ADDRESS']


async def main():

    # WsClient = wsclient.WsClient('public')
    # await WsClient.connect()
    # await WsClient.subscribe(['btcusdc.trades',
    #                           'btcusdc.ob-inc',
    #                           'btcusdc.kline-5m',])
    Client = client.Client()
    login = Client.complete_login(eth_address, private_key)
    WsClient = wsclient.WsClient('private', login['token']['access'])
    await WsClient.connect()
    await WsClient.subscribe(['trade', 'order'])
    await WsClient.unsubscribe(['order'])

    async for message in WsClient.websocket:
        print(message)

    await WsClient.disconnect()


# async def handler(websocket):
#     async for message in websocket:
#         print(message)
#         break

asyncio.run(main())
