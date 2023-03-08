import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("Jon", 50.00)
        self.customer2 = Customer("Rodger", 40.00)
        
    def test_have_names(self):
        self.assertEqual("Jon", self.customer1.name)
        self.assertEqual("Rodger", self.customer2.name)

    def test_have_money(self):
        self.assertEqual(50.00, self.customer1.wallet)
        self.assertEqual(40.00, self.customer2.wallet)




    