"""
WebSocket Trading Example

Demonstrates trading operations via WebSocket:
- Place order
- Amend order
- Cancel order
- Batch operations

WebSocket trading provides lower latency compared to HTTP API.
"""

from abfinance_api.unified_trading import WebSocketTrading
from time import sleep

# =============================================================================
# Connect to trading WebSocket
# =============================================================================

ws = WebSocketTrading(
    testnet=True,
    api_key="DmYz0aRKBG9fOFrF4d",
    api_secret="WLVU3Jz1n1L0KHoMzJ1kR5hnegm2ZESRs2dL",
    skip_ssl_verify=True,  # Skip SSL certificate verification for testing
)

# Wait for connection and authentication
sleep(2)

# =============================================================================
# Place order
# =============================================================================

def handle_place_order(message):
    print(f"[Place Order Response]")
    print(f"  retCode: {message.get('retCode')}")
    print(f"  retMsg: {message.get('retMsg')}")
    data = message.get("data", {})
    print(f"  orderId: {data.get('orderId')}")
    print(f"  orderLinkId: {data.get('orderLinkId')}")

print("=== Place Limit Order ===")
ws.place_order(
    handle_place_order,
    category="spot",
    symbol="BTCUSDT",
    side="Buy",
    orderType="Limit",
    qty="0.001",
    price="50000",
)

sleep(1)

# =============================================================================
# Batch place orders
# =============================================================================

def handle_batch_place(message):
    print(f"[Batch Place Response]")
    print(f"  retCode: {message.get('retCode')}")
    data = message.get("data", {})
    for item in data.get("list", []):
        print(f"  - orderId: {item.get('orderId')}, status: {item.get('retCode')}")

print("\n=== Batch Place Orders ===")
batch_request = [
    {
        "symbol": "BTCUSDT",
        "side": "Buy",
        "orderType": "Limit",
        "qty": "0.001",
        "price": "48000",
    },
    {
        "symbol": "BTCUSDT",
        "side": "Buy",
        "orderType": "Limit",
        "qty": "0.001",
        "price": "47000",
    },
]
ws.place_batch_order(handle_batch_place, category="spot", request=batch_request)

sleep(1)

# =============================================================================
# Amend order (requires orderId from place_order response)
# =============================================================================

def handle_amend_order(message):
    print(f"[Amend Order Response]")
    print(f"  retCode: {message.get('retCode')}")
    print(f"  retMsg: {message.get('retMsg')}")

# Uncomment and fill orderId to test
# print("\n=== Amend Order ===")
# ws.amend_order(
#     handle_amend_order,
#     category="spot",
#     symbol="BTCUSDT",
#     orderId="YOUR_ORDER_ID",
#     price="49000",
# )

# =============================================================================
# Cancel order
# =============================================================================

def handle_cancel_order(message):
    print(f"[Cancel Order Response]")
    print(f"  retCode: {message.get('retCode')}")
    print(f"  retMsg: {message.get('retMsg')}")

# Uncomment and fill orderId to test
# print("\n=== Cancel Order ===")
# ws.cancel_order(
#     handle_cancel_order,
#     category="spot",
#     symbol="BTCUSDT",
#     orderId="YOUR_ORDER_ID",
# )

# =============================================================================
# Keep connection alive for responses
# =============================================================================

print("\nWaiting for responses...")
sleep(3)

print("\nClosing connection...")
ws.exit()
print("Done.")
