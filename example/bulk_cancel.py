import os
import requests
import sys
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.tanxconnector import Client
from src.tanxconnector import exception  # noqa: E402

load_dotenv()

PRIVATE_KEY = os.environ['PRIVATE_KEY']
ETH_ADDRESS = os.environ['ETH_ADDRESS']

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



# Run the function
res = client.bulk_cancel({
    'market': 'btcusdt',
    'limit': 100, # optional
    'side': 'buy' # optional
})
print(res)