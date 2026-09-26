from dataclasses import dataclass, field

from .discount import apply_discount


@dataclass
class Line:
    item: str
    qty: int
    unit_price: float

    @property
    def amount(self) -> float:
        return round(self.qty * self.unit_price, 2)


@dataclass
class Invoice:
    lines: list[Line] = field(default_factory=list)
    discount_percent: float = 0
    gst_category: str = "standard"

    def subtotal(self) -> float:
        return round(sum(line.amount for line in self.lines), 2)

    def tax(self) -> float:
        # GST slabs in percent.
        rate = {"exempt": 0, "essential": 5, "standard": 18, "luxury": 28}[self.gst_category]
        return round(self.subtotal() * rate / 100, 2)

    def total(self) -> float:
        return round(apply_discount(self.subtotal(), self.discount_percent) + self.tax(), 2)
