import requests
import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.tanxconnector import Client  # noqa: E402
from src.tanxconnector import exception  # noqa: E402
from src.tanxconnector.typings import CreateOrderNonceBody  # noqa: E402
from src.tanxconnector import sign_order_with_stark_private_key

load_dotenv()

PRIVATE_KEY = os.environ['PRIVATE_KEY']
ETH_ADDRESS = os.environ['ETH_ADDRESS']
stark_private_key = os.environ['STARK_PRIVATE_KEY']

client = Client()
try:
    # login to use private endpoints
    login = client.complete_login(ETH_ADDRESS, PRIVATE_KEY)
    print('Login Successful')
# Error: AuthenticationError | requests.exceptions.HTTPError

except exception.AuthenticationError as exc:
    print(exc)
except requests.exceptions.HTTPError as exc:
    print(exc.response.json())

# create an order nonce
nonce: CreateOrderNonceBody = {'market': 'ethusdc', 'ord_type': 'market',
                            'price': 29580.51, 'side': 'sell', 'volume': 0.0005}
# create order (private)

# create complete order
order = client.create_complete_order(nonce, stark_private_key)
print(order)
# calls below functions internally, we recommend using createCompleteOrder for ease of use

# or

nonce_res = client.create_order_nonce(nonce)
msg_hash = sign_order_with_stark_private_key(stark_private_key, nonce_res['payload'])
order = client.create_new_order(msg_hash)
print(order)

nonce: CreateOrderNonceBody = {'market': 'btcusdt', 'ord_type': 'market',
                            'price': 29580.51, 'side': 'buy', 'volume': 0.0001}

# cancel order (private)
nonce_res_for_order_to_cancel = client.create_order_nonce(nonce)
msg_hash = sign_order_with_stark_private_key(stark_private_key, nonce_res_for_order_to_cancel['payload'])
try:
    order_to_cancel = client.create_new_order(msg_hash)
    cancelled_order = client.cancel_order(order_to_cancel['payload']['id'])
    print(cancelled_order)
except requests.exceptions.HTTPError as exc:
    print(exc.response.json())

# get all orders (private)
orders_list = client.list_orders()
print(orders_list)

# get profile info (private)
profile = client.get_profile_info()
print(profile['payload']['username'])
