class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.max_drunkenness = 25
    

    def sell_drink(self, drink, customer):
        self.till += drink.price
