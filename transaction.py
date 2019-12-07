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
            for x in range(data['quant']): #prevent rounding issues with huge quantities
                after_markdown = discount.apply_markdown_price(item, data['price'])
                total += after_markdown
        return float(format(total, ".2f"))