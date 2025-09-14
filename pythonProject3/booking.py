# booking.py

def calculate_price(nights: int, price_per_night: float) -> float:
    """Return total cost of the stay."""
    if nights <= 0:
        raise ValueError("Number of nights must be positive")
    return nights * price_per_night

def apply_discount(total: float, percent: float) -> float:
    """Apply a discount percentage (0–100)."""
    if not (0 <= percent <= 100):
        raise ValueError("Discount percent must be between 0 and 100")
    return total * (1 - percent / 100)
