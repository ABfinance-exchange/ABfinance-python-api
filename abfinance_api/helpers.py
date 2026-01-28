# Helper functions for spot trading


def opposite_side(side: str) -> str:
    """Get the opposite side of a trade.

    Args:
        side: "Buy" or "Sell"

    Returns:
        The opposite side.
    """
    if side == "Buy":
        return "Sell"
    return "Buy"
