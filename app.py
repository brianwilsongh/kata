import argparse
import unittest
import inventory
import discount
import transaction

class App:
    
    def __init__(self):
        print("App initiated!")

    def run(self):
        print("Running Application!")
        #in here we will initiate required object, accept scanned items, display total
        self.inv = inventory.Inventory()
        self.inv.add("beef", 3.99, by_weight=True)
        self.inv.add("milk", 2.99)
        self.inv.add("carrot", 1.99, by_weight=True)
        self.inv.add("cashew", 6.99, by_weight=True)
        self.inv.delete("cashew")
        self.inv.modify("beef", 4.99, by_weight=True)
        
        self.disc = discount.Discount()
        self.disc.add_markdown("milk", 5)
        
        self.trans = transaction.Transaction()
        self.trans.add(self.inv, "beef", 3)
        self.trans.add(self.inv, "carrot", 21)
        
        print("that will be: " + str(self.trans.get_total(self.inv, self.disc)))
        

if __name__ == "__main__":
    app = App()
    app.run()