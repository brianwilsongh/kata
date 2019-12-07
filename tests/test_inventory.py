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

if __name__ == '__main__':
    unittest.main()