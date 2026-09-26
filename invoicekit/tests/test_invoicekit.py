import unittest

from invoicekit import Invoice, Line, apply_discount, format_inr, split_bill


class MoneyTest(unittest.TestCase):
    def test_small_amount(self):
        self.assertEqual(format_inr(250), "₹250.00")


class SplitTest(unittest.TestCase):
    def test_even_split(self):
        self.assertEqual(split_bill(90, 3), [30.0, 30.0, 30.0])

    def test_uneven_split_preserves_total(self):
        shares = split_bill(100, 3)
        self.assertEqual(shares, [33.34, 33.33, 33.33])
        self.assertEqual(sum(shares), 100.0)

    def test_split_distributes_multiple_remainder_paise(self):
        shares = split_bill(10, 6)
        self.assertEqual(shares, [1.67, 1.67, 1.67, 1.67, 1.66, 1.66])
        self.assertEqual(sum(shares), 10.0)

    def test_rejects_nobody(self):
        with self.assertRaises(ValueError):
            split_bill(90, 0)


class DiscountTest(unittest.TestCase):
    def test_ten_percent(self):
        self.assertEqual(apply_discount(200, 10), 180.0)

    def test_rejects_percent_over_100(self):
        with self.assertRaises(ValueError):
            apply_discount(200, 150)

    def test_rejects_negative_percent(self):
        with self.assertRaises(ValueError):
            apply_discount(200, -1)

    def test_accepts_zero_and_100_percent(self):
        self.assertEqual(apply_discount(200, 0), 200.0)
        self.assertEqual(apply_discount(200, 100), 0.0)


class InvoiceTest(unittest.TestCase):
    def test_subtotal(self):
        inv = Invoice([Line("Notebook", 2, 45.0), Line("Pen", 3, 10.0)])
        self.assertEqual(inv.subtotal(), 120.0)

    def test_total_without_discount(self):
        inv = Invoice([Line("Notebook", 2, 50.0)])
        self.assertEqual(inv.total(), 118.0)


if __name__ == "__main__":
    unittest.main()
