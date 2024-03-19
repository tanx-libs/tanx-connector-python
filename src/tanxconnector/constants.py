import json
import os

path_ = os.path.dirname(__file__)

with open(f'{path_}/bin/starkex_abi_main.json') as f:
    starkex_abi_main = json.load(f)

with open(f'{path_}/bin/starkex_abi_test.json') as f:
    starkex_abi_test = json.load(f)

with open(f'{path_}/bin/erc20_abi.json') as f:
    erc20Abi = json.load(f)

with open(f'{path_}/bin/polygon_deposit.json') as f:
    polygon_deposit_abi = json.load(f)


class Config:
    ALLOWED_NETWORK_NAME_MAINNET = "mainnet"
    ALLOWED_NETWORK_NAME_SEPOLIA = "sepolia"
    STARK_CONTRACT = {
        "mainnet": "0x1390f521A79BaBE99b69B37154D63D431da27A07",
        "testnet": "0xA2eC709125Ea693f5522aEfBBC3cb22fb9146B52",
        # "testnet": "0x87eB0b1B5958c7fD034966925Ea026ad8Bf3d6dD", # old adress used at the time of goerli
    }
    STARK_ABI = {
        "mainnet": starkex_abi_main,
        "testnet": starkex_abi_test,
    }
    POLYGON_ABI = polygon_deposit_abi
    ERC20_ABI = erc20Abi

MAX_INT_ALLOWANCE = '115792089237316195423570985008687907853269984665640564039457584007913129639935'
