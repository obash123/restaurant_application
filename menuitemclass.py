class MenuItem:
    def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def item_name(self):
        return self.name

    def item_price(self):
        return self.price
    
    def __str__(self) -> str:
        return f'{self.name}, {self.price}, {self.quantity}'
    
