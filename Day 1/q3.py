# Program to calculate area and circumference of a circle

# Input the radius of the circle from the user
r = float(input("Enter radius of a circle. "))

# Calculate area using the formula: area = π * r^2
area = 3.14*(r**2)
# Calculate circumference using the formula: circumference = 2 * π * r
cir = 2*3.14*r

# Display the area of the circle
print("Area of a Circle :", area)
# Display the circumference of the circle
print("Circumference of  Circle :", cir)
