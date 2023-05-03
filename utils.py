from datetime import datetime, timedelta
from item import Item, Discount
from supplier import Supplier, Combo

now = datetime.now()
d1 = Discount(0.1, 10)
d2 = Discount(0.15, 15)
d3 = Discount(0.05, interval=(now - timedelta(days=30), now+timedelta(days=30)))

iphone1 = Item("Iphone 13", 650, now+timedelta(days=5), 50, [d1, d3])
iphone2 = Item("Iphone 13", 660, now+timedelta(days=4), 55, [d3])

sg1 = Item("Samsung Galaxy S21", 700, now+timedelta(days=10), 30, [d1, d2])
sg2 = Item("Samsung Galaxy S21", 680, now+timedelta(days=15), 40, [d1, d3])

s1 = Supplier("Euronics")
s1.items = [iphone1, sg1]
s2 = Supplier("Mediaworld")
s2.items = [iphone2, sg2]
