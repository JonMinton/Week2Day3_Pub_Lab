from src.pub import Pub

class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    
    def buy_a_drink(self, drink_name, pub):
        