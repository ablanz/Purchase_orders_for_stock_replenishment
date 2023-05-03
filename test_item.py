from item import Item, Discount
from supplier import Supplier
from datetime import datetime, timedelta
import unittest

class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = Item("Test Item", 10.0, datetime.now()+timedelta(days=5), 10)

    def test_calculate_total_price_no_discount(self):
        # Test that the total price is correct when there are no discounts
        total_price = self.item.calculate_total_price(5)
        self.assertEqual(total_price, 50.0)

    def test_calculate_total_price_discount(self):
        # Test that the total price is correct when a discount is applied
        discount = Discount(percentage=0.1, quantity=3)
        self.item.discounts = [discount]
        total_price = self.item.calculate_total_price(5)
        self.assertEqual(total_price, 45.0)

    def test_calculate_total_price_multiple_discounts(self):
        # Test that the total price is correct when multiple discounts are applied
        discount1 = Discount(percentage=0.1, quantity=3)
        discount2 = Discount(percentage=0.2, quantity=5)
        self.item.discounts = [discount1, discount2]
        total_price = self.item.calculate_total_price(7)
        self.assertEqual(total_price, 56.0)

    def test_calculate_delivery_days(self):
        self.assertEqual(self.item.calculate_delivery_days(), 5)    

class TestDiscount(unittest.TestCase):
    def setUp(self):
        self.discount = Discount(0.15, quantity=5, value=50, interval=(datetime.now(), datetime.now() + timedelta(days=7)))  # 15% discount for quantity >= 5 during the next 7 days

    def test_discount(self):
        item = Item("Test Item", 10.0, timedelta(days=1), 50, discounts=[self.discount])
        discounted_price = item.calculate_total_price(40)
        self.assertEqual(discounted_price, 340.0)
   


if __name__ == '__main__':
    unittest.main()    