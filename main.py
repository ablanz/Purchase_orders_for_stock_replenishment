from item import Item, Discount
from supplier import Supplier, Combo
from functools import cmp_to_key
from datetime import datetime, timedelta
from flask import Flask, jsonify, request, render_template
from utils import s1, s2 



suppliers: list[Supplier] = []
now = datetime.now()
trial_suppliers = [s1, s2]

def comp(x:Combo, y:Combo):
    if x.item.calculate_total_price(x.quantity) < y.item.calculate_total_price(y.quantity):
        return -1
    
    elif x.item.calculate_total_price(x.quantity) > y.item.calculate_total_price(y.quantity):
        return 1
    
    else:
        if x.item.delivery_date < y.item.delivery_date:
            return -1
        
        elif x.item.delivery_date > y.item.delivery_date:
            return 1
        else:
            return 0
    
def find_cheapest_supplier(item_name:str, quant: int, suppliers=suppliers)-> list[Combo]:
    mylist = []
    for supplier in suppliers:
        sup_list = supplier.search_item_byname(item_name)
        for item in sup_list:
         if item.stock >= quant:
          mylist.append(Combo(item, quant, supplier))
    return sorted(mylist, key=cmp_to_key(comp))

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        item_name = request.form['item_name']
        quant = int(request.form['quantity'])

        combos = find_cheapest_supplier(item_name, quant, suppliers=trial_suppliers)
        results = []
        for combo in combos:
            results.append({
                'supplier': combo.supplier.name,
                'item': combo.item.name,
                'price': combo.item.calculate_total_price(combo.quantity),
                'delivery_days': combo.item.calculate_delivery_days()+1,
                'delivery_date': combo.item.delivery_date.strftime('%Y-%m-%d')
            })

        return jsonify(results)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
