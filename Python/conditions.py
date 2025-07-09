# online = False
# if online:
#     print("You are online")
# else:
#     print("You are offline")
# # Check if the user is online or offline
# # Check if the user is an admin
# is_admin = True
# if is_admin:
#     print("You have admin privileges")
# else:
#     print("You do not have admin privileges")
# # Check if the user is a guest
# is_guest = check_guest = False  # Assuming a function or condition to check if the user is a guest
# if is_guest:
#     print("You are a guest user")
# else:
#     print("You are not a guest user")
#Python weight conversion program
weight = float(input("Enter your weight: "))  # Input weight in kilograms
unit = input("Enter the unit to convert to (Pounds or Kilograms): ").strip().lower()  # Input unit for conversion
print(f"Your weight is: {weight}  and you to convert it into { "pounds" if unit == "p" else "kilograms" } ")
#yes/no
print("Is that right? (yes/no)")
response = input().strip().lower()  # Input response from the user
if response == "yes" or response == "y":
    print("Great! Let's proceed with the conversion.")
else:
    print("Please restart the program and enter the correct weight and unit.")
    exit()
if unit == "pounds" or unit == "p":
    # Convert kilograms to pounds
    weight_in_pounds = weight * 2.20462
    print(f"Your weight in pounds is: {weight_in_pounds:.2f} lbs")
elif unit == "kilograms" or unit == "kg":
    # Convert pounds to kilograms
    weight_in_kilograms = weight / 2.20462
    print(f"Your weight in kilograms is: {weight_in_kilograms:.2f} kg")
else:
    print("Invalid unit. Please enter either 'Pounds' or 'Kilograms'.")


