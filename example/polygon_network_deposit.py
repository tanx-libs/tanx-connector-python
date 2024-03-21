import requests
import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.tanxconnector import Client  # noqa: E402
from src.tanxconnector import exception  # noqa: E402
from web3 import Web3, Account
from web3.middleware.geth_poa import geth_poa_middleware

load_dotenv()

PRIVATE_KEY = os.environ['PRIVATE_KEY']
ETH_ADDRESS = os.environ['ETH_ADDRESS']
polygon_rpc_provider = os.environ['POLYGON_RPC_PROVIDER']

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

# initialize the provider and signer
provider = Web3(Web3.HTTPProvider(polygon_rpc_provider))
provider.middleware_onion.inject(geth_poa_middleware, layer=0)
signer = Account.from_key(PRIVATE_KEY)

# deposit with eth private key
deposit_res_with_private_key = client.deposit_from_polygon_network(
    polygon_rpc_provider,
    PRIVATE_KEY,
    'matic',
    0.00001
)
print(deposit_res_with_private_key)


# approval for unlimited allowance for ERC20 contracts
allowance = client.approve_unlimited_allowance_polygon_network(coin='btc', signer=signer, w3=provider)
print(allowance)

# deposit with signer
deposit_res_with_signer = client.deposit_from_polygon_network_with_signer(
    signer,
    provider,
    'btc',
    0.0001,
)
print(deposit_res_with_signer)
