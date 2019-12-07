import unittest
import sys, os
sys.path.append(os.getcwd())
import inventory

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inv = inventory.Inventory()

    def test_add_item_to_inventory_is_stored(self):
        self.inv.add("ground beef", 3.99)
        self.assertEqual(1, len(self.inv._store))
    
    def test_get_price_data_of_added_item(self):
        self.inv.add("potato", 1.05)
        potato_data = self.inv.read("potato")
        self.assertIsNotNone(potato_data)
        self.assertIsInstance(potato_data["price"], float)
        
    def test_added_item_priced_by_unit(self):
        self.inv.add("milk", 2.97)
        milk_data = self.inv.read("milk")
        self.assertEqual(False, milk_data["by_weight"])
    
    def test_added_item_priced_by_weight(self):
        self.inv.add("peanuts", 3.50, by_weight=True)
        peanut_data = self.inv.read("peanuts")
        self.assertEqual(True, peanut_data["by_weight"])
    
    def test_delete_item(self):
        self.inv.add("tomato", 2.99, by_weight=True)
        self.inv.delete("tomato")
        self.assertEqual(None, self.inv.read("tomato"))
    
    def test_update_item(self):
        self.inv.add("coffee beans", 6.99, by_weight=True)
        self.inv.modify("coffee beans", 7.99, by_weight=True)
        coffee_data = self.inv.read("coffee beans")
        self.assertEqual(7.99, coffee_data["price"])
        self.inv.modify("coffee beans", 7.99, by_weight=False)
        coffee_data = self.inv.read("coffee beans")
        self.assertFalse(coffee_data["by_weight"])
if __name__ == '__main__':
    unittest.main()