import unittest
import sys, os
sys.path.append(os.getcwd())
import transaction
import inventory

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.trans = transaction.Transaction()
        self.inv = inventory.Inventory()
        self.inv.add("caviar", 46.52, by_weight=True)
        self.inv.add("nutella", 7.99)
        self.inv.add("corn", 1.99, by_weight=True)
    
    def test_add_item_to_transaction_is_stored(self):
        self.trans.add(self.inv.read("corn"))
        self.trans.add(self.inv.read("caviar"))
        assertEqual(2, len(self.trans.items))