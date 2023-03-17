from .session import Session
from .utils import params_to_dict
from .bin.blockchain_utils import sign_msg
from .exception import AuthenticationException
from .bin.signature import sign, get_stark_key_pair_from_signature
from typing import Optional, Union, List
from .data_types import Response, LoginResponse, FullDayPricePayload, CandleStickPayload, OrderBookPayload, RecentTradesPayload, ProfileInformationPayload, Balance, ProfitAndLossPayload, CreateOrderNoncePayload, CreateNewOrderBody, OrderPayload, CreateOrderNonceBody, CancelOrder, TradePayload, Order


class Client:
    def __init__(self, base_url: str = "https://api-testnet.brine.fi"):
        self.session = Session(self.retry_login, base_url)
        self.eth_address: Optional[str] = None
        self.user_signature: Optional[str] = None

    def retry_login(self) -> Union[LoginResponse, None]:
        if self.eth_address and self.user_signature:
            return self.login(self.eth_address, self.user_signature)

    def set_token(self, token) -> None:
        self.session.headers.update(
            {'Authorization': f"JWT {token}"})

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
            self.eth_address = eth_address
            self.user_signature = user_signature
        except KeyError:
            raise AuthenticationException('Invalid Credentials')
        return js

    def complete_login(self, eth_address: str, private_key: str) -> LoginResponse:
        try:
            nonce = self.get_nonce(eth_address)
            user_signature = sign_msg(nonce['payload'], private_key)
            login = self.login(eth_address, user_signature)
        except KeyError:
            raise AuthenticationException('Invalid Credentials')
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
            raise AuthenticationException(
                'This is a private endpoint... Please use login() or complete_login() first')
        return False

    def create_order_nonce(self, body: CreateOrderNonceBody) -> Response[CreateOrderNoncePayload]:
        self.get_auth_status()
        r = self.session.post('/sapi/v1/orders/nonce/',
                              json=body)
        return r.json()

    def sign_msg_hash(self, nonce: CreateOrderNoncePayload, private_key: str) -> CreateNewOrderBody:
        msg_to_be_signed = "Click sign to verify you're a human - Brine.finance"
        signature = sign_msg(msg_to_be_signed, private_key)
        stark_creds = get_stark_key_pair_from_signature(
            signature=signature)
        stark_private_key = stark_creds["stark_private_key"]
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

    def create_new_order(self, body: CreateNewOrderBody) -> Response[Order]:
        self.get_auth_status()
        r = self.session.post('/sapi/v1/orders/create/',
                              json=body)
        return r.json()

    def create_complete_order(self, nonce: CreateOrderNonceBody,  private_key: str) -> Response[Order]:
        self.get_auth_status()
        nonce_res = self.create_order_nonce(nonce)
        msg_hash = self.sign_msg_hash(nonce_res['payload'], private_key)
        order = self.create_new_order(msg_hash)
        return order

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
