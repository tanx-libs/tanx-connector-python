import requests
from dotenv import load_dotenv
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.brineconnector import Client  # noqa: E402
from src.brineconnector import sign_msg  # noqa: E402
from src.brineconnector import exception  # noqa: E402
from src.brineconnector.typings import CreateOrderNonceBody  # noqa: E402
from src.brineconnector import create_user_signature, sign_order_with_stark_private_key

load_dotenv()
PRIVATE_KEY = os.environ['PRIVATE_KEY']
ETH_ADDRESS = os.environ['ETH_ADDRESS']


def main():

    client = Client()
    # create a rest client instance (default is mainnet)
    client.test_connection()
    # you can use public endpoints right away
    trades = client.get_recent_trades('btcusdc')
    orderbook = client.get_orderbook('btcusdc')
    try:
        # login to use private endpoints
        login = client.complete_login(ETH_ADDRESS, PRIVATE_KEY)
    # Error: AuthenticationError | requests.exceptions.HTTPError
    except exception.AuthenticationError as exc:
        print(exc)
    except requests.exceptions.HTTPError as exc:
        print(exc)

    # create an order nonce
    nonce: CreateOrderNonceBody = {'market': 'btcusdt', 'ord_type': 'market',
                                   'price': 29580.51, 'side': 'buy', 'volume': 0.0001}

    # create order (private)
    # order = client.create_complete_order(nonce, PRIVATE_KEY)
    # print(order['payload'])
    nonce_res = client.create_order_nonce(nonce)
    stark_private_key = '0x' # replace with your stark private key
    msg_hash = sign_order_with_stark_private_key(stark_private_key, nonce_res['payload'])
    # msg_hash = sign_msg_hash(nonce_res['payload'], PRIVATE_KEY, 'testnet')
    try:
        order = client.create_new_order(msg_hash)
        print(order)
    except requests.exceptions.HTTPError as exc:
        print(exc.response.json())
        

    # get all orders (private)
    orders = client.list_orders()

    # get profile info (private)
    profile = client.get_profile_info()
    print(profile['payload']['username'])


main()
