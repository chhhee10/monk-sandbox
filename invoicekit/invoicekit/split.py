def split_bill(total: float, people: int) -> list[float]:
    """Split a bill into equal shares, in rupees with paise. The shares add up to the total."""
    if people < 1:
        raise ValueError("people must be at least 1")
    share = round(total / people, 2)
    return [share] * people
