import unittest
import sys, os
sys.path.append(os.getcwd())
import discount

class TestDiscount(unittest.TestCase):
    def setUp(self):
        disc = discount.Discount()
    
    def test_adding_discount_is_stored(self):
        discount = {"type": "Markdown", "id": "corn", "pct": 25}
        disc.add(discount)
        self.assertEqual(1, len(disc.discounts))