"""
WebSocket Private Example

Demonstrates subscribing to private account data streams:
- Order stream
- Execution stream
- Wallet stream
"""

from abfinance_api.unified_trading import WebSocket
from time import sleep

# =============================================================================
# Connect to private WebSocket (requires authentication)
# =============================================================================

ws = WebSocket(
    testnet=True,
    channel_type="private",
    api_key="DmYz0aRKBG9fOFrF4d",
    api_secret="WLVU3Jz1n1L0KHoMzJ1kR5hnegm2ZESRs2dL",
    skip_ssl_verify=True,  # Skip SSL certificate verification for testing
)
# =============================================================================
# Subscribe to order stream
# =============================================================================

def handle_order(message):
    data = message.get("data", [])
    for order in data:
        print(f"[Order] {order.get('symbol')} {order.get('side')} {order.get('orderStatus')}: "
              f"qty={order.get('qty')} price={order.get('price')}")

ws.order_stream(handle_order)

# =============================================================================
# Subscribe to execution stream
# =============================================================================

def handle_execution(message):
    data = message.get("data", [])
    for exec in data:
        print(f"[Execution] {exec.get('symbol')} {exec.get('side')}: "
              f"qty={exec.get('execQty')} price={exec.get('execPrice')}")

ws.execution_stream(handle_execution)

# =============================================================================
# Subscribe to wallet stream
# =============================================================================

def handle_wallet(message):
    data = message.get("data", [])
    for wallet in data:
        coins = wallet.get("coin", [])
        for coin in coins:
            print(f"[Wallet] {coin.get('coin')}: balance={coin.get('walletBalance')}")

ws.wallet_stream(handle_wallet)

# =============================================================================
# Keep connection alive
# =============================================================================

print("Subscribed to private streams. Press Ctrl+C to exit.\n")
print("Place orders via HTTP API or web interface to see updates.\n")

try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    print("\nClosing connection...")
    ws.exit()
    print("Done.")
