# GST slabs in percent.
RATES = {"exempt": 0, "essential": 5, "standard": 18, "luxury": 28}


def gst(amount: float, category: str = "standard") -> float:
    """GST on an amount for a category, rounded to paise."""
    if category not in {"exempt": 0, "essential": 5, "standard": 18, "luxury": 28}:
        raise ValueError(f"unknown GST category: {category}")
    return round(amount * RATES[category] / 100, 2)
