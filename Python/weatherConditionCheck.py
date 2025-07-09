# Python program for temperature condition
temperature = float(input("Enter the temperature: "))  # Input temperature in Celsius
unit = input("Enter the temperature unit (Celsius or Fahrenheit): ").strip().lower()  # Input unit for conversion
if unit != "celsius" and unit != "fahrenheit" and unit != "c" and unit != "f":
    print("Invalid unit. Please enter either 'Celsius' or 'Fahrenheit'.")
    exit()
print(f"Your temperature is in {unit}")
print(f"Do you want to convert it into { 'celsius' if unit == 'f' or unit == 'fahrenheit' else 'fahrenheit' }?")
# yes/no
print("(yes/no)")
response = input().strip().lower()  # Input response from the user
if response == "yes" or response == "y":
    print("Great! Let's proceed with the conversion.")
    delay = 1.56  # Simulating a delay for user experience
    import time
    time.sleep(delay) 
    if unit == "fahrenheit" or unit == "f":
    # Convert Celsius to Fahrenheit
        temperature_in_fahrenheit = (temperature * 9/5) + 32
        print(f"Your temperature in Fahrenheit is: {temperature_in_fahrenheit:.2f} °F")
        temperature = temperature_in_fahrenheit
        unit = "fahrenheit"
    elif unit == "celsius" or unit == "c":
        # Convert Fahrenheit to Celsius
        temperature = (temperature - 32) * 5/9
        print(f"Your temperature in Celsius is: {temperature:.2f} °C")
        temperature = temperature
        unit = "celsius"
    else:
        print("Please restart the program and enter the correct temperature and unit.")
        exit()
elif response == "no" or response == "n":
    print("Conversion cancelled. ")
    print("Do you just want to know the weather condition? (yes/no)")
    response = input().strip().lower()
    if response == "yes" or response == "y":
        print("Great! Let's check the weather condition.")
if unit == "celsius" or unit == "c":
    if temperature < 0:
        print("It's freezing cold outside!")
    elif 0 <= temperature < 20:
        print("It's quite chilly outside.")
    elif 20 <= temperature < 30:
        print("The weather is pleasant.")
    elif 30 <= temperature < 40:
        print("It's getting warm outside.")
    elif temperature >= 40:
        print("It's extremely hot outside!")
elif unit == "fahrenheit" or unit == "f":
    if temperature < 32:
        print("It's freezing cold outside!")
    elif 32 <= temperature < 68:
        print("It's quite chilly outside.")
    elif 68 <= temperature < 86:
        print("The weather is pleasant.")
    elif 86 <= temperature < 104:
        print("It's getting warm outside.")
    elif temperature >= 104:
        print("It's extremely hot outside!")
