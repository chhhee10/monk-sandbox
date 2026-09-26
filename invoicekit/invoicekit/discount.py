def apply_discount(total: float, percent: float) -> float:
    """Take a percentage off a total, e.g. apply_discount(200, 10) -> 180.0."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(total * (1 - percent / 100), 2)
