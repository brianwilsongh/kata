

class Inventory:
    def __init__(self):
        print("Initiatilizing inventory")
        self._store = {}
        
    def add(self, id):
        self._store[id] = {}
        return None