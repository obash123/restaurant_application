from loyaltyprogramclass import LoyaltyProgram
from PercentageDiscountclass import PercentageDiscount

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def show_order(self):
        for item in self.items:
            print(f"{item.name} \t\t ${item.price} \t\t x{item.quantity}")

    def calculate_total_cost(self):
        total_cost = 0
        for item in self.items:
            total_cost += (item.price * int(item.quantity))
        loyalty_points = LoyaltyProgram.loyalty_points(total_cost)
        discount = PercentageDiscount.apply_discount(total_cost)
        return (f"total: ${total_cost} \n loyalty points: {loyalty_points} \n discount price: {discount}")