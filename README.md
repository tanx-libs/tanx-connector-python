# Brine Connector Python

## _A Python Connector for the Brine API_

Brine-connector-python is a Python connector/wrapper for the [Brine API](https://docs.brine.fi/api-documentation).

## Features

- Complete endpoints including REST and WebSockets
- Methods return parsed JSON.
- High level abstraction for ease of use.
- Easy authentication
- Automatically sets JWT token internally
- Auto refresh tokens when access token expires

Brine-connector-python includes utility/connector functions which can be used to interact with the Brine API. It uses requests internally to handle all requests.

## Installation

First go to the [Brine Website](https://www.brine.finance/) and create an account with your wallet.

Install the package.

```sh
pip install brine-connector
```

## Getting Started

The default base url for mainnet is https://api.brine.fi and testnet is https://api-testnet.brine.fi. You can choose between mainnet and testnet by providing it through the constructor. The default is mainnet. All REST apis, WebSockets are handled by Client, WsClient classes respectively.

### Workflow

Check out the [example files](./example) to see an example workflow.

### Rest Client

Import the REST Client

```py
from brineconnector import Client
```

Create a new instance

```ts
client = Client()
// or
client = Client('testnet') 
// default is mainnet
```

### General Endpoints

#### Test connectivity

`GET /sapi/v1/health/`

```ts
client.test_connection()
```

#### 24hr Price

`GET /sapi/v1/market/tickers/`

```ts
client.get_24h_price('btcusdt')
```

#### Kline/Candlestick Data

`GET /sapi/v1/market/kline/`

```ts
client.get_candlestick('btcusdt')
```

#### Order Book

`GET /sapi/v1/market/orderbook/`

```ts
client.get_orderbook('btcusdt')
```

#### Recent trades

`GET /sapi/v1/market/trades/`

```ts
client.get_recent_trades('btcusdt')
```

#### Login

Both login() and complete_Login() sets tokens internally. Optionally, set_access_token() and set_refresh_token() can be used to set tokens directly.

getNonce: `POST /sapi/v1/auth/nonce/`  
login: `POST /sapi/v1/auth/login/`

```js
from brineconnector import sign_msg

nonce = client.get_nonce(ETH_ADDRESS)
user_signature = sign_msg(nonce['payload'], PRIVATE_KEY)
login = client.login(ETH_ADDRESS, user_signature)

// or

client.complete_login(ETH_ADDRESS, PRIVATE_KEY)  // calls above functions internally

// or

client.set_access_token(token)
client.set_refresh_token(token)
// these functions are called internally when you use login or complete_login
```

#### Refresh Token

`POST /sapi/v1/auth/token/refresh/`

If refresh token is set (manually or by using login functions), the refresh endpoint is called automatically when access token expires. Optionally, you can call `refresh_tokens` manually by passing in refresh_token (passing it is optional, it'll work if has been set before).

```ts
res = client.refresh_tokens(refresh_token)
```

#### Logout

Sets tokens to null

```ts
client.logout()
```

#### Profile Information (Private 🔒)

`GET /sapi/v1/user/profile/`

```ts
client.get_profile_info()
```

#### Balance details (Private 🔒)

`GET /sapi/v1/user/balance/`

```ts
client.get_balance()
```

#### Profit and Loss Details (Private 🔒)

`GET /sapi/v1/user/pnl/`

```ts
client.get_profit_and_loss()
```

#### Create order (Private 🔒)

Create Nonce Body

```py
from brineconnector.typings import CreateOrderNonceBody
nonce: CreateOrderNonceBody = {'market': 'btcusdt', 'ord_type': 'market',
                               'price': 29580.51, 'side': 'buy', 'volume': 0.0001}
```

Create Order

create_order_nonce: `POST /sapi/v1/orders/nonce/`  
create_new_order: `POST /sapi/v1/orders/create/`

Currently generating L2 Key Pairs (stark keys) are only supported with the [NodeJS SDK](https://github.com/Brine-Finance-Libs/brine-connector-nodejs#create-l2-key-pair)

```ts
from brineconnector import sign_order_with_stark_private_key

nonce_res = client.create_order_nonce(nonce)
msg_hash = sign_order_with_stark_private_key(stark_private_key, nonce_res['payload'])
order = client.create_new_order(msg_hash)
```

#### Get Order (Private 🔒)

`GET /sapi/v1/orders/{order_id}/`

```ts
client.get_order(order_id)
```

#### List Orders (Private 🔒)

`GET /sapi/v1/orders/`

```ts
client.list_orders()
```

#### Cancel Order (Private 🔒)

`POST /sapi/v1/orders/cancel/`

```ts
client.cancel_order(order_id)
```

#### List Trades (Private 🔒)

`GET /sapi/v1/trades/`

```ts
client.list_trades()
```

### WebSocket Client

Import the WebSocket Client. All WsClient methods are asynchronous (use async/await method).

```py
from brineconnector import WsClient
import asyncio
```

Create a new instance

```ts
ws_client = WsClient('public')
// or
ws_client = WsClient('public', 'mainnet')
// default is mainnet
// or
login = client.complete_login(ETH_ADDRESS, PRIVATE_KEY)
ws_client =  WsClient('private', 'mainnet', login['token']['access'])
```

#### Connect

```py
await ws_client.connect()
```

#### Subscribe

```py
streams = [
  'btcusdc.trades',
  'btcusdc.ob-inc',
  'btcusdc.kline-5m',
]
await ws_client.subscribe(streams)

# or for private

await ws_client.subscribe(['trade', 'order'])
```

#### Unsubscribe

```py
streams = [
  'btcusdc.trades',
  'btcusdc.ob-inc',
  'btcusdc.kline-5m',
]
await ws_client.unsubscribe(streams)

# or for private

await ws_client.unsubscribe(['trade', 'order'])
```

#### Disconnect

```py
ws_client.disconnect()
```

#### Usage

WsClient includes a member called websocket which is initialized with websockets.connect(). You may use it to handle WebSocket operations.

```py
async for message in ws_client.websocket:
    print(message)
```

### Error Handling

Errors thrown are of types `AuthenticationError or requests.exceptions.HTTPError`.  

Example

```py
try:
    # call methods
except brineconnector.exception.AuthenticationError as exc:
    print(exc)
except requests.exceptions.HTTPError as exc:
    print(exc)
```

