def format_inr(amount: float) -> str:
    """Format an amount in rupees, e.g. 1234567.5 -> "₹12,34,567.50"."""
    return f"₹{amount:,.2f}"
