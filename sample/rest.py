from dotenv import load_dotenv
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.brine_wrapper import client  # noqa: E402
from src.brine_wrapper.bin.blockchain_utils import sign_msg  # noqa: E402
import requests

load_dotenv()
private_key = os.environ['PRIVATE_KEY']
eth_address = os.environ['ETH_ADDRESS']


def main():

    Client = client.Client()

    trades = Client.get_recent_trades('btcusdt')
    orderbook = Client.get_orderbook('btcusdt')
    print(trades['message'])
    print(orderbook['message'])
    login = Client.complete_login(eth_address, private_key)
    print(login['message'])
    trades = Client.list_trades()
    print(trades['message'])
    # nonce = Client.create_order_nonce('btcusdt', 'market', 29580.51, 'buy', 0.0001)

    # msg_hash = Client.sign_msg_hash(nonce['payload'], private_key)
    # print(Client.create_new_order(msg_hash))
    try:
        print(Client.create_complete_order('btcusdt', 'market', 29580.51, 'buy', 0.00001, private_key))
    except requests.exceptions.HTTPError as exc:
        print(exc.response.json())


main()
