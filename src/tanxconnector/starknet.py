# import { Account, Contract, uint256, Provider } from 'starknet'
# import starkErc20Abi from './bin/starknet_erc20_abi.json'
# import { dequantize } from './utils'

#arush
from decimal import Decimal

# from common.choices import Environment
# from common.exceptions import EstimatedGasFeeCrossedDefaultMaxGasFeeException, InsufficientFundsInAdminWalletException, InsufficientGasFeeFundsInAdminWalletException, RowAlreadyLockException, StarknetFastWithdrawalExtrasNotFoundException
# from krypto_common.alerts.enum import AlertLevelsEnum, RegisteredAlertServicesEnum, OncallAlertService
# from krypto_common.alerts.service import AlertService
# from payment.choices import FastWithdrawalBlockchainStatus, FastWithdrawalTransactionStatus, NetworkChoice
# from starknet_py.net.account.account import Account, _parse_calls_v2, _execute_payload_serializer_v2, ensure_iterable, _merge_calls, _execute_payload_serializer
from starknet_py.net.account.account import Account
from starknet_py.net.models import StarknetChainId
from starknet_py.net.signer.stark_curve_signer import KeyPair
import json
from starknet_py.contract import Contract
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.client_errors import ClientError
# from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.models.transaction import Invoke
from starknet_py.net.client_models import (
    SierraContractClass,
)
# from django.conf import settings
# from krypto_common.constants import CrossChainConfig
# from payment.helpers.fast_wd_status_update_helper import FastWithdrawalStatusUpdateHelper
# from payment.models import FastWithdrawalTransaction, StarknetFastWithdrawalExtra
# from payment.service.dexrefund_utility import DexRefundUtility
# from static_data.coin_config.config_helper import CoinConfigHelper
import logging
# from django.utils import timezone
# from django.db import transaction
# from django.contrib.auth import get_user_model

logger = logging.getLogger(__file__)

#arush 

from starknet_py.net.models import DeclareV3
from starknet_py.net.account.account import Account
from starknet_py.contract import Contract
from starknet_py.serialization import Uint256Serializer
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.models import StarknetChainId
from .constants import Config
from .utils import dequantize
import json
from starknet_py.hash.selector import get_selector_from_name
from starknet_py.net.client_models import Call

class StarkNetHelper:
    def __init__(self):
        pass
    def get_account(self, starknet_rpc:str, public_address:str, private_address:str):
        return Account(
                    address=public_address,
                    client=FullNodeClient(node_url=starknet_rpc),
                    key_pair=(private_address,public_address),
                    chain=StarknetChainId.SEPOLIA,
                )
    @classmethod
    async def get_starknet_user_balance(self,token_address: str, starknet_rpc:str, public_address:str, private_address:str,):
        account = self.get_account(self, starknet_rpc,public_address, private_address)
        balance = await account.get_balance(token_address)
        l=[]
        for part in Uint256Serializer._serialize_from_int(balance):
            l.append(part)
        balance = dequantize(l[0], l[1])
        return balance
    

    async def execute_starknet_transaction(public_address:str, private_address:str, starknet_rpc:str,quantized_amount:int, data:str):
        client = FullNodeClient(node_url=starknet_rpc)

        account=Account(
            address=public_address,
            client=FullNodeClient(node_url=starknet_rpc),
            key_pair=(private_address,public_address),
            chain=StarknetChainId.MAINNET,
            )
        contract = Contract(provider=account,
                            abi=Config.STARK_NET_ABI,
                            address=public_address)
        
        data=data["ls_data"]
        to_address=data["to_address"]
        calldata=json.loads(data["data"])[0]['calldata']
        data = [int(data['to_address'], 16), 4000000]
        print(data,'❌')

        

        nonce = await account.get_nonce()
        
        # cairo_version = ""
        # call = Call(to_addr=to_address, selector=get_selector_from_name('transfer'), calldata=data)
        # resp = await account.execute_v3(calls=call, auto_estimate=True)
        # print(call, resp)


        # if isinstance(client, FullNodeClient):
        #     contract_class = await client.call_contract(
        #         call=call
        #     )
        # else:
        #     # assert isinstance(self._client, FullNodeClient)
        #     contract_class = client.get_class_at_sync(
        #         contract_address=public_address
        #     )
        # cairo_version = (
        #     1 if isinstance(contract_class, SierraContractClass) else 0
        # )


        # prepared_call = contract.functions['transfer'].prepare(int(to_address, 16), 10*10**6)
        # if True:
        #     parsed_calls = _parse_calls_v2(ensure_iterable(prepared_call))
        #     wrapped_calldata = _execute_payload_serializer_v2.serialize(
        #         {"calls": parsed_calls}
        #     )
        # else:
        #     call_descriptions, calldata = _merge_calls(ensure_iterable(prepared_call))
        #     wrapped_calldata = _execute_payload_serializer.serialize(
        #         {"call_array": call_descriptions, "calldata": calldata}
        #     )

        # blockchain_transfer = await contract.functions['transfer'].invoke_v3(
        #     calldata=wrapped_calldata,
        #     signature=[],
        #     max_fee=0,
        #     version=1,
        #     nonce=nonce,
        #     sender_address=public_address,
            # to_address, quantized_amount, auto_estimate=True, nonce=nonce
            #

        # contract
        # account.prepare_invoke()
        # print(blockchain_transfer)
        # if blockchain_transfer is None:
        #     print(None)
        # else:
        #     tx_hash = hex(blockchain_transfer.hash)
        #     while len(tx_hash) < 66:
        #         tx_hash = tx_hash[:2] + "0" + tx_hash[2:]
        #     print(tx_hash)

        # transaction = contract.invoke(estimated_fee)
        # estimated_fee = await account.estimate_fee()
        # invoke_result = await prepared_function_call.invoke()

        # print(estimated_fee, transaction)
        # estimated_fee = cls.estimate_gas_fee(contract, nonce, to_address, client, public_address, account)
        # max_fee = int(estimated_fee.overall_fee * Account.ESTIMATED_FEE_MULTIPLIER)

        # blockchain_transfer = contract.functions['transfer'].invoke_sync(int(data['to_address'], 16), quantized_amount, max_fee=max_fee)

        # call = Call(to_addr=data['to_addr'], selector=get_selector_from_name('balanceOf'), calldata=[account.address])
        # account_balance = await account.client.call_contract(call=call)
        # print(account_balance)
        
        # call = Call(to_addr=data['to_addr'], selector=get_selector_from_name("transfer"), calldata=calldata)
        
        # resp = await account.execute_v3(calls=call)
        # blockchain_transfer = contract.functions['transfer'].invoke_sync(int(to_address, 16), quantised_amount, max_fee=max_fee)
        # print(resp)
        return False


# @staticmethod
    # def _l1_wallet_transfer(to_address, quantised_amount, contract, max_fee):
    #     blockchain_transfer = contract.functions['transfer'].invoke_sync(int(to_address, 16), quantised_amount, max_fee=max_fee)
    #     if blockchain_transfer is None:
    #         return None
    #     else:
    #         tx_hash = hex(blockchain_transfer.hash)
    #         while len(tx_hash) < 66:
    #             tx_hash = tx_hash[:2] + "0" + tx_hash[2:]
    #         return tx_hash

        # data=data["ls_data"]
        # calldata=json.loads(data["data"])[0]['calldata']
        # data = {
        #     "to_addr":data['to_address'], 
        #     "calldata":calldata
        #     }

        # print(data)
        # res = await account.execute_v3(json.loads(data['ls_data']["data"]))
        # print(res, res.json())
        return False


# export const executeStarknetTransaction = async (
#   rpcUrl: string,
#   userPublicAddress: string,
#   privateKey: string,
#   data: any,
# ) => {
#   const provider = new Provider({ rpc: { nodeUrl: rpcUrl } })
#   let account = new Account(provider, userPublicAddress, privateKey)
#   const res = await account.execute(JSON.parse(data))
#   return res
# }

# export const getStarknetUserBalance = async (
#   tokenAddress: string,
#   starkNetRpc: string,
#   userAddress: string,
#   decimal: number,
# ) => {
#   const provider = new Provider({ rpc: { nodeUrl: starkNetRpc } })
#   const erc20 = new Contract(starkErc20Abi, tokenAddress, provider)

#   const res = await erc20.balanceOf(userAddress)
#   const balanceInWei = uint256.uint256ToBN(res.balance).toString()

#   const balance = dequantize(balanceInWei, decimal)

#   return balance
# }

