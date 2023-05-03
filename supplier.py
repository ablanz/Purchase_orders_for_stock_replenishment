from item import Item, Discount

class Supplier:
    def __init__(self, name):
          self.name = name
          self.items: list[Item] = []


    def search_item_byname(self, filter: str) -> list[Item]:
            mylist = []
            for item in self.items:
                  if filter.lower() in item.name.lower():
                        mylist.append(item)
            return mylist            

class Combo:
      def __init__(self, item: Item = None, quantity: int = None, supplier: Supplier = None):
            self.item = item
            self.quantity = quantity
            self.supplier = supplier
            
      def __str__(self) -> str:
             return f"""
             Oggetto: {self.item.name}
             Quantità: {self.quantity}
             Supplier: {self.supplier.name}
             Costo: {str(self.item.calculate_total_price(self.quantity))}"""     
