import decimal
import hashlib

from web3 import Web3

from brineconnector.bin.python_signature import (
    private_key_to_ec_point_on_stark_curve,
)
from brineconnector.bin.python_signature import (
    private_to_stark_key
)


def message_to_hash(message_string):
    """Generate a hash deterministically from an arbitrary string."""
    message = hashlib.sha256()
    message.update(message_string.encode())  # Encode as UTF-8.
    return int(message.digest().hex(), 16) >> 5


def private_key_from_bytes(data):
    """Generate a STARK key deterministically from binary data."""
    if not isinstance(data, bytes):
        raise ValueError('Input must be a byte-string')
    return hex(int(Web3.keccak(data).hex(), 16) >> 5)


def private_key_to_public_hex(private_key_hex):
    """Given private key as hex string, return the public key as hex string."""
    private_key_int = int(private_key_hex, 16)
    return hex(private_to_stark_key(private_key_int))


def private_key_to_public_key_pair_hex(private_key_hex):
    """Given private key as hex string, return the public x, y pair as hex."""
    private_key_int = int(private_key_hex, 16)
    x, y = private_key_to_ec_point_on_stark_curve(private_key_int)
    return [hex(x), hex(y)]
