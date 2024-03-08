import requests
import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.brineconnector import Client  # noqa: E402
from src.brineconnector import exception  # noqa: E402
from web3 import Web3, Account

load_dotenv()

PRIVATE_KEY = os.environ['PRIVATE_KEY']
ETH_ADDRESS = os.environ['ETH_ADDRESS']
stark_private_key = os.environ['STARK_PRIVATE_KEY']
stark_public_key = os.environ['STARK_PUBLIC_KEY']
rpc_provider = os.environ['RPC_PROVIDER']

def eth_withdrawals():
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

        key_pair = {'stark_private_key': stark_private_key, 'stark_public_key': stark_public_key}
        provider = Web3(Web3.HTTPProvider(rpc_provider))
        signer = Account.from_key(PRIVATE_KEY)

        # Withdrawals
        # Normal withdrawal
        # 1. Initiate your withdrawal request by calling "initiate_normal_withdrawal".

        # withdrawal_res = client.initiate_normal_withdrawal(key_pair=key_pair, amount=0.0001, coin_symbol='usdc')
        # print(withdrawal_res)

        # 2. WAIT for up to 24 hours.
        # 3. Call the function "get_pending_normal_withdrawal_amount_by_coin" by passing the required parameter
        #    to check whether the withdrawn balance is pending

        # pending_balance = client.get_pending_normal_withdrawal_amount_by_coin(coin_symbol='eth', user_public_eth_address=ETH_ADDRESS,
        #                                                                         signer=signer, provider=provider)
        # print(pending_balance)

        # 4. Final step - if you find the balance is more than 0, you can call "complete_normal_withdrawal"
        # to withdraw the cumulative amount to your ETH wallet.

        # complete_normal_withdrawal_res = client.complete_normal_withdrawal(
        #     'eth',
        #     ETH_ADDRESS,
        #     signer,
        #     provider
        # )
        # print(complete_normal_withdrawal_res)

        # Get a list of withdrawals
        # withdrawals_list = client.list_normal_withdrawals()

        # Fast Withdrawals
        # fast_withdrawal_res = client.fast_withdrawal(
        #     key_pair,
        #     10,
        #     'usdc',
        #     'ETHEREUM'
        # )
        # print(fast_withdrawal_res)

        # List Fast Withdrawals
        # list_fast_withdrawals_res = client.list_fast_withdrawals({
        #     'page': 2
        # }) # type:ignore
        # print(list_fast_withdrawals_res)

    except requests.exceptions.HTTPError as e:
        print(e.response.json())
    
    except Exception as e:
        print(e)

# eth_withdrawals()

def polygon_withdrawal():
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

        fast_withdrawal_res = client.fast_withdrawal(
            key_pair,
            0.0008,
            'btc',
            'POLYGON'
        )
        print(fast_withdrawal_res)

        # List Fast Withdrawals
        list_fast_withdrawals_res = client.list_fast_withdrawals({
            'page': 1,
            'network': 'POLYGON'
        })
        print(list_fast_withdrawals_res)

    except requests.exceptions.HTTPError as e:
        print(e.response.json())
    
    except Exception as e:
        print(e)

polygon_withdrawal()