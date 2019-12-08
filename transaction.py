class Transaction:
    def __init__(self):
        self.items = {}
    
    def add(self, inventory, id, quant=1):
        item_data = inventory.read(id)
        self.items[id] = {**{'quant': quant}, **item_data}
    
    def delete(self, id):
        self.items.pop(id)
    
    def get_total(self, discount):
        total = 0
        for item, data in self.items.items():
            transaction_quant = data['quant']
            after_quantified = discount.apply_quantified(item, transaction_quant)
            if after_quantified:
                total += after_quantified[0]
                transaction_quant = after_quantified[1]
            for x in range(transaction_quant): #prevent rounding issues with huge quantities
                after_markdown = discount.apply_markdown_price(item, data['price'])
                after_vol_markdown = discount.apply_volume_markdown_price(item, after_markdown)
                total += after_vol_markdown
        return float(format(total, ".2f"))