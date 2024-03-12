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
                "brine_deposit_status": "Pending",
                "deposit_blockchain_hash": "0x6dacf57358e59018d5202e78ea5fb5a81ccd8741c524ca712e16f14e55b31ec2",
                "amount": "100",
                "created_at": "2023-08-07T04:29:57.732857Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Pending",
                "brine_deposit_status": "Pending",
                "deposit_blockchain_hash": "0xbf41fa3a08446f5a8041fa7a3c80b3e2437a5f102de6d537e1cd9dc9b9258a87",
                "amount": "100000",
                "created_at": "2023-08-07T04:28:37.996150Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Pending",
                "brine_deposit_status": "Pending",
                "deposit_blockchain_hash": "0x3e21ef7e8cd5cb3ebab7fe755d732f17ebc6f2ae5c8a9e1cae2b71ffb162a0aa",
                "amount": "100",
                "created_at": "2023-08-07T04:27:12.461843Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Failed",
                "brine_deposit_status": "Pending",
                "deposit_blockchain_hash": "0xde7bdb6b221f09c066682da04c413eab89f71c08a4f629efee4c1e38eb2fca54",
                "amount": "100",
                "created_at": "2023-08-07T04:26:33.142663Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "brine_deposit_status": "Success",
                "deposit_blockchain_hash": "0x0531e0192df925f5d3d9de3333c699a01228ee8e636e5900ea03546ea4f8a35e",
                "amount": "100",
                "created_at": "2023-08-07T04:24:50.528657Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "brine_deposit_status": "Success",
                "deposit_blockchain_hash": "0x6789e1aa8db08a697e88381788503ea8e5714a3d59d524a84f619585cb56ace5",
                "amount": "100000",
                "created_at": "2023-08-07T04:16:37.757650Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "brine_deposit_status": "Success",
                "deposit_blockchain_hash": "0x24e2dd84b19410a59a00440794f6a70e111ec4fa4a30e3827fdc5e4a000c5461",
                "amount": "100000",
                "created_at": "2023-08-04T16:30:51.278421Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "brine_deposit_status": "Success",
                "deposit_blockchain_hash": "0x1b83e88ef5a8f4ad8c2de83ea366474727c7e64b10f6b2d1e1f0a9911170af47",
                "amount": "1000",
                "created_at": "2023-08-04T16:29:01.481086Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "brine_deposit_status": "Success",
                "deposit_blockchain_hash": "0xa4f05745ac8653b1a94f52835a94800c72475f348052dd1584c3b71e6c4d12c1",
                "amount": "1000",
                "created_at": "2023-08-04T13:39:42.430514Z"
            },
            {
                "token_id": "0x2705737cd248ac819034b5de474c8f0368224f72a0fda9e031499d519992d9e",
                "blockchain_deposit_status": "Success",
                "brine_deposit_status": "Success",
                "deposit_blockchain_hash": "0x1e654643b696f33d54a05c2c5f17a104be8a0a17da2bcb7dc310459e0e7c3a52",
                "amount": "1000",
                "created_at": "2023-08-04T06:57"
            }
        ]
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
            "logo": "https://brine-mainnet-fe-assets.s3.ap-southeast-1.amazonaws.com/ETHEREUM.png",
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
            "logo": "https://brine-mainnet-fe-assets.s3.ap-southeast-1.amazonaws.com/USDC.png",
            "description": "USD Coin (known by its ticker USDC) is a stablecoin that is pegged to the U.S. dollar on a 1:1 basis. Every unit of this cryptocurrency in circulation is backed up by $1 that is held in reserve, in a mix of cash and short-term U.S. Treasury bonds. The Centre consortium, which is behind this asset, says USDC is issued by regulated financial institutions."
        },
    }
}

get_vault_id_response = {"status": "success", "message": "", "payload": {"id": 252, "coin": "eth"}}