

class Inventory:
    def __init__(self):
        print("Initiatilizing inventory")
        self._store = {}
        
    def add(self, id, price):
        self._store[id] = {
            'price': price
        }
        return None
    
    def read(self, id):
        return self._store[id]