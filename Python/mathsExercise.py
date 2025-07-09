import math
# x= float(input("Enter a number: "))  # Input a number from the user
# print("You entered:", x)  # Print the number entered by the user
# print(math.pi)  # Print the value of pi
# print(math.e)   # Print the value of e
# print(math.factorial(5))  # Print the factorial of 5
# print(math.sqrt(16))  # Print the square root of 16
# print(math.pow(x, 3))  # Print 2 raised to the power of 3
# print(math.sin(math.pi / 2))  # Print the sine of 90 degrees (pi/2 radians)
# print(math.ceil(x))  # Print the smallest integer greater than or equal to 4.2

'''radius = float(input("Enter the radius of the circle: "))  # Input radius from the user
area = math.pi * radius ** 2  # Calculate the area of the circle
print("The area of the circle is:", area)
# Calculate the circumference of the circle
circumference = 2 * math.pi * radius  # Calculate the circumference of the circle
print("The circumference of the circle is:", round(circumference, 2))  # Print the circumference
# Calculate the diameter of the circle
diameter = 2 * radius  # Calculate the diameter of the circle
print("The diameter of the circle is:", diameter)  # Print the diameter'''

a= float(input("Enter Side A: "))  # Input first number from the user
b= float(input("Enter Side B: "))  # Input second number from the user
c= round(math.sqrt((pow(a,2) + pow(b,2))),2)  # Calculate the hypotenuse using Pythagorean theorem
print("The length of the hypotenuse is:", c)  # Print the length of the hypotenuse
# Calculate the area of the triangle
area = (a * b) / 2  # Calculate the area of the triangle
print("The area of the triangle is:", area)  # Print the area of the triangle
# Calculate the perimeter of the triangle
perimeter = a + b + c  # Calculate the perimeter of the triangle
print("The perimeter of the triangle is:", perimeter)  # Print the perimeter of the triangle
# Calculate the angles of the triangle
angle_A = math.degrees(math.asin(a / c))  # Calculate angle A in
# degrees using the sine function
angle_B = math.degrees(math.asin(b / c))  # Calculate angle B in
# degrees using the sine function
angle_C = 180 - angle_A - angle_B  # Calculate angle C in degrees
print("The angles of the triangle are:")  # Print the angles of the triangle
print("Angle A:", angle_A)  # Print angle A
print("Angle B:", angle_B)  # Print angle B
print("Angle C:", angle_C)  # Print angle C
