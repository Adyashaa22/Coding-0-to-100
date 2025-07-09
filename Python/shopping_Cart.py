import math
print("Welcome to the Shopping Cart Program!")
print("Please enter the details of the item you want to purchase.")
item= input("Enter the item name: ")
quantity = int(input("Enter the quantity: "))
price = float(input("Enter the price per item: "))
total_price = quantity * price
print("Shopping Cart Summary:")
print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Your Total Price: {total_price}")
print("Thank you for shopping with us!")