class PercentageDiscount:
   
    @staticmethod
    def apply_discount(total_cost):
        percentage = 5
        discounted_total = 0
        if total_cost >= 200:
            discount_amount = (percentage / 100) * total_cost
            discounted_total += total_cost - discount_amount
        return discounted_total