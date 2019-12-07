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
        self.trans.add(self.inv, "corn", 3)
        self.trans.add(self.inv, "caviar", 41)
        self.trans.add(self.inv, "nutella")
    
    def test_add_item_to_transaction_is_stored(self):
        # self.trans.add(self.inv, "corn", 3)
        # self.trans.add(self.inv, "caviar", 41)
        self.assertEqual(3, len(self.trans.items))
        
    def test_add_item_tracks_quantity(self):
        # self.trans.add(self.inv, "corn", 842)
        self.assertEqual(1, self.trans.items["nutella"]["quant"])
    
    def test_remove_item_from_transaction(self):
        self.trans.delete("corn")
        items = self.trans.items
        self.assertIsNone(items.get("corn"))
        self.assertEqual(2, len(items))
        
    def test_retrieve_total_without_discounts(self):
        total = self.trans.get_total()
        self.assertEqual(1921.28, total)
        