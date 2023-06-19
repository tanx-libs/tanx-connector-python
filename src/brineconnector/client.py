from .session import Session
from .utils import params_to_dict
from .bin.blockchain_utils import sign_msg
from .exception import AuthenticationError
from typing import Optional, Union, List, Literal
from .typings import Response, LoginResponse, FullDayPricePayload, CandleStickPayload, OrderBookPayload, RecentTradesPayload, ProfileInformationPayload, Balance, ProfitAndLossPayload, CreateOrderNoncePayload, CreateNewOrderBody, OrderPayload, CreateOrderNonceBody, CancelOrder, TradePayload, Order, TokenType


class Client:
    def __init__(self, option: Literal['mainnet', 'testnet'] = 'mainnet'):
        base_url = "https://api-testnet.brine.fi" if option == 'testnet' else 'https://api.brine.fi'
        self.session = Session(self.refresh_tokens, base_url)
        self.access_token: Optional[str] = None
        self.refresh_token: Optional[str] = None

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
        r = self.session.post('/sapi/v1/auth/nonce/',
                              json=body)
        return r.json()

    def login(self, eth_address: str, user_signature: str) -> LoginResponse:
        loc = locals()
        body = params_to_dict(loc)
        r = self.session.post('/sapi/v1/auth/login/',
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

    def list_orders(self) -> Response[List[OrderPayload]]:
        self.get_auth_status()
        r = self.session.get('/sapi/v1/orders')
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
