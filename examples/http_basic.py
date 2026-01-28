"""
HTTP Basic Example

Demonstrates basic HTTP API usage:
- Public endpoints (no authentication required)
- Private endpoints (authentication required)
"""

from abfinance_api.unified_trading import HTTP

# =============================================================================
# Public endpoints (no authentication required)
# =============================================================================

session = HTTP(testnet=True)

# Get server time
print("=== Server Time ===")
print(session.get_server_time())

# Get market tickers
print("\n=== Tickers (BTCUSDT) ===")
print(session.get_tickers(category="spot", symbol="BTCUSDT"))

# Get orderbook
print("\n=== Orderbook ===")
print(session.get_orderbook(category="spot", symbol="BTCUSDT", limit=5))

# Get kline data
print("\n=== Kline (15min) ===")
print(session.get_kline(category="spot", symbol="BTCUSDT", interval="15", limit=3))

# Get instruments info
print("\n=== Instruments Info ===")
result = session.get_instruments_info(category="spot", symbol="BTCUSDT")
print(result)

# =============================================================================
# Private endpoints (authentication required)
# =============================================================================

session_auth = HTTP(
    testnet=True,
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET",
)

# Get wallet balance
print("\n=== Wallet Balance ===")
print(session_auth.get_wallet_balance(accountType="UNIFIED"))

# Get account info
print("\n=== Account Info ===")
print(session_auth.get_account_info())

# Get fee rates
print("\n=== Fee Rates ===")
print(session_auth.get_fee_rates(category="spot", symbol="BTCUSDT"))
