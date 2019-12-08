import unittest
import sys, os
sys.path.append(os.getcwd())
import transaction
import inventory
import discount

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.trans = transaction.Transaction()
        self.inv = inventory.Inventory()
        self.disc = discount.Discount()
        self.inv.add("caviar", 46.52, by_weight=True)
        self.inv.add("nutella", 7.99)
        self.inv.add("corn", 1.99, by_weight=True)
        self.trans.add(self.inv, "corn", 3)
        self.trans.add(self.inv, "caviar", 41)
        self.trans.add(self.inv, "nutella")
    
    def test_add_item_to_transaction_is_stored(self):
        self.assertEqual(3, len(self.trans.items))
        
    def test_add_item_tracks_quantity(self):
        self.assertEqual(1, self.trans.items["nutella"]["quant"])
    
    def test_remove_item_from_transaction(self):
        self.trans.delete("corn")
        items = self.trans.items
        self.assertIsNone(items.get("corn"))
        self.assertEqual(2, len(items))
        
    def test_retrieve_total_without_discounts(self):
        total = self.trans.get_total(self.disc)
        self.assertEqual(1921.28, total)
    
    def test_retrieve_total_with_markdown(self):
        self.disc.add_markdown("corn", 10)
        total = self.trans.get_total(self.disc)
        self.assertEqual(1920.68, total)
    
    def test_buy_x_triggers_markdown(self):
        self.disc.add_volume_markdown("caviar", 1, 50)
        total = self.trans.get_total(self.disc)
        self.assertEqual(990.88, total)
    
    def test_transaction_triggers_x_for_y_promo(self):
        self.disc.add_quantified("corn", 3, 2.50)
        total = self.trans.get_total(self.disc)
        self.assertEqual(1917.81, total)
        
    def test_transaction_triggers_x_for_y_promo_multiple_times(self):
        self.inv.add("apple", 5.00)
        self.trans.add(self.inv, "apple", 10)
        self.disc.add_quantified("apple", 2, 0.20)
        total = self.trans.get_total(self.disc)
        self.assertEqual(1922.28, total)
    
    def test_transaction_x_for_y_obeys_limit(self):
        self.inv.add("apple", 5.00)
        self.trans.add(self.inv, "apple", 20)
        self.disc.add_quantified("apple", 2, 1.00, limit=6)
        total = self.trans.get_total(self.disc)
        self.assertEqual(1967.28, total)
        
    def test_weighted_discount_applies_to_own_item_type(self):
        self.inv.add("apple", 1.00, by_weight=True)
        self.trans.add(self.inv, "apple", 20)
        self.disc.add_weighted("corn", 2, 1, 75) #third weight unit of corn will be 75% off
        total = self.trans.get_total(self.disc)
        self.assertEqual(1940.78, total)
        
    def test_weighted_discount_applies_to_cheaper_item_type(self):
        self.inv.add("apple", 1.00, by_weight=True)
        self.trans.add(self.inv, "apple", 20)
        self.disc.add_weighted("corn", 3, 10, 50) #corn weight discount should transfer to apples
        total = self.trans.get_total(self.disc)
        self.assertEqual(1936.28, total)
        
        