import unittest
from src.drink import Drink
from src.pub import Pub

class TestPub(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Beer", 4.00)
        self.drink2 = Drink("Wine", 6.00)
        self.drink3 = Drink("Champagne", 12.00)
        self.drinks = [self.drink1, self.drink2, self.drink3]
        self.pub = Pub("Simpletons", 500.00, self.drinks)

    def test_has_name(self):
        self.assertEqual("Simpletons", self.pub.name)

    

    

