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
        
    def test_adding_volume_markdown_discount_is_stored(self):
        self.disc.add_volume_markdown("corn", 5, 1.50)
        self.assertEqual(1, len(self.disc.volume_markdowns))
        
    def test_adding_quantified_discount_is_stored(self):
        self.disc.add_quantified("corn", 3, 1.00)
        self.assertEqual(1, len(self.disc.quantified))
        
    def test_adding_volume_markdown_discount_is_stored(self):
        self.disc.add_volume_markdown("corn", 5, 25)
        self.assertEqual(1, len(self.disc.volume_markdowns))
    
    def test_retrieve_markdown_for_item(self):
        self.disc.add_markdown("carrot", 95)
        self.assertEqual(95, self.disc.get_markdown("carrot"))
    
    def test_retrieve_markdown_price_for_item(self):
        self.disc.add_markdown("carrot", 95)
        self.disc.add_markdown("beets", 23)
        self.assertEqual(0.50, self.disc.apply_markdown_price("carrot", 10.00))
        self.assertEqual(1804.11, self.disc.apply_markdown_price("beets", 2343))