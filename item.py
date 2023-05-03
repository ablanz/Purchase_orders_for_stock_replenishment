from datetime import datetime, timedelta


class Discount:
    def __init__(self, percentage: float, quantity: int = 0, value: float = 0, interval: tuple[datetime, datetime] = None):
             self.quantity = quantity
             self.percentage = percentage
             self.value = value
             self.interval = interval #Costituito da una tupla di 2 oggetti di tipo datetime, il primo rappresenta la data di inizio sconto, la seconda la data di fine sconto

    def is_applicable(self, price, quant):
                  #Ritorna True se lo sconto è applicabile in base alla quantità di oggetti da ordinare, altrimenti False
                  return quant >= self.quantity and price*quant >= self.value and(self.interval is None or self.interval[0] <= datetime.now() <= self.interval[1])
    

class Item:
    def __init__(self, name: str, price: float, delivery_date: datetime, stock: int, discounts: list[Discount] = []):
        self.name = name
        self.price = price
        self.stock = stock
        self.discounts = discounts
        self.delivery_date = delivery_date

    def calculate_total_price(self, quant:int):
         #Confronta i prezzi di tutti gli sconti applicabili per la quantità desiderata e ritorna il più basso
         prices = [self.price*quant]
         for discount in self.discounts:
              if discount.is_applicable(self.price, quant):
                    prices.append((self.price*(1-discount.percentage)*quant))
         return min(prices)
    
    def  calculate_delivery_days(self):
          #Calcola i giorni che ci impiega la spedizione ad arrivare
          return (self.delivery_date-datetime.now()).days
    
    def __str__(self) -> str:
          return f"""
          Nome articolo: {self.name}
          Disponibilità: {self.stock}
          Prezzo: {self.price}
          Giorni di consegna: {(self.delivery_date-datetime.now()).days}"""