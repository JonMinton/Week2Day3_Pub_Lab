import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Beer", 4.00)
        self.drink2 = Drink("Wine", 6.00)

    def test_beer_is_beer(self):
        self.assertEqual("Beer", self.drink1.name)

    def test_wine_is_wine(self):
        self.assertEqual("Wine", self.drink2.name)

    
