import unittest
import sys, os
sys.path.append(os.getcwd())
import discount

class TestDiscount(unittest.TestCase):
    def setUp(self):
        self.disc = discount.Discount()
    
    def test_adding_markdown_discount_is_stored(self):
        self.disc.add_markdown("corn", 25)
        self.assertEqual(1, len(self.disc.markdowns))