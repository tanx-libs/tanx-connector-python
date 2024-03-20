from typing import TypeVar, Generic, Dict, Tuple, Union, List, Optional
from typing_extensions import TypedDict

T = TypeVar("T")


class Response(TypedDict, Generic[T]):
    status: str
    message: str
    payload: T


class Ticker(TypedDict):
    at: str
    avg_price: str
    high: str
    last: str
    low: str
    open: str
    price_change_percent: str
    volume: str
    amount: str


class MarketType(TypedDict):
    at: str
    ticker: Ticker


FullDayPricePayload = Dict[str, MarketType]

CandleStickPayload = Tuple[int, int, int, int, int, int]


class AskBid(TypedDict):
    id: int
    uuid: str
    side: str
    ord_type: str
    price: str
    avg_price: str
    state: str
    market: str
    created_at: str
    updated_at: str
    origin_volume: str
    remaining_volume: str
    executed_volume: str
    maker_fee: str
    taker_fee: str
    trades_count: int


class OrderBookPayload(TypedDict):
    asks: List[AskBid]
    bids: List[AskBid]


class RecentTradesPayload(TypedDict):
    id: int
    price: int
    amount: int
    total: int
    market: str
    created_at: int
    taker_type: str


class CreateOrderNoncePayload(TypedDict):
    nonce: int
    msg_hash: str


class Signature(TypedDict):
    r: str
    s: str


class CreateNewOrderBody(CreateOrderNoncePayload):
    signature: Signature

class CreateOrderNonceBody(TypedDict):
    market: str
    ord_type: str
    price: float
    side: str
    volume: float

class Order(TypedDict):
    id: int
    uuid: str
    side: str
    ord_type: str
    price: str
    avg_price: str
    state: str
    market: str
    created_at: str
    updated_at: str
    origin_volume: str
    remaining_volume: str
    executed_volume: str
    maker_fee: str
    taker_fee: str
    trades_count: int


class OrderPayload(Order):
    trades: list


class CancelOrder(Order):
    order_id: int


class TradePayload(TypedDict):
    id: int
    price: str
    amount: str
    total: str
    fee_currency: str
    fee: str
    fee_amount: str
    market: str
    created_at: str
    taker_type: str
    side: str
    order_id: int


class LoginPayload(TypedDict):
    uid: str


class TokenType(TypedDict):
    refresh: str
    access: str


class LoginResponse(Response[LoginPayload]):
    token: TokenType


class ProfileInformationPayload(TypedDict):
    name: str
    customer_id: str
    img: str
    username: str
    stark_key: str


class Balance(TypedDict):
    currency: str
    balance: str
    locked: str
    deposit_address: str


class ProfitAndLoss(TypedDict):
    currency: str
    pnl_currency: str
    total_credit: str
    total_debit: str
    total_credit_value: str
    total_debit_value: str
    average_buy_price: str
    average_sell_price: str
    average_balance_price: str
    total_balance_value: str


ProfitAndLossPayload = List[ProfitAndLoss]

class CoinStat(TypedDict):
    stark_asset_id: str
    quanitization: str
    token_contract: str
    decimal: str
    symbol: str
    blockchain_decimal: str

CoinStatPayload = Dict[str, CoinStat]

class ListDepositParams(TypedDict):
    limit: int
    page: int
    network: str

class ListWithdrawalParams(TypedDict):
    page: Optional[int]
    network: Optional[str]

class InitiateWithdrawalPayload(TypedDict):
    amount: float
    symbol: str
    network: Optional[str]

class StarkSignature(TypedDict):
    r: str
    s: str
    recoveryParam: Optional[int]

class ProcessFastWithdrawalPayload(TypedDict):
    msg_hash: str
    signature: StarkSignature
    fastwithdrawal_withdrawal_id: int

class InternalTransferKey(TypedDict):
    organization_key: str
    api_key: str

class InternalTransferInitiateBody(InternalTransferKey):
    client_reference_id: Optional[int]
    currency: str
    amount: float
    destination_address: str

class InternalTransferProcessBody(InternalTransferKey):
    signature: StarkSignature
    nonce: int
    msg_hash: str

class ListInternalTransferParams(TypedDict):
    limit: Optional[int]
    offset: Optional[int]
