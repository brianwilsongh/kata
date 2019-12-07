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
        self.trans.add(self.inv, "corn", 3)
        self.trans.add(self.inv, "caviar", 41)
        self.assertEqual(2, len(self.trans.items))
        
    def test_add_item_tracks_quantity(self):
        self.trans.add(self.inv, "corn", 842)
        self.assertEqual(842, self.trans.items["corn"]["quant"])
        