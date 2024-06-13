import requests
import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.tanxconnector import Client  # noqa: E402
from src.tanxconnector import exception  # noqa: E402

load_dotenv()

PRIVATE_KEY = os.environ['PRIVATE_KEY']
ETH_ADDRESS = os.environ['ETH_ADDRESS']
stark_private_key = os.environ['STARK_PRIVATE_KEY']
stark_public_key = os.environ['STARK_PUBLIC_KEY']


client = Client("testnet")

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

# Fast Withdrawals on eth network
fast_withdrawal_res = client.fast_withdrawal(
    key_pair,
    10,
    'usdt',     # coin
    'OPTIMISM'  # network
)
print(fast_withdrawal_res)

# List Fast Withdrawals
list_fast_withdrawals_res = client.list_fast_withdrawals({
    'page': 2,  # page (optional)
    'network': 'ETHEREUM'  # network (optional)
}) # type:ignore
print(list_fast_withdrawals_res)

# Fast Withdrawals
fast_withdrawal_res = client.fast_withdrawal(
    key_pair,
    10,
    'usdc',
    'ETHEREUM'
)
print(fast_withdrawal_res)

# List Fast Withdrawals
list_fast_withdrawals_res = client.list_fast_withdrawals({
    'page': 1,
    'network': 'POLYGON'
})
print(list_fast_withdrawals_res)
