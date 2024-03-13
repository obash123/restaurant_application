Loyalty Program class(it's a static class):
•	create a global variable
•	create a static method for the function
•	it needs the total cost which would be gotten from the order class
•	equate loyalty points to 0
•	if the total price is 1000 or greater add 5 points to the loyalty points
•	return loyalty points

Menu Item class:
•	create a constructor
•	instantiate parameters in the constructor
•	create a function that returns the price
•	create a function that returns the name
•	create a string function that returns the name, price, and quantity, using f string manipulation

Percentage Discount class(static class):
•	create a static method
•	equate percentage to 5
•	equate discounted_total to 0
•	if the total price is greater than 200 give a discounted price using 5% as the rate of discount

Order class:
•	request to call loyalty_program_class from loyalty_program
•	request to call Percentage_discount_class from percentage_discount
•	create an empty list 
•	create a function to append items to the list
•	create a function to remove items from the list
•	create a function to show what's in the list: this is done by looping through the list and printing out item names, prices, and quantity.
•	create a function to calculate the total cost: 
•	equate the total cost to 0
•	loop through the list, to add (price * quantity) to the total cost
•	create variables for the objects of the loyalty_program_class and Percentage_discount_class that were imported earlier
•	return total cost, loyalty points, and the discounted price using f string manipulation 

Project 1:
•	request to call order_class from order
•	request to call menu_item_class from menu_item
•	create a dictionary containing items and their prices
•	print the dictionary
•	create an empty list to append customer orders into
•	create a while loop that asks for the item the user wants, then asks for the quantity they want till the exit is entered.
•	make the quantity the value of the empty dictionary and the item the key to the dictionary
•	create a for loop to add the items being inputted by the user into the empty dictionary
•	create a try-and-catch function to account for errors in the inputs 
•	create an object of order class that has been imported 
•	print the object

