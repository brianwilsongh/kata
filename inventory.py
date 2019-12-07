

class Inventory:
    def __init__(self):
        print("Initiatilizing inventory")
        self._store = {}
        
    def add(self, id, price, by_weight=False):
        self._store[id] = {
            "price": price,
            "by_weight": by_weight
        }
        return None
    
    def read(self, id):
        return self._store[id]