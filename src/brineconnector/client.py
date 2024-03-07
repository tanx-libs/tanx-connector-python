from .session import Session
from .utils import *
from .bin.blockchain_utils import sign_msg
from .exception import *
from typing import Optional, Union, List, Literal
from .typings import (
    Response,
    LoginResponse,
    FullDayPricePayload,
    CandleStickPayload,
    OrderBookPayload,
    RecentTradesPayload,
    ProfileInformationPayload,
    Balance,
    ProfitAndLossPayload,
    CreateOrderNoncePayload,
    CreateNewOrderBody,
    OrderPayload,
    CreateOrderNonceBody,
    CancelOrder,
    TradePayload,
    Order,
    TokenType,
    ListDepositParams,
    ListWithdrawalParams,
)
from web3 import Web3, Account
from .constants import Config

class Client:
    def __init__(self, option: Literal['mainnet', 'testnet'] = 'mainnet'):
        base_url = "https://api-testnet.tanx.fi" if option == 'testnet' else 'https://api.tanx.fi'
        self.session = Session(self.refresh_tokens, base_url)
        self.access_token: Optional[str] = None
        self.refresh_token: Optional[str] = None
        self.option = option

    def refresh_tokens(self, refresh_token: Optional[str] = None) -> Union[Response[TokenType], None]:
        if refresh_token or self.refresh_token:
            r = self.session.post('/sapi/v1/auth/token/refresh/', {
                "refresh": refresh_token if refresh_token else self.refresh_token
            })
            self.set_access_token(r.json()['payload']['access'])
            self.set_refresh_token(r.json()['payload']['refresh'])
            return r.json()

    def set_access_token(self, token: str) -> None:
        self.access_token = token
        self.session.headers.update(
            {'Authorization': f"JWT {token}"})
        
    def set_refresh_token(self, token: str) -> None:
        self.refresh_token = token

    def logout(self) -> None:
        self.access_token = None
        self.refresh_token = None
        if self.session.headers.get('Authorization'):
            del self.session.headers['Authorization']

    def test_connection(self) -> Response[str]:
        r = self.session.get('/sapi/v1/health/')
        return r.json()

    def get_24h_price(self, market: str) -> Response[FullDayPricePayload]:
        r = self.session.get('/sapi/v1/market/tickers/',
                             params={market: market})
        return r.json()

    def get_candlestick(self, market: str, limit: Optional[int] = None,
                        period: Optional[int] = None, start_time: Optional[int] = None,
                        end_time: Optional[int] = None) -> Response[CandleStickPayload]:
        loc = locals()
        params = params_to_dict(loc)
        r = self.session.get('/sapi/v1/market/kline/',
                             params=params)
        return r.json()

    def get_orderbook(self, market: str, asks_limit: Optional[int] = None,
                      bids_limit: Optional[int] = None) -> Response[OrderBookPayload]:

        loc = locals()
        params = params_to_dict(loc)
        r = self.session.get('/sapi/v1/market/orderbook/',
                             params=params)
        return r.json()

    def get_recent_trades(self, market: str, limit: Optional[int] = None,
                          timestamp: Optional[int] = None, order_by: Optional[int] = None) -> Response[List[RecentTradesPayload]]:
        loc = locals()
        params = params_to_dict(loc)
        r = self.session.get('/sapi/v1/market/trades/',
                             params=params)
        return r.json()

    def get_nonce(self, eth_address: str) -> Response[str]:
        loc = locals()
        body = params_to_dict(loc)
        r = self.session.post('/sapi/v1/auth/v2/nonce/',
                              json=body)
        return r.json()

    def login(self, eth_address: str, user_signature: str) -> LoginResponse:
        loc = locals()
        body = params_to_dict(loc)
        r = self.session.post('/sapi/v1/auth/v2/login/',
                              json=body)
        js = r.json()
        try:
            self.session.headers.update(
                {'Authorization': f"JWT {js['token']['access']}"})
            self.set_refresh_token(js['token']['refresh'])
        except KeyError:
            raise AuthenticationError('Invalid Credentials')
        return js

    def complete_login(self, eth_address: str, private_key: str) -> LoginResponse:
        try:
            nonce = self.get_nonce(eth_address)
            user_signature = sign_msg(nonce['payload'], private_key)
            login = self.login(eth_address, user_signature)
        except KeyError:
            raise AuthenticationError('Invalid Credentials')
        return login

    def get_profile_info(self) -> Response[ProfileInformationPayload]:
        self.get_auth_status()
        r = self.session.get('/sapi/v1/user/profile/')
        return r.json()

    def get_balance(self, currency: Optional[str] = None) -> Response[Union[Balance, List[Balance]]]:
        self.get_auth_status()
        loc = locals()
        params = params_to_dict(loc)
        r = self.session.get('/sapi/v1/user/balance/', params=params)
        return r.json()

    def get_profit_and_loss(self) -> Response[ProfitAndLossPayload]:
        self.get_auth_status()
        r = self.session.get('/sapi/v1/user/pnl/')
        return r.json()

    def get_auth_status(self) -> bool:
        try:
            if self.session.headers['Authorization']:
                return True
        except KeyError:
            raise AuthenticationError(
                'This is a private endpoint... Please use login() or complete_login() first')
        return False

    def create_order_nonce(self, body: CreateOrderNonceBody) -> Response[CreateOrderNoncePayload]:
        self.get_auth_status()
        r = self.session.post('/sapi/v1/orders/nonce/',
                              json=body)
        return r.json()

    def create_new_order(self, body: CreateNewOrderBody) -> Response[Order]:
        self.get_auth_status()
        r = self.session.post('/sapi/v1/orders/create/',
                              json=body)
        return r.json()

    def get_order(self, order_id: int) -> Response[OrderPayload]:
        self.get_auth_status()
        r = self.session.get(f'/sapi/v1/orders/{order_id}')
        return r.json()

    def list_orders(self, limit: Optional[int] = 50, page: Optional[int] = None, market: Optional[str] = None, ord_type: Optional[str] = None, state: Optional[str] = None, base_unit: Optional[str] = None, quote_unit: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, side: Optional[str] = None) -> Response[List[OrderPayload]]:
        self.get_auth_status()
        loc = locals()
        params = params_to_dict(loc)
        r = self.session.get('/sapi/v1/orders', params=params)
        return r.json()

    def cancel_order(self, order_id: int) -> Response[CancelOrder]:
        self.get_auth_status()
        loc = locals()
        body = params_to_dict(loc)
        r = self.session.post('/sapi/v1/orders/cancel/', json=body)
        return r.json()

    def list_trades(self, limit: Optional[int] = None, page: Optional[int] = None, market: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, order_by: Optional[str] = None) -> Response[List[TradePayload]]:
        self.get_auth_status()
        loc = locals()
        body = params_to_dict(loc)
        r = self.session.get('/sapi/v1/trades/', json=body)
        return r.json()

    def get_coin_stats(self):
        r = self.session.post('/main/stat/v2/coins/')
        return r.json()

    def get_vault_id(self, coin: str):
        self.get_auth_status()
        loc = locals()
        body = params_to_dict(loc)
        r = self.session.post('/main/user/create_vault/', json=body)
        return r.json()

    def list_deposits(self, params: ListDepositParams):
        self.get_auth_status()
        loc = locals()
        body = params_to_dict(loc)
        r = self.session.get('/sapi/v1/deposits/', json=body)
        return r.json()

    def get_token_balance(self, provider: Web3, eth_address: str, currency: str):
        if currency == 'eth':
            balance_wei = provider.eth.get_balance(eth_address) # type: ignore
            balance_eth = provider.fromWei(balance_wei, 'ether')
            return balance_eth

        coin_stats =  self.get_coin_stats()
        current_coin = filter_ethereum_coin(coin_stats['payload'], currency)
        token_contract = current_coin['token_contract']
        decimal = current_coin['decimal']
        
        contract = provider.eth.contract(address=token_contract, abi=Config.ERC20_ABI) # type:ignore
        balance = contract.functions.balanceOf(eth_address).call()
        normal_balance = int(balance) / (10 ** int(decimal)) # type:ignore
        return normal_balance

    def crypto_deposit_start(self, amount: int, stark_asset_id: str, stark_public_key: str, deposit_blockchain_hash: str, deposit_blockchain_nonce: str, vault_id: str):
        amount_to_string = str(amount)
        payload = {
            'amount': amount_to_string,
            'token_id': stark_asset_id,
            'stark_key': stark_public_key,
            'deposit_blockchain_hash': deposit_blockchain_hash,
            'deposit_blockchain_nonce': deposit_blockchain_nonce,
            'vault_id': vault_id
        }
        r = self.session.post('/sapi/v1/payment/stark/start/', json=payload)
        return r.json()

    def approve_unlimited_allowance_ethereum_network(self, coin: str, signer, w3: Web3):
        coin_stats = self.get_coin_stats()
        current_coin = filter_ethereum_coin(coin_stats['payload'], coin)
        token_contract = current_coin['token_contract']
        stark_contract = Config.STARK_CONTRACT[self.option]
        res = approve_unlimited_allowance_util(contract_address=stark_contract, token_contract=token_contract, signer=signer, w3=w3)
        return res


    def deposit_from_ethereum_network_with_starkKey(self, signer: Account, provider: Web3, stark_public_key: str, amount: float, currency: str):
        w3 = provider
        amount = float(amount)
        if amount <= 0:
            raise InvalidAmountError("Please enter a valid amount. It should be a numerical value greater than zero.")

        self.get_auth_status()
        coin_stats = self.get_coin_stats()['payload']
        current_coin = filter_ethereum_coin(coin_stats, currency)
        quanitization = current_coin['quanitization']
        decimal = current_coin['decimal']
        token_contract = current_coin['token_contract']
        stark_asset_id = current_coin['stark_asset_id']

        quantized_amount = amount*(10**int(quanitization))
        quantized_amount = int(quantized_amount)

        vault = self.get_vault_id(currency)
        stark_contract = Config.STARK_CONTRACT[self.option]
        # ABI is what defines the intrinsic properties of a smart contract
        stark_abi = Config.STARK_ABI[self.option]

        contract_instance = w3.eth.contract(address=stark_contract, abi=stark_abi) # type:ignore
        parsed_amount = w3.toWei(amount, 'ether')
        gwei = w3.toWei(amount, 'gwei')

        # In the context of building transactions on the Ethereum network, 
        # "overrides" typically refer to parameters that allow you to customize 
        # the behavior of a transaction. These overrides can be used when interacting 
        # with smart contracts, and they provide a way to specify details such as 
        # the amount of gas to use, the gas price, the recipient address, and the value to send.
        overrides = {
            'from': signer.address, # type:ignore
            'nonce': get_nonce(signer, provider)
        }


        balance = self.get_token_balance(provider, signer.address, currency) # type:ignore

        if balance < amount:
            raise BalanceTooLowError(f'Current Balance ({balance}) for "{currency}" is too low, please add balance before deposit')

        stark_public_key_uint = int(get_0x0_to_0x(stark_public_key), 16)
        stark_asset_id_uint = int(get_0x0_to_0x(stark_asset_id), 16)
        if currency == 'eth':
            # On the smart contracts itself (not override parameter)
            # - For transactions involving Ether (ETH), the value is implicit and 
            #     doesn't need to be explicitly specified.
            # - For transactions involving other tokens on the Ethereum network, 
            #     you typically interact with smart contracts, and you need to explicitly specify 
            #     the value and other parameters required by the contract.
            overrides['value'] = w3.toWei(amount, 'ether')
            transaction_pre_build = contract_instance.functions.depositEth(
                stark_public_key_uint,
                stark_asset_id_uint,
                vault['payload']['id']
            )

        else:
            allowance = get_allowance(user_address=signer.address, stark_contract=stark_contract, token_contract=token_contract, decimal=decimal, w3=provider) # type:ignore
            if allowance < amount:
                raise InvalidAmountError(f"Current Allowance ({allowance}) is too low, please use Client.approveUnlimitedAllowanceEthereumNetwork()")
            transaction_pre_build = contract_instance.functions.depositERC20(
                stark_public_key_uint,
                stark_asset_id_uint,
                vault['payload']['id'],
                int(quantized_amount)
            )

        transaction = transaction_pre_build.buildTransaction(overrides)
        signed_tx = signer.sign_transaction(transaction)
        # send this signed transaction to blockchain
        w3.eth.sendRawTransaction(signed_tx.rawTransaction).hex()
        deposit_response = signed_tx

        res = self.crypto_deposit_start(
            gwei * 10 if currency == 'eth' else quantized_amount,
            get_0x0_to_0x(stark_asset_id),
            get_0x0_to_0x(stark_public_key),
            deposit_response['hash'].hex(),
            transaction['nonce'],
            vault['payload']['id']
        )

        res['payload'] = {'transaction_hash': deposit_response['hash'].hex()}

        return res

    def start_normal_withdrawal(self, body: dict):
        payload = {
            'amount': body['amount'],
            'token_id': body['symbol']
        }
        r = self.session.post('/sapi/v1/payment/withdrawals/v1/initiate/', json=payload)
        return r.json()

    def validate_normal_withdrawal(self, body: dict):
        r = self.session.post('/sapi/v1/payment/withdrawals/v1/validate/', json=body)
        return r.json()

    def initiate_normal_withdrawal(self, key_pair: dict, amount: float, coin_symbol: str):
        if float(amount)<=0:
            raise InvalidAmountError('Please enter a valid amount. It should be a numerical value greater than zero.')
        self.get_auth_status()
        initiate_response = self.start_normal_withdrawal({'amount': amount, 'symbol': coin_symbol})
        signature = sign_withdrawal_tx_msg_hash(key_pair, initiate_response['payload']['msg_hash'])
        msg_hex = initiate_response['payload']['msg_hash']
        msg_hex = hex(int(msg_hex))

        validate_response = self.validate_normal_withdrawal({
            'msg_hash': str(msg_hex[2:]),
            'signature': signature,
            'nonce': initiate_response['payload']['nonce']
        })
        return validate_response

    def get_pending_normal_withdrawal_amount_by_coin(self, coin_symbol: str, user_public_eth_address: str, signer: Account, provider: Web3):
        self.get_auth_status()
        w3 = provider
        coin_stats = self.get_coin_stats()['payload']
        current_coin = filter_ethereum_coin(coin_stats_payload=coin_stats, coin=coin_symbol)
        stark_asset_id = current_coin['stark_asset_id']
        blockchain_decimal = current_coin['blockchain_decimal']
        stark_contract = Config.STARK_CONTRACT[self.option]
        stark_abi = Config.STARK_ABI[self.option]

        contract_instance = w3.eth.contract(address=stark_contract, abi=stark_abi) # type:ignore
        
        balance = contract_instance.functions.getWithdrawalBalance(
            int(user_public_eth_address, 16),
            int(stark_asset_id, 16)
        ).call()

        return format_withdrawal_amount(amount=balance, decimals=int(blockchain_decimal), symbol=coin_symbol)

    def complete_normal_withdrawal(self, coin_symbol: str, user_public_eth_address: str, signer: Account, provider: Web3):
        self.get_auth_status()
        w3 = provider
        coin_stats = self.get_coin_stats()['payload']
        current_coin = filter_ethereum_coin(coin_stats_payload=coin_stats, coin=coin_symbol)
        stark_asset_id = current_coin['stark_asset_id']
        stark_contract = Config.STARK_CONTRACT[self.option]
        stark_abi = Config.STARK_ABI[self.option]

        contract_instance = w3.eth.contract(address=stark_contract, abi=stark_abi) # type:ignore

        transaction_pre_build = contract_instance.functions.withdraw(int(user_public_eth_address, 16), int(stark_asset_id, 16))

        overrides = {
            'nonce': get_nonce(signer, provider)
        }
        transaction = transaction_pre_build.buildTransaction(overrides)
        signed_tx = signer.sign_transaction(transaction)
        # send this signed transaction to blockchain
        w3.eth.sendRawTransaction(signed_tx.rawTransaction).hex()
        res = signed_tx
        return res

    def list_normal_withdrawals(self, params: Optional[ListWithdrawalParams]=None):
        self.get_auth_status()
        r = self.session.get('/sapi/v1/payment/withdrawals/', json=params)
        return r.json()
