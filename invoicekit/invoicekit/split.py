def split_bill(total: float, people: int) -> list[float]:
    """Split a bill into equal shares, in rupees with paise. The shares add up to the total."""
    if people < 1:
        raise ValueError("people must be at least 1")

    # Work in paise so rounding is done once and the remainder is assigned
    # deterministically to the first shares.
    total_paise = round(total * 100)
    base_share, remainder = divmod(total_paise, people)
    return [
        (base_share + (1 if index < remainder else 0)) / 100
        for index in range(people)
    ]
