class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
    

    def sell_drink(self, drink, customer):
        if drink.price <= customer.wallet:
            self.till += drink.price
