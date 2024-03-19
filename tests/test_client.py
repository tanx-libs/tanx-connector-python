import responses
import sys
import os
import pytest
import requests
from typing import List, cast
from responses import matchers
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.tanxconnector import Client  # noqa: E402
from src.tanxconnector import sign_order_with_stark_private_key  # noqa: E402
from src.tanxconnector.typings import Balance  # noqa: E402
from src.tanxconnector.exception import InvalidAmountError, BalanceTooLowError
from tests.mock_responses import *
from web3 import EthereumTesterProvider, Account, Web3
BASE_URL = 'https://api.tanx.fi'

# load_dotenv()
PRIVATE_KEY = '7d6384d6877be027aa25bd458f2058e3f7ff68347dc583a9baf96f5f97b413a8'
ETH_ADDRESS = '0x713Cf80b7c71440E7a09Dede1ee23dCBf862fB66'

client = Client()
client2 = Client()


@responses.activate
def test_ping():
    responses.get(f'{BASE_URL}/sapi/v1/health/', json={
        "status": 'success',
        "message": 'Working fine!',
        "payload": '',
    })
    assert "Working" in client.test_connection()['message']


@responses.activate
def test_get_24h_price():
    responses.get(f'{BASE_URL}/sapi/v1/market/tickers/',
                  json={
                      "status": 'success',
                      "message": 'Retrieval Successful',
                      "payload": {
                          "btcusdc": {"at": '1681903275', "ticker": [{}]},
                          "btcusdt": {"at": '1681903275', "ticker": [{}]},
                          "ethusdc": {"at": '1681903275', "ticker": [{}]},
                          "ethusdt": {"at": '1681903275', "ticker": [{}]},
                          "usdcusdt": {"at": '1681903275', "ticker": [{}]},
                      },
                  }
                  )
    assert "btcusdc" in client.get_24h_price('btcusdc')['payload']


@responses.activate
def test_get_candlestick():
    responses.get(f'{BASE_URL}/sapi/v1/market/kline/', json={
        "status": 'success',
        "message": 'Retrieval Successful',
        "payload": [
            [1681689600, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681696800, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681704000, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681711200, 2014.02, 2014.02, 2014.02, 2014.02, 0.01],
            [1681718400, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681725600, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681732800, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681740000, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681747200, 2014.02, 2014.02, 2014.02, 2014.02, 0.1618],
            [1681754400, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681761600, 2014.02, 2014.02, 2014.02, 2014.02, 0.008400000000000001],
            [1681768800, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681776000, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681783200, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681790400, 2014.02, 2014.02, 2014.02, 2014.02, 0.1],
            [1681797600, 2014.02, 2014.02, 2014.02, 2014.02, 0.3694],
            [1681804800, 2014.02, 2014.02, 2014.02, 2014.02, 0.05],
            [1681812000, 2014.02, 2014.02, 2014.02, 2014.02, 0.0993],
            [1681819200, 2014.02, 2014.02, 2014.02, 2014.02, 0.015],
            [1681826400, 2014.02, 2014.02, 2014.02, 2014.02, 0.0066],
            [1681833600, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681840800, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681848000, 2014.02, 2014.02, 2014.02, 2014.02, 0.0005],
            [1681855200, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681862400, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681869600, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681876800, 2014.02, 2014.02, 2014.02, 2014.02, 0],
            [1681884000, 2014.02, 2014.02, 2014.02, 2014.02, 0.01],
            [1681891200, 2014.02, 2014.02, 2014.02, 2014.02, 0.0993],
            [1681898400, 2014.02, 2014.02, 2014.02, 2014.02, 0],
        ],
    })
    assert "Retrieval" in client.get_candlestick('btcusdc')['message']


@responses.activate
def test_get_candlestick_raises_400_error():
    responses.get(f'{BASE_URL}/sapi/v1/market/kline/', json={
        "status": 'error',
        "message": 'please enter a valid market',
        "payload": '',
    }, status=400)
    with pytest.raises(requests.exceptions.HTTPError):
        client.get_candlestick('test')['message']


@responses.activate
def test_get_orderbook():
    responses.get(f'{BASE_URL}/sapi/v1/market/orderbook/', json={
        "status": 'success',
        "message": 'Retrieval Successful',
        "payload": {
            "asks": [
                {
                    "id": 100,
                    "uuid": '6f11fcb2-1ef5-4fe3-852d-c73ddc28a8d1',
                    "side": 'sell',
                    "ord_type": 'limit',
                    "price": '2000.0',
                    "avg_price": '0.0',
                    "state": 'wait',
                    "market": 'ethusdc',
                    "created_at": '2023-04-19T11:02:50+02:00',
                    "updated_at": '2023-04-19T11:02:51+02:00',
                    "origin_volume": '0.001',
                    "remaining_volume": '0.001',
                    "executed_volume": '0.0',
                    "maker_fee": '0.001',
                    "taker_fee": '0.001',
                    "trades_count": 0,
                }
            ],
            "bids": [
                {
                    "id": 94,
                    "uuid": '06755d51-fcee-4936-b847-2d4da33588ba',
                    "side": 'buy',
                    "ord_type": 'limit',
                    "price": '1990.0',
                    "avg_price": '0.0',
                    "state": 'wait',
                    "market": 'ethusdc',
                    "created_at": '2023-04-19T11:01:18+02:00',
                    "updated_at": '2023-04-19T11:01:18+02:00',
                    "origin_volume": '0.001',
                    "remaining_volume": '0.001',
                    "executed_volume": '0.0',
                    "maker_fee": '0.001',
                    "taker_fee": '0.001',
                    "trades_count": 0,
                },
            ],
        },
    })
    payload = client.get_orderbook('btcusdc')['payload']
    assert "asks" in payload
    assert "bids" in payload


def test_get_orderbook_raises_type_error():
    with pytest.raises(TypeError):
        client.get_orderbook()['payload'] # type:ignore


@responses.activate
def test_get_recent_trades():
    responses.get(f'{BASE_URL}/sapi/v1/market/trades/', json={
        "status": 'success',
        "message": 'Retrieval Successful',
        "payload": [
            {
                "id": 40,
                "price": 1990,
                "amount": 0.001,
                "total": 1.99,
                "market": 'ethusdc',
                "created_at": 1681894870,
                "taker_type": 'buy',
            }
        ]})
    assert "amount" in client.get_recent_trades('btcusdc')['payload'][0]


@responses.activate
def test_complete_login():
    responses.post(url=f"{BASE_URL}/sapi/v1/auth/v2/nonce/",
                   json={'status': 'success', 'message': 'Cached Nonce Acquired',
                         'payload': 'You’re now signing into Tanx Testnet, make sure the origin is https://testnet.tanx.fi (Login-code:abc)'},
                   status=200)
    responses.post(url=f"{BASE_URL}/sapi/v1/auth/v2/login/",
                   json={'status': 'success', 'message': 'Login Successful', 'payload': {
                       'uid': ''}, 'token': {'refresh': 'test', 'access': 'test'}},
                   status=200)
    assert "token" in client.complete_login(ETH_ADDRESS, PRIVATE_KEY)
    assert "token" in client2.complete_login(ETH_ADDRESS, PRIVATE_KEY)


@responses.activate
def test_complete_login_raises_invalid_eth_address_400_error():
    responses.post(url=f"{BASE_URL}/sapi/v1/auth/v2/nonce/",
                   json={
                       'status': 'error', 'message': 'Ensure eth_address has at least 30 characters.', 'payload': ''},
                   status=400)
    with pytest.raises(requests.exceptions.HTTPError):
        print(client.complete_login('test', PRIVATE_KEY))


@responses.activate
def test_complete_login_raises_incorrect_eth_address_400_error():
    responses.post(url=f"{BASE_URL}/sapi/v1/auth/v2/nonce/",
                   json={'status': 'success', 'message': 'Cached Nonce Acquired',
                         'payload': 'You’re now signing into Tanx Testnet, make sure the origin is https://testnet.tanx.fi (Login-code:abc)'},
                   status=200)
    responses.post(url=f"{BASE_URL}/sapi/v1/auth/v2/login/",
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
                      'name': 'test', 'img': None, 'username': '0x7tanx', 'stark_key': '0x'}},
                  status=200)
    assert "name" in client.get_profile_info()['payload']


@responses.activate
def test_get_balance():
    responses.get(url=f"{BASE_URL}/sapi/v1/user/balance/",
                  json={'status': 'success', 'message': 'Retrieved Successfully', 'payload': [{'currency': 'btc', 'balance': '0.0091892', 'locked': '0.0'}, {
                      'currency': 'eth', 'balance': '0.2179175', 'locked': '0.0'}, {'currency': 'usdc', 'balance': '56.354237624', 'locked': '0.0'}, {'currency': 'usdt', 'balance': '79.699671653', 'locked': '0.0'}]},
                  status=200)
    r = cast(List[Balance], client.get_balance()['payload'])
    assert "balance" in r[0]


@responses.activate
def test_get_balance_expired_access_token():

    responses.get(url=f"{BASE_URL}/sapi/v1/user/balance/",
                  json={
                      "status": 'error',
                      "message": 'Given token not valid for any token type',
                      "payload": {
                          "token_class": 'AccessToken',
                          "token_type": 'access',
                          "message": 'Token is invalid or expired',
                          "code": 'token_not_valid',
                      },
                  },
                  status=401)

    responses.post(url=f"{BASE_URL}/sapi/v1/auth/token/refresh/", 
                   json={
                        "status": 'success',
                        "message": '',
                        "payload": {
                            "access": 'ferasdfklre',
                            "refresh": 'fekcjicbd',
                        },
                    },
                    status=200)
                
    responses.get(url=f"{BASE_URL}/sapi/v1/user/balance/",
                json={'status': 'success', 'message': 'Retrieved Successfully', 'payload': [{'currency': 'btc', 'balance': '0.0091892', 'locked': '0.0'}, {
                    'currency': 'eth', 'balance': '0.2179175', 'locked': '0.0'}, {'currency': 'usdc', 'balance': '56.354237624', 'locked': '0.0'}, {'currency': 'usdt', 'balance': '79.699671653', 'locked': '0.0'}]},
                status=200)
    
    r = cast(List[Balance], client2.get_balance()['payload'])

    assert "balance" in r[0]

@responses.activate
def test_get_balance_expired_refresh_token():
    responses.get(url=f"{BASE_URL}/sapi/v1/user/balance/",
                  json={
                      "status": 'error',
                      "message": 'Given token not valid for any token type',
                      "payload": {
                          "token_class": 'AccessToken',
                          "token_type": 'access',
                          "message": 'Token is invalid or expired',
                          "code": 'token_not_valid',
                      },
                  },
                 status=401)

    responses.post(url=f"{BASE_URL}/sapi/v1/auth/token/refresh/", json={
        "status": "error",
        "message": "Token is invalid or expired",
        "payload": {
            "code": "token_not_valid"
        }
    },
      status=401)
    

    with pytest.raises(requests.exceptions.HTTPError):
        r = client2.get_balance()['payload']


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
    nonce_res = client.create_order_nonce({'market': 'btcusdt', 'ord_type': 'market',
                                           'price': 29580.51, 'side': 'buy', 'volume': 0.0001})
    stark_private_key = '0x64004f706c1eaa39348afb3191c74812d86e5b14b967e578addb4d89ce1234c'
    # replace with your stark private key
    msg_hash = sign_order_with_stark_private_key(
        stark_private_key, nonce_res['payload'])
    assert "Order" in client.create_new_order(msg_hash)['message']


@responses.activate
def test_create_order_nonce_raises_400_error():
    responses.post(url=f"{BASE_URL}/sapi/v1/orders/nonce/",
                   json={
                       'status': 'error', 'message': 'Maximum decimals allowed for volume is 4 in btcusdt market', 'payload': ''},
                   status=400)
    with pytest.raises(requests.exceptions.HTTPError):
        nonce_res = client.create_order_nonce({'market': 'btcusdt', 'ord_type': 'market',
                                               'price': 29580.51, 'side': 'buy', 'volume': 0.00001})
        stark_private_key = '0x64004f706c1eaa39348afb3191c74812d86e5b14b967e578addb4d89ce1234c'
        # replace with your stark private key
        msg_hash = sign_order_with_stark_private_key(
            stark_private_key, nonce_res['payload'])
        client.create_new_order(msg_hash)['message']


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

@responses.activate
def test_eth_deposits_with_stark_key_success():
    responses.post(url=f'{BASE_URL}/sapi/v1/payment/stark/start/',
                    json={'status': 'success',
                        'message': 'Success! Awaiting Blockchain Confirmation',
                        'payload': ''})
    res = client.crypto_deposit_start(100000,'0x27..','0x27..','0x67..','930','65707',)
    assert 'status' in res
    assert 'success' == res['status']
    assert 'payload' in res

@responses.activate
def test_eth_deposits_with_stark_key_fail():
    responses.post(url=f'{BASE_URL}/main/payment/stark/start/',
                    json={'status':'error',
                        'message':'Essential parameters are missing',
                        'payload': ''})
    with pytest.raises(requests.exceptions.RequestException):
        res = client.crypto_deposit_start(100000,'0x27..','0x27..','0x67..','930','65707',)
    # Handle exception
        
        data = res.response.json()
        assert 'status' in data
        assert data['status'] == 'error'
        assert 'Essential parameters' in data['message']

@responses.activate
def test_list_deposits():
    responses.get(url=f'{BASE_URL}/sapi/v1/deposits/',
                    json=list_deposits_response)
    data = client.list_deposits({'network': 'ETHEREUM'}) # type:ignore

    assert 'status' in data
    assert data['status'] == 'success'
    assert 'payload' in data

@responses.activate
def test_initiate_withdrawals_success():
    responses.post(url=f'{BASE_URL}/sapi/v1/payment/withdrawals/v1/initiate/',
                    json={'status': 'success',
                        'message': 'successfully initiated withdrawal',
                        'payload': {
                            'nonce': 7819,
                            'msg_hash': '686148137588728084357640508492604406021032862346002124816784805415214096923'
                        }})
    res = client.start_normal_withdrawal({
        'amount': 0.00001,
        'symbol': 'eth'
    })
    assert 'status' in res
    assert res['status'] == 'success'
    assert 'payload' in res

@responses.activate
def test_validate_withdrawal_success():
    responses.post(url=f'{BASE_URL}/sapi/v1/payment/withdrawals/v1/validate/',
                    json=validate_withdrawal_response)
    res = client.validate_normal_withdrawal({
            'msg_hash':
                '1845898ec19c65beac9eb12be93adc8fa4fe00a494aa005e2f2cc5bade3a21b',
            'signature': {
                'r': '0x4a0a8a...',
                's': '0x7fc5d01...',
                'recoveryParam': 1,
            },
            'nonce': '7819',
        })
    
    assert 'status' in res
    assert res['status'] == 'success'
    assert 'payload' in res

@responses.activate
def test_validate_withdrawal_failure():
    responses.post(url=f'{BASE_URL}/sapi/v1/payment/withdrawals/v1/validate/',
                    json={'status': 'error',
                    'message': 'Withdrawal Validation Failed, please try again',
                    'payload': ''})
    res = client.validate_normal_withdrawal({
            'msg_hash':
                '1845898ec19c65beac9eb12be93adc8fa4fe00a494aa005e2f2cc5bade3a21b',
            'signature': {
                'r': '0x4a0a8a...',
                's': '0x7fc5d01...',
                'recoveryParam': 1,
            },
            'nonce': '7819',
        })
    
    assert 'status' in res
    assert res['status'] == 'error'
    assert 'Withdrawal Validation Failed' in res['message']

@responses.activate
def test_list_withdrawals():
    responses.get(url=f'{BASE_URL}/sapi/v1/payment/withdrawals/',
                    json=list_withdrawals_response)
    res = client.list_normal_withdrawals()

    assert 'status' in res
    assert res['status'] == 'success'
    assert 'payload' in res
def test_deposit_from_ethereum_network_with_stark_key_invalid_amount():
    w3 = Web3()
    test_signer = w3.eth.account.create()

    test_provider = Web3(EthereumTesterProvider())

    with pytest.raises(InvalidAmountError):
        client.deposit_from_ethereum_network_with_stark_key(signer=test_signer, provider=test_provider, stark_public_key='0x27..', amount=0, currency='eth')

@responses.activate
def test_deposit_from_ethereum_network_with_stark_key_low_balance():
    responses.post(f'{BASE_URL}/main/stat/v2/coins/', json=coin_stats_response)
    responses.post(f'{BASE_URL}/main/user/create_vault/', json=get_vault_id_response)

    test_provider = Web3(EthereumTesterProvider())
    w3 = Web3()
    test_signer = w3.eth.account.create()

    with pytest.raises(BalanceTooLowError):
        client.deposit_from_ethereum_network_with_stark_key(signer=test_signer, provider=test_provider, stark_public_key='0x27..', amount=0.0001, currency='eth')

@responses.activate
def test_initiat_internal_transfer_succcess():
    responses.post(url=f'{BASE_URL}/sapi/v1/internal_transfers/v2/initiate/',
                    json={'status': 'success',
                        'message': 'Please sign the message, to complete the transaction',
                        'payload': {
                            'nonce': 797982128,
                            'msg_hash': '0x2af4af1aa1e47a8b4d71a111a0b5a0649d80d586090548f7bb5a7ba74c287d3',
                        }
                    })
    res = client.initiate_internal_transfer({
        'organization_key': 'abcd...',
        'api_key': 'xyz...',
        'currency': 'usdc',
        'amount': 1,
        'destination_address': '0xF5...',
        'client_reference_id': 10
    })

    assert 'status' in res
    assert res['status'] == 'success'
    assert 'payload' in res
    assert 'nonce' in res['payload']

@responses.activate
def test_execute_internal_transfer_success():
    responses.post(url=f'{BASE_URL}/sapi/v1/internal_transfers/v2/process/',
                    json={
                        'status': 'success',
                        'message': 'Internal transfer processed successfully',
                        'payload': {
                            'client_reference_id': '6462569061361987',
                            'amount': '1.0000000000000000',
                            'currency': 'usdc',
                            'from_address': '0x6c875514E42F14B891399A6a8438E6AA8F77B178',
                            'destination_address': '0xF5F467c3D86760A4Ff6262880727E854428a4996',
                            'status': 'success',
                            'created_at': '2023-07-26T06:28:52.350343Z',
                            'updated_at': '2023-07-26T06:28:52.902831Z'
                        }
                    })
    res = client.execute_internal_transfers({
        'organization_key': 'abcd...',
        'api_key': 'xyz...',
        'signature': {
            'r': '0x12...',
            's': '0x4a...',
        },
        'nonce': 14214931,
        'msg_hash': '0xda0...'
    }) # type:ignore
    assert 'status' in res
    assert res['status'] == 'success'
    assert 'payload' in res
    assert 'client_reference_id' in res['payload']    

@responses.activate
def test_initiate_internal_transfer_403_invalid_credential():
    responses.post(f'{BASE_URL}/sapi/v1/internal_transfers/v2/initiate/',
                    json={
                        'status': 'error',
                        'message': 'Invalid organization key',
                        'payload': ''
                    }, status=403)
    with pytest.raises(requests.exceptions.HTTPError):
        res = client.initiate_internal_transfer({
            'organization_key': 'abcd...',
            'api_key': 'xyz...',
            'currency': 'usdc',
            'amount': 1,
            'destination_address': '0xF5...',
            'client_reference_id': 10
        })
        assert 'status' in res
        assert res['status'] == 'error'

@responses.activate
def test_execute_internal_transfer_403_invalid_credential():
    responses.post(f'{BASE_URL}/sapi/v1/internal_transfers/v2/process/',
                    json={
                        'status': 'error',
                        'message': 'Invalid organization key',
                        'payload': ''
                    }, status=403)
    
    with pytest.raises(requests.exceptions.HTTPError):
        res = client.execute_internal_transfers({
            'organization_key': 'abcd...',
            'api_key': 'xyz...',
            'signature': {
                'r': '0x12...',
                's': '0x4a...',
            },
            'nonce': 14214931,
            'msg_hash': '0xda0...'
        }) # type:ignore
        assert 'status' in res
        assert res['status'] == 'error'

@responses.activate
def test_list_internal_transfers_success():
    responses.get(url=f'{BASE_URL}/sapi/v1/internal_transfers/v2/',
                    json=list_internal_transfer_response, status=200)
    res = client.list_internal_transfers()
    assert 'status' in res
    assert res['status']=='success'
    assert 'client_reference_id' in res['payload']['internal_transfers'][0]

@responses.activate
def test_get_internal_transfer_by_client_id():
    client_id = 1234
    responses.get(url=f'{BASE_URL}/sapi/v1/internal_transfers/v2/{client_id}',
                    json=get_internal_transfer_by_client_id_response, status=200)
    res = client.get_internal_transfer_by_client_id(client_reference_id=client_id)
    assert 'status' in res
    assert res['status'] == 'success'

@responses.activate
def test_transfer_does_not_exist():
    client_id = 1234
    responses.get(url=f'{BASE_URL}/sapi/v1/internal_transfers/v2/{client_id}',
                    json={
                        'status': 'error',
                        'message': 'Transfer does not exist',
                        'payload': ''
                    }, status=404)
    
    with pytest.raises(requests.exceptions.HTTPError):
        res = client.get_internal_transfer_by_client_id(client_reference_id=client_id)
        assert 'status' in res
        assert res['status'] == 'error'

@responses.activate
def test_user_exists_success():
    responses.post(url=f'{BASE_URL}/sapi/v1/internal_transfers/v2/check_user_exists/',
                    json={
                        'status': 'success',
                        'message': 'User exists',
                        'payload': {
                            'destination_address': '0xF5...',
                            'exists': True
                        }
                    })

    res = client.check_internal_transfer_user_exists(
        organization_key='abcd...',
        api_key='xyz...',
        destination_address='0xF5...'
    )
    assert 'status' in res
    assert res['status'] == 'success'
    assert 'payload' in res

@responses.activate
def test_user_exists_failure():
    responses.post(url=f'{BASE_URL}/sapi/v1/internal_transfers/v2/check_user_exists/',
                    json={
                        'status': 'success',
                        'message': 'User does not exists',
                        'payload': {
                            'destination_address': '0xF5...',
                            'exists': False
                        }
                    }, status=404)

    with pytest.raises(requests.exceptions.HTTPError):
        res = client.check_internal_transfer_user_exists(
            organization_key='abcd...',
            api_key='xyz...',
            destination_address='0xF5...'
        )
        assert 'status' in res
        assert res['status'] == 'error'

@responses.activate
def test_start_polygon_deposits_success():
    responses.post(url=f'{BASE_URL}/sapi/v1/deposits/crosschain/create/',
                    json={'status': 'success',
                        'message': 'Success! Awaiting Blockchain Confirmation',
                        'payload': {
                            'transaction_hash': ''
                        },
                    })

    res = client.cross_chain_deposit_start(100000,'0x27..','0x67..','930',)

    assert 'status' in res
    assert res['status'] == 'success'
    assert 'payload' in res

@responses.activate
def test_start_polygon_deposits_failure():
    responses.post(url=f'{BASE_URL}/sapi/v1/deposits/crosschain/create/',
                    json={'status': 'error',
                        'message': 'Essential parameters are missing',
                        'payload': '',
                    })
    
    data = client.cross_chain_deposit_start(100000,'0x27..','0x67..','930',)
    assert 'status' in data
    assert data['status'] == 'error'
    assert 'Essential parameters' in data['message']

@responses.activate
def test_list_polygon_deposits():
    responses.get(url=f'{BASE_URL}/sapi/v1/deposits/',
                    json=list_polygon_deposits_response)

    res = client.list_deposits({'network': 'POLYGON'})      # type:ignore
    assert 'status' in res
    assert res['status'] == 'success'
    assert 'payload' in res

@responses.activate
def test_deposit_from_polygon_network_with_signer_invalid_amount():
    w3 = Web3()
    test_signer = w3.eth.account.create()

    test_provider = Web3(EthereumTesterProvider())

    with pytest.raises(InvalidAmountError):
        client.deposit_from_polygon_network_with_signer(signer=test_signer, provider=test_provider, amount=0, currency='matic')

@responses.activate
def test_deposit_from_polygon_network_with_signer_low_balance():
    responses.post(f'{BASE_URL}/main/stat/v2/app-and-markets/', json=network_config_response)
    responses.post(f'{BASE_URL}/main/user/create_vault/', json=get_vault_id_response)

    test_provider = Web3(EthereumTesterProvider())
    w3 = Web3()
    test_signer = w3.eth.account.create()

    with pytest.raises(BalanceTooLowError):
        client.deposit_from_polygon_network_with_signer(signer=test_signer, provider=test_provider, amount=0.0001, currency='matic')

