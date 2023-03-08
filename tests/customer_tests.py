import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Beer", 4.00)
        self.drink2 = Drink("Wine", 6.00)
        self.drink3 = Drink("Champagne", 12.00)
        self.drinks = [self.drink1, self.drink2, self.drink3]
        self.pub = Pub("Simpletons", 500.00, self.drinks)
        self.customer1 = Customer("Jon", 50.00)
        self.customer2 = Customer("Rodger", 40.00)
        
    def test_have_names(self):
        self.assertEqual("Jon", self.customer1.name)
        self.assertEqual("Rodger", self.customer2.name)

    def test_have_money(self):
        self.assertEqual(50.00, self.customer1.wallet)
        self.assertEqual(40.00, self.customer2.wallet)

    def test_can_buy_drink(self):
        self.assertEqual(500.00, self.pub.till)
        self.assertEqual(50.00, self.customer1.wallet)
        self.customer1.buy_a_drink(self.pub, self.drink2)
        self.assertEqual(44.00, self.customer1.wallet)
        self.assertEqual(506.00, self.pub.till)
        




    