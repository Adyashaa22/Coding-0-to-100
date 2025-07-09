# age= 2
# if age <=18:
#     message = "Not Eligible"
#     print(message)
# else:
#     message = "Eligible"
#     print(message) 
# # print(message)

# message="Eligible" if age >=18 else "Not Eligible"
# print(message)

'''high_income= False
good_credit=False
student= False
if high_income or good_credit or not student:
    print("Eligible")
else:
    print("Not Eligible") '''
    
#hmm
"""age= int(input())
if 18<= age <65:
    print("Eligible")
else:
    print("Not Eligible")
"""
# for number in range(1,4):
#     print('Attempt', number, (number+1)* ".")

'''number=100
while number >0:
    print (number)
    number //=2
'''    
    
# command = ""
# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() =="quit":
#         break
    
    
#for x in range(1,10):
#     if x%2==0:
#         print(x)
#         x +=x
        
'''def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")
    
greet("Adyasha", "Nayak")'''

# name= str(input(""))
# def greet(name):
#     print(f"hello {name}")
# greet(name)

def multiply (x,y):
    return x * y
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def divide(x,y):
    return x / y
def calculator(x, y, operation):
    if operation == "multiply":
        return multiply(x, y)
    elif operation == "add":
        return add(x, y)
    elif operation == "subtract":
        return subtract(x, y)
    elif operation == "divide":
        return divide(x, y)
    else:
        return "Invalid operation"
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
operation = input("Enter operation (multiply, add, subtract, divide): ")
result = calculator(x, y, operation)
print("Result:", result)
def greet(name):
    print(f"Hello, {name}!")
greet("Adyasha")
# def add_numbers(a, b):
#     return a + b
# result = add_numbers(5, 3)
# print(f"The sum is: {result}") 

