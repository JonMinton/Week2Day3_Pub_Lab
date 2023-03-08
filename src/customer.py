from src.pub import Pub
from src.drink import Drink

class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    
    def buy_a_drink(self, pub, drink):
        pub.sell_drink(drink, self)
        self.wallet -= drink.price