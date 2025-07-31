# Program to calculate area of a triangle using Heron's formula
# Heron's formula: area = sqrt(s*(s-a)*(s-b)*(s-c)), where s = (a+b+c)/2

# Input the Lengths of the sides of the triangle
a = float(input("Enter a. "))
b = float(input("Enter b. "))
c = float(input("Enter c. "))

# Calculate the semi-perimeter
s = (a+b+c)/2.0

# Calculate the area using Heron's formula (** is used for exponentiation)
area = (s*(s-a)*(s-b)*(s-c))**0.5

# Output the area
print("Area of a tringle is", area)