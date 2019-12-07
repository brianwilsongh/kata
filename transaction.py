class Transaction:
    def __init__(self):
        self.items = {}
    
    def add(self, inventory, id, quant=1):
        item_data = inventory.read(id)
        self.items[id] = {**{'quant': quant}, **item_data}
    
    def delete(self, id):
        self.items.pop(id)
    
    def get_total(self):
        total = 0