from .session import Session
from .utils import params_to_dict
from .bin.blockchain_utils import sign_msg
from .exception import AuthenticationException
from .bin.signature import sign, get_stark_key_pair_from_signature
from typing import Optional


class Client:
    def __init__(self, base_url: str = "https://api-testnet.brine.fi"):
        self.session = Session(base_url)

    def test_connection(self) -> dict:
        r = self.session.get('/sapi/v1/health/')
        return r.json()

    def get_24h_price(self, market: str) -> dict:
        r = self.session.get('/sapi/v1/market/tickers/',
                             params={market: market})
        return r.json()

    def get_candlestick(self, market: str, limit: int = None,
                        period: int = None, start_time: int = None,
                        end_time: int = None) -> dict:
        loc = locals()
        params = params_to_dict(loc)
        r = self.session.get('/sapi/v1/market/kline/',
                             params=params)
        return r.json()

    def get_orderbook(self, market: str, asks_limit: int = None,
                      bids_limit: int = None) -> dict:
        loc = locals()
        params = params_to_dict(loc)
        r = self.session.get('/sapi/v1/market/orderbook/',
                             params=params)
        return r.json()

    def get_recent_trades(self, market: str, limit: int = None,
                          timestamp: int = None, order_by: str = None) -> dict:
        loc = locals()
        params = params_to_dict(loc)
        r = self.session.get('/sapi/v1/market/trades/',
                             params=params)
        return r.json()

    def get_nonce(self, eth_address: str) -> dict:
        loc = locals()
        body = params_to_dict(loc)
        r = self.session.post('/sapi/v1/auth/nonce/',
                              json=body)
        return r.json()

    def login(self, eth_address: str, user_signature: str) -> dict:
        loc = locals()
        body = params_to_dict(loc)
        r = self.session.post('/sapi/v1/auth/login/',
                              json=body)
        js = r.json()
        try:
            self.session.headers.update(
                {'Authorization': f"JWT {js['token']['access']}"})
        except KeyError:
            raise AuthenticationException('Incorrect Credentials')
        return js

    def complete_login(self, eth_address: str, private_key: str):
        try:
            nonce = self.get_nonce(eth_address)
            user_signature = sign_msg(nonce['payload'], private_key)
            login = self.login(eth_address, user_signature)
        except KeyError:
            return nonce
        return login

    def get_profile_info(self) -> dict:
        self.get_auth_status()
        r = self.session.get('/sapi/v1/user/profile/')
        return r.json()

    def get_balance(self, currency: str = None) -> dict:
        self.get_auth_status()
        loc = locals()
        params = params_to_dict(loc)
        r = self.session.get('/sapi/v1/user/balance/', params=params)
        return r.json()

    def get_profit_and_loss(self):
        self.get_auth_status()
        r = self.session.get('/sapi/v1/user/pnl/')
        return r.json()

    def get_auth_status(self):
        try:
            if self.session.headers['Authorization']:
                return True
        except KeyError:
            raise AuthenticationException(
                'This is a private endpoint... Please use login() or complete_login() first')

    def create_order_nonce(self, market: str, ord_type: str,
                           price: int, side: str, volume: float) -> dict:
        self.get_auth_status()
        loc = locals()
        body = params_to_dict(loc)
        r = self.session.post('/sapi/v1/orders/nonce/',
                              json=body)
        return r.json()

    def sign_msg_hash(self, nonce: dict, private_key: str) -> dict:
        msg_to_be_signed = "Click sign to verify you're a human - Brine.finance"
        signature = sign_msg(msg_to_be_signed, private_key)
        stark_creds = get_stark_key_pair_from_signature(
            signature=signature)
        stark_private_key = stark_creds["stark_private_key"]
        r, s = sign(msg_hash=int(nonce['msg_hash'], 16),
                    stark_private_key=stark_private_key)
        create_order_request_data = {
            "nonce": nonce['nonce'],
            "msg_hash": nonce['msg_hash'],
            "signature": {
                "r": hex(r),
                "s": hex(s)
            }
        }
        return create_order_request_data

    def create_new_order(self, body: dict) -> dict:
        self.get_auth_status()
        r = self.session.post('/sapi/v1/orders/create/',
                              json=body)
        return r.json()

    def create_complete_order(self, market: str, ord_type: str,
                              price: int, side: str, volume: float, private_key: str) -> dict:
        self.get_auth_status()
        try:
            nonce = self.create_order_nonce(
                market, ord_type, price, side, volume)
            msg_hash = self.sign_msg_hash(nonce['payload'], private_key)
            order = self.create_new_order(msg_hash)
        except KeyError:
            return nonce
        return order

    def get_order(self, order_id: int) -> dict:
        self.get_auth_status()
        r = self.session.post(f'/sapi/v1/orders/{order_id}')
        return r.json()

    def list_orders(self) -> dict:
        self.get_auth_status()
        r = self.session.post('/sapi/v1/orders')
        return r.json()

    def cancel_order(self, order_id: int) -> dict:
        self.get_auth_status()
        loc = locals()
        body = params_to_dict(loc)
        r = self.session.post('/sapi/v1/orders/cancel/', json=body)
        return r.json()

    def list_trades(self, limit: Optional[int] = None, page: Optional[int] = None, market: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, order_by: Optional[str] = None) -> dict:
        self.get_auth_status()
        loc = locals()
        body = params_to_dict(loc)
        r = self.session.get('/sapi/v1/trades/', json=body)
        return r.json()
