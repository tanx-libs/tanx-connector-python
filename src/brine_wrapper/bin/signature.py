import math
import json
import os
from typing import Optional, Tuple
import hashlib
from . import blockchain_utils
from .math_utils import div_mod, ec_mult, ECPoint, ec_add
from ecdsa.rfc6979 import generate_k


PEDERSEN_HASH_POINT_FILENAME = os.path.join(
    os.path.dirname(__file__), 'pedersen_params.json')
PEDERSEN_PARAMS = json.load(open(PEDERSEN_HASH_POINT_FILENAME))
FIELD_PRIME = PEDERSEN_PARAMS['FIELD_PRIME']
N_ELEMENT_BITS_ECDSA = math.floor(math.log(FIELD_PRIME, 2))
EC_ORDER = PEDERSEN_PARAMS['EC_ORDER']
CONSTANT_POINTS = PEDERSEN_PARAMS['CONSTANT_POINTS']
EC_GEN = CONSTANT_POINTS[1]
ALPHA = PEDERSEN_PARAMS['ALPHA']

# A type for the digital signature.
ECSignature = Tuple[int, int]


def generate_k_rfc6979(msg_hash: int, stark_private_key: str, seed: Optional[int] = None) -> int:
    stark_private_key_int = int(stark_private_key, 16)
    # Pad the message hash, for consistency with the elliptic.js library.
    if 1 <= msg_hash.bit_length() % 8 <= 4 and msg_hash.bit_length() >= 248:
        # Only if we are one-nibble short:
        msg_hash *= 16

    if seed is None:
        extra_entropy = b''
    else:
        extra_entropy = seed.to_bytes(math.ceil(seed.bit_length() / 8), 'big')

    return generate_k(EC_ORDER, stark_private_key_int, hashlib.sha256,
                      msg_hash.to_bytes(math.ceil(msg_hash.bit_length() / 8), 'big'),
                      extra_entropy=extra_entropy)


def inv_mod_curve_size(x: int) -> int:
    return div_mod(1, x, EC_ORDER)


def sign(msg_hash: int, stark_private_key: str, seed: Optional[int] = None) -> ECSignature:
    stark_private_key_int = int(stark_private_key, 16)
    # Note: msg_hash must be smaller than 2**N_ELEMENT_BITS_ECDSA.
    # Message whose hash is >= 2**N_ELEMENT_BITS_ECDSA cannot be signed.
    # This happens with a very small probability.
    assert 0 <= msg_hash < 2**N_ELEMENT_BITS_ECDSA, 'Message not signable.'

    # Choose a valid k. In our version of ECDSA not every k value is valid,
    # and there is a negligible probability a drawn k cannot be used for signing.
    # This is why we have this loop.
    while True:
        k = generate_k_rfc6979(msg_hash, stark_private_key, seed)
        # Update seed for next iteration in case the value of k is bad.
        if seed is None:
            seed = 1
        else:
            seed += 1

        # Cannot fail because 0 < k < EC_ORDER and EC_ORDER is prime.
        x = ec_mult(k, EC_GEN, ALPHA, FIELD_PRIME)[0]

        # DIFF: in classic ECDSA, we take int(x) % n.
        r = int(x)
        if not (1 <= r < 2**N_ELEMENT_BITS_ECDSA):
            # Bad value. This fails with negligible probability.
            continue

        if (msg_hash + r * stark_private_key_int) % EC_ORDER == 0:
            # Bad value. This fails with negligible probability.
            continue

        w = div_mod(k, msg_hash + r * stark_private_key_int, EC_ORDER)
        if not (1 <= w < 2**N_ELEMENT_BITS_ECDSA):
            # Bad value. This fails with negligible probability.
            continue

        s = inv_mod_curve_size(w)
        return r, s


def stark_private_key_to_ec_point_on_stark_curve(stark_private_key: str) -> ECPoint:
    stark_private_key_int = int(stark_private_key, 16)
    assert 0 < stark_private_key_int < EC_ORDER
    return ec_mult(stark_private_key_int, EC_GEN, ALPHA, FIELD_PRIME)


def stark_private_key_to_stark_public_key(stark_private_key: str) -> str:
    return hex(stark_private_key_to_ec_point_on_stark_curve(stark_private_key)[0])


def get_stark_key_pair_from_signature(
        signature: str
) -> "dict[str, str]":
    '''
    Derive a STARK key pair deterministically from an Ethereum key.
    This is the function used by the Brine frontend to derive a user's
    STARK key pair in a way that is recoverable. Programmatic traders may
    optionally derive their STARK key pair in the same way.
    :param signature: mandatory
    :type signature: str
    '''
    signature_int = int(signature, 16)
    hashed_signature = blockchain_utils.get_key_seed(signature=signature_int)
    # grind key
    grinded_key = grind_key(key_seed=int(hashed_signature.hex(), 16), key_value_limit=EC_ORDER)
    stark_private_key = hex(grinded_key)
    stark_public_key = stark_private_key_to_stark_public_key(
        stark_private_key=stark_private_key
    )
    return {
        'stark_private_key': stark_private_key,
        'stark_public_key': stark_public_key
        # 'stark_public_key_y_coordinate': public_y,
    }


def grind_key(key_seed: int, key_value_limit: int) -> int:
    max_allowed_value = 2**256 - (2**256 % key_value_limit)
    current_index = 0

    def indexed_sha256(seed: int, index: int) -> int:
        def padded_hex(x: int) -> str:
            # Hex string should have an even number of characters to convert to bytes.
            hex_str = hex(x)[2:]
            return hex_str if len(hex_str) % 2 == 0 else "0" + hex_str

        digest = hashlib.sha256(bytes.fromhex(padded_hex(seed) + padded_hex(index))).hexdigest()
        return int(digest, 16)

    key = indexed_sha256(seed=key_seed, index=current_index)
    while key >= max_allowed_value:
        current_index += 1
        key = indexed_sha256(seed=key_seed, index=current_index)

    return key % key_value_limit
