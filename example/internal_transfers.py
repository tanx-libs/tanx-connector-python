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
ETH_ADDRESS_2 = os.environ['ETH_ADDRESS_2']
stark_private_key = os.environ['STARK_PRIVATE_KEY']
stark_public_key = os.environ['STARK_PUBLIC_KEY']
rpc_provider = os.environ['RPC_PROVIDER']
BRINE_ORGANIZATION_KEY = os.environ['BRINE_ORGANIZATION_KEY']
BRINE_API_KEY = os.environ['BRINE_API_KEY']

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
        provider = Web3(Web3.HTTPProvider(rpc_provider))
        signer = Account.from_key(PRIVATE_KEY)

        # internal_transfer_response = client.intiate_and_process_internal_transfers(
        #     key_pair=key_pair,
        #     organization_key=BRINE_ORGANIZATION_KEY,
        #     api_key=BRINE_API_KEY,
        #     currency='usdc',
        #     amount=1,
        #     destination_address=ETH_ADDRESS_2,
        #     client_reference_id=1
        # )
        # print(internal_transfer_response)

        internal_trasnfers_list = client.list_internal_transfers({
            'limit': 10
        })  # type:ignore
        print(internal_trasnfers_list)

        if len(internal_trasnfers_list['payload']['internal_transfers']):
            # get the internal transfer by client ID
            internal_transfer_by_id = client.get_internal_transfer_by_client_id(client_reference_id=internal_trasnfers_list['payload']['internal_transfers'][0]['client_reference_id'])
            print(internal_transfer_by_id)
        
        # check if user exists by their destination address
        check_user_res = client.check_internal_transfer_user_exists(
            organization_key=BRINE_ORGANIZATION_KEY,
            api_key=BRINE_API_KEY,
            destination_address=ETH_ADDRESS_2,
        )
        print(check_user_res)


    # except requests.exceptions.HTTPError as e:
    #     print(e.response.json())

    except Exception as e:
        print(e)

internal_transfers()
