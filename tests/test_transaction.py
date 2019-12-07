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
        self.trans.add(self.inv, "nutella", 842)
    
    def test_add_item_to_transaction_is_stored(self):
        # self.trans.add(self.inv, "corn", 3)
        # self.trans.add(self.inv, "caviar", 41)
        self.assertEqual(3, len(self.trans.items))
        
    def test_add_item_tracks_quantity(self):
        # self.trans.add(self.inv, "corn", 842)
        self.assertEqual(842, self.trans.items["nutella"]["quant"])
    
    def test_remove_item_from_transaction(self):
        self.trans.delete("corn")
        self.assertIsNone(self.items.get("corn"))
        self.assertEquals(2, len(self.items("corn")))
        