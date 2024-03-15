from .bin.signature import sign, get_stark_key_pair_from_signature
from .bin.blockchain_utils import sign_msg
from .typings import CreateOrderNoncePayload, CreateNewOrderBody, CoinStatPayload, StarkSignature
from .exception import CoinNotFoundError
from .constants import Config, MAX_INT_ALLOWANCE
from typing import Literal
from web3 import Web3, Account
import os

def params_to_dict(dict: dict) -> dict:
    del dict['self']
    d = {}
    for key, val in dict.items():
        if (val):
            d[key] = val
    return d


def sign_order_with_stark_private_key(stark_private_key: str, nonce: CreateOrderNoncePayload,):
    r, s = sign(msg_hash=int(nonce['msg_hash'], 16),
                stark_private_key=stark_private_key)

    create_order_request_data: CreateNewOrderBody = {
        "nonce": nonce['nonce'],
        "msg_hash": nonce['msg_hash'],
        "signature": {
            "r": hex(r),
            "s": hex(s)
        }
    }
    return create_order_request_data

def filter_ethereum_coin(coin_stats_payload: CoinStatPayload, coin: str):
    for coin_name, coin_stat in coin_stats_payload.items():
        if coin_stat["symbol"] == coin:
            return coin_stat
    raise CoinNotFoundError(f"Coin '{coin}' not found")

def get_nonce(signer, provider: Web3):
    base_nonce = provider.eth.get_transaction_count(signer.address)
    nonce_offset = 0
    return base_nonce + nonce_offset

def get_0x0_to_0x(address: str):
    if address and (address[:3] == '0x0' or address[:3] == '0X0'):
        return '0x' + address[4:]
    else:
        return address

def dequantize(number: float, decimals: int):
    factor = 10**decimals
    return number/factor

def get_allowance(user_address: str, stark_contract: str, token_contract: str, decimal: str, w3: Web3):
    contract_instance = w3.eth.contract(address=token_contract, abi=Config.ERC20_ABI) # type:ignore
    allowance = contract_instance.functions.allowance(user_address, stark_contract).call()
    allowance_decimal = dequantize(int(allowance), int(decimal))
    return allowance_decimal

def approve_unlimited_allowance_util(contract_address: str, token_contract: str, signer: Account, w3: Web3):
    gas_price = w3.eth.gas_price
    contract_instance = w3.eth.contract(address=token_contract, abi=Config.ERC20_ABI) # type:ignore

    gas_limit = contract_instance.functions.approve(
        contract_address,
        Web3.to_int(int('100'))
    ).estimate_gas({"from": token_contract})
    # so basically, if token contract is not provided, it'll try to approve from 0 address account,
    # so providing a from account, other way is to initialize web3 using private key
    overrides = {
        'gas': gas_limit,
        'gasPrice': gas_price,
        'nonce': get_nonce(signer=signer, provider=w3),
    }
    amount = int(MAX_INT_ALLOWANCE)
    transaction_pre_build = contract_instance.functions.approve(contract_address, amount)
    transaction = transaction_pre_build.build_transaction(overrides) # type: ignore
    signed_tx = signer.sign_transaction(transaction)
    # send this signed transaction to blockchain
    w3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()
    approval = signed_tx
    return approval

def sign_internal_tx_msg_hash(key_pair: dict, msg_hash: str):
    r, s = sign(int(msg_hash, 16), key_pair['stark_private_key'])
    signature: StarkSignature = {
        'r': hex(r),
        's': hex(s),
    } # type:ignore
    return signature
