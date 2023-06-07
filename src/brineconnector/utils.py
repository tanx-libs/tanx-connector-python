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
