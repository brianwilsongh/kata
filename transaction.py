class Transaction:
    def __init__(self):
        self.items = {}
    
    def add(self, inventory, id, quant):
        item_data = inventory.read(id)
        self.items[id] = {**{'quant': quant}, **item_data}
        