from abfinance_api.unified_trading import HTTP

session = HTTP(
    testnet=True,
    api_key="...",
    api_secret="...",
)

# Get server time (no authentication required)
print("=== Get Server Time ===")
print(session.get_server_time())

# Get kline (candlestick) data for spot market
print("\n=== Get Kline ===")
print(session.get_kline(
    category="spot",
    symbol="BTCUSDT",
    interval="15",  # 15 minutes
))

# Get instruments info for spot market
print("\n=== Get Instruments Info ===")
print(session.get_instruments_info(
    category="spot",
))

# Get orderbook for spot market
print("\n=== Get Orderbook ===")
print(session.get_orderbook(
    category="spot",
    symbol="BTCUSDT",
))

# Get tickers for spot market
print("\n=== Get Tickers ===")
print(session.get_tickers(
    category="spot",
))

# Get public trade history for spot market
print("\n=== Get Public Trade History ===")
print(session.get_public_trade_history(
    category="spot",
    symbol="BTCUSDT",
))

# Get RPI orderbook for spot market
print("\n=== Get RPI Orderbook ===")
print(session.get_rpi_orderbook(
    category="spot",
    symbol="BTCUSDT",
    limit=10,
))
