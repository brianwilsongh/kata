

class Inventory:
    def __init__(self):
        print("Initiatilizing inventory")
        self._store = None
        
    def add(self, id):
        if not self._store:
            self._store = {}
        return None