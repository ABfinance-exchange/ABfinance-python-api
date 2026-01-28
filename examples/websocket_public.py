"""
WebSocket Public Example

Demonstrates subscribing to public market data streams:
- Ticker stream
- Orderbook stream
- Trade stream
- Kline stream
"""

from abfinance_api.unified_trading import WebSocket
from time import sleep

# =============================================================================
# Connect to public WebSocket
# =============================================================================

ws = WebSocket(
    testnet=True,
    channel_type="spot",
    skip_ssl_verify=True,  # Skip SSL certificate verification for testing
)

# =============================================================================
# Subscribe to ticker stream
# =============================================================================

def handle_ticker(message):
    data = message.get("data", {})
    print(f"[Ticker] {data.get('symbol')}: {data.get('lastPrice')}")

ws.ticker_stream("BTCUSDT", handle_ticker)

# =============================================================================
# Subscribe to orderbook stream
# =============================================================================

def handle_orderbook(message):
    data = message.get("data", {})
    bids = data.get("b", [])[:3]
    asks = data.get("a", [])[:3]
    print(f"[Orderbook] Best Bid: {bids[0] if bids else 'N/A'}, Best Ask: {asks[0] if asks else 'N/A'}")

ws.orderbook_stream(50, "ETHUSDT", handle_orderbook)

# =============================================================================
# Subscribe to trade stream
# =============================================================================

def handle_trade(message):
    data = message.get("data", [])
    for trade in data:
        print(f"[Trade] {trade.get('s')}: {trade.get('p')} x {trade.get('v')}")

ws.trade_stream("BTCUSDT", handle_trade)

# =============================================================================
# Subscribe to kline stream
# =============================================================================

def handle_kline(message):
    data = message.get("data", [])
    for kline in data:
        print(f"[Kline] {kline.get('symbol')}: O={kline.get('open')} H={kline.get('high')} L={kline.get('low')} C={kline.get('close')}")

ws.kline_stream(1, "BTCUSDT", handle_kline)

# =============================================================================
# Keep connection alive
# =============================================================================

print("Subscribed to streams. Press Ctrl+C to exit.\n")

try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    print("\nClosing connection...")
    ws.exit()
    print("Done.")
