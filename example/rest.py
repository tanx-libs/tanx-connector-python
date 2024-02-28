import requests
import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.brineconnector import Client  # noqa: E402
from src.brineconnector import sign_msg  # noqa: E402
from src.brineconnector import exception  # noqa: E402
from src.brineconnector.typings import CreateOrderNonceBody  # noqa: E402
from src.brineconnector import create_user_signature, sign_order_with_stark_private_key, sign_msg_hash
from src.brineconnector.bin.signature import get_stark_key_pair_from_signature
from web3 import Web3, Account

load_dotenv()

PRIVATE_KEY = os.environ['PRIVATE_KEY']
ETH_ADDRESS = os.environ['ETH_ADDRESS']
stark_private_key = os.environ['STARK_PRIVATE_KEY']
rpc_provider = os.environ['RPC_PROVIDER']

def main():

    client = Client('testnet')
    # create a rest client instance (default is mainnet)
    # client.test_connection()
    # you can use public endpoints right away
    trades = client.get_recent_trades('btcusdc')
    # print(trades)
    orderbook = client.get_orderbook('btcusdc')
    try:
        # login to use private endpoints
        login = client.complete_login(ETH_ADDRESS, PRIVATE_KEY)
        print(login)
    # Error: AuthenticationError | requests.exceptions.HTTPError

    except exception.AuthenticationError as exc:
        print(exc)
    except requests.exceptions.HTTPError as exc:
        print(exc.response.json())

    # # create an order nonce
    # nonce: CreateOrderNonceBody = {'market': 'btcusdt', 'ord_type': 'market',
    #                                'price': 29580.51, 'side': 'buy', 'volume': 0.0001}

    # # create order (private)
    # nonce_res = client.create_order_nonce(nonce)
    # # msg_hash = sign_order_with_stark_private_key(stark_private_key, nonce_res['payload'])
    # msg_hash = sign_msg_hash(nonce_res['payload'], PRIVATE_KEY, 'testnet')
    # try:
    #     order = client.create_new_order(msg_hash)
    #     print(order)
    # except requests.exceptions.HTTPError as exc:
    #     print(exc.response.json())

    # nonce: CreateOrderNonceBody = {'market': 'ethusdc', 'ord_type': 'market',
    #                                'price': 29580.51, 'side': 'sell', 'volume': 0.0005}

    # # cancel order (private)
    # nonce_res_for_order_to_cancel = client.create_order_nonce(nonce)
    # msg_hash = sign_order_with_stark_private_key(stark_private_key, nonce_res_for_order_to_cancel['payload'])
    # msg_hash = sign_msg_hash(nonce_res_for_order_to_cancel['payload'], PRIVATE_KEY, 'testnet')
    # try:
    #     order_to_cancel = client.create_new_order(msg_hash)
    #     cancelled_order = client.cancel_order(order_to_cancel['payload']['id'])
    #     print(cancelled_order)
    # except requests.exceptions.HTTPError as exc:
    #     print(exc.response.json())

    # get all orders (private)
    # orders = client.list_orders()

    # get profile info (private)
    # profile = client.get_profile_info()
    # print(profile['payload']['username'])


# main()

# Deposits
def ethereum_deposit_and_withdrawal():
    try:
        client = Client('testnet')
        try:
            # login to use private endpoints
            login = client.complete_login(ETH_ADDRESS, PRIVATE_KEY)
            print('Login Successful')
        # Error: AuthenticationError | requests.exceptions.HTTPError
        except exception.AuthenticationError as exc:
            print(exc)
        except requests.exceptions.HTTPError as exc:
            print(exc.response.json())

        user_signature = create_user_signature(PRIVATE_KEY, 'testnet')
        key_pair = get_stark_key_pair_from_signature(user_signature)
        stark_public_key = key_pair['stark_public_key']
        provider = Web3(Web3.HTTPProvider(rpc_provider))
        signer = Account.from_key(PRIVATE_KEY)

        # # deposit with eth private key
        # deposit_res_with_private_key = client.deposit_from_ethereum_network(
        #     rpc_provider,
        #     PRIVATE_KEY,
        #     'testnet',
        #     'eth',
        #     0.00001
        # )
        # print(deposit_res_with_private_key)


        # # approval for unlimited allowance for ERC20 contracts
        # allowance = client.approve_unlimited_allowance_ethereum_network('usdc', signer, provider)
        # print(allowance)

        # # deposit with L2 key
        # deposit_res_with_stark_keys = client.deposit_from_ethereum_network_with_starkKey(
        #     signer,
        #     provider,
        #     f'0x{stark_public_key}',
        #     0.0001,
        #     'usdc'
        # )
        # print(deposit_res_with_stark_keys)

        # # Withdrawals
        # # Normal withdrawal
        # # 1. Initiate your withdrawal request by calling "initiateNormalWithdrawal".
        # withdrawal_res = client.initiate_normal_withdrawl(key_pair=key_pair, amount=0.0001, coin_symbol='usdc')
        # print(withdrawal_res)
        # # 2. WAIT for up to 24 hours.
        # # 3. Call the function "get_pending_normal_withdrawal_amount_by_coin" by passing the required parameter
        # #    to check whether the withdrawn balance is pending
        # pending_balance = client.get_pending_normal_withdrawal_amount_by_coin(coin_symbol='eth', user_public_eth_address=ETH_ADDRESS,
        #                                                                         signer=signer, provider=provider)
        # print(pending_balance)
        # 4. Final step - if you find the balance is more than 0, you can call "completeNormalWithdrawal"
        #    to withdraw the cumulative amount to your ETH wallet.
        # complete_normal_withdrawal_res = client.complete_normal_withdrawal(
        #     'eth',
        #     ETH_ADDRESS,
        #     signer,
        #     provider
        # )
        # print(complete_normal_withdrawal_res)



    except Exception as e:
        print(e)

ethereum_deposit_and_withdrawal()