#Shopping Cart Program

foods=[]
price=[]
total=0

print("Welcome to your Shopping Cart!")
# print("Enter the food item you want to buy (type 'q' to quit): ")
while True:
    food=input("Food item: ")
    if food=='q':
        break
    else:
        foods.append(food)
        price.append(float(input(f"Enter the Price of {food}: $")))
        print(f"{food} added to your cart.")
        
print("-------YOUR CART-------");
for food in foods:
       print(food, end=' ')
for price in price:
       total += price
print(f"Total price: ${total:.2f}")
print("Thank you for shopping with us!")