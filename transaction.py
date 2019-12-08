class Transaction:
    def __init__(self):
        self.items = {}
    
    def add(self, inventory, id, quant=1):
        item_data = inventory.read(id)
        self.items[id] = {**{'quant': quant}, **item_data}
    
    def delete(self, id):
        self.items.pop(id)
    
    def get_total(self, inventory, discount):
        total = 0
        weighted_item_memo = {'items': {}, 'active_discounts': []}
        for item, data in self.items.items():
            #TODO: determine order of discount applicaiton, i.e. should quantified discounts come before weighted?
            transaction_quant = data['quant']
            after_quantified = discount.apply_quantified(item, transaction_quant)
            if after_quantified:
                total += after_quantified[0]
                transaction_quant = after_quantified[1]
            for x in range(transaction_quant): #prevent rounding issues with huge quantities
                price = discount.apply_markdown_price(item, data['price'])
                price = discount.apply_volume_markdown_price(item, price)
                if inventory.read(item)["by_weight"]:
                    result = discount.apply_weighted(weighted_item_memo, item, price)
                    weighted_item_memo = result[0]
                    price = result[1]
                total += price
        return float(format(total, ".2f"))