import requests
import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.tanxconnector import Client  # noqa: E402
from src.tanxconnector import exception  # noqa: E402
from web3 import Web3, Account

load_dotenv()

PRIVATE_KEY = os.environ['PRIVATE_KEY']
ETH_ADDRESS = os.environ['ETH_ADDRESS']
ETH_ADDRESS_2 = os.environ['ETH_ADDRESS_2']
stark_private_key = os.environ['STARK_PRIVATE_KEY']
stark_public_key = os.environ['STARK_PUBLIC_KEY']
TANX_ORGANIZATION_KEY = os.environ['TANX_ORGANIZATION_KEY']
TANX_API_KEY = os.environ['TANX_API_KEY']

def internal_transfers():
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

        # check if user exists by their destination address
        check_user_res = client.check_internal_transfer_user_exists(
            organization_key=TANX_ORGANIZATION_KEY,
            api_key=TANX_API_KEY,
            destination_address=ETH_ADDRESS_2,
        )
        print(check_user_res)

        internal_transfer_response = client.intiate_and_process_internal_transfers(
            key_pair=key_pair,
            organization_key=TANX_ORGANIZATION_KEY,
            api_key=TANX_API_KEY,
            currency='usdc',
            amount=1,
            destination_address=ETH_ADDRESS_2,
            client_reference_id=123
        )
        print(internal_transfer_response)

        internal_trasnfers_list = client.list_internal_transfers({
            'limit': 10
        })  # type:ignore
        print(internal_trasnfers_list)

        # if len(internal_trasnfers_list['payload']['internal_transfers']):
        #     # get the internal transfer by client ID
        #     internal_transfer_by_id = client.get_internal_transfer_by_client_id(client_reference_id=internal_trasnfers_list['payload']['internal_transfers'][0]['client_reference_id'])
        #     print(internal_transfer_by_id)
        

    # except requests.exceptions.HTTPError as e:
    #     print(e.response.json())

    except Exception as e:
        print(e)

internal_transfers()
