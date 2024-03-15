import sys
import os
import asyncio
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.tanxconnector.client import Client  # noqa: E402
from src.tanxconnector import WsClient  # noqa: E402

load_dotenv()
private_key = os.environ['PRIVATE_KEY']
eth_address = os.environ['ETH_ADDRESS']


async def main():
    # create a public websocket instance
    ws_client = WsClient('public', 'testnet')

    # check to see if connected
    await ws_client.connect()

    # subscribe to streams
    await ws_client.subscribe(['btcusdc.trades',
                              'btcusdc.ob-inc',
                               'btcusdc.kline-5m',])

    # unsubscribe to streams
    await ws_client.unsubscribe(['btcusdc.trades'])

    # operate on ws member
    if ws_client.websocket:
        async for message in ws_client.websocket:
            print(message)

    # create a rest client instance if you need to create a private websocket
    client = Client()

    # login to get jwt access token
    login = client.complete_login(eth_address, private_key)

    # create a private websocket instance
    ws_client_priv = WsClient('private', 'mainnet', login['token']['access'])

    # check if connected
    await ws_client_priv.connect()

    # subscribe to streams
    await ws_client_priv.subscribe(['trade', 'order'])

    # disconnect
    await ws_client_priv.disconnect()

asyncio.run(main())
