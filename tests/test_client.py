import responses
from dotenv import load_dotenv
import sys
import os
import pytest
import requests
from typing import List, cast
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.brineconnector import Client  # noqa: E402
from src.brineconnector.typings import Balance  # noqa: E402
BASE_URL = 'https://api-testnet.brine.fi'

load_dotenv()  # load env variables from .env
PRIVATE_KEY = os.environ['PRIVATE_KEY']
ETH_ADDRESS = os.environ['ETH_ADDRESS']

client = Client()


def test_ping():
    assert "Working" in client.test_connection()['message']


def test_get_24h_price():
    assert "btcusdt" in client.get_24h_price('btcusdt')['payload']


def test_get_candlestick():
    assert "Retrieval" in client.get_candlestick('btcusdt')['message']


def test_get_candlestick_raises_400_error():
    with pytest.raises(requests.exceptions.HTTPError):
        client.get_candlestick('test')['message']


def test_get_orderbook():
    assert "asks" in client.get_orderbook('btcusdt')['payload']


def test_get_orderbook_raises_type_error():
    with pytest.raises(TypeError):
        client.get_orderbook()['payload']


def test_get_recent_trades():
    assert "amount" in client.get_recent_trades('btcusdt')['payload'][0]


@responses.activate
def test_complete_login():
    responses.post(url=f"{BASE_URL}/sapi/v1/auth/nonce/",
                   json={'status': 'success', 'message': 'Cached Nonce Acquired',
                         'payload': 'You’re now signing into Brine Testnet, make sure the origin is https://testnet.brine.fi (Login-code:abc)'},
                   status=200)
    responses.post(url=f"{BASE_URL}/sapi/v1/auth/login/",
                   json={'status': 'success', 'message': 'Login Successful', 'payload': {
                       'uid': ''}, 'token': {'refresh': 'test', 'access': 'test'}},
                   status=200)
    assert "token" in client.complete_login(ETH_ADDRESS, PRIVATE_KEY)


@responses.activate
def test_complete_login_raises_invalid_eth_address_400_error():
    responses.post(url=f"{BASE_URL}/sapi/v1/auth/nonce/",
                   json={
                       'status': 'error', 'message': 'Ensure eth_address has at least 30 characters.', 'payload': ''},
                   status=400)
    with pytest.raises(requests.exceptions.HTTPError):
        print(client.complete_login('test', PRIVATE_KEY))


@responses.activate
def test_complete_login_raises_incorrect_eth_address_400_error():
    responses.post(url=f"{BASE_URL}/sapi/v1/auth/nonce/",
                   json={'status': 'success', 'message': 'Cached Nonce Acquired',
                         'payload': 'You’re now signing into Brine Testnet, make sure the origin is https://testnet.brine.fi (Login-code:abc)'},
                   status=200)
    responses.post(url=f"{BASE_URL}/sapi/v1/auth/login/",
                   json={
                       'status': 'error', 'message': 'Invalid Credentials or Token Expired, Kindly login again.', 'payload': ''},
                   status=400)
    with pytest.raises(requests.exceptions.HTTPError):
        client.complete_login(
            '0x83D37295507F7C838f6a7dd1E41a4A81aC7C9a5E', PRIVATE_KEY)


@responses.activate
def test_get_profile_info():
    responses.get(url=f"{BASE_URL}/sapi/v1/user/profile/",
                  json={'status': 'success', 'message': 'Successful', 'payload': {
                      'name': 'test', 'img': None, 'username': '0x7brine', 'stark_key': '0x'}},
                  status=200)
    assert "name" in client.get_profile_info()['payload']


@responses.activate
def test_get_balance():
    responses.get(url=f"{BASE_URL}/sapi/v1/user/balance/",
                  json={'status': 'success', 'message': 'Retrieved Successfully', 'payload': [{'currency': 'btc', 'balance': '0.0091892', 'locked': '0.0'}, {
                      'currency': 'eth', 'balance': '0.2179175', 'locked': '0.0'}, {'currency': 'usdc', 'balance': '56.354237624', 'locked': '0.0'}, {'currency': 'usdt', 'balance': '79.699671653', 'locked': '0.0'}]},
                  status=200)
    r= cast(List[Balance], client.get_balance()['payload'])
    assert "balance" in r[0]


@responses.activate
def test_get_profit_and_loss():
    responses.get(url=f"{BASE_URL}/sapi/v1/user/pnl/",
                  json={'status': 'success',
                        'message': 'Retrieval Successful', 'payload': [{}]},
                  status=200)
    assert "Retrieval" in client.get_profit_and_loss()[
        'message']


def test_get_auth_status():
    assert client.get_auth_status()


@responses.activate
def test_create_complete_order():
    responses.post(url=f"{BASE_URL}/sapi/v1/orders/nonce/",
                   json={'status': 'success', 'message': 'order nonce created successfully, please sign the msg_hash to place the order',
                         'payload': {'nonce': 35179980, 'msg_hash': '0xe5eea5423fbb8332c24d750bc49c899eba99af665306aaddc9968972002e1'}},
                   status=200)
    responses.post(url=f"{BASE_URL}/sapi/v1/orders/create/",
                   json={'status': 'success', 'message': 'Created Order Successfully',
                         'payload': {}},
                   status=200)
    assert "Order" in client.create_complete_order({'market': 'btcusdt', 'ord_type': 'market',
                                                    'price': 29580.51, 'side': 'buy', 'volume': 0.0001}, PRIVATE_KEY)['message']


@responses.activate
def test_create_order_nonce_raises_400_error():
    responses.post(url=f"{BASE_URL}/sapi/v1/orders/nonce/",
                   json={
                       'status': 'error', 'message': 'Maximum decimals allowed for volume is 4 in btcusdt market', 'payload': ''},
                   status=400)
    with pytest.raises(requests.exceptions.HTTPError):
        client.create_complete_order({'market': 'btcusdt', 'ord_type': 'market',
                                      'price': 29580.51, 'side': 'buy', 'volume': 0.0001}, PRIVATE_KEY)['message']


@responses.activate
def test_get_order():
    responses.get(url=f"{BASE_URL}/sapi/v1/orders/1234",
                  json={'status': 'success',
                        'message': 'Order Retrieved Successfully', 'payload': {}},
                  status=200)

    assert "Order" in client.get_order(1234)['message']


@responses.activate
def test_list_orders():
    responses.get(url=f"{BASE_URL}/sapi/v1/orders",
                  json={'status': 'success',
                        'message': 'Orders Retrieved Successfully', 'payload': {}},
                  status=200)

    assert "Orders" in client.list_orders()['message']


@responses.activate
def test_cancel_order():
    responses.post(url=f"{BASE_URL}/sapi/v1/orders/cancel/",
                   json={'status': 'success',
                         'message': 'Order is successfully queued for cancellation', 'payload': {}},
                   status=200)
    assert "Order" in client.cancel_order(1234)['message']


@responses.activate
def test_list_trades():
    responses.get(url=f"{BASE_URL}/sapi/v1/trades/",
                  json={'status': 'success',
                        'message': 'Trades Retrieved Successfully', 'payload': [{}]},
                  status=200)
    assert "Trades" in client.list_trades()['message']
