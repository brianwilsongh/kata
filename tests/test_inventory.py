import unittest
import sys, os
sys.path.append(os.getcwd())
import inventory

class TestInventory(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('abc'.upper(), 'ABC')

    def test_add_item_to_inventory(self):
        inv = inventory.Inventory()
        inv.add("ground beef")
        self.assertEqual(0, len(inv._store))

if __name__ == '__main__':
    unittest.main()