import requests
import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.brineconnector import Client  # noqa: E402
from src.brineconnector import exception  # noqa: E402
from web3 import Web3, Account
from web3.middleware.geth_poa import geth_poa_middleware

load_dotenv()

PRIVATE_KEY = os.environ['PRIVATE_KEY']
ETH_ADDRESS = os.environ['ETH_ADDRESS']
stark_private_key = os.environ['STARK_PRIVATE_KEY']
stark_public_key = os.environ['STARK_PUBLIC_KEY']
rpc_provider = os.environ['RPC_PROVIDER']
polygon_rpc_provider = os.environ['POLYGON_RPC_PROVIDER']

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

        provider = Web3(Web3.HTTPProvider(rpc_provider))
        signer = Account.from_key(PRIVATE_KEY)

        # approval for unlimited allowance for ERC20 contracts
        # allowance = client.approve_unlimited_allowance_ethereum_network('usdc', signer, provider)
        # print(allowance)

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

# Deposits for polygon Network
def polygonDeposit():
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

        provider = Web3(Web3.HTTPProvider(polygon_rpc_provider))
        provider.middleware_onion.inject(geth_poa_middleware, layer=0)
        signer = Account.from_key(PRIVATE_KEY)

        # # deposit with eth private key
        # deposit_res_with_private_key = client.deposit_from_polygon_network(
        #     polygon_rpc_provider,
        #     PRIVATE_KEY,
        #     'matic',
        #     0.00001
        # )
        # print(deposit_res_with_private_key)


        # # approval for unlimited allowance for ERC20 contracts
        # allowance = client.approve_unlimited_allowance_polygon_network(coin='btc', signer=signer, w3=provider)
        # print(allowance)

        # deposit with signer
        deposit_res_with_signer = client.deposit_from_polygon_network_with_signer(
            signer,
            provider,
            'btc',
            0.0001,
        )
        print(deposit_res_with_signer)

    except Exception as e:
        print(e)

polygonDeposit()
