# ABfinance Python API

[![PyPI version](https://img.shields.io/pypi/v/abfinance-python-api.svg)](https://pypi.org/project/abfinance-python-api/)
[![Python](https://img.shields.io/pypi/pyversions/abfinance-python-api.svg)](https://pypi.org/project/abfinance-python-api/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Official Python3 API connector for ABFinance's HTTP and WebSocket APIs.

## Installation

```bash
pip install abfinance-python-api
```

Requires Python 3.9+

## Quick Start

### HTTP API

```python
from abfinance_api.unified_trading import HTTP

# Public endpoints (no authentication required)
session = HTTP(testnet=True)
print(session.get_server_time())
print(session.get_orderbook(category="linear", symbol="BTCUSDT"))

# Private endpoints (authentication required)
session = HTTP(
    testnet=True,
    api_key="your_api_key",
    api_secret="your_api_secret",
)

# Get wallet balance
print(session.get_wallet_balance(accountType="UNIFIED"))

# Place an order
print(session.place_order(
    category="linear",
    symbol="BTCUSDT",
    side="Buy",
    orderType="Limit",
    qty="0.01",
    price="30000",
))
```

### WebSocket API

```python
from abfinance_api.unified_trading import WebSocket

def handle_message(message):
    print(message)

# Public WebSocket
ws = WebSocket(testnet=True, channel_type="linear")
ws.orderbook_stream(depth=50, symbol="BTCUSDT", callback=handle_message)

# Private WebSocket
ws_private = WebSocket(
    testnet=True,
    channel_type="private",
    api_key="your_api_key",
    api_secret="your_api_secret",
)
ws_private.order_stream(callback=handle_message)
```

## Features

- HTTP API support for all endpoints
- WebSocket API for real-time data
- HMAC and RSA authentication
- Testnet and mainnet support

## Examples

See the [examples](./examples) directory for more usage examples.

## License

MIT License
