list_deposits_response = {
    "status": "success",
    "message": "",
    "payload": {
        "count": 493,
        "next": "",
        "previous": None,
        "results": [
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Pending",
                "tanx_deposit_status": "Pending",
                "deposit_blockchain_hash": "0x6dacf57358e59018d5202e78ea5fb5a81ccd8741c524ca712e16f14e55b31ec2",
                "amount": "100",
                "created_at": "2023-08-07T04:29:57.732857Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Pending",
                "tanx_deposit_status": "Pending",
                "deposit_blockchain_hash": "0xbf41fa3a08446f5a8041fa7a3c80b3e2437a5f102de6d537e1cd9dc9b9258a87",
                "amount": "100000",
                "created_at": "2023-08-07T04:28:37.996150Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Pending",
                "tanx_deposit_status": "Pending",
                "deposit_blockchain_hash": "0x3e21ef7e8cd5cb3ebab7fe755d732f17ebc6f2ae5c8a9e1cae2b71ffb162a0aa",
                "amount": "100",
                "created_at": "2023-08-07T04:27:12.461843Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Failed",
                "tanx_deposit_status": "Pending",
                "deposit_blockchain_hash": "0xde7bdb6b221f09c066682da04c413eab89f71c08a4f629efee4c1e38eb2fca54",
                "amount": "100",
                "created_at": "2023-08-07T04:26:33.142663Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "Success",
                "deposit_blockchain_hash": "0x0531e0192df925f5d3d9de3333c699a01228ee8e636e5900ea03546ea4f8a35e",
                "amount": "100",
                "created_at": "2023-08-07T04:24:50.528657Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "Success",
                "deposit_blockchain_hash": "0x6789e1aa8db08a697e88381788503ea8e5714a3d59d524a84f619585cb56ace5",
                "amount": "100000",
                "created_at": "2023-08-07T04:16:37.757650Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "Success",
                "deposit_blockchain_hash": "0x24e2dd84b19410a59a00440794f6a70e111ec4fa4a30e3827fdc5e4a000c5461",
                "amount": "100000",
                "created_at": "2023-08-04T16:30:51.278421Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "Success",
                "deposit_blockchain_hash": "0x1b83e88ef5a8f4ad8c2de83ea366474727c7e64b10f6b2d1e1f0a9911170af47",
                "amount": "1000",
                "created_at": "2023-08-04T16:29:01.481086Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "Success",
                "deposit_blockchain_hash": "0xa4f05745ac8653b1a94f52835a94800c72475f348052dd1584c3b71e6c4d12c1",
                "amount": "1000",
                "created_at": "2023-08-04T13:39:42.430514Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "Success",
                "deposit_blockchain_hash": "0x1e654643b696f33d54a05c2c5f17a104be8a0a17da2bcb7dc310459e0e7c3a52",
                "amount": "1000",
                "created_at": "2023-08-04T06:57"
            }
        ]
    }
}

validate_withdrawal_response= {
    "status": "success",
    "message": "successfully initiated withdrawal",
    "payload": {
        "id": 7819,
        "amount": "0.0000100000000000",
        "token_id": "eth",
        "created_at": "2023-08-07T05:12:50.012516Z",
        "transaction_status": "INITIATED",
        "extras": {
            "errors": [],
            "exp_timestamp": 3997985,
            "quantised_amount": 100000
        }
    }
}
bulk_cancel_response ={'status': 'success', 'message': 'Orders are successfully queued for cancellation', 'payload': {}}
list_withdrawals_response= {
    "status": "success",
    "message": "",
    "payload": {
        "count": 315,
        "next": "",
        "previous": None,
        "results": [
            {
                "id": 7817,
                "amount": "20.0000000000000000",
                "token_id": "usdc",
                "created_at": "2023-08-04T12:34:14.863865Z",
                "transaction_status": "CONFIRMING",
                "extras": {
                    "errors": [],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 20000000
                }
            },
            {
                "id": 7816,
                "amount": "20.0000000000000000",
                "token_id": "usdc",
                "created_at": "2023-08-04T11:11:06.828763Z",
                "transaction_status": "CONFIRMING",
                "extras": {
                    "errors": [],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 20000000
                }
            },
            {
                "id": 7815,
                "amount": "20.0000000000000000",
                "token_id": "usdc",
                "created_at": "2023-08-04T11:10:35.030033Z",
                "transaction_status": "FAILED",
                "extras": {
                    "errors": ["NOT_VALIDATED"],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 20000000
                }
            },
            {
                "id": 7814,
                "amount": "20.0000000000000000",
                "token_id": "eth",
                "created_at": "2023-08-04T10:42:12.537837Z",
                "transaction_status": "FAILED",
                "extras": {
                    "errors": ["NOT_VALIDATED"],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 200000000000
                }
            },
            {
                "id": 7813,
                "amount": "0.0000100000000000",
                "token_id": "eth",
                "created_at": "2023-08-04T10:30:30.232291Z",
                "transaction_status": "CONFIRMING",
                "extras": {
                    "errors": [],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 100000
                }
            },
            {
                "id": 7812,
                "amount": "0.0000100000000000",
                "token_id": "eth",
                "created_at": "2023-08-04T10:28:54.938646Z",
                "transaction_status": "CONFIRMING",
                "extras": {
                    "errors": [],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 100000
                }
            },
            {
                "id": 7811,
                "amount": "0.0000100000000000",
                "token_id": "eth",
                "created_at": "2023-08-04T10:27:48.480858Z",
                "transaction_status": "CONFIRMING",
                "extras": {
                    "errors": [],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 100000
                }
            },
            {
                "id": 7810,
                "amount": "0.0000100000000000",
                "token_id": "eth",
                "created_at": "2023-08-04T10:26:03.211778Z",
                "transaction_status": "FAILED",
                "extras": {
                    "errors": ["HASH_MISMATCH"],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 100000
                }
            },
            {
                "id": 7809,
                "amount": "0.0000100000000000",
                "token_id": "eth",
                "created_at": "2023-08-04T10:24:56.251147Z",
                "transaction_status": "FAILED",
                "extras": {
                    "errors": ["HASH_MISMATCH"],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 100000
                }
            },
            {
                "id": 7808,
                "amount": "0.0000100000000000",
                "token_id": "eth",
                "created_at": "2023-08-04T09:42:35.114010Z",
                "transaction_status": "CONFIRMING",
                "extras": {
                    "errors": [],
                    "exp_timestamp": 3997985,
                    "quantised_amount": 100000
                }
            }
        ]
    }
}

start_fast_withdrawal_response = {
   "status":"success",
   "message":"successfully initiated withdrawal",
   "payload":{
      "fastwithdrawal_withdrawal_id":359,
      "msg_hash":"0x7f3e0f70980d079c4d777dc965ebbf0746f9b0845a3759937e6b7868962d8d6"
   }
}
sign_withdrawal_tx_msg_hash_response = {
    'r': '0x3a59acad62929e148f4b9711bd03b6b77e4cadc4bacbc8e91914fa2fdde9081',
    's': '0x4a93cf575b3e3972554b726a7efeeb83a4cecd68962dff3d8497c34313c0d79',
    'recoveryParam': 0
}
process_fast_withdrawal_response = {
   "status":"success",
   "message":"successfully processed withdrawal",
   "payload":{
      "id":361,
      "amount":"10.0000000000000000",
      "fee_amount":"9.470979",
      "token_id":"usdc",
      "network":"ETHEREUM",
      "created_at":"2024-06-13T07:58:47.196361Z",
      "l1_withdrawal_blockchain_hash":"None",
      "transaction_status":"PROCESSING",
      "blockchain_status":"PENDING",
      "extras":{
         "errors":[
            
         ],
         "exp_timestamp":3997985,
         "quantised_amount":19470979
      }
   }
}

coin_stats_response = {
    "status": "success",
    "message": "Retrieval Successful",
    "payload": {
        "ethereum": {
            "name": "Ethereum",
            "symbol": "eth",
            "type": "crypto",
            "fee": "0.0001",
            "quanitization": "10",
            "stark_asset_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
            "token_contract": "",
            "news_name": "ETH",
            "trade_fee": "0.00",
            "chart_name": "ethereum",
            "minimum_order": "0.0002",
            "minimum_withdraw": "0.04",
            "maximum_order": "2",
            "minimum_deposit": "0.01",
            "frontend_visibility": True,
            "starkex_deposits_enabled": True,
            "starkex_deposits_enabled_frontend": True,
            "fast_withdrawals_enabled": True,
            "fast_withdrawal_fee": "0.0001",
            "max_fast_withdrawal_for_platform_per_day": "5",
            "max_fast_withdrawal_for_user_per_day": "2",
            "min_fast_withdrawal": "0.001",
            "decimal": "8",
            "color": "#617EEA",
            "trade_decimal": "4",
            "blockchain_decimal": "18",
            "chart": "BITFINEX:ETHUSD|12M",
            "logo": "https://tanx-mainnet-fe-assets.s3.ap-southeast-1.amazonaws.com/ETHEREUM.png",
            "description": "Ethereum is an open platform that enables developers to build and deploy decentralized applications such as smart contracts and other complex legal and financial applications. "
        },
        "usdc": {
            "name": "USDC",
            "symbol": "usdc",
            "decimal": "6",
            "fee": "1",
            "quanitization": "6",
            "type": "crypto",
            "stark_asset_id": "0x2893294412a4c8f915f75892b395ebbf6859ec246ec365c3b1f56f47c3a0a5d",
            "token_contract": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
            "trade_fee": "0.00",
            "color": "#26A17B",
            "minimum_withdraw": "0",
            "news_name": "USDC",
            "chart_name": "usdc",
            "chart": "KRAKEN:USDCUSD|12M",
            "minimum_order": "1",
            "maximum_order": "250000",
            "trade_decimal": "2",
            "blockchain_decimal": "6",
            "minimum_deposit": "1",
            "frontend_visibility": True,
            "starkex_deposits_enabled": True,
            "starkex_deposits_enabled_frontend": True,
            "fast_withdrawals_enabled": True,
            "fast_withdrawal_fee": "1",
            "max_fast_withdrawal_for_platform_per_day": "20000",
            "max_fast_withdrawal_for_user_per_day": "10000",
            "min_fast_withdrawal": "10",
            "logo": "https://tanx-mainnet-fe-assets.s3.ap-southeast-1.amazonaws.com/USDC.png",
            "description": "USD Coin (known by its ticker USDC) is a stablecoin that is pegged to the U.S. dollar on a 1:1 basis. Every unit of this cryptocurrency in circulation is backed up by $1 that is held in reserve, in a mix of cash and short-term U.S. Treasury bonds. The Centre consortium, which is behind this asset, says USDC is issued by regulated financial institutions."
        },
    }
}

get_vault_id_response = {"status": "success", "message": "", "payload": {"id": 252, "coin": "usdt"}}

list_polygon_deposits_response = {
    "status": "success",
    "message": "",
    "payload": {
        "count": 23,
        "next": "",
        "previous": "",
        "results": [
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0x2a868c8884b6b5f0f3b44c2ec6f4278b56652d33ad98bbb51cd45656e8bfc65e",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-16T06:53:31.761603Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0x54c3505c612797ce01d11b73e7bb1238f4be292be6771cf2ea38cfb48353052c",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-16T06:53:20.098033Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0x0edc159590c62769631ab92bae0fd1a20754444f471704fa40106226bc430a7e",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-16T06:37:40.229312Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0x561122a3fefa8aa2e9cacd60874e3ee5cea58bbf562dc23f95c3f3f05727bdee",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-16T06:29:18.100068Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0x539ba8330580add2723c76af88386f1d31e3b93315839b4eae7a174c5e59c2ed",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-16T06:28:21.778246Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0xe032d2c9115b83d77d981cb77fac88207631bcf23cee0574b1ffbbe40685cada",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-16T06:01:51.446800Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0xbb08968f78b81143066e13b995a588587dfafee9b1040f942858fd3e37080f4a",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-11T10:24:54.095723Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0xe72d32666acf7aa3f1ade0bea4440ada3457a99b5d617f20e075ea06c49d6263",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-11T10:21:43.632555Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0xf9a8ab38af7ccc694078b7622761e392964c1f32e76c44d723451cf27b90fcf7",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-11T10:19:43.389197Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0x42e414638908dc566ee5fee6f3a5c8413da9ee5276ab33cfbd1fb4659a63ffab",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-11T10:18:43.681993Z"
            }
        ]
    }
}

network_config_response = {
    'payload': {
      "network_config":{
        "ETHEREUM": {
            "deposit_contract": "0xe17F8e501bF5e968e39D8702B30c3A8b955d8f52",
            "tokens": {
                "eth": {
                    "blockchain_decimal": "18",
                    "token_contract": "0x0000000000000000000000000000000000001010"
                },
                "usdc": {
                    "blockchain_decimal": "6",
                    "token_contract": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                    "max_fast_withdrawal_for_platform_per_day": "15000",
                    "max_fast_withdrawal_for_user_per_day": "12000"
                }
            },
            "allowed_tokens_for_deposit": [
                "usdc",
                "eth"
            ],
            "allowed_tokens_for_deposit_frontend": [],
            "allowed_tokens_for_fast_wd": [
                "usdc",
                "eth"
            ],
            "allowed_tokens_for_fast_wd_frontend": [
                "usdc"
            ]
        },
         "POLYGON":{
            "deposit_contract":"0x2714C5958e2b1417B3f2b7609202FFAD359a5965",
            "tokens":{
               "usdc":{
                  "blockchain_decimal":"6",
                  "token_contract":"0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
                  "max_fast_withdrawal_for_platform_per_day":"15000",
                  "max_fast_withdrawal_for_user_per_day":"12000"
               },
               "matic":{
                  "blockchain_decimal":"18",
                  "token_contract":"0x0000000000000000000000000000000000001010",
                  "max_fast_withdrawal_for_platform_per_day":"15000",
                  "max_fast_withdrawal_for_user_per_day":"12000"
               },
               "usdt":{
                  "blockchain_decimal":"6",
                  "token_contract":"0xc2132D05D31c914a87C6611C10748AEb04B58e8F",
                  "max_fast_withdrawal_for_platform_per_day":"10000",
                  "max_fast_withdrawal_for_user_per_day":"8000"
               }
            },
            "allowed_tokens_for_deposit":[
               "usdc",
               "matic",
               "usdt"
            ],
            "allowed_tokens_for_deposit_frontend":[
               "usdc",
               "matic",
               "usdt"
            ],
            "allowed_tokens_for_fast_wd":[
               "usdc",
               "matic",
               "usdt"
            ],
            "allowed_tokens_for_fast_wd_frontend":[
               "usdc",
               "matic",
               "usdt"
            ]
         },
         "STARKNET":{
            "tokens":{
               "usdc":{
                  "blockchain_decimal":"6",
                  "token_contract":"0x053C91253BC9682c04929cA02ED00b3E423f6710D2ee7e0D5EBB06F3eCF368A8"
               }
            },
            "allowed_tokens_for_deposit":[
               "usdc"
            ],
            "allowed_tokens_for_deposit_frontend":[
               "usdc"
            ],
            "allowed_tokens_for_fast_wd":[
               "usdc"
            ],
            "allowed_tokens_for_fast_wd_frontend":[
               "usdc"
            ]
         },
         "SCROLL":{
            "deposit_contract":"0x1e4a1a0d31cFDDC722965a0c2d3bBecF748252d6",
            "tokens":{
               "usdc":{
                  "blockchain_decimal":"6",
                  "token_contract":"0x06eFdBFf2a14a7c8E15944D1F4A48F9F95F663A4",
                  "max_fast_withdrawal_for_platform_per_day":"8000",
                  "max_fast_withdrawal_for_user_per_day":"7000"
               },
               "eth":{
                  "blockchain_decimal":"18",
                  "token_contract":"0x0000000000000000000000000000000000001010"
               },
               "usdt":{
                  "blockchain_decimal":"6",
                  "token_contract":"0xf55BEC9cafDbE8730f096Aa55dad6D22d44099Df",
                  "max_fast_withdrawal_for_platform_per_day":"8000",
                  "max_fast_withdrawal_for_user_per_day":"7000"
               }
            },
            "allowed_tokens_for_deposit":[
               "usdc",
               "usdt"
            ],
            "allowed_tokens_for_deposit_frontend":[
               "usdc",
               "usdt"
            ],
            "allowed_tokens_for_fast_wd":[
               "usdc",
               "usdt"
            ],
            "allowed_tokens_for_fast_wd_frontend":[
               "usdc",
               "usdt"
            ]
         },
         "OPTIMISM":{
            "deposit_contract":"0xBdd40916bBC43bE14dd7183C30a64EE4A893D97f",
            "tokens":{
               "usdc":{
                  "blockchain_decimal":"6",
                  "token_contract":"0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85",
                  "max_fast_withdrawal_for_platform_per_day":"15000",
                  "max_fast_withdrawal_for_user_per_day":"12000"
               },
               "eth":{
                  "blockchain_decimal":"18",
                  "token_contract":"0x0000000000000000000000000000000000001010"
               },
               "usdt":{
                  "blockchain_decimal":"6",
                  "token_contract":"0x94b008aA00579c1307B0EF2c499aD98a8ce58e58"
               }
            },
            "allowed_tokens_for_deposit":[
               "usdc",
               "usdt"
            ],
            "allowed_tokens_for_deposit_frontend":[
               "usdc",
               "usdt"
            ],
            "allowed_tokens_for_fast_wd":[
               "usdc",
               "usdt"
            ],
            "allowed_tokens_for_fast_wd_frontend":[
               "usdc",
               "usdt"
            ]
         },
         "ARBITRUM":{
            "deposit_contract":"0x149e2C169f10914830EF39B9d184AE62BbCdF526",
            "tokens":{
               "usdc":{
                  "blockchain_decimal":"6",
                  "token_contract":"0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
                  "max_fast_withdrawal_for_platform_per_day":"15000",
                  "max_fast_withdrawal_for_user_per_day":"12000"
               },
               "eth":{
                  "blockchain_decimal":"18",
                  "token_contract":"0x0000000000000000000000000000000000001010"
               },
               "usdt":{
                  "blockchain_decimal":"6",
                  "token_contract":"0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9"
               }
            },
            "allowed_tokens_for_deposit":[
               "usdc",
               "usdt"
            ],
            "allowed_tokens_for_deposit_frontend":[
               "usdc",
               "usdt"
            ],
            "allowed_tokens_for_fast_wd":[
               "usdc",
               "usdt"
            ],
            "allowed_tokens_for_fast_wd_frontend":[
               "usdc",
               "usdt"
            ]
         },
         "LINEA":{
            "deposit_contract":"0x508f001baa00976fc1d679af880267555900ab09",
            "tokens":{
               "usdc":{
                  "blockchain_decimal":"6",
                  "token_contract":"0x176211869cA2b568f2A7D4EE941E073a821EE1ff"
               },
               "usdt":{
                  "blockchain_decimal":"6",
                  "token_contract":"0xA219439258ca9da29E9Cc4cE5596924745e12B93"
               },
               "eth":{
                  "blockchain_decimal":"18",
                  "token_contract":"0x0000000000000000000000000000000000001010",
                  "max_fast_withdrawal_for_platform_per_day":"1",
                  "max_fast_withdrawal_for_user_per_day":"0.8"
               }
            },
            "allowed_tokens_for_deposit":[
               "usdc",
               "usdt",
               "eth"
            ],
            "allowed_tokens_for_deposit_frontend":[
               "usdc",
               "usdt",
               "eth"
            ],
            "allowed_tokens_for_fast_wd":[
               "usdc",
               "usdt",
               "eth"
            ],
            "allowed_tokens_for_fast_wd_frontend":[
               "usdc",
               "usdt",
               "eth"
            ]
         },
         "MODE":{
            "deposit_contract":"0xB884389d818046F48Ca63d4cCAF303ba65f6DbC1",
            "tokens":{
               "usdc":{
                  "blockchain_decimal":"6",
                  "token_contract":"0xd988097fb8612cc24eeC14542bC03424c656005f",
                  "max_fast_withdrawal_for_platform_per_day":"30000",
                  "max_fast_withdrawal_for_user_per_day":"25000"
               },
               "eth":{
                  "blockchain_decimal":"18",
                  "token_contract":"0x0000000000000000000000000000000000001010",
                  "max_fast_withdrawal_for_platform_per_day":"8",
                  "max_fast_withdrawal_for_user_per_day":"7"
               },
               "usdt":{
                  "blockchain_decimal":"6",
                  "token_contract":"0xf0F161fDA2712DB8b566946122a5af183995e2eD",
                  "max_fast_withdrawal_for_platform_per_day":"30000",
                  "max_fast_withdrawal_for_user_per_day":"25000"
               }
            },
            "allowed_tokens_for_deposit":[
               "usdc",
               "usdt",
               "eth"
            ],
            "allowed_tokens_for_deposit_frontend":[
               "usdc",
               "usdt",
               "eth"
            ],
            "allowed_tokens_for_fast_wd":[
               "usdc",
               "usdt",
               "eth"
            ],
            "allowed_tokens_for_fast_wd_frontend":[
               "usdc",
               "usdt",
               "eth"
            ]
         },
         "ZKPOLY":{
            "deposit_contract":"0xD5FA54014c364a17F120A47117e5312ee858a13C",
            "tokens":{
               "usdc":{
                  "blockchain_decimal":"6",
                  "token_contract":"0x37eAA0eF3549a5Bb7D431be78a3D99BD360d19e5"
               },
               "eth":{
                  "blockchain_decimal":"18",
                  "token_contract":"0x0000000000000000000000000000000000001010"
               }
            },
            "allowed_tokens_for_deposit":[
               "usdc"
            ],
            "allowed_tokens_for_deposit_frontend":[
               
            ],
            "allowed_tokens_for_fast_wd":[
               "usdc"
            ],
            "allowed_tokens_for_fast_wd_frontend":[
               
            ]
         }
      }
    }
}

list_internal_transfer_response = {
    'status': 'success',
    'message': 'Fetched internal transfers successfully',
    'payload': {
        'internal_transfers': [
            {
                'client_reference_id': '3845010178310545',
                'amount': '1.0000000000000000',
                'currency': 'usdc',
                'from_address': '0x6c875514E42F14B891399A6a8438E6AA8F77B178',
                'destination_address': '0xF5F467c3D86760A4Ff6262880727E854428a4996',
                'status': 'success',
                'created_at': '2023-07-26T05:11:47.285117Z',
                'updated_at': '2023-07-26T05:11:47.698994Z',
            },
            {
                'client_reference_id': '4645497856683096',
                'amount': '1.0000000000000000',
                'currency': 'usdc',
                'from_address': '0x6c875514E42F14B891399A6a8438E6AA8F77B178',
                'destination_address': '0xF5F467c3D86760A4Ff6262880727E854428a4996',
                'status': 'success',
                'created_at': '2023-07-26T05:11:13.502647Z',
                'updated_at': '2023-07-26T05:11:14.047787Z',
            },
        ],
        'total_count': 26,
        'limit': 2,
        'offset': 0,
    }
}

get_internal_transfer_by_client_id_response = {
    'status': 'success',
    'message': 'Fetched internal transfer successfully',
    'payload': {
        'client_reference_id': '1234',
        'amount': '1.0000000000000000',
        'currency': 'usdc',
        'from_address': '0x6c875514E42F14B891399A6a8438E6AA8F77B178',
        'destination_address': '0xF5F467c3D86760A4Ff6262880727E854428a4996',
        'status': 'success',
        'created_at': '2023-07-26T05:16:31.557629Z',
        'updated_at': '2023-07-26T05:16:32.047285Z',
    }
}

list_polygon_deposits_response = {
    "status": "success",
    "message": "",
    "payload": {
        "count": 23,
        "next": "",
        "previous": "",
        "results": [
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0x2a868c8884b6b5f0f3b44c2ec6f4278b56652d33ad98bbb51cd45656e8bfc65e",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-16T06:53:31.761603Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0x54c3505c612797ce01d11b73e7bb1238f4be292be6771cf2ea38cfb48353052c",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-16T06:53:20.098033Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0x0edc159590c62769631ab92bae0fd1a20754444f471704fa40106226bc430a7e",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-16T06:37:40.229312Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0x561122a3fefa8aa2e9cacd60874e3ee5cea58bbf562dc23f95c3f3f05727bdee",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-16T06:29:18.100068Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0x539ba8330580add2723c76af88386f1d31e3b93315839b4eae7a174c5e59c2ed",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-16T06:28:21.778246Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0xe032d2c9115b83d77d981cb77fac88207631bcf23cee0574b1ffbbe40685cada",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-16T06:01:51.446800Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0xbb08968f78b81143066e13b995a588587dfafee9b1040f942858fd3e37080f4a",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-11T10:24:54.095723Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0xe72d32666acf7aa3f1ade0bea4440ada3457a99b5d617f20e075ea06c49d6263",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-11T10:21:43.632555Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0xf9a8ab38af7ccc694078b7622761e392964c1f32e76c44d723451cf27b90fcf7",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-11T10:19:43.389197Z"
            },
            {
                "token_id": "0x36823b9f4fa9bdbae9eecdef9f69432df22ad79e2f8fcf2d826a0f4ae15dd77",
                "blockchain_deposit_status": "Success",
                "tanx_deposit_status": "SUCCESS",
                "deposit_blockchain_hash": "0x42e414638908dc566ee5fee6f3a5c8413da9ee5276ab33cfbd1fb4659a63ffab",
                "network": "POLYGON",
                "amount": "100",
                "created_at": "2023-08-11T10:18:43.681993Z"
            }
        ]
    }
}
