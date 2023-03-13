from web3.auto import w3
from eth_account.messages import encode_defunct
from eth_account.datastructures import SignedMessage
from web3 import Web3


def sign_msg(msg: str, private_key: str) -> str:
    message = encode_defunct(text=msg)
    signed_message: SignedMessage = w3.eth.account.sign_message(
        message, private_key=private_key)
    return signed_message.signature.hex()

