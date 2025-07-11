#credit card information
credit_card = input("Enter your credit card number:")
# Check if the credit card number is valid
if len(credit_card) == 12 and credit_card.isdigit():
    last_digit = int(credit_card[-4:])
    print("Credit card number is valid.")
    print(f"Credit card number: XXXX-XXXX-{last_digit}")
else:
    print("Credit card number is invalid.") 

#format specifier exercises
price1 = input("Enter the first price: ")
price1 = float(price1)  # Convert input to float for calculations
price2 = input("Enter the second price: ")
price2 = float(price2)  # Convert input to float for calculations
price3 = input("Enter the third price: ")
price3 = float(price3)  # Convert input to float for calculations
total_price = price1 + price2 + price3
print(f" {price1: >11.2f} \n {price2:>11.2f} \n+{price3:>11.2f} \n------------\n={total_price:>11.2f}")
print(f" {price1:=11.2f} \n {price2:=11.2f} \n+{price3:=11.2f} \n------------\n={total_price:=11.2f}")
print(f" {price1:>11,.2f} \n {price2:>11,.2f} \n+{price3:>11,.2f} \n------------\n={total_price:>11,.2f}")

#while loop exercises
name= input("Enter your name: ")
if name == "":
    print("You didn't enter your name.")
else:
    print(f"Hello, {name}!")
#name validation exercise    
name= input("Enter your name: ")
while name == "":
    print("You didn't enter your name.")
    name = input("Please enter your name: ")
print(f"Hello, {name}!")

# age validation exercise
age = int(input("Enter your age: "))
while age < 0:
    print("Age cannot be negative. Please enter a valid age.")
    age = int(input("Please enter your age: "))
print(f"You are {age} years old.")

#favorite food excercise

food= input("Enter your favorite food (q to quit): ")
while food != "q":
    print(f"Your favorite food is {food}.")
    food = input("Enter your other favorite food (q to quit): ")
print("Thank you for sharing your favorite foods!")

# Number validation exercise

number = int(input("Enter a number between 0 to 10: "))
while number >10 or number<0:
    print(f"{number} is not between 0 to 10. Please try again.")
    number = int(input("Enter a number between 0 to 10: "))
print(f"You entered a valid number: {number}")


#compound interest calculation exercise

principle= 0
rate=0
time=0
while principle <= 0:
    principle = float(input("Enter the principal amount (greater than 0): "))
    if principle <= 0:
        print("Principal amount must be greater than 0. Please try again.")
while rate <= 0:
    rate = float(input("Enter the rate of interest (greater than 0): "))
    if rate <= 0:
        print("Rate of interest must be greater than 0. Please try again.")
while time <= 0:
    time = float(input("Enter the time period in years (greater than 0): "))
    if time <= 0:
        print("Time period must be greater than 0. Please try again.")
compound_interest = principle * (1 + rate / 100) ** time
print(f"The compound interest for the given inputs is: {compound_interest:.2f}")
# Display the final amount after compound interest
final_amount = principle * (1 + rate / 100) ** time
print(f"The final amount after {time} years is: {final_amount:.2f}")
# Display the total interest earned
total_interest = final_amount - principle
print(f"The total interest earned over {time} years is: {total_interest:.2f}")
# Display the breakdown of the calculation
print(f"Calculation Breakdown:")
print(f"Principal Amount: {principle:.2f}")
print(f"Rate of Interest: {rate:.2f}%")
print(f"Time Period: {time:.2f} years")
# Display the formula used for compound interest calculation
print(f"Compound Interest Formula: A = P(1 + r/n)^(nt)")
# where:
print(f"A = Final Amount")
print(f"P = Principal Amount")
print(f"r = Rate of Interest (as a decimal)")
print(f"n = Number of times interest is compounded per year (assumed to be 1 for this calculation)")
print(f"t = Time Period in years")
# Display the final amount using the formula
print(f"Final Amount Calculation: A = {principle:.2f}(1 + {rate / 100:.2f})^{time:.2f}")
print(f"Final Amount: {final_amount:.2f}")