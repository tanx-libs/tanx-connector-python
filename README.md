<h1 align="center">tanX Connector Python</h1>

<p align="center">
  The official Python connector for <a href="https://docs.tanx.fi/tech/api-documentation">tanX's API</a> 🚀
</p>

<!-- <div align="center">

  [![npm version](https://img.shields.io/npm/v/@tanx-fi/tanx-connector)](https://www.npmjs.org/package/@tanx-fi/tanx-connector)
  [![Build status](https://img.shields.io/github/actions/workflow/status/tanx-Libs/tanx-connector-nodejs/main.yml)](https://github.com/tanX-Finance-Libs/tanX-connector-nodejs/actions/workflows/main.yml)
  [![npm bundle size](https://img.shields.io/bundlephobia/minzip/@tanx-fi/tanx-connector)](https://bundlephobia.com/package/@tanx-fi/tanx-connector@latest)

</div> -->


## Features

- Complete endpoints including REST and WebSockets
- Methods return parsed JSON.
- High level abstraction for ease of use.
- Easy authentication
- Automatically sets JWT token internally
- Auto refresh tokens when access token expires

Tanx-connector-python includes utility/connector functions which can be used to interact with the Brine API. It uses requests internally to handle all requests.

## Installation

First go to the [tanX Website](https://www.tanx.fi/) and create an account with your wallet.

## Getting Started

The default base url for mainnet is https://api.tanx.fi and testnet is https://api-testnet.tanx.fi. You can choose between mainnet and testnet by providing it through the constructor. The default is mainnet. All REST apis, WebSockets are handled by Client, WsClient classes respectively.

### Workflow

Check out the [example files](./example) to see an example workflow.

### Rest Client

Import the REST Client

```py
from tanxconnector import Client
```

Create a new instance

```python
client = Client()
// or
client = Client('testnet') 
// default is mainnet
```

### General Endpoints

#### Test connectivity

`GET /sapi/v1/health/`

```python
client.test_connection()
```

#### 24hr Price

`GET /sapi/v1/market/tickers/`

```python
client.get_24h_price('btcusdt')
```

#### Kline/Candlestick Data

`GET /sapi/v1/market/kline/`

```python
client.get_candlestick('btcusdt')
```

#### Order Book

`GET /sapi/v1/market/orderbook/`

```python
client.get_orderbook('btcusdt')
```

#### Recent trades

`GET /sapi/v1/market/trades/`

```python
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

```python
res = client.refresh_tokens(refresh_token)
```

#### Logout

Sets tokens to null

```python
client.logout()
```

#### Profile Information (Private 🔒)

`GET /sapi/v1/user/profile/`

```python
client.get_profile_info()
```

#### Balance details (Private 🔒)

`GET /sapi/v1/user/balance/`

```python
client.get_balance()
```

#### Profit and Loss Details (Private 🔒)

`GET /sapi/v1/user/pnl/`

```python
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

Currently generating L2 Key Pairs (stark keys) are only supported with the [NodeJS SDK](https://github.com/tanx-libs/tanx-connector-nodejs#create-l2-key-pair)

```python
from brineconnector import sign_order_with_stark_private_key

nonce_res = client.create_order_nonce(nonce)
msg_hash = sign_order_with_stark_private_key(stark_private_key, nonce_res['payload'])
order = client.create_new_order(msg_hash)
```

#### Get Order (Private 🔒)

`GET /sapi/v1/orders/{order_id}/`

```python
client.get_order(order_id)
```

#### List Orders (Private 🔒)

`GET /sapi/v1/orders/`

```python
client.list_orders(
  limit=50,
  page=1,
  market='btcusdc',
  state='wait',
  base_unit='btc',
  quote_unit='usdc',
  start_time=1694785739,
  end_time=1694785839,
  side='buy'
)
```

#### Cancel Order (Private 🔒)

`POST /sapi/v1/orders/cancel/`

```python
client.cancel_order(order_id)
```

#### List Trades (Private 🔒)

`GET /sapi/v1/trades/`

```python
client.list_trades()
```

### WebSocket Client

Import the WebSocket Client. All WsClient methods are asynchronous (use async/await method).

```py
from brineconnector import WsClient
import asyncio
```

Create a new instance

```python
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
except tanxconnector.exception.AuthenticationError as exc:
    print(exc)
except requests.exceptions.HTTPError as exc:
    print(exc.response.json())
```

### Deposit

#### Ethereum Deposit

There are two ways to make a deposit on the Ethereum network:

<!-- 1. Using ETH Private Key and RPC URL: This approach utilizes your ETH private key and an rpcUrl (e.g., from Infura or Alchemy).
2. Custom Provider and Signer: This method involves creating your provider and signer using web3.py. You'll also need the stark_public_key. -->

#### Using Custom Provider and Signer:

This method involves using a custom provider and signer, which can be created using the web3.py library. The `stark_public_key` mentioned in the code should be obtained using the steps described in the [Create L2 Key Pair](#create-l2-key-pair) section of the nodejs connector(https://github.com/tanx-libs/tanx-connector-nodejs#create-l2-key-pair). Here's the code snippet for this method:

```python
# Note: Please use web3 version 5.25.0
from web3 import Web3, Account

provider = Web3(Web3.HTTPProvider(rpc_provider))
signer = Account.from_key(PRIVATE_KEY)

deposit_res_with_stark_keys = client.deposit_from_ethereum_network_with_starkKey(
  signer,
  provider,
  f'0x{stark_public_key}',
  0.0001,
  'usdc'
)
```

#### Polygon Deposit

There are two ways to make a deposit on the Polygon network:

#### 1. Using ETH Private Key and RPC URL:

In this method, you will use an ETH private key and an RPC URL to execute a Polygon deposit. You'll also need to create an RPC URL using services like Infura, Alchemy, etc. Here's the code snippet for this method:

```python
deposit_res = client.deposit_from_polygon_network(
  polygon_rpc_provider, # Use 'Polygon Mumbai' for the testnet and 'Polygon mainnet' for the mainnet.
  PRIVATE_KEY,  # ETH Private Key
  'matic',  # Coin Symbol
  0.00001 # Amount to be deposited
)
```

#### 2. Using Custom Provider and Signer:

This method involves using a custom provider and signer, which can be created using the web3.py library. Here's the code snippet for this method:

```python
# Note: Please use ethers version 5.25.0.
from web3 import Web3, Account
from web3.middleware.geth_poa import geth_poa_middleware

provider = Web3(Web3.HTTPProvider(polygon_rpc_provider))
provider.middleware_onion.inject(geth_poa_middleware, layer=0)

signer = Account.from_key(PRIVATE_KEY)

polygon_deposit_res = client.deposit_from_polygon_network_with_signer(
  signer, # Signer Created above
  provider, # Provider created above
  'btc',  # Enter the coin symbol
  0.0001, # Amount to be deposited
)
```

#### List Deposits

To get the deposit history, you can use the following code:

```python
deposit_list = client.list_deposits({
  'page': 1,  # This field is optional
  'limit': 1, # This field is optional
  'network': 'ETHEREUM' # Network for which you want to list the deposit history. Allowed networks are ETHEREUM & POLYGON
})
```

