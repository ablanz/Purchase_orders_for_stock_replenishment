from item import Item, Discount
from supplier import Supplier, Combo
from datetime import datetime, timedelta
from main import comp, find_cheapest_supplier
import unittest

class TestFuncs(unittest.TestCase):
    def test_find_cheapest_supplier(self):
        
        discount1 = Discount(0.1)
        item1 = Item("Test Item", 10.0, timedelta(days=10), 9, discounts=[discount1])
        item2 = Item("Test Item", 10.0, timedelta(days=6), 10)
        item3 = Item("Test Item", 10.0, timedelta(days=5), 10)
        supplier1 = Supplier('Supplier1')
        supplier1.items = [item1, item2]
        supplier2 = Supplier('Supplier2')
        supplier2.items = [item3]
        mylist = find_cheapest_supplier('Test Item', 5, [supplier1, supplier2])
        self.assertEqual(mylist[0].item, item1)
        self.assertEqual(mylist[1].item, item3)
        self.assertEqual(mylist[2].item, item2)
   


if __name__ == '__main__':
    unittest.main()