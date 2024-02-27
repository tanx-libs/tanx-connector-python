from .bin.signature import sign, get_stark_key_pair_from_signature
from .bin.blockchain_utils import sign_msg
from .typings import CreateOrderNoncePayload, CreateNewOrderBody
from typing import Literal


def params_to_dict(dict: dict) -> dict:
    del dict['self']
    d = {}
    for key, val in dict.items():
        if (val):
            d[key] = val
    return d


def sign_msg_hash(nonce: CreateOrderNoncePayload, private_key: str, option: Literal['mainnet', 'testnet'] = 'mainnet') -> CreateNewOrderBody:
    signature = create_user_signature(private_key, option)
    stark_creds = get_stark_key_pair_from_signature(
        signature=signature)
    stark_private_key = stark_creds["stark_private_key"]
    return sign_order_with_stark_private_key(stark_private_key, nonce)


def create_user_signature(private_key: str, option: Literal['mainnet', 'testnet'] = 'mainnet') -> str:
    msg_to_be_signed = "Click sign to verify you're a human - Brine.finance" if option == 'testnet' else 'Get started with Brine. Make sure the origin is https://trade.brine.fi'
    user_signature = sign_msg(msg_to_be_signed, private_key)
    return user_signature


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

def get_nonce(signer, provider):
    base_nonce = provider.eth.get_transaction_count(signer.address)
    nonce_offset = 1
    return base_nonce + nonce_offset

def get_0x0_to_0x(address):
    if address and (address[:3] == '0x0' or address[:3] == '0X0'):
        return '0x' + address[4:]
    else:
        return address

def dequantize(number, decimals):
    factor = 10**decimals
    return number/factor

def get_allowance(user_address, stark_contract, token_contract, decimal, w3):
    contract_instance = w3.eth.contract(address=token_contract, abi=Config.ERC20_ABI) # type:ignore
    allowance = contract_instance.functions.allowance(user_address, stark_contract).call()
    allowance_decimal = dequantize(int(allowance), int(decimal))
    return allowance_decimal

def approve_unlimited_allowance_util(contract_address, token_contract, signer, w3):
    gas_price = w3.eth.gas_price
    contract_instance = w3.eth.contract(address=token_contract, abi=Config.ERC20_ABI)

    gas_limit = contract_instance.functions.approve(
        contract_address,
        Web3.toInt(int('100'))
    ).estimateGas({"from": token_contract})
    # so basically, if token contract is not provided, it'll try to approve from 0 address account,
    # so providing a from account, other way is to initialize web3 using private key
    overrides = {
        'gas': gas_limit,
        'gasPrice': gas_price,
        'nonce': get_nonce(signer=signer, provider=w3),
    }
    amount = int(MAX_INT_ALLOWANCE)
    transaction_pre_build = contract_instance.functions.approve(contract_address, amount)
    transaction = transaction_pre_build.buildTransaction(overrides) # type: ignore
    signed_tx = signer.sign_transaction(transaction)
    # send this signed transaction to blockchain
    w3.eth.sendRawTransaction(signed_tx.rawTransaction).hex()
    approval = signed_tx
    return approval

def filter_cross_chain_coin(config, coin, type):
    allowed_tokens = config['tokens']
    allowed_tokens_for_deposit = config['allowed_tokens_for_deposit']
    allowed_tokens_for_fast_withdrawl = config['allowed_tokens_for_fast_wd']

    if type == 'TOKENS':
        allowed_token = allowed_tokens[coin]
    elif type == 'DEPOSIT':
        allowed_token = next((token for token in allowed_tokens_for_deposit if token == coin), None)
    elif type == 'WITHDRAWL':
        allowed_token = next((token for token in allowed_tokens_for_fast_withdrawl if token == coin), None)
    else:
        raise CoinNotFoundError('Type not found')
    if not allowed_token:
        raise CoinNotFoundError(f'Coin {coin} not found')

    current_coin = allowed_tokens[coin]
    return current_coin

