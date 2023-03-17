import requests
from dotenv import load_dotenv
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.brineconnector import Client  # noqa: E402
from src.brineconnector import sign_msg  # noqa: E402
from src.brineconnector.data_types import CreateOrderNonceBody  # noqa: E402

load_dotenv()
PRIVATE_KEY = os.environ['PRIVATE_KEY']
ETH_ADDRESS = os.environ['ETH_ADDRESS']


def main():

    client = Client()

    # trades = client.get_recent_trades('btcusdt')
    # orderbook = client.get_orderbook('btcusdt')
    # print(trades['message'])
    # print(orderbook['message'])
    t = client.test_connection()
    try:
        login = client.complete_login(ETH_ADDRESS, PRIVATE_KEY)
        print(login['token']['access'])
    except requests.exceptions.HTTPError as exc:
        print(exc.response.json())

    # print(client.get_profile_info())
    # print(client.get_balance())
    # print(client.get_profit_and_loss())
    # print(login['message'])
    # trades = client.list_trades()
    # # print(trades['message'])
    # nonce = Client.create_order_nonce(
    #     'btcusdt', 'market', 29580.51, 'buy', 0.0001)

    # msg_hash = Client.sign_msg_hash(nonce['payload'], private_key)
    # print(Client.create_new_order(msg_hash))
    # try:\
    nonce: CreateOrderNonceBody = {'market': 'btcusdt', 'ord_type': 'market',
                                   'price': 29580.51, 'side': 'buy', 'volume': 0.0001}
    client.create_complete_order(nonce, PRIVATE_KEY)['message']
    #     # print(client.list_trades())
    # except requests.exceptions.HTTPError as exc:
    #     print(exc.response.json())


main()
