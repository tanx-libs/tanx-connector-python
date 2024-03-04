import requests
import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.brineconnector import Client  # noqa: E402
from src.brineconnector import exception  # noqa: E402
from src.brineconnector import create_user_signature
from src.brineconnector.bin.signature import get_stark_key_pair_from_signature
from web3 import Web3, Account

load_dotenv()

PRIVATE_KEY = os.environ['PRIVATE_KEY']
ETH_ADDRESS = os.environ['ETH_ADDRESS']
stark_private_key = os.environ['STARK_PRIVATE_KEY']
rpc_provider = os.environ['RPC_PROVIDER']

# Deposits
def ethereumDeposit():
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

        # deposit with eth private key
        deposit_res_with_private_key = client.deposit_from_ethereum_network(
            rpc_provider,
            PRIVATE_KEY,
            'testnet',
            'eth',
            0.00001
        )
        print(deposit_res_with_private_key)


        # approval for unlimited allowance for ERC20 contracts
        allowance = client.approve_unlimited_allowance_ethereum_network('usdc', signer, provider)
        print(allowance)

        # deposit with L2 key
        deposit_res_with_stark_keys = client.deposit_from_ethereum_network_with_starkKey(
            signer,
            provider,
            f'0x{stark_public_key}',
            0.0001,
            'usdc'
        )
        print(deposit_res_with_stark_keys)

        deposit_list = client.list_deposits({
            'page': 1,
            'limit': 1,
            'network': 'ETHEREUM'
        })
        print(deposit_list)

    except Exception as e:
        print(e)

# ethereumDeposit()