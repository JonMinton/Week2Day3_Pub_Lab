import unittest
from src.drink import Drink
from src.pub import Pub
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Beer", 4.00)
        self.drink2 = Drink("Wine", 6.00)
        self.drink3 = Drink("Champagne", 12.00)
        self.drinks = [self.drink1, self.drink2, self.drink3]
        self.pub = Pub("Simpletons", 500.00, self.drinks)
        self.customer1 = Customer("Alice", 50)

    def test_has_name(self):
        self.assertEqual("Simpletons", self.pub.name)

    def test_pub_can_sell_a_drink(self):
        self.assertEqual(500.00, self.pub.till)
        self.pub.sell_drink(self.drink1, self.customer1)
        self.assertEqual(504.00, self.pub.till)
        self.pub.sell_drink(self.drink2, self.customer1)
        self.assertEqual(510.00, self.pub.till)



    

    

