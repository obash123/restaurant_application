from Orderclass import Order
from menuitemclass import MenuItem

food_items = {"cocktails":20,"salad":5,"soup":15,"meats":70,"pizza":5,"pasta":15,"baked":10,"frozen":20,"drinks":30}
print (food_items)

customer_orders = {}

while True:
    customer_order = input("what would you like to order(press s to stop): ")
    if customer_order == 's':
        break
    quantity = (input("how many would you like to order: "))
    customer_orders[customer_order] = quantity 

order = Order()

try:
    for cus_order in customer_orders:
        cus_menu_item = MenuItem(cus_order, food_items[cus_order], customer_orders[cus_order])
        order.add_item(cus_menu_item)
except Exception as error:
    print(f"an error occured: {error}")

total_cost = order.calculate_total_cost()
print(total_cost)


'''
loyalty program, if total amount > 1000 and < 2000 give them 5 points, 
so for every thousand dollars increment by 5 dollars.
if points is worth an amount of goods you'll let them buy goods 
then remove points 
'''